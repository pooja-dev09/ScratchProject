import math, random 
from app import *
import mysql.connector 
from werkzeug import secure_filename
import base64
import uuid
import requests
import urllib
import hashlib
import re 
def generateOTP() :
	digits = "0123456789"
	OTP = ""
	for i in range(4) : 
		OTP += digits[math.floor(random.random() * 10)]
	return str(OTP)
	

def RegisterCustomer(totalval):
	totalval += 1
	Result = 'SCAA'+ str(totalval)
	return str(Result)

def RequestCustomer(totalval):
	totalval += 1
	print('increment',totalval)
	Result = 'SENR0'+ str(totalval)
	return str(Result)

def AreaManager(totalval):
	totalval += 1
	Result = 'SEAM0' + str(totalval)
	return str(Result)


	
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
	filename = 'static/video/'+str(uuid.uuid4())+'.jpg'  # I assume you have a way of picking unique filenames
	with open(filename, 'wb') as f:
		f.write(imgdata)
		return (filename.replace('static/video/',''))
		

def EmpIdSM(totalval):
	totalval += 1
	Result = 'SESM0'+ str(totalval)
	return str(Result)

def EmpIdAU(totalval):
	totalval += 1
	Result = 'SEAU0'+ str(totalval)
	return str(Result)
	
def ClaimNo(totalval):
	totalval += 1
	Result = 'SECL0' + str(totalval)
	return str(Result)


def SMS_Integration(msg,contactno):
	print('msg',msg)
	uname ='krititech'
	pwd = 'kriti@2705'
	senderid='SCREXP'
	
	msg = urllib.parse.quote(msg)
	
	smsurl='http://cloud.smsindiahub.in/vendorsms/pushsms.aspx?user='+str(uname)+'&password='+str(pwd)+'&msisdn='+str(contactno)+'&sid='+str(senderid)+'&msg='+str(msg)+'&fl=0&gwid=2'
	r = requests.post(url = smsurl)
	x=r.json()
	print(x)


def Password_encoded(MobileNo):
	result = hashlib.sha256(MobileNo.encode())
	result=(result.hexdigest())	
	return result

#--------------------------------validation--------------------------------------------------	
	
def request_form(Name,MobileNo,VehicleCategory,DateOfPurchase,PoliceStation,District,State):
	if Name != "" and MobileNo !="" and VehicleCategory != "" and DateOfPurchase != "" and 	PoliceStation != "" and District != "" and State != "":
		return True
		
		
def validNumber(phone_number):
	if len(phone_number) == 10:
		print(phone_number)
		return True

		
def check(email):
	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
	if(re.search(regex,email)):  
		return True
		
def accountNo(accountno):
	if len(accountno) >= 14 and len(accountno) <= 16:
		return True
	
def vehicleNo(vehicleno):
	if len(vehicleno) >= 8 and len(vehicleno) <= 10:
		return True
	
def adharNo(adharNo):
	if len(adharNo) == 12: 
		return True
		
def GSTINo(GSTINo):
	if len(GSTINo) == 15: 
		return True
		
def ChassisNo(ChassisNo):
	if len(ChassisNo) == 17:
		return True


def pancard(Pancard):
	if re.match("[A-Za-z]{5}\d{4}[A-Za-z]{1}", Pancard):
		print(Pancard)
		return True


def pincode(Pincode):
	if len(Pincode) == 6:
		return True

		
def fun_ifsc(IFSC):
	if re.match("^[A-Z]{4}\d{7}$", IFSC):
		return True

