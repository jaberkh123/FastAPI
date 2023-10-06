
import socketio
import requests
import mysql.connector
from datetime import datetime
import time
import json
import time
# import urllib library
from urllib.request import urlopen
print(socketio.__file__)
sio = socketio.Client()
@sio.event
def connect():
    print('connection established')
    #sio.emit('box1_check')
    #sio.emit('box2_check')    
    #sio.emit('box5_check')
    #sio.emit('box4_check')
    sio.emit('check_block_page')
@sio.event
def transaction_page_Transfer_Counts(data):
    print('block_box_one_two::: ', data)
    #sio.emit('my response', {'response': 'my response'})
@sio.event
def transaction_page_Trading_Volume(data):
    print('block_box_three ::: ', data)
    #sio.emit('my response', {'response': 'my response'})
@sio.event
def transaction_page_Transfer_Type(data):
    print('message received with ', data)


@sio.event
def transaction_page_Transfer_box4(data):
    print('message received with ', data)
    #sio.emit('my response', {'response': 'my response'}

@sio.event
def disconnect():
    print('disconnected from server')
def dgold_check():
    return 1

while True:
            time.sleep(10)
            cnx = mysql.connector.connect(user='root', password='mishe123321', host='localhost',port=3306,database='delta')
            mycursor = cnx.cursor()
            z=[]
            sql = "select * from checker"
            mycursor.execute(sql)
            for x in mycursor:
                     z.append(x)
            a=[]
               
            sio.connect('http://81.12.30.167:8011')            
            for j in z :
                  if j[1]==1:
                     sio.emit(j[1])
            sio.disconnect()
           
            cnx.close()







