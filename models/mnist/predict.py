# coding: utf-8
import tensorflow as tf
from PIL import Image
import numpy as np
import os.path
import string
import sys

def predict(img):
	with tf.Session() as sess:

		#load model
		MODELS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'models')
		model = tf.saved_model.loader.load(sess, ['Captcha'], MODELS_DIR)
		image = sess.graph.get_tensor_by_name(model.signature_def['signature'].inputs["image"].name)
		captcha = sess.graph.get_tensor_by_name(model.signature_def['signature'].outputs["captcha"].name)

		#run model
		image_resized = img.resize((100,30), Image.BICUBIC)
		captcha = sess.run(captcha, feed_dict={image:[np.array(image_resized)]})
		charset = string.digits + string.ascii_lowercase
		result = ''.join([charset[x] for x in captcha[0]])

	return result
	