from flask import Flask,request,jsonify,render_template,make_response
from PIL import Image, ImageEnhance, ImageOps
from scipy import misc
from array import *
import numpy as np
import urllib.request
import base64
import cv2
import io

app = Flask(__name__)
try:
  import pynq
  import bnn
  pynq_overlay = pynq.Overlay("base.bit")
  mnist_classifier = bnn.LfcClassifier(bnn.NETWORK_LFCW1A1,"mnist",bnn.RUNTIME_HW)
except ImportError:
  pynq = None

@app.route('/extension/<name>')
def extension_led(name):
  resp = make_response(render_template(name + '.js', url_root=request.url_root))
  resp.headers['Content-type'] = 'application/javascript'
  return resp

@app.route('/led')
def led():
  status = int(request.args.get('status')) 
  index  = int(request.args.get('index')) - 1
  print("status:", status)
  print("index:", index)
  if pynq is None:
    #with urllib.request.urlopen(url) as response:
    pass
  else:
    pynq_overlay.rgbleds_gpio[index].write(status)
  return jsonify(status)

@app.route('/mnist', methods = ['POST'])
def mnist():
  img_data = request.get_json().get('data')
  img_data = base64.b64decode(img_data)
  img = Image.open(io.BytesIO(img_data))
  img = img.convert("L")   
  img = ImageEnhance.Contrast(img).enhance(3)  
  img = ImageEnhance.Brightness(img).enhance(4.0)  
  box = ImageOps.invert(img).getbbox()  
  img = img.crop(box) 
  width, height = img.size  
  ratio = min((28./height), (28./width))  
  smallimg = Image.new('RGB', (28,28), (255,255,255))  
  if(height>width):  
      img = img.resize((int(width*ratio),28))  
      smallimg.paste(img, (int((28-img.size[0])/2),int((28-img.size[1])/2)))  
  else:  
      img = img.resize((28, int(height*ratio)))  
      smallimg.paste(img, (int((28-img.size[0])/2),int((28-img.size[1])/2)))  
  smallimg = ImageOps.invert(smallimg).convert("L")  
  #smallimg.save("smallimg.png")

  if pynq is None:
    return jsonify({"error":"Error: pynq is not found"})

  data_image = array('B', [0, 0, 8, 3, 0, 0, 0, 1, 0, 0, 0, 28, 0, 0, 0, 28])
  pixel = smallimg.load()  
  for x in range(0,28):  
    for y in range(0,28):  
        data_image.append(255 if pixel[y,x] == 255 else 1)  
  with open('/tmp/mnist_processed', 'wb') as file:
    data_image.tofile(file)  
  result = mnist_classifier.classify_mnist('/tmp/mnist_processed')
  return jsonify({"class":str(result)})

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)