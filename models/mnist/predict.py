# coding: utf-8
import tensorflow as tf
from PIL import Image
import numpy as np
import os.path
import string
import sys
import time

sess = None
image = None
captcha = None

def init():
	global sess, image, captcha
	sess = tf.Session()
	MODELS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'models')
	model = tf.saved_model.loader.load(sess, ['Captcha'], MODELS_DIR)
	image = sess.graph.get_tensor_by_name(model.signature_def['signature'].inputs["image"].name)
	captcha = sess.graph.get_tensor_by_name(model.signature_def['signature'].outputs["captcha"].name)

def predict(img):
	global sess, image, captcha
	image_resized = img.resize((100,30), Image.BICUBIC)
	start_time = time.time()
	result = sess.run(captcha, feed_dict={image:[np.array(image_resized)]})
	charset = string.digits + string.ascii_lowercase
	return ''.join([charset[x] for x in result[0]])
	