from flask import Flask,request,jsonify,render_template,make_response
import base64
import cv2
import io
import os
import pygame
import random

app = Flask(__name__)

def display_init():
  os.environ["SDL_FBDEV"]    = "/dev/fb1"
  os.environ["SDL_MOUSEDEV"] = "/dev/tty0"
  pygame.init()

def display(x, y, text):
  screen = pygame.display.set_mode((480,320))
  font = pygame.font.SysFont("comicsansms", 128)
  text = font.render(str(text), True, (0, 128, 0))
  screen.fill((255, 255, 255))
  screen.blit(text,(x, y))
  pygame.display.flip()

@app.route('/extension/<name>')
def extension_led(name):
  resp = make_response(render_template(name + '.js', url_root=request.url_root))
  resp.headers['Content-type'] = 'application/javascript'
  return resp

@app.route('/mnist', methods = ['POST'])
def mnist():
  img_data = request.get_json().get('data')
  result = random.randint(0,9)



  display(150, 50, result)
  return jsonify({"class":str(result)})

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
  display_init()
  app.run(host='0.0.0.0', port=80)