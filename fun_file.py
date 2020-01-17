import math, random 
from app import *
import mysql.connector 
from werkzeug import secure_filename
import base64
import uuid

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
	
	
	
	

	