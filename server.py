from flask import Flask,request,jsonify,render_template,make_response
from PIL import Image, ImageEnhance, ImageOps
from scipy import misc
from array import *
import numpy as np
import urllib.request
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

def display(text):
  screen = pygame.display.set_mode((480,320))
  font = pygame.font.SysFont("comicsansms", 72)
  text = font.render(str(text), True, (0, 128, 0))
  screen.fill((255, 255, 255))
  screen.blit(text,(50, 50))
  pygame.display.flip()

@app.route('/extension/<name>')
def extension_led(name):
  resp = make_response(render_template(name + '.js', url_root=request.url_root))
  resp.headers['Content-type'] = 'application/javascript'
  return resp

@app.route('/mnist', methods = ['POST'])
def mnist():
  img_data = request.get_json().get('data')
  result = random.random()



  display(result)
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