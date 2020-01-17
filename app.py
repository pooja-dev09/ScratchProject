from flask import Flask,session, jsonify,request
from flask_restful import Api, Resource,reqparse,request
import mysql.connector
import datetime 
from fun_file import *
from flask_cors import CORS, cross_origin
import werkzeug
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'video/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp4','mp3'])
app = Flask(__name__)
cors = CORS(app)
CORS(app, support_credentials=True)
api = Api(app,prefix="/api",catch_all_404s=True)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="colourfade",
  database="Scratch"
)
mycursor = mydb.cursor()

class Request(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('Name',required=True,type=str, help='UserName cannot be found')
		parser.add_argument('MobileNo',required=True,type=str, help='MobileNo cannot be found')
		parser.add_argument('VehicleCategory', required=True,type=str, help='VehicleCategory cannot be found')
		parser.add_argument('DateOfPurchase',required=True,type=str,help='DateOfPurchase cannot be found')
		parser.add_argument('PoliceStation',required=True,type=str, help='PoliceStation cannot be found')
		parser.add_argument('District',required=True,type=str, help='District cannot be found')
		parser.add_argument('State',required=True,type=str, help='State cannot be found')
		args = parser.parse_args()
		Name = args['Name']
		MobileNo = args['MobileNo']
		VehicleCategory = args['VehicleCategory']
		DateOfPurchase = args['DateOfPurchase']
		PoliceStation = args['PoliceStation']
		District = args['District']
		State = args['State']
		CurrentTime = datetime.datetime.now()
		required = request_form(Name,MobileNo,VehicleCategory,DateOfPurchase,PoliceStation,District,State)
		if required == True:
			sql = "INSERT INTO customerrequest (Name,Mobile,VehicleCategory,DateOfPurchase,PoliceStation,District,State,DateOfRegistration) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (Name,MobileNo,VehicleCategory,DateOfPurchase,PoliceStation,District,State,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			return jsonify({'Message':' You are Successfully submitted your Request we will contact you soon ',
							'Name':Name,
							'Mobile':MobileNo,
							'VehicleCategory':VehicleCategory,
							'DateOfPurchase' :DateOfPurchase,
							'PoliceStation' :PoliceStation,
							'District':District,
							'State':State,
							'Status':'1'})
		else:
			return jsonify({'Message':' Something is wrong ',
							
							'Status':'0'})
	
		
api.add_resource(Request, "/newCustomerRequest")	

class Login(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('RoleID',required=True,type=int, help='RoleID cannot be found')
		parser.add_argument('UserName' ,required=True,type=str, help='VehicleNo cannot be found')
		parser.add_argument('Password',required=True,type=int, help='Password cannot be found')
		args = parser.parse_args()
		RoleID = args['RoleID']
		UserName = args['UserName']
		Password = args['Password']
		
		if RoleID == 2:
			mycursor.execute("SELECT UserID,RoleID from user WHERE VehicleNo = '%s' AND Password = '%s'" % (UserName, Password))
			rowcursor=mycursor.fetchall()
			
			if len(rowcursor) > 0:
				for i in rowcursor:
					UserID = i[0]
					RoleID = i[1]
					OTP=generateOTP()
					mycursor.execute("UPDATE user SET OTP = '"+str(OTP)+"' WHERE UserID = '"+str(UserID)+"'")
					mydb.commit()
					return jsonify ({'Message':'OTP Send Successfully',
									'UserID':UserID,
									'RoleID':RoleID,
									'Status':"1"
									})
			else:
				return	jsonify ({'Message':'Please Check Your UserId or Password May be wrong',
								'Status':"0"
								})
						
		elif RoleID == 3 or RoleID == 4 or RoleID == 5:
			mycursor.execute("SELECT UserID from user WHERE EmployeeId = '%s' AND Mobile = '%s'" % (UserName, Password))
			rowcursor=mycursor.fetchall()
			length =len(rowcursor)
			if length > 0:
				for i in rowcursor:
					UserID = i[0]
					OTP=generateOTP()
					mycursor.execute("UPDATE user SET OTP = '"+str(OTP)+"' WHERE UserID = '"+str(UserID)+"'")
					mydb.commit()
					return jsonify ({'Message':'OTP Send Successfully',
									'UserID':UserID,
									'RoleID':RoleID,
									'Status':"1"
				
						})
			else:
				return jsonify ({'Message':'Please Check Your UserId or Password May be wrong',
								'Status':"0"
								})
			
		
		
api.add_resource(Login, "/login")
	
	
class Otpverification(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=int, help='UserID cannot be found')
		parser.add_argument('OTP',required=True,type=int, help='OTP cannot be found')
		args = parser.parse_args()
		UserID = args['UserID']
		Userotp = args['OTP']
		mycursor.execute("SELECT OTP,RoleID from user WHERE UserID = '"+str(UserID)+"'")
		rowcursor=mycursor.fetchall()
		if len(rowcursor) > 0:
			for i in rowcursor:
				dataotp = i[0]
				RoleID = i[1]
				if Userotp == dataotp:
					return jsonify ({'Message':'Login Successfully',
									'RoleID':RoleID,
									'Status':"1"})

				else:
					return jsonify ({'Message':'Invalid Otp','Status':"0"})
		else:
			return jsonify ({'Message':'Sorry We dont have any data','Status':"0"})
api.add_resource(Otpverification, "/otpverification")


class Resend(Resource):				
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID' ,required=True,type=int, help='UserID cannot be found')
		args = parser.parse_args()
		UserID = args['UserID']
		mycursor.execute("SELECT OTP ,UserID from user WHERE UserID = '"+str(UserID)+"'")
		rowcursor=mycursor.fetchall()
		if len(rowcursor) > 0:
			for i in rowcursor:
				OTP = i[0]
				UserID = i[1]
				OTP=generateOTP()
				mycursor.execute("UPDATE user SET OTP = '"+str(OTP)+"' WHERE UserID = '"+str(UserID)+"'")
				mydb.commit()
				return jsonify ({'Message':'OTP Resend Sent','Status':"1"})
		else:
			return jsonify ({'Message':'Sorry We dont have any data','Status':"0"})
		
api.add_resource(Resend, "/resend")

class RegisterProfile(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=int, help='UserID cannot be found')
		parser.add_argument('RoleID',required=True,type=int, help='RoleID cannot be found')
		args = parser.parse_args()
		UserID = args['UserID']
		RoleID = args['RoleID']
		if RoleID == 2:
			sql = mycursor.execute("SELECT RegdNo,Name,VehicleNo,Mobile,DateOfRegd,DateOfExp from user WHERE UserID = '"+str(UserID)+"'")
			rowcursor=mycursor.fetchall()
			if len(rowcursor) > 0:
				for i in rowcursor:
					RegdNo = i[0]
					Name = i[1]
					VehicleNo=i[2]
					Mobile = i[3]
					DateOfRegd = i[4]
					DateOfExp = i[5]
					return jsonify ({'Message':'Result View Successfully',
									'RegdNo':RegdNo,
									'RoleID':RoleID,
									'Name':Name,
									'VehicleNo':VehicleNo,
									'UserID':UserID,
									'Mobile':Mobile,
									'DateOfRegd':DateOfRegd,
									'DateOfExp':DateOfExp,
									'Status':"1"})
			else:
				return jsonify ({'Message':'Sorry We dont have any data','Status':"0"})
		elif RoleID == 3 or RoleID == 4 or RoleID == 5:
			sql = mycursor.execute("SELECT EmployeeId,Name,Mobile,DateOfJoining from user WHERE UserID = '"+str(UserID)+"'")
			rowcursor=mycursor.fetchall()
			if len(rowcursor) > 0:
				for i in rowcursor:
					EmployeeId = i[0]
					Name=i[1]
					Mobile = i[2]
					DateOfJoining = i[3]
					
					return jsonify ({'Message':'Result View Successfully',
									'EmployeeId':EmployeeId,
									'RoleID':RoleID,
									'Name':Name,
									'UserID':UserID,
									'Mobile':Mobile,
									'DateOfJoining':DateOfJoining,
									'Status':"1"})
			else:
				return jsonify ({'Message':'Sorry We dont have any data','Status':"0"})
			
		
api.add_resource(RegisterProfile, "/getProfile")


class ProfileUpdate(Resource):				
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID' ,required=True,type=int, help='User Id cannot be found')
		parser.add_argument('MobileNo' ,required=True,type=int, help='Mobile cannot be found')
		args = parser.parse_args()
		UserID = args['UserID']
		MobileNo = args['MobileNo']
		if MobileNo != "":
			mycursor.execute("SELECT Mobile from user WHERE UserID = '"+str(UserID)+"'")
			rowcursor=mycursor.fetchall()
			mycursor.execute("UPDATE user SET Mobile = '"+str(MobileNo)+"',Password = '"+str(MobileNo)+"'WHERE UserID = '"+str(UserID)+"'")
			mydb.commit()
			return jsonify ({'Message':'Mobile Number Successfully Update',
						'Mobile':MobileNo,
						'Status':"1"})
							
api.add_resource(ProfileUpdate, "/MobileUpdate")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class Newclaim(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=str, help='UserID Id cannot be found')
		parser.add_argument('Content',required=True,type=str, help='Content Id cannot be found')
		parser.add_argument('DateOfIncident',required=True,type=str, help='DateOfIncident Id cannot be found')
		parser.add_argument('DateOfClaim',required=True,type=str, help='DateofClaim cannot be found')
		parser.add_argument('AreaName',required=True,type=str, help='AreaName cannot be found')
		parser.add_argument('PoliceStation',required=True,type=str, help='Police station cannot be found')
		parser.add_argument('District',required=True,type=str, help='District cannot be found')
		parser.add_argument('State',required=True,type=str, help='State cannot be found')
		parser.add_argument('Video',type=werkzeug.datastructures.FileStorage,required=False, help='Video/Photo cannot be found',location='files')
		args = parser.parse_args()
		UserID = args['UserID']
		Content = args['Content']
		DateOfIncident = args['DateOfIncident']
		DateOfClaim = args['DateOfClaim']
		AreaName = args['AreaName']
		Ps = args['PoliceStation']
		Dist = args['District']
		State = args['State']
		file = args['Video']
		ClaimNos = ClaimNo()
		print(ClaimNos)
		if not file is None:
			filename=Upload_fun(file)
			CurrentTime = datetime.datetime.now()
			sql = "INSERT INTO claim (ClaimNo,UserID,Content,DateOfIncident,DateOfClaim,AreaName,Ps,District,State,VehiclesaffectedAreaVideo,Ondate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (ClaimNos,UserID,Content,DateOfIncident,DateOfClaim,AreaName,Ps,Dist,State,filename,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			
			return jsonify ({
			'Message':"You submit your claim successfully.",
			'Content':Content,
			'DateOfIncident':DateOfIncident,
			'DateOfClaim':DateOfClaim,
			'AreaName':AreaName,
			'Police Station':Ps,
			'District':Dist,
			'State':State,
			'Status':"1",
			'video':filename})
		else:
			CurrentTime = datetime.datetime.now()
			sql = "INSERT INTO claim (ClaimNo,UserID,Content,DateOfIncident,DateOfClaim,AreaName,Ps,District,State,Ondate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (ClaimNos,UserID,Content,DateOfIncident,DateOfClaim,AreaName,Ps,Dist,State,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			
			return jsonify ({
			'Message':"You submit your claim successfully. ",
			'Content':Content,
			'DateOfIncident':DateOfIncident,
			'DateOfClaim':DateOfClaim,
			'AreaName':AreaName,
			'Police Station':Ps,
			'District':Dist,
			'State':State,
			'Status':"1",
			'video':'Video filed is blank'})
			
			
api.add_resource(Newclaim, "/NewCustomerClaim")
####when user want to check his/her status
class claimStatus(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=int, help='UserID Id cannot be found')
		args = parser.parse_args()
		UserID = args['UserID']
		mycursor.execute("SELECT claim.UserID, claiminspection.ClaimDate,claiminspection.RegdNo,claiminspection.ClaimStatus FROM claim LEFT JOIN claiminspection ON claim.ClaimNo=claiminspection.ClaimNo where claim.ClaimNo=claiminspection.ClaimNo AND claim.UserID = "+str(UserID))
		
		rowcursor=mycursor.fetchall()
		if len(rowcursor) > 0:
			for i in rowcursor:
				print(rowcursor)
				UserID = i[0]
				ClaimDate = i[1]
				RegdNo = i[2]
				ClaimStatus = i[3]
				return jsonify ({'Message':" Successfully claim recorded.",
				'UserID':UserID,
				'ClaimDate':ClaimDate,
				'RegistrationNo':RegdNo,
				'ClaimStatus':ClaimStatus,
				'Status':'1'})
			
		else:
			return jsonify ({'Message':"You have no claim in your status.",'Status':"0"})
				
	
api.add_resource(claimStatus, "/ClaimStatus")

##------------------------------------SALES MANAGER-------------------------------------------------

class SalesReport(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID' ,required=True,type=int, help='UserID Id cannot be found')
		args = parser.parse_args()
		UserID = args['UserID']
		mycursor.execute("SELECT Date,VehicleCategory from user WHERE UserID = '"+str(UserID)+"'")
		rowcursor=mycursor.fetchall()
		if len(rowcursor) > 0:
			for i in rowcursor:
				Date = i[0]
				VehicleCategory = i[1]
			
				return jsonify ({
					'Date':Date,
					'VehicleCategory':VehicleCategory,
					'Status':"1"})
		else:
			return jsonify ({'Message':"Error","Status":0})
				
api.add_resource(SalesReport, "/getSalesReport")
###### sales manager check claim
class ClaimActionSM(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('ClaimInspectionID' ,required=True,type=int, help='ClaimInspectionId cannot be found')
		args = parser.parse_args()
		mycursor.execute("UPDATE claiminspection set ClaimStatus = 1 WHERE ClaimInspectionID='"+str(ClaimInspectionID)+"'")
		rowcursor=mycursor.fetchall()
		new.append(data)
		return jsonify ({
					'Status':"1"})
		
api.add_resource(ClaimActionSM, "/ClaimActionSM")


class ClaimViewSM(Resource):
	def get(self):
		new = []
		mycursor.execute("SELECT claim.DateOfClaim,claim.ClaimNo,claim.UserID,claiminspection.ClaimInspectionID,claiminspection.ClaimStatus FROM claim LEFT JOIN claiminspection ON claim.ClaimNo=claiminspection.ClaimNo where claim.ClaimNo=claiminspection.ClaimNo")
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			DateOfClaim = i[0]
			ClaimNo = i[1]
			UserID = i[2]
			ClaimInspectionID = i[3]
			ClaimStatus = i[4]
			mycursor.execute("SELECT Name from user WHERE UserID = '"+str(UserID)+"'")
			rowcursor=mycursor.fetchall()
			for i in rowcursor:
				Name = i[0]
				data = ({'Name':Name,'DateOfClaim':DateOfClaim,'ClaimNo':ClaimNo,'ClaimInspectionID':ClaimInspectionID,'ClaimStatus':ClaimStatus})
				new.append(data)
		return jsonify({'Status':1,'new':new})
		
api.add_resource(ClaimViewSM, "/ClaimViewSM")

class VehicleContract(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=str, help='UserID cannot be found')
		parser.add_argument('PaymentMode',required=True,type=str, help='PayementMode cannot be found')
		parser.add_argument('Amount',required=True,type=str, help='Amount Id cannot be found')
		parser.add_argument('DateOfContract',required=True,type=str, help='DateOfContract Id cannot be found')
		parser.add_argument('VehicleCategory',required=True,type=str, help='VehicleCategory Id cannot be found')
		parser.add_argument('VehicleNo',required=True,type=str, help='VehicleNo cannot be found')
		parser.add_argument('Maker',required=True,type=str,help='Maker cannot be found')
		parser.add_argument('Model',required=True,type=str,help='Model cannot be found')
		parser.add_argument('ChassisNo',required=True,type=str,help='ChassisNo  cannot be found')
		parser.add_argument('Color',required=True,type=str,help='Color  cannot be found')
		parser.add_argument('RegdNo',required=True,type=str,help='RegdNo  cannot be found')
		parser.add_argument('DateofRegd',required=True,type=str,help='DateofRegd  cannot be found')
		parser.add_argument('OwnerName',required=True,type=str,help='OwnerName  cannot be found')
		parser.add_argument('Mobile',required=True,type=str,help='MobileNo cannot be found')
		parser.add_argument('Email',required=True,type=str,help='Email Id cannot be found')
		parser.add_argument('Location',required=True,type=str,help='Location cannot be found')
		parser.add_argument('PostOffice',required=True,type=str,help='PostOfficcannot be found')
		parser.add_argument('PoliceStation',required=True,type=str,help='PoliceStation Id cannot be found')
		parser.add_argument('District',required=True,type=str,help='District cannot be found')
		parser.add_argument('State',required=True,type=str,help='State cannot be found')
		parser.add_argument('Video',type=werkzeug.datastructures.FileStorage,required=False, help='Video cannot be found',location='files')
		args = parser.parse_args()
		PaymentMode = (args['PaymentMode'].upper())
		Amount = args['Amount']
		DateOfContract = args['DateOfContract']
		VehicleNo = args['VehicleNo']
		VehicleCategory = args['VehicleCategory']
		Maker = args['Maker']
		Model = args['Model']
		ChassisNo = args['ChassisNo']
		Color = args['Color']
		RegdNo = args['RegdNo']
		DateofRegd = args['DateofRegd']
		OwnerName = args['OwnerName']
		MobileNo = args['Mobile']
		Email = args['Email']
		Location = args['Location']
		PostOffice = args['PostOffice']
		PoliceStation = args['PoliceStation']
		District = args['District']
		State = args['State']
		file = args['Video']
		AddedBy = args['UserID']
		EmployeeId = RegisterNo()
		RoleID = 2
		
		if not file is None:
			Video=Upload_fun(file)
			CurrentTime = datetime.datetime.now()
			sql = "INSERT INTO user (EmployeeId,RoleID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,RegdNo,DateofRegd,Name,Mobile,Email,CenterLocation,Po,Ps,District,State,VehiclePhoto,Password,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (EmployeeId,RoleID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,RegdNo,DateofRegd,OwnerName,MobileNo,Email,Location,PostOffice,PoliceStation,District,State,Video,MobileNo,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			UserID = mycursor.lastrowid
			sql = "INSERT INTO vehiclecontract (AddedBy,UserID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,RegdNo,DateofRegd,OwnerName,Mobile,Email,Location,Po,Ps,District,State,VehicleVideo,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (AddedBy,UserID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,RegdNo,DateofRegd,OwnerName,MobileNo,Email,Location,PostOffice,PoliceStation,District,State,Video,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			sql = "INSERT INTO paymentrequest (UserID,Paymenttype,Amount,OnDate) VALUES (%s,%s,%s,%s)"
			val = (UserID,PaymentMode,Amount,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			return jsonify ({'Message':'Payment Confirmed we will send certificate within 48 Hours.'+EmployeeId,"RoleID":RoleID,"Status":1,"UserID":UserID})
			
		else:
			CurrentTime = datetime.datetime.now()
			sql = "INSERT INTO user (EmployeeId,RoleID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,RegdNo,DateofRegd,Name,Mobile,Email,CenterLocation,Po,Ps,District,State,Password,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (EmployeeId,RoleID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,RegdNo,DateofRegd,OwnerName,MobileNo,Email,Location,PostOffice,PoliceStation,District,State,MobileNo,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			UserID = mycursor.lastrowid
			sql = "INSERT INTO vehiclecontract (AddedBy,UserID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,RegdNo,DateofRegd,OwnerName,Mobile,Email,Location,Po,Ps,District,State,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (AddedBy,UserID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,RegdNo,DateofRegd,OwnerName,MobileNo,Email,Location,PostOffice,PoliceStation,District,State,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			sql = "INSERT INTO paymentrequest (UserID,Paymenttype,Amount,OnDate) VALUES (%s,%s,%s,%s)"
			val = (UserID,PaymentMode,Amount,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			
			return jsonify ({'Message':'Payment Confirmed we will send certificate within 48 Hours.'+EmployeeId,"RoleID":RoleID,"Status":1,"UserID":UserID})
			

api.add_resource(VehicleContract, "/getVehicleContract")

class ServiceCenterAuthorization(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=str, help='UserID Id cannot be found')
		parser.add_argument('DateOfAuthorisation',required=True,type=str, help='DateOfAuthorisation Id cannot be found')
		parser.add_argument('CenterName',required=True,type=str, help='CenterName Id cannot be found')
		parser.add_argument('OwnerName',required=True,type=str, help='OwnerName Id cannot be found')
		parser.add_argument('MobileNo',required=True,type=str, help='MobileNo Id cannot be found')
		parser.add_argument('GSTINNumber',required=True,type=str, help='GSTINNumber Id cannot be found')
		parser.add_argument('CenterLocation',required=True,type=str, help='CenterLocation Id cannot be found')
		parser.add_argument('Town',required=True,type=str, help='Town Id cannot be found')
		parser.add_argument('PostOffice',required=True,type=str, help='PostOffice Id cannot be found')
		parser.add_argument('PoliceStation',required=True,type=str, help='PoliceStation Id cannot be found')
		parser.add_argument('District',required=True,type=str, help='District Id cannot be found')
		parser.add_argument('State',required=True,type=str, help='State Id cannot be found')
		parser.add_argument('DentingPainting',required=True,type=int, help='DentingPainting Id cannot be found')
		parser.add_argument('Mechanical',required=True,type=int, help='Mechanical Id cannot be found')
		parser.add_argument('Working',required=True,type=str, help='Working Id cannot be found')
		parser.add_argument('Video',type=werkzeug.datastructures.FileStorage,required=False, help='shine board Photo Copy cannot be found',location='files')
		parser.add_argument('imageData',type=str,required=False,help='Photo From Camera')
		args = parser.parse_args()
		AddedBy = args['UserID']
		DateOfAuthorisation = args['DateOfAuthorisation']
		CenterName = args['CenterName']
		OwnerName = args['OwnerName']
		MobileNo = args['MobileNo']
		GSTINNumber = args['GSTINNumber']
		CenterLocation = args['CenterLocation']
		Town = args['Town']
		PostOffice = args['PostOffice']
		PoliceStation = args['PoliceStation']
		District = args['District']
		State = args['State']
		DentingPainting = args['DentingPainting']
		Mechanical = args['Mechanical']
		Working = args['Working']
		file = args['Video']
		Photo= args['imageData']
		CurrentTime = datetime.datetime.now()
		EmployeeId = EmpId()
		RoleID = 5
		if not Photo is None and file is None :
			Photo=save(Photo)
			sql = "INSERT INTO user (Password,EmployeeId,RoleID,DateOfAuthorize,NameCenter,Name,Mobile,GSTINno,CenterLocation,Town,Po,Ps,District,State,DentingPainting,Mechanical,WorkingFor,ShineBoardPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (MobileNo,EmployeeId,RoleID,DateOfAuthorisation,CenterName,OwnerName,MobileNo,GSTINNumber,CenterLocation,Town,PostOffice,PoliceStation,District,State,DentingPainting,Mechanical,Working,Photo,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			UserID = mycursor.lastrowid
			sql = "INSERT INTO servicecenterauthorize (AddedBy,EmployeeId,UserID,DateOfAuthorize,CenterName,OwnerName,MobileNo,GSTINno,CenterLocation,Town,Po,Ps,District,State,DentingPainting,Mechanical,WorkingFor,ShineBoardPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (AddedBy,EmployeeId,UserID,DateOfAuthorisation,CenterName,OwnerName,MobileNo,GSTINNumber,CenterLocation,Town,PostOffice,PoliceStation,District,State,DentingPainting,Mechanical,Working,Photo,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			return jsonify ({'Message':"Service Center Authorized Successfully","RoleID":RoleID,"Status":1,"UserID":UserID})
		elif not file is None and Photo is None :
			video=Upload_fun(file)
			sql = "INSERT INTO user (Password,EmployeeId,RoleID,DateOfAuthorize,NameCenter,Name,Mobile,GSTINno,CenterLocation,Town,Po,Ps,District,State,DentingPainting,Mechanical,WorkingFor,ShineBoardPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (MobileNo,EmployeeId,RoleID,DateOfAuthorisation,CenterName,OwnerName,MobileNo,GSTINNumber,CenterLocation,Town,PostOffice,PoliceStation,District,State,DentingPainting,Mechanical,Working,video,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			UserID = mycursor.lastrowid
			sql = "INSERT INTO servicecenterauthorize (AddedBy,EmployeeId,UserID,DateOfAuthorize,CenterName,OwnerName,MobileNo,GSTINno,CenterLocation,Town,Po,Ps,District,State,DentingPainting,Mechanical,WorkingFor,ShineBoardPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (AddedBy,EmployeeId,UserID,DateOfAuthorisation,CenterName,OwnerName,MobileNo,GSTINNumber,CenterLocation,Town,PostOffice,PoliceStation,District,State,DentingPainting,Mechanical,Working,video,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			
			return jsonify ({'Message':"Service Center Authorized Successfully","RoleID":RoleID,"Status":1,"UserID":UserID})

		
									
api.add_resource(ServiceCenterAuthorization, "/getServiceCenterAuthorization")


class ClaimInspection(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID' ,required=True,type=str, help='UserID Id cannot be found')
		parser.add_argument('ClaimNo' ,required=True,type=str, help='ClaimNo Id cannot be found')
		parser.add_argument('VehicleNo' ,required=True,type=str, help='VehicleNo Id cannot be found')
		parser.add_argument('ChassisNo' ,required=True,type=str, help='ChassisNo Id cannot be found')
		parser.add_argument('Content' ,required=True,type=str, help='Content Id cannot be found')
		parser.add_argument('Video',type=werkzeug.datastructures.FileStorage,required=False, help='photo cannot be found',location='files')
		parser.add_argument('imageData',type=str,required=False,help='Photo From Camera')
		args = parser.parse_args()
		UserID = args['UserID']
		ClaimNo = args['ClaimNo']
		VehicleNo = args['VehicleNo']
		ChassisNo = args['ChassisNo']
		Content = args['Content']
		file = args['Video']
		Photo= args['imageData']
		CurrentTime = datetime.datetime.now()		
		if not file is None and Photo is None :
			filename=Upload_fun(file)
			sql = "INSERT INTO claiminspection (InspectBy,OnDate,ClaimNo,ChassisNo,VehicleNo,Content,photo) VALUES (%s,%s,%s,%s,%s,%s,%s)"
			val=(UserID,CurrentTime,ClaimNo,ChassisNo,VehicleNo,Content,filename)
			result = mycursor.execute(sql,val)
			mydb.commit()
			return jsonify ({'Message':" claim inspection successfully","Status":1})
		elif not Photo is None and file is None :
			Photo=save(Photo)
			sql = "INSERT INTO claiminspection (InspectBy,OnDate,ClaimNo,ChassisNo,VehicleNo,Content,photo) VALUES (%s,%s,%s,%s,%s,%s,%s)"
			val=(UserID,CurrentTime,ClaimNo,ChassisNo,VehicleNo,Content,Photo)
			result = mycursor.execute(sql,val)
			mydb.commit()
			return jsonify ({'Message':" claim inspection successfully","Status":1})
				
	
api.add_resource(ClaimInspection, "/claimInspectionSM")
###------------------------------sales manager part over-----------------------------------------
###------------------------------Area manager part start-----------------------------------------
class AdminAddSM(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=str, help='UserID cannot be found')
		parser.add_argument('DateOfJoining',required=True,type=str, help='DateOfJoining cannot be found')
		parser.add_argument('Name',required=True,type=str, help='Name cannot be found')
		parser.add_argument('DOB',required=True,type=str, help='DOB cannot be found')
		parser.add_argument('Qualification',required=True,type=str, help='Qualification  cannot be found')
		parser.add_argument('AdharNo',required=True,type=int, help='AdharNo cannot be found')
		parser.add_argument('MobileNo',required=True,type=str, help='MobileNo cannot be found')
		parser.add_argument('EmailId',required=True,type=str, help='EmailId cannot be found')
		parser.add_argument('BankAccountNo',required=True,type=str, help='BankAccountNo Id cannot be found')
		parser.add_argument('IFSC',required=True,type=str, help='IFSC  cannot be found')
		parser.add_argument('BankName',required=True,type=str, help='BankName cannot be found')
		parser.add_argument('PresentlyWorking',required=True,type=str, help='PresentlyWorking Id cannot be found')
		parser.add_argument('AppointCenter',required=True,type=str, help='AppointCenter cannot be found')
		parser.add_argument('NameCenter',required=True,type=str, help='NameCenter cannot be found')
		parser.add_argument('CenterBrand',required=True,type=str, help='CenterBrand cannot be found')
		parser.add_argument('CenterFor',required=True,type=str, help='CenterFor cannot be found')
		parser.add_argument('CenterLocation',required=True,type=str, help='CenterLocation cannot be found')
		parser.add_argument('PostOffice',required=True,type=str, help='PostOffice cannot be found')
		parser.add_argument('PoliceStation',required=True,type=str, help='PoliceStation cannot be found')
		parser.add_argument('District',required=True,type=str, help='District cannot be found')
		parser.add_argument('State',required=True,type=str, help='State cannot be found')
		parser.add_argument('CenterContactNo',required=True,type=str, help='CenterContactNo cannot be found')
		parser.add_argument('IdProofPhoto',type=werkzeug.datastructures.FileStorage,required=False,help='IdProofPhoto cannot be found',location='files')
		parser.add_argument('imageData',type=str,required=False,help='Photo From Camera')
		args = parser.parse_args()
		AddedBy = args['UserID']
		DateOfJoining = args['DateOfJoining']
		Name = args['Name']
		DOB = args['DOB']
		Qualification = args['Qualification']
		AdharNo = args['AdharNo']
		MobileNo = args['MobileNo']
		EmailId = args['EmailId']
		BankAccountNo = args['BankAccountNo']
		IFSC = args['IFSC']
		BankName = args['BankName']
		PresentlyWorking = args['PresentlyWorking']
		AppointCenter = args['AppointCenter']
		NameCenter = args['NameCenter']
		CenterBrand = args['CenterBrand']
		CenterFor = args['CenterFor']
		CenterLocation = args['CenterLocation']
		PostOffice = args['PostOffice']
		PoliceStation = args['PoliceStation']
		District = args['District']
		State = args['State']
		CenterContactNo = args['CenterContactNo']
		CurrentTime = datetime.datetime.now()
		EmployeeId = EmpId()
		file = args['IdProofPhoto']
		Photo= args['imageData']
		RoleID = 3
		if not file is None and Photo is None :
			
			filename=Upload_fun(file)
			print(filename)
			sql = "INSERT INTO user (Password,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,Mobile,Email,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,Sale_ScFor,CenterLocation,Po,Ps,District,State,CenterContctNo,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(MobileNo,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation,PostOffice,PoliceStation,District,State,CenterContactNo,filename,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			UserID = mycursor.lastrowid
			sql = "INSERT INTO salesmanager (AddedBy,UserID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,Sale_ScFor,CenterLocation	,Po,Ps,District,State,CenterContctNo,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(AddedBy,UserID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation,PostOffice,PoliceStation,District,State,CenterContactNo,filename,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			return jsonify ({'Message':" SalesManager successfully Added",
			"Status":1,
			"RoleID":RoleID})	
			
		if not Photo is None and file is None :
			Photo=save(Photo)
			sql = "INSERT INTO user (Password,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,Mobile,Email,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,Sale_ScFor,CenterLocation,Po,Ps,District,State,CenterContctNo,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(MobileNo,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation,PostOffice,PoliceStation,District,State,CenterContactNo,Photo,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			UserID = mycursor.lastrowid
			sql = "INSERT INTO salesmanager (AddedBy,UserID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,Sale_ScFor,CenterLocation	,Po,Ps,District,State,CenterContctNo,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(AddedBy,UserID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation,PostOffice,PoliceStation,District,State,CenterContactNo,Photo,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			return jsonify ({'Message':" SalesManager successfully Added",
			"Status":1,
			"RoleID":RoleID})	
			
api.add_resource(AdminAddSM, "/AppointSM")

class SMTeam(Resource):
	def get(self):
		new = []
		mycursor.execute("SELECT Name,NameCenter,CenterLocation,District,Sale_ScFor,MobileNo FROM salesmanager")
		row=mycursor.fetchall()
		for i in row:
			Name = i[0]
			NameCenter = i[1]
			CenterLocation = i[2]
			District = i[3]
			CenterFor = i[4]
			MobileNo = i[5]
			data = {'Name':Name,'NameCenter':NameCenter,'CenterLocation':CenterLocation,'District':District,'CenterFor':CenterFor,'MobileNo':MobileNo}
			new.append(data)
		return jsonify({'Status':1,'new':new})
api.add_resource(SMTeam, "/SMTeam")

# class MyTeamSalesRpt(Resource):
	# def get(self):
	# new = []
	# mycursor.execute("SELECT Name,NameCenter,CenterLocation,District,Sale_ScFor,MobileNo FROM salesmanager")
	# row=mycursor.fetchall()
	
if __name__ == '__main__':
	app.run(port='5000',host='0.0.0.0',debug=False)
  