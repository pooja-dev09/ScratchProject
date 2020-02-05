from flask import Flask,session, jsonify,request
from flask_restful import Api, Resource,reqparse,request
import mysql.connector
import datetime
import json 
from decimal import Decimal
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
		parser.add_argument('Name',required=True,type=str,help='UserName cannot be found')
		parser.add_argument('MobileNo',required=True,type=int,help='MobileNo cannot be found')
		parser.add_argument('VehicleCategory', required=True,type=str,help='VehicleCategory cannot be found')
		parser.add_argument('DateOfPurchase',required=True,type=str,help='DateOfPurchase cannot be found')
		parser.add_argument('PoliceStation',required=True,type=str, help='PoliceStation cannot be found')
		parser.add_argument('District',required=True,type=str, help='District cannot be found')
		parser.add_argument('State',required=True,type=str, help='State cannot be found')
		args = parser.parse_args()
		Name = args['Name']
		MobileNo = str(args['MobileNo'])
		VehicleCategory = args['VehicleCategory']
		DateOfPurchase = args['DateOfPurchase']
		PoliceStation = args['PoliceStation']
		District = args['District']
		State = args['State']
		CurrentTime = datetime.datetime.now()
		CurrentTime = CurrentTime.strftime("%m-%d-%Y")
		if validNumber(MobileNo)== True :
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
		parser.add_argument('UserName' ,required=True,type=str, help='UserName cannot be found')
		parser.add_argument('Password',required=True,type=str, help='Password cannot be found')
		args = parser.parse_args()
		RoleID = args['RoleID']
		print('bdijbvdf',RoleID)
		UserName = args['UserName']
		UserPassword = args['Password']
		UserPassword=Password_encoded(UserPassword)
		print('UserPassword:',UserPassword)
		if RoleID == 2:
			mycursor.execute("SELECT UserID,RoleID,Mobile from user WHERE VehicleNo = '%s' AND Password = '%s'" % (UserName, UserPassword))
			rowcursor=mycursor.fetchall()
			print(rowcursor)
			if len(rowcursor) > 0:
				for i in rowcursor:
					UserID = i[0]
					RoleID = i[1]
					Mobile = i[2]
					OTP=generateOTP()
					msg='Dear Customer, Your One Time Password for Account Login is : '+str(OTP)
					#SMS_Integration(msg,Mobile)
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
			mycursor.execute("SELECT UserID,Mobile from user WHERE EmployeeId = '%s' AND Password = '%s'" % (UserName, UserPassword))
			rowcursor=mycursor.fetchall()
			print('dkjcjvd',rowcursor)
			length =len(rowcursor)
			if length > 0:
				for i in rowcursor:
					UserID = i[0]
					OTP=generateOTP()
					msg='Dear Customer, Your One Time Password for Account Login is : '+str(OTP)
					#SMS_Integration(msg,Mobile)
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
		mycursor.execute("SELECT OTP ,UserID, Mobile from user WHERE UserID = '"+str(UserID)+"'")
		rowcursor=mycursor.fetchall()
		if len(rowcursor) > 0:
			for i in rowcursor:
				OTP = i[0]
				UserID = i[1]
				Mobile = i[2]
				OTP=generateOTP()
				msg='Dear Customer, Your One Time Password for Account Login is : '+str(OTP)
				#SMS_Integration(msg,Mobile)
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
			sql = mycursor.execute("SELECT EmployeeId,Name,VehicleNo,Mobile,DateOfRegd,DateOfExp from user WHERE UserID = '"+str(UserID)+"'")
			rowcursor=mycursor.fetchall()
			if len(rowcursor) > 0:
				for i in rowcursor:
					EmployeeId = i[0]
					Name = i[1]
					VehicleNo=i[2]
					Mobile = i[3]
					DateOfRegd = i[4]
					DateOfExp = i[5]
					return jsonify ({'Message':'Result View Successfully',
									'RegdNo':EmployeeId,
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
		MobileNo = str(args['MobileNo'])
		if MobileNo != "":
			password = Password_encoded(MobileNo)
			mycursor.execute("SELECT Mobile from user WHERE UserID = '"+str(UserID)+"'")
			rowcursor=mycursor.fetchall()
			mycursor.execute("UPDATE user SET Mobile = '"+str(MobileNo)+"',Password = '"+str(password)+"'WHERE UserID = '"+str(UserID)+"'")
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
		parser.add_argument('DateOfIncident',required=True,type=str, help='DateOfIncident Id cannot be found')
		parser.add_argument('DateOfClaim',required=True,type=str, help='DateofClaim cannot be found')
		parser.add_argument('AreaName',required=True,type=str, help='AreaName cannot be found')
		parser.add_argument('PoliceStation',required=True,type=str, help='Police station cannot be found')
		parser.add_argument('District',required=True,type=str, help='District cannot be found')
		parser.add_argument('State',required=True,type=str, help='State cannot be found')
		parser.add_argument('Video',type=werkzeug.datastructures.FileStorage,required=False, help='Video/Photo cannot be found',location='files')
		args = parser.parse_args()
		UserID = args['UserID']
		DateOfIncident = args['DateOfIncident']
		DateOfClaim = args['DateOfClaim']
		AreaName = args['AreaName']
		Ps = args['PoliceStation']
		Dist = args['District']
		State = args['State']
		file = args['Video']
		mycursor.execute("SELECT count(*) as totalval from claim")
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			totalval = i[0]
		ClaimNos = ClaimNo(totalval)
		mycursor.execute("SELECT VcID,Mobile from vehiclecontract WHERE UserID = '"+str(UserID)+"'")
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			VcID = i[0]
			Mobile = i[1] 
		if not file is None:
			filename=Upload_fun(file)
			CurrentTime = datetime.datetime.now()
			CurrentTime = CurrentTime.strftime("%m-%d-%Y")
			sql = "INSERT INTO claim (ClaimNo,VcID,UserID,DateOfIncident,DateOfClaim,AreaName,Ps,District,State,VehiclesaffectedAreaVideo,Ondate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (ClaimNos,VcID,UserID,DateOfIncident,DateOfClaim,AreaName,Ps,Dist,State,filename,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			#msg = 'You submit your claim successfully'+str(ClaimNos)
			#SMS_Integration(msg,Mobile)
			return jsonify ({
			'Message':"You submit your claim successfully.",
			'DateOfIncident':DateOfIncident,
			'DateOfClaim':DateOfClaim,
			'AreaName':AreaName,
			'Police Station':Ps,
			'District':Dist,
			'State':State,
			'Status':"1",
			'video':filename})
	
api.add_resource(Newclaim, "/NewCustomerClaim")

class claimAmount(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=str, help='UserID Id cannot be found')
		parser.add_argument('PaymentMode',required=True,type=str, help='Paymenttype cannot be found')
		parser.add_argument('Video',type=werkzeug.datastructures.FileStorage,required=True, help='Video/Photo cannot be found',location='files')
		args = parser.parse_args()
		UserID = args['UserID']
		print('sdkjbccbdis')
		Paymenttype = str(args['PaymentMode'])
		print(Paymenttype)
		print('skjdcjdh')
		file = args['Video']
		if Paymenttype == 'online':
			parser.add_argument('BankName',required=True,type=str, help='BankName Id cannot be found')
			parser.add_argument('BankAccountNo',required=True,type=int, help='BankAccountNo Id cannot be found')
			parser.add_argument('IFSC',required=True,type=str, help='IFSC Id cannot be found')
			args = parser.parse_args()
			BankAccountNo = args['BankAccountNo']
			BankName = args['BankName']
			IFSC = args['IFSC']
			filename=Upload_fun(file)
			CurrentTime = datetime.datetime.now()
			CurrentTime = CurrentTime.strftime("%m-%d-%Y")
			mycursor.execute("UPDATE claim SET AccountNumber = '"+str(BankAccountNo)+"',IFSC ='"+str(IFSC)+"', MoneyReceiptPhoto = '"+str(filename)+"',BankName = '"+str(BankName)+"' , OnDate = '"+str(CurrentTime)+"' WHERE UserID = '"+str(UserID)+"' ")
			mydb.commit()
			return jsonify ({
			'Message':"You submit your claim successfully;we send your claim amount within one working day",
			'Status':"1",
			})
			
		else:
			
			parser.add_argument('UPI',required=True,type=str, help='UPI cannot be found')
			parser.add_argument('WalletName',required=True,type=str, help='WalletName cannot be found')
			args = parser.parse_args()
			UPI = args['UPI']
			print('UPI',UPI)
			WalletName = args['WalletName']
			print('WalletName',WalletName)
			filename=Upload_fun(file)
			CurrentTime = datetime.datetime.now()
			CurrentTime = CurrentTime.strftime("%m-%d-%Y")
			mycursor.execute("UPDATE claim SET UPI = '"+str(UPI)+"', MoneyReceiptPhoto = '"+str(filename)+"',WalletName = '"+str(WalletName)+"' , OnDate = '"+str(CurrentTime)+"' WHERE UserID = '"+str(UserID)+"' ")
			mydb.commit()
			return jsonify ({
			'Message':"You submit your claim successfully;we send your claim amount within one working day",
			'Status':"1",
			})
api.add_resource(claimAmount,"/claimAmount")



####when user want to check his/her status
class claimStatus(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=int, help='UserID Id cannot be found')
		args = parser.parse_args()
		UserID = args['UserID']
		mycursor.execute("SELECT claim.DateOfClaim,claim.VcID,claiminspection.ClaimStatus FROM claim LEFT JOIN claiminspection ON claim.ClaimID=claiminspection.ClaimID where claim.UserID = "+str(UserID))
		rowcursor=mycursor.fetchall()
		if len(rowcursor) > 0:
			for i in rowcursor:
				ClaimDate = i[0]
				VcID = i[1]
				ClaimStatus = i[2]
				if ClaimStatus is None:
					ClaimStatus = 0
				mycursor.execute("SELECT VehicleNo from vehiclecontract where VcID = "+str(VcID))
				rowcursor=mycursor.fetchall()
				for i in rowcursor:
					VehicleNo = i[0]
					return jsonify ({'Message':" Successfully claim recorded.",
					'ClaimDate':ClaimDate,
					'VehicleNo':VehicleNo,
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
class ClaimAction(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('ClaimID' ,required=True,type=int, help='ClaimID cannot be found')
		args = parser.parse_args()
		Amount = args['ClaimID']
		mycursor.execute("SELECT claim.ClaimNo,vehiclecontract.VehicleNo,vehiclecontract.ChassisNo FROM claim LEFT JOIN vehiclecontract ON claim.VcID=vehiclecontract.VcID where claim.VcID=vehiclecontract.VcID")
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			ClaimNo = i[0]
			VehicleNo = i[1]
			ChassisNo = i[2]
		return jsonify ({'Status':"1",'ClaimNo':ClaimNo,'VehicleNo':VehicleNo,'ChassisNo':ChassisNo})
		
api.add_resource(ClaimAction, "/ClaimAction")


class ClaimViewSM(Resource):
	def get(self):
		new = []
		arraynew=[]
		mycursor.execute("SELECT claim.DateOfClaim,claim.ClaimNo,claim.UserID,claim.ClaimID,claiminspection.ClaimStatus FROM claim LEFT JOIN claiminspection ON claim.ClaimID=claiminspection.ClaimID ")
		rowcursor=mycursor.fetchall()
		if len(rowcursor) > 0:
			for i in rowcursor:
				DateOfClaim = i[0]
				ClaimNo = i[1]
				UserID = i[2]
				ClaimID = i[3]
				ClaimStatus = i[4]
				if ClaimStatus is None:
					ClaimStatus = 0
				mycursor.execute("SELECT Name from user WHERE UserID = '"+str(UserID)+"'")
				rowcursor=mycursor.fetchall()
				for i in rowcursor:
					name=i[0]
				data = {'DateOfClaim':DateOfClaim,'ClaimNo':ClaimNo,'name':name,'ClaimID':ClaimID,'ClaimStatus':ClaimStatus}
				new.append(data)
					
			return jsonify({'Status':1,'new':new})
		
api.add_resource(ClaimViewSM, "/ClaimViewSM")


class VehicleContract(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=str, help='UserID cannot be found')
		parser.add_argument('PaymentMode',required=True,type=str, help='PayementMode cannot be found')
		parser.add_argument('DateOfContract',required=True,type=str, help='DateOfContract Id cannot be found')
		parser.add_argument('VehicleCategory',required=True,type=str, help='VehicleCategory Id cannot be found')
		parser.add_argument('VehicleNo',required=True,type=str, help='VehicleNo cannot be found')
		parser.add_argument('Maker',required=True,type=str,help='Maker cannot be found')
		parser.add_argument('Model',required=True,type=str,help='Model cannot be found')
		parser.add_argument('ChassisNo',required=True,type=str,help='ChassisNo  cannot be found')
		parser.add_argument('Color',required=True,type=str,help='Color  cannot be found')
		parser.add_argument('DateofRegd',required=True,type=str,help='DateofRegd  cannot be found')
		parser.add_argument('Package',required=True,type=str,help='Package  cannot be found')
		parser.add_argument('OwnerName',required=True,type=str,help='OwnerName  cannot be found')
		parser.add_argument('Mobile',required=True,type=int,help='MobileNo cannot be found')
		parser.add_argument('Email',required=True,type=str,help='Email Id cannot be found')
		parser.add_argument('Location',required=True,type=str,help='Location cannot be found')
		parser.add_argument('PostOffice',required=True,type=str,help='PostOfficcannot be found')
		parser.add_argument('PoliceStation',required=True,type=str,help='PoliceStation Id cannot be found')
		parser.add_argument('District',required=True,type=str,help='District cannot be found')
		parser.add_argument('State',required=True,type=str,help='State cannot be found')
		parser.add_argument('Video',type=werkzeug.datastructures.FileStorage,required=True, help='Video cannot be found',location='files')
		args = parser.parse_args()
		PaymentMode = (args['PaymentMode'].upper())
		Amount = args['Package']
		DateOfContract = args['DateOfContract']
		VehicleNo = args['VehicleNo']
		VehicleCategory = args['VehicleCategory']
		Maker = args['Maker']
		Model = args['Model']
		ChassisNo = args['ChassisNo']
		Color = args['Color']
		DateofRegd = args['DateofRegd']
		OwnerName = args['OwnerName']
		MobileNo = str(args['Mobile'])
		Email = args['Email']
		Location = args['Location']
		PostOffice = args['PostOffice']
		PoliceStation = args['PoliceStation']
		District = args['District']
		State = args['State']
		file = args['Video']
		AddedBy = args['UserID']
		mycursor.execute("SELECT count(*) as totalval from user")
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			totalval = i[0]
		EmployeeId = RegisterNo(totalval)
		password = Password_encoded(MobileNo)
		RoleID = 2
		
		if not file is None:
			Video=Upload_fun(file)
			CurrentTime = datetime.datetime.now()
			endDate= CurrentTime+datetime.timedelta(days=1*365)
			endDate = endDate.strftime("%m-%d-%Y")
			sql = "INSERT INTO user (EmployeeId,RoleID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,DateofRegd,Name,Mobile,Email,CenterLocation,Po,Ps,District,State,VehiclePhoto,Password,OnDate,DateOfExp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (EmployeeId,RoleID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,DateofRegd,OwnerName,MobileNo,Email,Location,PostOffice,PoliceStation,District,State,Video,password,CurrentTime,endDate)
			result = mycursor.execute(sql,val)
			mydb.commit()
			UserID = mycursor.lastrowid
			sql = "INSERT INTO vehiclecontract (AddedBy,UserID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,DateofRegd,OwnerName,Mobile,Email,Location,Po,Ps,District,State,VehicleVideo,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (AddedBy,UserID,DateOfContract,VehicleCategory,VehicleNo,Maker,Model,ChassisNo,Color,DateofRegd,OwnerName,MobileNo,Email,Location,PostOffice,PoliceStation,District,State,Video,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			sql = "INSERT INTO paymentrequest (UserID,Paymenttype,Amount,OnDate) VALUES (%s,%s,%s,%s)"
			val = (UserID,PaymentMode,Amount,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			
			#msg = 'Payment Confirmed we will send certificate within 48 Hours.'+str(EmployeeId)
			#SMS_Integration(msg,Mobile)
			
			return jsonify ({'Message':'Payment Confirmed we will send certificate within 48 Hours.'+EmployeeId,"RoleID":RoleID,"Status":1,"UserID":UserID})
		else:
			return jsonify ({'Message':'error',"Status":1})
		

api.add_resource(VehicleContract, "/getVehicleContract")



class getRange(Resource):
	def post(self):
		new = []
		parser = reqparse.RequestParser()
		parser.add_argument('VehicleType',required=True,type=str, help='VehicleType Id cannot be found')
		args = parser.parse_args()
		VehicleType = args['VehicleType']
		mycursor.execute("SELECT `RangeID`,`Range`,`Price` FROM vehiclerange WHERE Vehicle = '"+str(VehicleType)+"'" )
		row=mycursor.fetchall()
		for i in row:
			id = i[0]
			Range = i[1]
			Price = i[2]
			data = {'id':id,'Range':Range,'Price':Price}
			new.append(data)
		return jsonify({'Status':1,'new':new})	
api.add_resource(getRange, "/getRange")		


class ServiceCenterAuthorization(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=str, help='UserID Id cannot be found')
		parser.add_argument('DateOfAuthorisation',required=True,type=str, help='DateOfAuthorisation Id cannot be found')
		parser.add_argument('CenterName',required=True,type=str, help='CenterName Id cannot be found')
		parser.add_argument('OwnerName',required=True,type=str, help='OwnerName Id cannot be found')
		parser.add_argument('MobileNo',required=True,type=str,help='MobileNo Id cannot be found')
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
		MobileNo = str(args['MobileNo'])
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
		CurrentTime = CurrentTime.strftime("%m-%d-%Y")
		mycursor.execute("SELECT count(*) as totalval from user")
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			totalval = i[0]
		EmployeeId = EmpId(totalval)
		RoleID = 5
		UserPassword=Password_encoded(MobileNo)
		if not Photo is None and file is None :
			Photo=save(Photo)
			sql = "INSERT INTO user (Password,EmployeeId,RoleID,DateOfAuthorize,NameCenter,Name,Mobile,GSTINno,CenterLocation,Town,Po,Ps,District,State,DentingPainting,Mechanical,WorkingFor,ShineBoardPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val = (UserPassword,EmployeeId,RoleID,DateOfAuthorisation,CenterName,OwnerName,MobileNo,GSTINNumber,CenterLocation,Town,PostOffice,PoliceStation,District,State,DentingPainting,Mechanical,Working,Photo,CurrentTime)
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
			val = (UserPassword,EmployeeId,RoleID,DateOfAuthorisation,CenterName,OwnerName,MobileNo,GSTINNumber,CenterLocation,Town,PostOffice,PoliceStation,District,State,DentingPainting,Mechanical,Working,video,CurrentTime)
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
		parser.add_argument('ClaimID',required=True,type=str, help='UserID Id cannot be found')
		parser.add_argument('imageData',type=werkzeug.datastructures.FileStorage,required=True, help='photo cannot be found',location='files')
		args = parser.parse_args()
		ClaimID= args['ClaimID']
		Photo= args['imageData']
		CurrentTime = datetime.datetime.now()
		CurrentTime = CurrentTime.strftime("%m-%d-%Y")
		if not Photo is None:
			filename=Upload_fun(Photo)
			sql = "INSERT INTO claiminspection (ClaimID,photo,OnDate) VALUES (%s,%s,%s)"
			val=(ClaimID,filename,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			mycursor.execute("UPDATE claiminspection SET ClaimStatus = 1 WHERE ClaimID = '"+str(ClaimID)+"'")
			mydb.commit()
			return jsonify ({'Message':" claim inspection successfully","Status":1})
		else:
	
			return jsonify ({'Message':"something wrong","Status":0})
api.add_resource(ClaimInspection, "/claimInspection")
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
		parser.add_argument('BankAccountNo',required=True,type=int,help='BankAccountNo Id cannot be found')
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
		AdharNo = str(args['AdharNo'])
		MobileNo = str(args['MobileNo'])
		print('jk',MobileNo)
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
		CurrentTime = CurrentTime.strftime("%m-%d-%Y")
		mycursor.execute("SELECT count(*) as totalval from user")
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			totalval = i[0]
		EmployeeId = EmpId(totalval)
		file = args['IdProofPhoto']
		Photo= args['imageData']
		RoleID = 3
		UserPassword=Password_encoded(MobileNo)
		if not file is None and Photo is None :
			
			filename=Upload_fun(file)
			print(filename)
			sql = "INSERT INTO user (Password,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,Mobile,Email,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,Sale_ScFor,CenterLocation,Po,Ps,District,State,CenterContctNo,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(UserPassword,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation,PostOffice,PoliceStation,District,State,CenterContactNo,filename,CurrentTime)
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
			val=(UserPassword,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation,PostOffice,PoliceStation,District,State,CenterContactNo,Photo,CurrentTime)
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

class SalesRpt(Resource):
	def get(self):
		new = []
		arraynew=[]
		mycursor.execute("SELECT SUM( CASE WHEN Sale_ScFor = 'car' THEN 1 ELSE 0 END ) AS carcount, SUM( CASE WHEN Sale_ScFor = 'motorcycle' THEN 1 ELSE 0 END ) AS motorcyclecount,date(OnDate) FROM `salesmanager` GROUP BY DATE(`OnDate`)")
		row=mycursor.fetchall()
		for i in row:
			new.append(list(map(str,list(i))))
			for i in new:
				car=i[0]
				motorcycle=i[1]
				date = i[2]
				data={'car':car,'motorcycle':motorcycle,'date':date}
				arraynew.append(data)		
		return jsonify({'Status':1,'new':arraynew})		
api.add_resource(SalesRpt, "/SalesRpt")


class MyTeamSalesRpt(Resource):
	def post(self):
		new = []
		arraynew=[]
		parser = reqparse.RequestParser()
		parser.add_argument('UserID',required=True,type=str, help='UserID cannot be found')
		args = parser.parse_args()
		AddedBy = args['UserID']
		mycursor.execute("SELECT SUM( CASE WHEN Sale_ScFor = 'car' THEN 1 ELSE 0 END ) AS carcount, SUM( CASE WHEN Sale_ScFor = 'motorcycle' THEN 1 ELSE 0 END ) AS motorcyclecount,date(OnDate) FROM `salesmanager` WHERE ( Sale_ScFor='car' or Sale_ScFor='motorcycle' ) AND AddedBy = '"+str(AddedBy)+"' GROUP BY DATE(`OnDate`)")
		row=mycursor.fetchall()
		for i in row:
			new.append(list(map(str,list(i))))
			for i in new:
				car=i[0]
				motorcycle=i[1]
				date = i[2]
				data={'car':car,'motorcycle':motorcycle,'date':date}
				arraynew.append(data)		
		return jsonify({'Status':1,'new':arraynew})		
api.add_resource(MyTeamSalesRpt, "/MyTeamSalesRpt")



	
if __name__ == '__main__':
	app.run(port='5000',host='0.0.0.0',debug=False)
