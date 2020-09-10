# Module 1 - Create a Blockchain

# To be installed:
# Flask==0.12.2: pip install Flask==0.12.2
# Postman HTTP Client: https://www.getpostman.com/

# Importing the libraries
import datetime,os
import json
import hashlib
from flask import Flask, jsonify,render_template,request, redirect, url_for,session,flash
import binascii
from werkzeug.utils import secure_filename
from urllib.parse import urlparse
import requests
from uuid import uuid4
import numpy as np
from numpy import array
from tensorflow.keras.models import load_model

import pickle,joblib
# from tensorflow import keras
# from flask_login import LoginManager,UserMixin,login_user,login_required,current_user,logout_user
# from keras import tensorflow
# from sklearn.externals import joblib
# importing libraries required for ELA Conversion
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import seaborn as sns

from datetime import timedelta

from PIL import Image
import os
# from pylab import *

import re

from PIL import Image, ImageChops, ImageEnhance
# from io import StringIO

from user import User
from database import Database
from blockchain import Blockchain
#import tensorflow as tf
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# Creating a Web App
app = Flask(__name__)
app.secret_key = "Docufy"
# mp = pickle.load(open('model_pickle','rb'))
blockchain = Blockchain()
# app.config['UPLOAD_FOLDER'] = r'C:\Users\Shantanu\Desktop\Docufy\static'
app.config['UPLOAD_FOLDER'] = os.path.abspath("static/")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.config["CACHE_TYPE"] = "null"

app.permanent_session_lifetime = timedelta(minutes=10)

#Creating an address for the node on Port 5000
# node_address = str(uuid4()).replace('-','')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/to_slider')
# def to_slider():
#     return render_template("rangeSlider-1.html")

# @app.route('/range_slider',methods=['POST'])
# def range_slider():
#     quality = 90
#     file = request.files["img1"]
#     scale1 = int(request.form["range_slider"])

#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'Original.jpg'))
#     filename = os.path.abspath("static/Original.jpg")

#     resaved_filename = filename.split('.')[0] + '.resaved.jpg'
#     ELA_filename = filename.split('.')[0] + '.ela.png'
    
    
#     im = Image.open(filename).convert('RGB')
#     im.save(resaved_filename, 'JPEG', quality=quality)
#     resaved_im = Image.open(resaved_filename)
    
#     ela_im = ImageChops.difference(im, resaved_im)
    
#     extrema = ela_im.getextrema()
#     max_diff = max([ex[1] for ex in extrema])
#     if max_diff == 0:
#         max_diff = 1
#     scale = 255.0 / max_diff
    
#     scale_im = ImageEnhance.Brightness(ela_im).enhance(scale1)
#     ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
#     # print(ela_im)
#     # print(type(ela_im))
#     #ela_im.save(r"path")
#     ela_im.save(os.path.abspath("static/ela_image.jpeg"))
#     scale_im.save(os.path.abpicspath("static/scale_image.jpeg"))
#     # print(ela_im)

#     return render_template('rangeSlider.html')



# # Creating a Blockchain
# @app.route('/index')
# def index():
#     return render_template('index.html')

@app.route('/')
def newindex():
    return render_template('newindex.html')


# @app.route('/sahil')
# def sahil():
#     return render_template('sahil.html')

# @app.route('/ela')
# def ela():
#     return render_template('ela.html')

# @app.route('/admin')
# def admin():
#     return render_template('adminLogin.html')

# @app.route('/userlogin')
# def userlogin():
#     return render_template('Login.html')

# @app.route('/register')
# def register():
#     return render_template('Register.html')

# # @app.after_request
# # def after_request(response):
# #     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
# #     return response

# @app.route('/logout')
# def admin_logout():
#     if "admin" in session:
#         admin = session["admin"]
#         flash(f"You have been logged out,{admin}","info")
#     session.pop('admin', None)
#     return render_template("adminLogin.html")

# @app.route('/user/logout')
# def user_logout():
#     if "user" in session:
#         user = session["user"]
#         flash(f"You have been logged out,{user}","info")
#     session.pop('user', None)   
#     return render_template("Login.html")

# @app.route('/user/register', methods=['POST'])
# def user_register():
#     username = request.form['username']
#     password = request.form['password']

#     user = User.getUser({'username':username})

#     if user is None:
#         user = User(username = username, password = password)
#         user.addUser()
#         session['user'] = username
#         flash('Registration successful', 'info')
#         return redirect(url_for('wh'))
#     else:
#         flash('Registration unsuccessful.Credentials Already Present', 'error')
#         return redirect(url_for('newindex'))

# @app.route('/admin/authenticate', methods=['GET','POST'])
# def admin_authenticate():
#     username = request.form['username']
#     password = request.form['password']

#     admin = User.getUser({'username':username,'password':password})

#     if admin is None:
#         session.pop('admin', None)
#         flash('Username or Password is wrong! Try Again', 'danger')
#         return redirect(url_for('admin'))
#     else:
#         session['admin'] = username
#         flash('Login successful', 'success')
#         return redirect(url_for('index'))


# @app.route('/user/authenticate', methods=['GET','POST'])
# def user_authenticate():
#     username = request.form['username']
#     password = request.form['password']

#     user = User.getUser({'username':username,'password':password})

#     if user is None:
#         session.pop('user', None)
#         flash('Username or Password is wrong! Try Again', 'danger')
#         return redirect(url_for('admin'))
#     else:
#         session['user'] = username
#         return redirect(url_for('wh'))

# @app.route('/fela',methods = ['GET','POST'])
# def fela():

#     quality = 90
#     file = request.files["img1"]
#     # filename = file.filename
#     filename = secure_filename(file.filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'Original.jpg'))
#     # filename = r'C:\Users\Shantanu\Desktop\Docufy\static\Original.jpg'
#     filename = os.path.abspath("static/Original.jpg")
#     print(filename)
#     # im = Image.open(filename)
#     # im.save(file)
#     # resaved_filename = request.files["img1"]
#     # ELA_filename = request.files["img1"]
#     # filename = 'Original.jpg'
#     resaved_filename = filename.split('.')[0] + '.resaved.jpg'
#     ELA_filename = filename.split('.')[0] + '.ela.png'
        
#     im = Image.open(filename).convert('RGB')
#     im.save(resaved_filename, 'JPEG', quality=quality)
#     resaved_im = Image.open(resaved_filename)
        
#     ela_im = ImageChops.difference(im, resaved_im)
        
#     extrema = ela_im.getextrema()
#     max_diff = max([ex[1] for ex in extrema])
#     if max_diff == 0:
#         max_diff = 1
#     scale = 255.0 / max_diff
        
#     ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
#         # print(ela_im)
#         # print(type(ela_im))
#         #ela_im.save(r"path")
#     ela_im.save(os.path.abspath("static/ela_image.jpeg"))
#         # print(ela_im) 
#     print(ela_im)
#     print(type(ela_im))

#         # # import pickle
#         # with open('model/model_pickle','rb') as f:
#         #     mp = pickle.load(f)

#         # Load h5 model
#     mp = load_model('model/model.h5')


#         # mp = joblib.load('model/model_pickle')
#         # mp = keras.models.load_model('model_pickle')
#     feature = array(ela_im.resize((128, 128))).flatten() / 255.0
#         # feature = array(convert_to_ela_image('Casia/casia/CASIA2/Au/Au_ani_10194.jpg', 90).resize((128, 128))).flatten() / 255.0

#     feature = feature.reshape(-1,128,128,3)
#     print(feature)
#     output = mp.predict(feature)
#     output = output.flatten()
#     print(output)
        
        
#     prediction_true = output[1]
#     prediction_false = output[0]
#     acc = "accuracy"
#     per = "%"
#     if output[1] > 0.50:
#         print('True')
#         prediction = output[1] 
#         newvar = 'Image is Authentic' 
#     else:
#         print('False')
#         prediction = output[0]
#         newvar = 'Image Is Tampered' 
        
#     prediction = round(prediction*100, 2)
#     print(newvar, prediction, acc, per )



#     return render_template('ela.html',newvar = newvar, prediction = prediction, acc = acc, per = per )  


# @app.route('/wh')
# def wh():
#     return render_template('wh.html')

# @app.route('/wholemodule',methods = ['GET','POST'])
# def wholemodule():
#     quality = 90
#     file = request.files["img1"]
    
#     # filename = file.filename
#     filename = secure_filename(file.filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'Original.jpg'))
#     filename = os.path.abspath("static/Original.jpg")
#     # filename = r'C:\Users\Shantanu\Desktop\Docufy\static\Original.jpg'
#     # im = Image.open(filename)
#     # im.save(file)
#     # resaved_filename = request.files["img1"]
#     # ELA_filename = request.files["img1"]
#     # filename = 'Original.jpg'
#     resaved_filename = filename.split('.')[0] + '.resaved.jpg'
#     ELA_filename = filename.split('.')[0] + '.ela.png'
    
    
#     im = Image.open(filename).convert('RGB')
#     im.save(resaved_filename, 'JPEG', quality=quality)
#     resaved_im = Image.open(resaved_filename)
    
#     ela_im = ImageChops.difference(im, resaved_im)
    
#     extrema = ela_im.getextrema()
#     max_diff = max([ex[1] for ex in extrema])
#     if max_diff == 0:
#         max_diff = 1
#     scale = 255.0 / max_diff
    
#     ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
#     # print(ela_im)
#     # print(type(ela_im))
#     # ela_im.save(r'C:\Users\Shantanu\Desktop\Docufy\static\ela_image.jpeg')
#     ela_im.save(os.path.abspath("static/ela_image.jpeg"))
#     # print(ela_im)
#     print(ela_im)
#     print(type(ela_im))

#     # import pickle
#     with open('model/model_pickle','rb') as f:
#         mp = pickle.load(f)
#     # mp = joblib.load('model/model_pickle')
#     # mp = keras.models.load_model('model_pickle')
#     feature = array(ela_im.resize((128, 128))).flatten() / 255.0
#     # feature = array(convert_to_ela_image('Casia/casia/CASIA2/Au/Au_ani_10194.jpg', 90).resize((128, 128))).flatten() / 255.0

#     feature = feature.reshape(-1,128,128,3)
#     print(feature)
#     output = mp.predict(feature)
#     output = output.flatten()
#     print(output)
#     if output[1] > 0.50:
#         print('True')
#         newvar = 'True'

#     else:
#         print('False')
#         newvar = 'False'
    
#     if newvar=='True':
#         filenew = os.path.abspath("static/Original.jpg")
#         # filenew = r'C:\Users\Shantanu\Desktop\Docufy\static\Original.jpg'
#         # filenew = '../static/Original.jpg'
#         with open(filenew, 'rb') as f:
#             content = f.read()
#         # content = filenew.read()
#         sha_signature = hashlib.sha256(str(content).encode()).hexdigest()
#         print(sha_signature)
#         is_valid = blockchain.is_check(blockchain.chain,sha_signature)
#         if is_valid:
#             response = 'All good. The Hash is valid. The Image is authentic'
#         else:
#             response = 'We have a problem. The Hash is not valid. Rejected by Blockchain Module'
#     else:
#         response = 'The image was rejected by Image Processing Module'

#     return render_template('wh.html',response = response)




# @app.route('/tocheck')
# def tocheck():
#     return render_template('tocheck.html')

# @app.route('/check',methods = ['GET','POST'])
# def check():
#     filename = request.files["img1"]
#     content = filename.read()
#     sha_signature = hashlib.sha256(str(content).encode()).hexdigest()

#     is_valid = blockchain.is_check(blockchain.chain,sha_signature)
#     if is_valid:
#         response = {'message': 'All good. The Hash is valid.'}
#     else:
#         response = {'message': 'We have a problem. The Hash is not valid.'}
#     return render_template("tocheck.html",response=zip(response,response.values()))



# # Mining a new block
# @app.route('/mine_block', methods = ['POST','GET'])
# def mine_block():
    
#     previous_block = blockchain.get_previous_block()
#     previous_proof = previous_block['proof']
#     proof = blockchain.proof_of_work(previous_proof)
#     previous_hash = blockchain.hash(previous_block)
    
    

#     filename = request.files['img1']
    
#     #with open(filename, 'rb') as f:
#         #content = f.read()
#     content = filename.read()

#     sha_signature = hashlib.sha256(str(content).encode()).hexdigest()
#     #print(sha_signature)
    
#     block = blockchain.create_block(proof, previous_hash,sha_signature)
    
#     response = {'message': 'Congratulations, you just mined a block!',
#                 'index': block['index'],
#                 'timestamp': block['timestamp'],
#                 'proof': block['proof'],
#                 'previous_hash': block['previous_hash'],
#                 'img_hash':block['img_hash']}
    
#     return render_template("result.html",response=zip(response,response.values()))

# #render_template("result.html",response=response)
# # Getting the full Blockchain list
# @app.route('/get_chain', methods = ['GET'])
# def get_chain():
#     response = {'chain': blockchain.chain,
#                 'length': len(blockchain.chain)}
#     return jsonify(response), 200

# # Checking if the Blockchain is valid
# @app.route('/is_valid', methods = ['GET'])
# def is_valid():
#     is_valid = blockchain.is_chain_valid(blockchain.chain)
#     if is_valid:
#         response = {'message': 'All good. The Blockchain is valid.'}
#     else:
#         response = {'message': 'We have a problem. The Blockchain is not valid.'}
#     return jsonify(response), 200

# @app.route('/connect_node', methods = ['GET','POST'])
# def connect_node():
#     json = request.get_json()
    
#     nodes = json.get('nodes')
#     if nodes is None:
#         return "No node", 400
#     for node in nodes:
#         blockchain.add_node(node)
#     response = {'message': 'All the nodes are now connected. The Hadcoin Blockchain now contains the following nodes:',
#                 'total_nodes': list(blockchain.nodes)}
#     return jsonify(response), 201

# # Replacing the chain by the longest chain if needed
# @app.route('/replace_chain', methods = ['GET'])
# def replace_chain():
#     is_chain_replaced = blockchain.replace_chain()
#     if is_chain_replaced:
#         response = {'message': 'The nodes had different chains so the chain was replaced by the longest one.',
#                     'new_chain': blockchain.chain}
#     else:
#         response = {'message': 'All good. The chain is the largest one.',
#                     'actual_chain': blockchain.chain}
#     return jsonify(response), 200

# Running the app
if __name__ == '__main__':
    app.run(debug=true)
