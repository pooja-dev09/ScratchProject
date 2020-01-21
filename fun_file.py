import math, random 
from app import *
import mysql.connector 
from werkzeug import secure_filename
import base64
import uuid
import requests
import urllib
from cryptography.fernet import Fernet
def generateOTP() :
	digits = "0123456789"
	OTP = ""
	for i in range(4) : 
		OTP += digits[math.floor(random.random() * 10)]
	return str(OTP)
	
	
	
	
def RegisterNo():
	digits = "0123456789"
	OTP = "" 
	for i in range(4) : 
		OTP += digits[math.floor(random.random() * 10)]
		Result = 'SEC' + OTP
	return Result
	
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def Upload_fun(file):
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

		return filename

def save(Photo):
	imgdata = base64.b64decode(Photo)
	filename = 'video/'+str(uuid.uuid4())+'.jpg'  # I assume you have a way of picking unique filenames
	with open(filename, 'wb') as f:
		f.write(imgdata)
		return (filename.replace('video/',''))
		
	
def request_form(Name,MobileNo,VehicleCategory,DateOfPurchase,PoliceStation,District,State):
	if Name != "" and MobileNo !="" and VehicleCategory != "" and DateOfPurchase != "" and 	PoliceStation != "" and District != "" and State != "":
		return True
	

def EmpId():
	digits = "0123456789"
	OTP = "" 
	for i in range(4) : 
		OTP += digits[math.floor(random.random() * 10)]
		Result = 'EMP'+ OTP
	return Result
	
def ClaimNo():
	digits = "0123456789"
	OTP = "" 
	for i in range(4) : 
		OTP += digits[math.floor(random.random() * 10)]
		Result = 'Cl'+ OTP
	return Result
	
	
def SMS_Integration(msg,contactno):
	uname ='krititech'
	pwd = 'kriti@2705'
	senderid='ARMEDI'
	
	msg = urllib.parse.quote(msg)
	
	smsurl='http://cloud.smsindiahub.in/vendorsms/pushsms.aspx?user='+str(uname)+'&password='+str(pwd)+'&msisdn='+str(contactno)+'&sid='+str(senderid)+'&msg='+str(msg)+'&fl=0&gwid=2'
	r = requests.post(url = smsurl)
	x=r.json()


def Password_encoded(MobileNo):
	print('asdxakxkx')
	key = Fernet.generate_key() 
	cipher_suite = Fernet(key)
	MobileNo = 	MobileNo.encode('utf-8')
	encoded_text = cipher_suite.encrypt(MobileNo)
	return encoded_text
	