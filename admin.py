from flask import Flask,url_for, redirect, flash,session, jsonify,request,render_template
from flask_cors import CORS, cross_origin
from fun_file import *
import datetime
import mysql.connector
from werkzeug.utils import secure_filename
from app import app
import os
UPLOAD_FOLDER = 'static/video/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp4','mp3'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app = Flask(__name__)
cors = CORS(app)
CORS(app, support_credentials=True)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'


def mycus():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="colourfade",
	  database="Scratch"
	)
	return mydb



@app.route('/seadmin/createareamanager',methods=['GET','POST'])
def createareamanager():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		if (request.method == 'POST'):
			Districtallocation=str(request.form.get('Districtallocation')).capitalize()
			DateOfJoining=str(request.form.get('DateOfJoining'))
			Name=str(request.form.get('Name')).title()
			DOB=str(request.form.get('DOB'))
			Qualification=str(request.form.get('Qualification').capitalize())
			AdharNo=str(request.form.get('AdharNo'))
			Pancard=str(request.form.get('Pancard').upper())
			print(type(Pancard))
			EmailId=str(request.form.get('Email').lower())
			MobileNo=str(request.form.get('Mobile'))
			Yearofexperience=str(request.form.get('Yearofexperience').title())
			ExperienceSector=str(request.form.get('ExperienceSector').title())
			PresentlyWorking=str(request.form.get('PresentlyWorking').capitalize())
			StreetVillage=str(request.form.get('StreetVillage').title())
			PostOffice=str(request.form.get('PostOffice').title())
			PoliceStation=str(request.form.get('PoliceStation').title())
			District=str(request.form.get('District').title())
			State=str(request.form.get('State').title())
			Pincode=str(request.form.get('Pincode'))
			BankName=str(request.form.get('BankName').title())
			BankAccountNo=str(request.form.get('BankAccountNo'))
			IFSC=str(request.form.get('IFSC').upper())
			file = request.files['inputfile']
			filename=Upload_fun(file)
			CurrentTime = datetime.datetime.now()
			RoleID = 4
			UserPassword=Password_encoded(MobileNo)
			mydb=mycus()
			mycursor = mydb.cursor()
			mycursor.execute("SELECT EmployeeId FROM `user` WHERE RoleID = 4 and EmployeeId LIKE 'SEAM%' ORDER BY UserID DESC LIMIT 1")
			rowcursor=mycursor.fetchall()
			if len(rowcursor) > 0:
				for i in rowcursor:
					Employeeid_user = i[0]
					Employeeid_user = Employeeid_user.split("M")
					print('Employeeid_user',Employeeid_user)
					totalval = int(Employeeid_user[1])
					print('jsc',totalval)
					EmployeeId = AreaManager(totalval)

			else:
				totalval = 'SEAM0123'
				EmployeeId = totalval
			if pincode(Pincode) == True:
				if pancard(Pancard) == True:
					print(Pancard)
					if validNumber(MobileNo) == True:
						if accountNo(BankAccountNo) == True:
							if adharNo(AdharNo) == True:
								if check (EmailId) == True:
									if fun_ifsc (IFSC) == True :
										if accountNo(BankAccountNo)== True and adharNo(AdharNo) == True and check (EmailId) == True and fun_ifsc (IFSC) == True and pancard(Pancard) == True:
											sql = "INSERT INTO user (Password,RoleID,EmployeeId,Districtallocation,DateOfJoining,Name,DOB,Qualification,AdharNo,Pancard,Mobile,Email,YrsOfExp,ExpSector,PresentlyWorking,Town,Po,Ps,District,State,Pincode,BankName,BankAccountNo,IFSC,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
											val=(UserPassword,RoleID,EmployeeId,Districtallocation,DateOfJoining,Name,DOB,Qualification,AdharNo,Pancard,MobileNo,EmailId,Yearofexperience,ExperienceSector,PresentlyWorking,StreetVillage,PostOffice,PoliceStation,District,State,Pincode,BankName,BankAccountNo,IFSC,filename,CurrentTime)
											result = mycursor.execute(sql,val)
											mydb.commit()
											UserID = mycursor.lastrowid
											sql = "INSERT INTO areamanager (UserID,EmployeeId,Districtallocation,DateOfJoining,Name,DOB,Qualification,AdharNo,Pancard,MobileNo,EmailId,Yearofexperience,ExperienceSector,PresentlyWorking,StreetVillage,Po,Ps,District,State,Pincode,BankName,BankAccountNo,IFSC,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
											val=(UserID,EmployeeId,Districtallocation,DateOfJoining,Name,DOB,Qualification,AdharNo,Pancard,MobileNo,EmailId,Yearofexperience,ExperienceSector,PresentlyWorking,StreetVillage,PostOffice,PoliceStation,District,State,Pincode,BankName,BankAccountNo,IFSC,filename,CurrentTime)
											result = mycursor.execute(sql,val)
											mydb.commit()
											mydb.close()
											msg = "Congratulation, you are selected as area manager in Scratch Exponent for "+str(District)+" district. Your employee ID is "+str(EmployeeId)+". You are eligible to login in our app for your job performance using your ID as username & registered mobile number as password. We send you T&C by your E-mail soon."
											SMS_Integration(msg, MobileNo)
											flash('Area Manager Register Successfully')
										else:
											flash('Something went wrong')
									else:
										flash('IFSC code invalid')
								else:
									flash('Email is invalid')
							else:
								flash('AadharNo should be 12 digit')
						else:
							flash('AccountNo should be 14 to 16 digit')
					else:
						flash('Please enter valid mobile number')
				else:
					flash('Please enter valid pancard')
			else:
				flash('Please enter valid pincode')
		return render_template('createareamanager.php')
	

@app.route('/seadmin/viewam')	
def viewam():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		new = []
		count = 0
		mydb=mycus()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT EmployeeId,District,UserID from areamanager")
		row=mycursor.fetchall()
		mydb.close()
		for i in row:
			EmployeeId = i[0]
			District = i[1]
			UserID = i[2]
			
			count = count + 1
			data = {'Id':count,'EmployeeId':EmployeeId,'District':District,'UserID':UserID}
			new.append(data)
			
		return render_template('viewam.php',result = new)
		
@app.route('/viewamdetails/<string:UserID>')	
def viewamdetails(UserID):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		new = []
		count = 0
		mydb=mycus()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM areamanager WHERE UserID= %s",[UserID])
		row=mycursor.fetchall()
		mydb.close()
		for i in row:
			EmployeeId = i[2]
			Dateofjoining = i[3]
			Name = i[4]
			DOB = i[5]
			Qualification = i[6]
			Adhar = i[7]
			Mobile = i[8]
			Pancard = i[9]
			Email = i[10]
			BankAccountNo = i[11]
			IFSC=i[12]
			BankName=i[13]
			PresentlyWorking = i[14]
			StreetVillage = i[15]
			YrsOfExp = i[16]
			ExpSector = i[17]
			Po=i[18]
			Ps = i[19]
			Dist = i[20]
			state = i[21]
			pincode = i[22]
			Districtallocation = i[23]
			IdproofPhoto = i[24]
			count = count + 1
			data = {'Id':count,'EmployeeId':EmployeeId,'Dateofjoining':Dateofjoining,'Name':Name,'DOB':DOB,'Qualification':Qualification,'Adhar':Adhar,'Mobile':Mobile,'Pancard':Pancard,'Email':Email,'BankAccountNo':BankAccountNo,'IFSC':IFSC,'BankName':BankName,'PresentlyWorking':PresentlyWorking,'StreetVillage':StreetVillage,'YrsOfExp':YrsOfExp,'ExpSector':ExpSector,'Po':Po,'Ps':Ps,'Dist':Dist,'state':state,'pincode':pincode,'Districtallocation':Districtallocation,'IdproofPhoto':IdproofPhoto,'UserID':UserID}
			new.append(data)
			
		return render_template('viewamdetails.php',result = new)	


@app.route('/viewamdetails_update',methods=['POST'])
def viewamdetails_update():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		if (request.method == 'POST'):
			Districtallocation=str(request.form.get('Districtallocation'))
			DateOfJoining=str(request.form.get('DateOfJoining'))
			DOB=str(request.form.get('DOB'))
			Qualification=str(request.form.get('Qualification'))
			AdharNo=str(request.form.get('AdharNo'))
			Pancard=str(request.form.get('Pancard'))
			EmailId=str(request.form.get('Email'))
			MobileNo=str(request.form.get('Mobile'))
			Yearofexperience=str(request.form.get('YrsOfExp'))
			ExperienceSector=str(request.form.get('ExpSector'))
			PresentlyWorking=str(request.form.get('PresentlyWorking'))
			StreetVillage=str(request.form.get('StreetVillage'))
			PostOffice=str(request.form.get('Po'))
			PoliceStation=str(request.form.get('Ps'))
			District=str(request.form.get('Dist'))
			State=str(request.form.get('state'))
			Pincode=str(request.form.get('pincode'))
			BankName=str(request.form.get('BankName'))
			BankAccountNo=str(request.form.get('BankAccountNo'))
			IFSC=str(request.form.get('IFSC'))
			UserID = str(request.form.get('UserID'))
			

			mydb=mycus()
			mycursor = mydb.cursor()
			sql="UPDATE areamanager SET Districtallocation = '"+str(Districtallocation)+"',DateOfJoining = '"+str(DateOfJoining)+"',DOB = '"+str(DOB)+"',Qualification = '"+str(Qualification)+"',AdharNo = '"+str(AdharNo)+"',Pancard = '"+str(Pancard)+"', EmailId = '"+str(EmailId)+"',MobileNo = '"+str(MobileNo)+"', Yearofexperience = '"+str(Yearofexperience)+"',ExperienceSector = '"+str(ExperienceSector)+"',PresentlyWorking = '"+str(PresentlyWorking)+"',StreetVillage = '"+str(StreetVillage)+"',Po ='"+str(PostOffice)+"',Ps = '"+str(PoliceStation)+"',District = '"+str(District)+"',State = '"+str(State)+"',Pincode = '"+str(Pincode)+"',BankName = '"+str(BankName)+"',BankAccountNo = '"+str(BankAccountNo)+"',IFSC = '"+str(IFSC)+"' WHERE UserID = '"+str(UserID)+"'"
			result = mycursor.execute(sql)
			mydb.commit()
			
			mycursor.execute("UPDATE user SET Districtallocation = '"+str(Districtallocation)+"',DateOfJoining = '"+str(DateOfJoining)+"',DOB = '"+str(DOB)+"',Qualification = '"+str(Qualification)+"',AdharNo = '"+str(AdharNo)+"',Pancard = '"+str(Pancard)+"',Email = '"+str(EmailId)+"',Mobile = '"+str(MobileNo)+"', YrsOfExp = '"+str(Yearofexperience)+"',ExpSector = '"+str(ExperienceSector)+"',PresentlyWorking = '"+str(PresentlyWorking)+"',Town = '"+str(StreetVillage)+"',Po ='"+str(PostOffice)+"',Ps = '"+str(PoliceStation)+"',District = '"+str(District)+"',State = '"+str(State)+"',Pincode = '"+str(Pincode)+"',BankName = '"+str(BankName)+"',BankAccountNo = '"+str(BankAccountNo)+"',IFSC = '"+str(IFSC)+"' WHERE UserID = '"+str(UserID)+"'")
			mydb.commit()
			mydb.close()
		return redirect(url_for('viewam'))

@app.route('/viewambusiness/<string:UserID>')
def viewambusiness(UserID):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		# if (request.method == 'POST'):
		new = []
		count = 0
		print(UserID)
		mydb = mycus()
		mycursor = mydb.cursor()
		sql='SELECT * FROM vehiclecontract WHERE AddedBy in (SELECT UserID FROM salesmanager where AddedBy='+str(158)+') or AddedBy='+str(158)+' ORDER BY VcID ASC'
		print(sql)
		result = mycursor.execute(sql)
		row = mycursor.fetchall()
		print(row)
		for i in row:
			AddedBy=row[AddedBy]
			print('ghej',AddedBy)


		return render_template('viewbusinessam.php')







@app.route('/viewsm/<string:UserID>')
def viewsm(UserID):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		new = []
		count = 0
		mydb=mycus()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT salesmanager.UserID,salesmanager.EmployeeId,salesmanager.Ps,salesmanager.CenterBrand,areamanager.EmployeeId,areamanager.District FROM areamanager LEFT JOIN salesmanager ON areamanager.UserID=salesmanager.AddedBy WHERE salesmanager.AddedBy = '"+str(UserID)+"'" )
		row=mycursor.fetchall()
		print(row)
		for i in row:
			Sales_UserId = i[0]
			Sales_EmployeeId = i[1]
			Sales_Ps = i[2]
			Sales_CenterBrand = i[3]
			Area_EmployeeId = i[4]
			Area_District = i[5]
			count = count + 1
			data = {'Id':count,'Sales_EmployeeId':Sales_EmployeeId,'Sales_Ps':Sales_Ps,'Sales_CenterBrand':Sales_CenterBrand,'Area_EmployeeId':Area_EmployeeId,'Area_District':Area_District,'UserID':UserID,'Sales_UserId':Sales_UserId}
			new.append(data)
		
			
		return render_template('viewsm.php',result = new)		


		
#view SM DETAILS		
@app.route('/viewsmdetails/<string:UserID>')	
def viewsmdetails(UserID):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		new = []
		count = 0
		mydb=mycus()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM salesmanager WHERE UserID= %s",[UserID])
		row=mycursor.fetchall()
		mydb.close()
		for i in row:
			EmployeeId = i[3]
			Dateofjoining = i[4]
			Name = i[5]
			DOB = i[6]
			Qualification = i[7]
			Adhar = i[8]
			Mobile = i[9]
			Email = i[10]
			BankAccountNo = i[11]
			IFSC=i[12]
			BankName=i[13]
			PresentlyWorking = i[14]
			AppointCenter = i[15]
			NameCenter = i[16]
			CenterBrand = i[17]
			CenterFor = i[28]
			CenterLocation = i[19]
			Po=i[19]
			Ps = i[20]
			Dist = i[21]
			state = i[22]
			CenterContactNo = i[23]
			IdproofPhoto = i[24]
			count = count + 1
			data = {'Id':count,'EmployeeId':EmployeeId,'Dateofjoining':Dateofjoining,'Name':Name,'DOB':DOB,'Qualification':Qualification,'Adhar':Adhar,'Mobile':Mobile,'Email':Email,'BankAccountNo':BankAccountNo,'IFSC':IFSC,'BankName':BankName,'PresentlyWorking':PresentlyWorking,'AppointCenter':AppointCenter,'NameCenter':NameCenter,'CenterBrand':CenterBrand,'Po':Po,'Ps':Ps,'Dist':Dist,'state':state,'CenterFor':CenterFor,'CenterLocation':CenterLocation,'CenterContactNo':CenterContactNo,'IdproofPhoto':IdproofPhoto,'UserID':UserID}
			new.append(data)
			
		return render_template('viewsmdetails.php',result = new)	
		
		
@app.route('/viewsmdetails_update',methods=['POST'])
def viewsmdetails_update():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		if (request.method == 'POST'):
			Districtallocation=str(request.form.get('Districtallocation'))
			DateOfJoining=str(request.form.get('DateOfJoining'))
			DOB=str(request.form.get('DOB'))
			Qualification=str(request.form.get('Qualification'))
			AdharNo=str(request.form.get('AdharNo'))
			EmailId=str(request.form.get('Email'))
			MobileNo=str(request.form.get('Mobile'))
			PresentlyWorking=str(request.form.get('PresentlyWorking'))
			AppointCenter=str(request.form.get('AppointCenter'))
			NameCenter=str(request.form.get('NameCenter'))
			CenterBrand=str(request.form.get('CenterBrand'))
			CenterFor=str(request.form.get('CenterFor'))
			CenterLocation=str(request.form.get('CenterLocation'))
			PostOffice=str(request.form.get('Po'))
			PoliceStation=str(request.form.get('Ps'))
			District=str(request.form.get('Dist'))
			State=str(request.form.get('State'))
			Pincode=str(request.form.get('pincode'))
			BankName=str(request.form.get('BankName'))
			BankAccountNo=str(request.form.get('BankAccountNo'))
			IFSC=str(request.form.get('IFSC'))
			UserID = str(request.form.get('UserID'))
			

			mydb=mycus()
			mycursor = mydb.cursor()
			sql="UPDATE areamanager SET Districtallocation = '"+str(Districtallocation)+"',DateOfJoining = '"+str(DateOfJoining)+"',DOB = '"+str(DOB)+"',Qualification = '"+str(Qualification)+"',AdharNo = '"+str(AdharNo)+"',Pancard = '"+str(Pancard)+"', EmailId = '"+str(EmailId)+"',MobileNo = '"+str(MobileNo)+"', Yearofexperience = '"+str(Yearofexperience)+"',ExperienceSector = '"+str(ExperienceSector)+"',PresentlyWorking = '"+str(PresentlyWorking)+"',StreetVillage = '"+str(StreetVillage)+"',Po ='"+str(PostOffice)+"',Ps = '"+str(PoliceStation)+"',District = '"+str(District)+"',State = '"+str(State)+"',Pincode = '"+str(Pincode)+"',BankName = '"+str(BankName)+"',BankAccountNo = '"+str(BankAccountNo)+"',IFSC = '"+str(IFSC)+"' WHERE UserID = '"+str(UserID)+"'"
			result = mycursor.execute(sql)
			mydb.commit()
			
			mycursor.execute("UPDATE user SET Districtallocation = '"+str(Districtallocation)+"',DateOfJoining = '"+str(DateOfJoining)+"',DOB = '"+str(DOB)+"',Qualification = '"+str(Qualification)+"',AdharNo = '"+str(AdharNo)+"',Pancard = '"+str(Pancard)+"',Email = '"+str(EmailId)+"',Mobile = '"+str(MobileNo)+"', YrsOfExp = '"+str(Yearofexperience)+"',ExpSector = '"+str(ExperienceSector)+"',PresentlyWorking = '"+str(PresentlyWorking)+"',Town = '"+str(StreetVillage)+"',Po ='"+str(PostOffice)+"',Ps = '"+str(PoliceStation)+"',District = '"+str(District)+"',State = '"+str(State)+"',Pincode = '"+str(Pincode)+"',BankName = '"+str(BankName)+"',BankAccountNo = '"+str(BankAccountNo)+"',IFSC = '"+str(IFSC)+"' WHERE UserID = '"+str(UserID)+"'")
			mydb.commit()
			mydb.close()
		return redirect(url_for('viewam'))

@app.route('/viewsmbusiness/<string:UserID>')
def viewsmbusiness(UserID):
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		print(UserID)
		new = []
		count = 0
		mydb = mycus()
		mycursor = mydb.cursor()
		sql='SELECT salesmanager.EmployeeId,salesmanager.Name,vehiclecontract.EmployeeId,vehiclecontract.Package,vehiclecontract.VehicleNo,vehiclecontract.OnDate FROM vehiclecontract LEFT JOIN salesmanager ON vehiclecontract.AddedBy=salesmanager.UserID WHERE vehiclecontract.AddedBy=salesmanager.UserID and salesmanager.UserID ='+UserID+''
		print(sql)
		result = mycursor.execute(sql)
		row = mycursor.fetchall()
		print(row)
		for i in row:
			salesemployeeId=i[0]
			salesname = i[1]
			vehicleemployeeId = i[2]
			package= i[3]
			vehicleno = i[4]
			date = i[5]
			count  = count + 1
			data = {'Id': count, 'salesemployeeId': salesemployeeId, 'salesname': salesname,'vehicleemployeeId': vehicleemployeeId, 'package': package,'vehicleno':vehicleno,'date':date,'UserID':UserID}
			new.append(data)


		return render_template('viewbusinesssm.php',result = new)









# @app.route('/seadmin/viewsm')	
# def viewsm():
	# if not session.get('logged_in'):
		# return render_template('login.html')
	# else:
		# new = []
		# count = 0
		# mydb=mycus()
		# mycursor = mydb.cursor()
		# mycursor.execute("SELECT salesmanager.EmployeeId,salesmanager.DateOfJoining,salesmanager.Name,salesmanager.MobileNo,vehiclecontract.OwnerName,vehiclecontract.AddedBy,salesmanager.UserID FROM vehiclecontract LEFT JOIN salesmanager ON vehiclecontract.AddedBy=salesmanager.UserID WHERE vehiclecontract.AddedBy=salesmanager.UserID")
		# row=mycursor.fetchall()
		# mydb.close()
		# for i in row:
			# EmployeeId = i[0]
			# DateOfJoining = i[1]
			# salesmanagername = i[2]
			# MobileNo = i[3]
			# CustomerName = i[4]
			# count = count + 1
			# data = {'Id':count,'EmployeeId':EmployeeId,'DateOfJoining':DateOfJoining,'salesmanagername':salesmanagername,'MobileNo':MobileNo,'CustomerName':CustomerName}
			# new.append(data)
			
		# return render_template('viewsm.php', result = new)	

	
# @app.route('/seadmin/vc',methods = ['GET','POST'])
# def vc():
	# if not session.get('logged_in'):
		# return render_template('login.html')
	
	# else:
		# mydb=mycus()
		# mycursor = mydb.cursor()
		# new = []
		# count = 0
		# if (request.method == 'POST'):
			
			# if request.form['submit_button'] == 'Submit':
				# start_dates = str(request.form.get('start'))
				# start_ends = str(request.form.get('End'))
				
				# sql="SELECT user.Name,user.RoleID,vehiclecontract.VehicleNo,vehiclecontract.OwnerName,vehiclecontract.	VehicleCategory,vehiclecontract.OnDate FROM user LEFT JOIN vehiclecontract ON user.UserID=vehiclecontract.AddedBy"
				
				# if start_dates!='' and start_dates is not None:
					# sql=sql+" AND user.OnDate >= '"+str(start_dates)+"'"
						
				# if start_ends!='' and start_ends is not None:
					# if  start_ends == "":
						# sql=sql+"AND user.OnDate <= '"+str(start_ends)+"' "
					# else:
						# sql=sql+" AND user.OnDate >= '"+str(start_dates)+"'"
						
					# mycursor.execute(sql)
					# myresult=mycursor.fetchall()
					
					
					# for i in myresult:
						# Name = i[0]
						# RoleID = i[1]
						# VehicleNo = i[2]
						# OwnerName = i[3]
						# VehicleCategory = i[4]
						# OnDate = i[5]
						# mycursor.execute("SELECT RoleName from role WHERE RoleID = '%s' " % (RoleID))
						# rowcursor=mycursor.fetchall()
						
						# for i in rowcursor:
							# count +=  1
							# designation = i[0]
							# data = {'slno':count,'Name':Name,'VehicleNo':VehicleNo,'OwnerName':OwnerName,'VehicleCategory':VehicleCategory,'OnDate':OnDate,'designation':designation}
							# new.append(data)
			# return render_template('vc.php',result = new)
		# else:
			
			# mycursor.execute("SELECT user.Name,user.RoleID,vehiclecontract.VehicleNo,vehiclecontract.OwnerName,vehiclecontract.	VehicleCategory,vehiclecontract.OnDate FROM user LEFT JOIN vehiclecontract ON user.UserID=vehiclecontract.AddedBy ORDER BY vehiclecontract.AddedBy desc limit 10")
			# row=mycursor.fetchall()
			# for i in row:
				# Name = i[0]
				# RoleID = i[1]
				# VehicleNo = i[2]
				# OwnerName = i[3]
				# VehicleCategory = i[4]
				# OnDate = i[5]
				# mycursor.execute("SELECT RoleName from role WHERE RoleID = '%s' " % (RoleID))
				# rowcursor=mycursor.fetchall()
				
				# for i in rowcursor:
					# count += 1
					# designation = i[0]
					# data = {'slno':count,'Name':Name,'VehicleNo':VehicleNo,'OwnerName':OwnerName,'VehicleCategory':VehicleCategory,'OnDate':OnDate,'designation':designation}
					# new.append(data)
		# mydb.close()
		# return render_template('vc.php',result = new)
	
# @app.route('/seadmin/viewsc',methods = ['GET','POST'])
# def viewsc():
	# if not session.get('logged_in'):
		# return render_template('login.html')
	# else:
		# mydb=mycus()
		# mycursor = mydb.cursor()
		# new = []
		# if (request.method == 'POST'):
			# if request.form['submit_button'] == 'Submit':
				# start_dates = str(request.form.get('start'))
				# start_ends = str(request.form.get('End'))
				
				# sql="SELECT user.Name,user.RoleID,servicecenterauthorize.OwnerName,servicecenterauthorize.CenterName,servicecenterauthorize.CenterLocation,servicecenterauthorize.Po,servicecenterauthorize.Ps,servicecenterauthorize.District,servicecenterauthorize.OnDate FROM user LEFT JOIN servicecenterauthorize ON user.UserID=servicecenterauthorize.AddedBy where user.UserID=servicecenterauthorize.AddedBy"
		
				# if start_dates!='' and start_dates is not None:
					# sql=sql+" AND user.OnDate >= '"+str(start_dates)+"'"
					# print(sql)	
				# if start_ends!='' and start_ends is not None:
					# if  start_ends == "":
						# sql=sql+"AND user.OnDate <= '"+str(start_ends)+"' "
						# print(sql)
					# else:
						# sql=sql+" AND user.OnDate >= '"+str(start_dates)+"'"
						# print(sql)
					# mycursor.execute(sql)
					# row=mycursor.fetchall()
					# for i in row:
						# Name = i[0]
						# RoleID = i[1]
						# OwnerName = i[2]
						# CenterName = i[3]
						# CenterLocation = i[4]
						# Po = i[5]
						# Ps = i[6]
						# District = i[7]
						# OnDate = i[8]
						# mycursor.execute("SELECT RoleName from role WHERE RoleID = '%s' " % (RoleID))
						# rowcursor=mycursor.fetchall()
						# for i in rowcursor:
							# designation = i[0]
							# data = {'Name':Name,'OwnerName':OwnerName,'CenterName':CenterName,'CenterLocation':CenterLocation,'Po':Po,'Ps':Ps,'District':District,'OnDate':OnDate,'designation':designation}
							# new.append(data)
				# return render_template('viewsc.php',result = new)
		# else:
			# mycursor.execute("SELECT user.Name,user.RoleID,servicecenterauthorize.OwnerName,servicecenterauthorize.	CenterName,servicecenterauthorize.CenterLocation,servicecenterauthorize.Po,servicecenterauthorize.Ps,servicecenterauthorize.District,servicecenterauthorize.OnDate FROM user LEFT JOIN servicecenterauthorize ON user.UserID=servicecenterauthorize.AddedBy where user.UserID=servicecenterauthorize.AddedBy ORDER BY servicecenterauthorize.AddedBy desc limit 10")
			# row=mycursor.fetchall()
			# for i in row:
				# Name = i[0]
				# RoleID = i[1]
				# OwnerName = i[2]
				# CenterName = i[3]
				# CenterLocation = i[4]
				# Po = i[5]
				# Ps = i[6]
				# District = i[7]
				# OnDate = i[8]
				# mycursor.execute("SELECT RoleName from role WHERE RoleID = '%s' " % (RoleID))
				# rowcursor=mycursor.fetchall()
				# for i in rowcursor:
					# designation = i[0]
					# data = {'Name':Name,'OwnerName':OwnerName,'CenterName':CenterName,'CenterLocation':CenterLocation,'Po':Po,'Ps':Ps,'District':District,'OnDate':OnDate,'designation':designation}
					# new.append(data)
		# mydb.close()
		# return render_template('viewsc.php',result = new)

	
@app.route('/claim',methods=['GET','POST'])
def claim():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		new = []
		count = 0
		mydb=mycus()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT claim.DateOfClaim,claim.ClaimNo,claim.UserID,claiminspection.ClaimStatus,claim.MoneyReceiptPhoto FROM claim LEFT JOIN claiminspection ON claiminspection.ClaimID=claim.ClaimID order by claim.DateOfClaim desc ")
		rowcursor=mycursor.fetchall()
		if len(rowcursor) > 0:
			for i in rowcursor:
				count = count + 1
				DateOfClaim = i[0]
				ClaimNo = i[1]
				UserID = i[2]
				ClaimStatus = i[3]
				MoneyReceiptPhoto = i[4]
				if ClaimStatus is None :
					ClaimStatus = 'Pending'
				elif ClaimStatus == 1 :
					ClaimStatus = 'Approved'
				mycursor.execute("SELECT Name from user WHERE UserID = '"+str(UserID)+"'")
				rowcursor=mycursor.fetchall()
				
				for i in rowcursor:
					name=i[0]
				data = {'count':count,'DateOfClaim':DateOfClaim,'ClaimNo':ClaimNo,'name':name,'ClaimStatus':ClaimStatus,'MoneyReceiptPhoto':MoneyReceiptPhoto}
				new.append(data)
		mydb.close()
		return render_template('claim.php',result = new)
	
@app.route('/seadmin/Registercustomer')
def Registercustomer():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		new = []
		count = 0
		mydb=mycus()
		mycursor = mydb.cursor()
		sql="SELECT vehiclecontract.UserID,vehiclecontract.VehicleCategory, vehiclecontract.Package, vehiclecontract.EmployeeId, vehiclecontract.DateOfExp,vehiclecontract.OnDate,user.EmployeeId FROM vehiclecontract LEFT JOIN user ON vehiclecontract.AddedBy = user.UserID ORDER BY vehiclecontract.VcID"
		print(sql)
		mycursor.execute(sql)
		rowcursor=mycursor.fetchall()
		print(rowcursor)
		if len(rowcursor) > 0:
			for i in rowcursor:
				UserID = i[0]
				VehicleCategory = i[1]
				Package = i[2]
				EmployeeId = i[3]
				DateOfExp = i[4]
				OnDate = i[5]
				AddedEmployeeId = i[6]
				count = count + 1
				# sql='SELECT SUM('+str(Package)+') as totalamount FROM vehiclecontract'
				# print(sql)
				# mycursor.execute(sql)
				# row = mycursor.fetchall()
				# for i in row:
				# 	totalamount = i[0]
				data = {'UserID':UserID,'count':count,'VehicleCategory':VehicleCategory,'Package':Package,'EmployeeId':EmployeeId,'DateOfExp':DateOfExp,'OnDate':OnDate,'AddedEmployeeId':AddedEmployeeId}
				new.append(data)
			mydb.close()
		return render_template('registercustomer.php',result = new)
	
@app.route('/contractrecord/<string:UserID>')
def contractrecord(UserID):
	count = 0
	new = []
	print()
	mydb=mycus()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM vehiclecontract WHERE VcID= %s",[UserID])
	rowcursor = mycursor.fetchall()
	for i in rowcursor:
		DateOfContract = i[3]
		VehicleCategory = i[4]
		Model = i[7]
		color = i[9]
		ownername = i[12]
		email = i[15]
		po = i[17]
		district = i[19]
		dateofexpiry = i[16]
		maker = i[5]
		chassis = i[8]
		dateofregd = i[11]
		mobile = i[14]
		streetvillage = i[16]
		ps = i[12]
		state = i[13]
		VehicleVideo = i[21]
		EmployeeId = i[24]
		count = count + 1
		data = {'count':count,'DateOfContract':DateOfContract,'VehicleCategory':VehicleCategory,'Model':Model,'color':color,'ownername':ownername,'email':email,'po':po,'district':district,'dateofexpiry':dateofexpiry,'maker':maker,'chassis':chassis,'dateofregd':dateofregd,'mobile':mobile,'streetvillage':streetvillage,'ps':ps,'state':state,'VehicleVideo':VehicleVideo,'EmployeeId':EmployeeId,'UserID':UserID}
		new.append(data)
	return render_template('contractrecord.php', result = new)


@app.route('/viewcontract_update',methods=['POST'])
def viewcontract_update():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		if (request.method == 'POST'):
			DateOfContract = str(request.form.get('DateOfContract'))
			VehicleCategory = str(request.form.get('VehicleCategory'))
			Model = str(request.form.get('Model'))
			color = str(request.form.get('color'))
			ownername = str(request.form.get('ownername'))
			email = str(request.form.get('email'))
			po = str(request.form.get('po'))
			district = str(request.form.get('district'))
			dateofexpiry = str(request.form.get('dateofexpiry'))
			maker = str(request.form.get('maker'))
			chassis = str(request.form.get('chassis'))
			dateofregd = str(request.form.get('dateofregd'))
			mobile = str(request.form.get('mobile'))
			streetvillage = str(request.form.get('streetvillage'))
			ps = str(request.form.get('ps'))
			state = str(request.form.get('state'))
			UserID = str(request.form.get('UserID'))

			mydb = mycus()
			mycursor = mydb.cursor()
			sql = "UPDATE vehiclecontract SET DateOfContract = '" + str(
				DateOfContract) + "',VehicleCategory = '" + str(VehicleCategory) + "',	Model = '" + str(
				Model) + "', Color = '" + str(color) + "',Name = '" + str(
				ownername) + "', Email = '" + str(email) + "',	Po = '" + str(
				po) + "',District = '" + str(district) + "',DateOfExp ='" + str(dateofexpiry) + "',Maker = '" + str(maker) + "',ChassisNo = '" + str(
				chassis) + "',DateOfRegd = '" + str(dateofregd) + "',mobile = '" + str(mobile) + "',	Location = '" + str(
				streetvillage) + "',	Ps = '" + str(ps) + "',	State = '" + str(
				state) + "' WHERE UserID = '" + str(UserID) + "'"
			result = mycursor.execute(sql)
			mydb.commit()

			mycursor.execute(
				"UPDATE user SET DateOfContract = '" + str(DateOfContract) + "',VehicleCategory = '" + str(
					VehicleCategory) + "',	Model = '" + str(Model) + "',	Color = '" + str(
					color) + "',Name = '" + str(ownername) + "',Email = '" + str(email) + "',	Po = '" + str(po) + "', District = '" + str(
					district) + "',DateOfExp = '" + str(dateofexpiry) + "',Maker = '" + str(maker
					) + "',	ChassisNo = '" + str(chassis) + "',	Ps ='" + str(
					ps) + "',State = '" + str(state) + "' WHERE UserID = '" + str(UserID) + "'")
			mydb.commit()
			mydb.close()
		return redirect(url_for('Registercustomer'))




@app.route('/seadmin/Vehiclereport')
def Vehiclereport():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		arraynew = []
		new = []
		count = 0
		mydb=mycus()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT SUM( CASE WHEN VehicleCategory = 'car' THEN 1 ELSE 0 END ) AS carcount, SUM( CASE WHEN VehicleCategory = 'motorcycle' THEN 1 ELSE 0 END ) AS motorcyclecount,date(OnDate) FROM `vehiclecontract` GROUP BY DATE(`OnDate`)  DESC ")
		row=mycursor.fetchall()
		mydb.close()
		for i in row:
			new.append(list(map(str,list(i))))
			for i in new:
				count = count + 1
				car=i[0]
				motorcycle=i[1]
				date = i[2]
				data={'count':count,'car':car,'motorcycle':motorcycle,'date':date}
				arraynew.append(data)
		return render_template('viewvehiclerpt.php', result = arraynew)	

@app.route('/seadmin/index')
def index():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('index.php')
	

	
@app.route('/login',methods=['GET', 'POST'])
def login():
	if (request.method == 'POST'):
		email = str(request.form.get('email'))
		password = str(request.form.get('password'))
		mydb=mycus()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * from admin WHERE Email = '%s' AND Password = '%s'" % (email, password))
		row=mycursor.fetchall()
		if len(row)>0:
			for i in row:
				email = i[0]
				password = i[1]
				username = i[2]
				session['logged_in'] = True
			
			return redirect(url_for('index'))
			
		else:
			flash('wrong password!')
	return render_template('login.php')

@app.route("/logout")
def logout():
	session['logged_in'] = False
	return login()


if __name__ == '__main__':
	app.run(port='7000',host='0.0.0.0',debug=True)
