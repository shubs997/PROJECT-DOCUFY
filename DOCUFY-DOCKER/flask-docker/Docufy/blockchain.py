# Module 1 - Create a Blockchain

# To be installed:
# Flask==0.12.2: pip install Flask==0.12.2
# Postman HTTP Client: https://www.getpostman.com/

# Importing the libraries
import datetime,os
import json
import hashlib
from flask import Flask, jsonify,render_template,request, redirect, url_for,session
import binascii
from werkzeug.utils import secure_filename
from urllib.parse import urlparse
import requests
from uuid import uuid4
import numpy as np

# import pickle
# from tensorflow import keras
# from sklearn.externals import joblib
# importing libraries required for ELA Conversion
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import seaborn as sns


# from PIL import Image
# import os
# from pylab import *
# import re
# from PIL import Image, ImageChops, ImageEnhance

# from io import StringIO

from user import User
from database import Database
# Part 1 - Building a Blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0',sha_signature='0')
        self.nodes = set()

    def create_block(self, proof, previous_hash,sha_signature):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'img_hash':sha_signature}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
    def is_check(self,chain,sha_signature):
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['img_hash'] == sha_signature:
                return True
            else:
                block_index += 1
        return False
    
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False
    
    def add_node(self,address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

# class ELA:
#     def convert_to_ela_image():
#         filename = path
#         resaved_filename = filename.split('.')[0] + '.resaved.jpg'
#         ELA_filename = filename.split('.')[0] + '.ela.png'
        
#         im = Image.open(filename).convert('RGB')
#         im.save(resaved_filename, 'JPEG', quality=quality)
#         resaved_im = Image.open(resaved_filename)
        
#         ela_im = ImageChops.difference(im, resaved_im)
        
#         extrema = ela_im.getextrema()
#         max_diff = max([ex[1] for ex in extrema])
#         if max_diff == 0:
#             max_diff = 1
#         scale = 255.0 / max_diff
        
#         ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
        
#         return ela_im



#Commeting start

# # Part 2 - Mining our Blockchain list

# # Creating a Web App
# app = Flask(__name__)
# app.secret_key = "Docufy"
# # mp = pickle.load(open('model_pickle','rb'))
# blockchain = Blockchain()
# app.config['UPLOAD_FOLDER'] = r'C:\Users\Shantanu\Desktop\Docufy\static'
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# #Creating an address for the node on Port 5000
# node_address = str(uuid4()).replace('-','')


# # Creating a Blockchain
# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/')
# def newindex():
#     return render_template('newindex.html')


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
#     return render_template('register.html')

# # @app.after_request
# # def after_request(response):
# #     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
# #     return response

# @app.route('/logout')
# def admin_logout():
#     session.pop('admin', None)
#     return render_template("adminLogin.html")

# @app.route('/user/logout')
# def user_logout():
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
#         return redirect(url_for('index'))
#     else:
#         return redirect(url_for('index'))

# @app.route('/admin/authenticate', methods=['POST'])
# def admin_authenticate():
#     username = request.form['username']
#     password = request.form['password']

#     admin = User.getUser({'username':username,'password':password})

#     if admin is None:
#         session.pop('admin', None)
#         return redirect(url_for('newindex'))
#     else:
#         session['admin'] = username
#         return redirect(url_for('index'))


# @app.route('/user/authenticate', methods=['POST'])
# def user_authenticate():
#     username = request.form['username']
#     password = request.form['password']

#     user = User.getUser({'username':username,'password':password})

#     if user is None:
#         session.pop('user', None)
#         return redirect(url_for('newindex'))
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
#     filename = r'C:\Users\Shantanu\Desktop\Docufy\static\Original.jpg'
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
#     ela_im.save(r'C:\Users\Shantanu\Desktop\Docufy\static\ela_image.jpeg')
#     # print(ela_im)
#     print(ela_im)
#     print(type(ela_im))

#     # import pickle
#     with open('model_pickle','rb') as f:
#         mp = pickle.load(f)
#     # mp = keras.models.load_model('model_pickle')
#     feature = array(ela_im.resize((128, 128))).flatten() / 255.0
#     # feature = array(convert_to_ela_image('Casia/casia/CASIA2/Au/Au_ani_10194.jpg', 90).resize((128, 128))).flatten() / 255.0

#     feature = feature.reshape(-1,128,128,3)
#     print(feature)
#     output = mp.predict(feature)
#     output = output.flatten()
#     print(output)
#     if output[1] > 0.95:
#         print('True')
#         newvar = 'Image is Authentic'
#     else:
#         print('False')
#         newvar = 'Image Is Tampered'

#     return render_template('ela.html',newvar = newvar)

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
#     filename = r'C:\Users\Shantanu\Desktop\Docufy\static\Original.jpg'
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
#     ela_im.save(r'C:\Users\Shantanu\Desktop\Docufy\static\ela_image.jpeg')
#     # print(ela_im)
#     print(ela_im)
#     print(type(ela_im))

#     # import pickle
#     with open('model_pickle','rb') as f:
#         mp = pickle.load(f)
#     # mp = keras.models.load_model('model_pickle')
#     feature = array(ela_im.resize((128, 128))).flatten() / 255.0
#     # feature = array(convert_to_ela_image('Casia/casia/CASIA2/Au/Au_ani_10194.jpg', 90).resize((128, 128))).flatten() / 255.0

#     feature = feature.reshape(-1,128,128,3)
#     print(feature)
#     output = mp.predict(feature)
#     output = output.flatten()
#     print(output)
#     if output[1] > 0.90:
#         print('True')
#         newvar = 'True'

#     else:
#         print('False')
#         newvar = 'False'
    
#     if newvar=='True':
#         filenew = r'C:\Users\Shantanu\Desktop\Docufy\static\Original.jpg'
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
#             response = 'We have a problem. The Hash is not valid.'
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
# # Running the app
# app.run(threaded=False)
