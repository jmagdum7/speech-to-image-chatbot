from flask import Flask, redirect, url_for, render_template, session, escape, request, jsonify
import requests
from collections import defaultdict
import pickle
import json
import random
# import regex
import subprocess
import os
import sys
import time
 
app = Flask(__name__)

cnt = 1

# click to open up
@app.route('/newbox')
def newboxes():
	return render_template('newbox.html')

# in the middle of screen
@app.route('/',methods=['GET','POST'])
def chatbots():
	return render_template('chatbot.html')


@app.route('/postmethod', methods=['POST'])
def postmethod():
	data = request.get_json()
	if data['location'] != 'hi, please enter a description and wait for the image.':
		with open("../AttnGAN-master/data/coco/example_captions.txt","w") as f:
			f.write(data['location'])

		global cnt
		os.system("./sct/abc.sh ")
		os.rename("/media/jmagdum7/STUDIES AND WORK/BE/BE Project/attngan/coco_chatbot/static/images/0_s_0_g3.png", "/media/jmagdum7/STUDIES AND WORK/BE/BE Project/attngan/coco_chatbot/static/images/" + str(cnt) + ".png")
		cnt = cnt+1 

	# data['location'] = str(data['cnt'])
	# time.sleep(15)
	#display output image here
	# data['location'] = '/media/jmagdum7/STUDIES\ AND\ WORK/BE/BE\ Project/attngan/AttnGAN-master/models/coco_AttnGAN2/example_captions/0_s_0_g2.png'
	return jsonify(data)

if __name__ == '__main__':
   app.run(debug=True)