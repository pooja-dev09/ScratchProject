from flask import Flask,url_for, redirect, flash,session, jsonify,request,render_template
from flask_cors import CORS, cross_origin
from fun_file import *
import datetime
app = Flask(__name__)
cors = CORS(app)
CORS(app, support_credentials=True)

app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="colourfade",
  database="Scratch"
)
mycursor = mydb.cursor()



@app.route('/seadmin/createareamanager',methods=['GET','POST'])
def createareamanager():
	if (request.method == 'POST'):
		DateOfJoining=str(request.form.get('DateOfJoining'))
		Name=str(request.form.get('Name'))
		DOB=str(request.form.get('DOB'))
		Qualification=str(request.form.get('Qualification'))
		AdharNo=str(request.form.get('AdharNo'))
		EmailId=str(request.form.get('Email'))
		MobileNo=str(request.form.get('Mobile'))
		BankAccountNo=str(request.form.get('BankAccountNo'))
		IFSC=str(request.form.get('IFSC'))
		BankName=str(request.form.get('BankName'))
		PresentlyWorking=str(request.form.get('PresentlyWorking'))
		AppointCenter=str(request.form.get('AppointCenter'))
		NameCenter=str(request.form.get('NameCenter'))
		CenterBrand=str(request.form.get('CenterBrand'))
		CenterFor=str(request.form.get('CenterFor'))
		CenterLocation=str(request.form.get('CenterLocation'))
		PostOffice=str(request.form.get('PostOffice'))
		PoliceStation=str(request.form.get('PoliceStation'))
		District=str(request.form.get('District'))
		State=str(request.form.get('State'))
		print(State)
		CenterContactNo=str(request.form.get('CenterContactNo'))
		file = request.files['inputfile']
		print(file)
		filename=Upload_fun(file)
		print(filename)
		CurrentTime = datetime.datetime.now()
		RoleID = 4
		EmployeeId=EmpId()
		if DateOfJoining != "" and Name != "" and DOB != "" and Qualification != " " and AdharNo != "" and EmailId != "" and MobileNo != "" and BankAccountNo != "" and IFSC != "" and BankName != "" and PresentlyWorking != "" and AppointCenter != "" and NameCenter != "" and CenterBrand != "" and CenterFor != "" and CenterLocation != "" and PostOffice != "" and PoliceStation != "" and District != "" and State != "" and CenterContactNo != " " and filename != "":
			sql = "INSERT INTO user (Password,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,Mobile,Email,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,Sale_ScFor,CenterLocation,Po,Ps,District,State,CenterContctNo,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(MobileNo,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation,PostOffice,PoliceStation,District,State,CenterContactNo,filename,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			UserID = mycursor.lastrowid
			sql = "INSERT INTO areamanager (UserID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation	,Po,Ps,District,State,CenterContctNo,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(UserID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation,PostOffice,PoliceStation,District,State,CenterContactNo,filename,CurrentTime)
			result = mycursor.execute(sql,val)
			mydb.commit()
			flash('You were Successfully Added')
		else:
			flash('Please check your filled ')
		
	return render_template('createareamanager.php')
	

@app.route('/seadmin/viewam')	
def viewam():
	new = []
	mycursor.execute("SELECT * FROM areamanager")
	row=mycursor.fetchall()
	for i in row:
		Id = i[0]
		EmployeeId = i[2]
		DateOfJoining = i[3]
		Name = i[4]
		DOB = i[5]
		Qualification = i[6]	
		AdharNo = i[7]
		MobileNo = i[8]
		EmailId = i[9]
		BankAccountNo = i[10]
		IFSC = i[11]
		BankName = i[12]
		PresentlyWorking = i[13]
		AppointCenter = i[14]
		NameCenter = i[15]
		CenterBrand = i[16]
		CenterFor = i[17]
		CenterLocation = i[18]
		Po = i[19]
		Ps = i[20]
		District = i[21]
		State = i[22]
		CenterContctNo = i[23]
		IdproofPhoto= i[24]
		data = {'Id':Id,'EmployeeId':EmployeeId,'DateOfJoining':DateOfJoining,'Name':Name,'DOB':DOB,'Qualification':Qualification,'AdharNo':AdharNo,'MobileNo':MobileNo,'EmailId':EmailId,'BankAccountNo':BankAccountNo,'IFSC':IFSC,'BankName':BankName,'PresentlyWorking':PresentlyWorking,'AppointCenter':AppointCenter,'NameCenter':NameCenter,'CenterBrand':CenterBrand,'CenterFor':CenterFor,'CenterLocation':CenterLocation,'Po':Po,'Ps':Ps,'District':District,'State':State,'CenterContctNo':CenterContctNo,'IdproofPhoto':IdproofPhoto}
		new.append(data)
		
	return render_template('viewam.php', result = new)	
	
	
@app.route('/seadmin/vc',methods = ['GET','POST'])
def vc():
	new = []
	
	if (request.method == 'POST'):
		
		if request.form['submit_button'] == 'Submit':
			start_dates = str(request.form.get('start'))
			start_ends = str(request.form.get('End'))
			sql="SELECT user.Name,user.RoleID,vehiclecontract.VehicleNo,vehiclecontract.OwnerName,vehiclecontract.	VehicleCategory,vehiclecontract.OnDate FROM user LEFT JOIN vehiclecontract ON user.UserID=vehiclecontract.AddedBy where user.UserID=vehiclecontract.AddedBy"
			
			if start_dates!='' and start_dates is not None:
				sql=sql+" AND user.OnDate >= '"+str(start_dates)+"'"
					
			if start_ends!='' and start_ends is not None:
				if  start_ends == "":
					sql=sql+"AND user.OnDate <= '"+str(start_ends)+"' "
				else:
					sql=sql+" AND user.OnDate >= '"+str(start_dates)+"'"
					
				mycursor.execute(sql)
				myresult=mycursor.fetchall()
				
				
				for i in myresult:
					Name = i[0]
					RoleID = i[1]
					VehicleNo = i[2]
					OwnerName = i[3]
					VehicleCategory = i[4]
					OnDate = i[5]
					
					mycursor.execute("SELECT RoleName from role WHERE RoleID = '%s' " % (RoleID))
					rowcursor=mycursor.fetchall()
					for i in rowcursor:
						designation = i[0]
						data = {'Name':Name,'VehicleNo':VehicleNo,'OwnerName':OwnerName,'VehicleCategory':VehicleCategory,'OnDate':OnDate,'designation':designation}
						new.append(data)
		return render_template('vc.php',result = new)
	else:
	
		mycursor.execute("SELECT user.Name,user.RoleID,vehiclecontract.VehicleNo,vehiclecontract.OwnerName,vehiclecontract.	VehicleCategory,vehiclecontract.OnDate FROM user LEFT JOIN vehiclecontract ON user.UserID=vehiclecontract.AddedBy where user.UserID=vehiclecontract.AddedBy ORDER BY vehiclecontract.AddedBy desc limit 10")
		row=mycursor.fetchall()
		for i in row:
			Name = i[0]
			RoleID = i[1]
			VehicleNo = i[2]
			OwnerName = i[3]
			VehicleCategory = i[4]
			OnDate = i[5]
			
			mycursor.execute("SELECT RoleName from role WHERE RoleID = '%s' " % (RoleID))
			rowcursor=mycursor.fetchall()
			for i in rowcursor:
				designation = i[0]
				data = {'Name':Name,'VehicleNo':VehicleNo,'OwnerName':OwnerName,'VehicleCategory':VehicleCategory,'OnDate':OnDate,'designation':designation}
				new.append(data)
			
	return render_template('vc.php',result = new)
	
@app.route('/seadmin/viewsc',methods = ['GET','POST'])
def viewsc():
	new = []
	
	if (request.method == 'POST'):
		if request.form['submit_button'] == 'Submit':
			start_dates = str(request.form.get('start'))
			start_ends = str(request.form.get('End'))
			sql="SELECT user.Name,user.RoleID,servicecenterauthorize.OwnerName,servicecenterauthorize.CenterName,servicecenterauthorize.CenterLocation,servicecenterauthorize.Po,servicecenterauthorize.Ps,servicecenterauthorize.District,servicecenterauthorize.OnDate FROM user LEFT JOIN servicecenterauthorize ON user.UserID=servicecenterauthorize.AddedBy where user.UserID=servicecenterauthorize.AddedBy"
	
			if start_dates!='' and start_dates is not None:
				sql=sql+" AND user.OnDate >= '"+str(start_dates)+"'"
				print(sql)	
			if start_ends!='' and start_ends is not None:
				if  start_ends == "":
					sql=sql+"AND user.OnDate <= '"+str(start_ends)+"' "
					print(sql)
				else:
					sql=sql+" AND user.OnDate >= '"+str(start_dates)+"'"
					print(sql)
				mycursor.execute(sql)
				row=mycursor.fetchall()
				for i in row:
					Name = i[0]
					RoleID = i[1]
					OwnerName = i[2]
					CenterName = i[3]
					CenterLocation = i[4]
					Po = i[5]
					Ps = i[6]
					District = i[7]
					OnDate = i[8]
					mycursor.execute("SELECT RoleName from role WHERE RoleID = '%s' " % (RoleID))
					rowcursor=mycursor.fetchall()
					
					for i in rowcursor:
						designation = i[0]
						
						data = {'Name':Name,'OwnerName':OwnerName,'CenterName':CenterName,'CenterLocation':CenterLocation,'Po':Po,'Ps':Ps,'District':District,'OnDate':OnDate,'designation':designation}
						new.append(data)
					
					
		
			return render_template('viewsc.php',result = new)
	else:
		mycursor.execute("SELECT user.Name,user.RoleID,servicecenterauthorize.OwnerName,servicecenterauthorize.	CenterName,servicecenterauthorize.CenterLocation,servicecenterauthorize.Po,servicecenterauthorize.Ps,servicecenterauthorize.District,servicecenterauthorize.OnDate FROM user LEFT JOIN servicecenterauthorize ON user.UserID=servicecenterauthorize.AddedBy where user.UserID=servicecenterauthorize.AddedBy ORDER BY servicecenterauthorize.AddedBy desc limit 10")
		 
		row=mycursor.fetchall()
		for i in row:
			Name = i[0]
			RoleID = i[1]
			OwnerName = i[2]
			CenterName = i[3]
			CenterLocation = i[4]
			Po = i[5]
			Ps = i[6]
			District = i[7]
			OnDate = i[8]
			mycursor.execute("SELECT RoleName from role WHERE RoleID = '%s' " % (RoleID))
			rowcursor=mycursor.fetchall()
			
			for i in rowcursor:
				designation = i[0]
				data = {'Name':Name,'OwnerName':OwnerName,'CenterName':CenterName,'CenterLocation':CenterLocation,'Po':Po,'Ps':Ps,'District':District,'OnDate':OnDate,'designation':designation}
				new.append(data)

	return render_template('viewsc.php',result = new)
	
	


	
	
@app.route('/seadmin/claim')
def claim():
	new = []
	mycursor.execute("SELECT claim.UserID,claiminspection.VehicleNo,claiminspection.ClaimNo,claiminspection.ClaimDate,claiminspection.InspectBy FROM claim LEFT JOIN claiminspection ON claim.ClaimNo=claiminspection.ClaimNo where claim.ClaimNo=claiminspection.ClaimNo ")
	row=mycursor.fetchall()
	for i in row:
		UserID = i[0]
		VehicleNo = i[1]
		ClaimNo = i[2]
		ClaimDate = i[3]
		InspectBy = i[4]
		mycursor.execute("SELECT Name,RoleID from user WHERE UserID = '%s' or RoleID = '%s' " % (UserID,InspectBy))
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			Name = i[0]
			Role = i[1] 
			mycursor.execute("SELECT RoleName from role WHERE RoleID = '%s'" % (Role))
			rowcursor=mycursor.fetchall()
			for i in rowcursor:
				rolename = i[0]
			data = {'Name':Name,'VehicleNo':VehicleNo,'rolename':rolename,'ClaimNo':ClaimNo,'ClaimDate':ClaimDate}
			new.append(data)
				
	return render_template('claim.php',result = new)
	
@app.route('/seadmin/index')
def index():
	return render_template('index.php')
		
	
	
if __name__ == '__main__':
	app.run(port='8000',host='0.0.0.0',debug=False)