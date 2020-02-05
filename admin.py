from flask import Flask,url_for, redirect, flash,session, jsonify,request,render_template
from flask_cors import CORS, cross_origin
from fun_file import *
import datetime
import mysql.connector
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
		CenterContactNo=str(request.form.get('CenterContactNo'))
		file = request.files['inputfile']
		filename=Upload_fun(file)
		CurrentTime = datetime.datetime.now()
		RoleID = 4
		UserPassword=Password_encoded(MobileNo)
		mycursor.execute("SELECT count(*) as totalval from user")
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			totalval = i[0]
		EmployeeId=EmpId(totalval)
		if DateOfJoining != "" and Name != "" and DOB != "" and Qualification != " " and AdharNo != "" and EmailId != "" and MobileNo != "" and BankAccountNo != "" and IFSC != "" and BankName != "" and PresentlyWorking != "" and AppointCenter != "" and NameCenter != "" and CenterBrand != "" and CenterFor != "" and CenterLocation != "" and PostOffice != "" and PoliceStation != "" and District != "" and State != "" and CenterContactNo != " " and filename != "":
			sql = "INSERT INTO user (Password,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,Mobile,Email,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,Sale_ScFor,CenterLocation,Po,Ps,District,State,CenterContctNo,IdproofPhoto,OnDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(UserPassword,RoleID,EmployeeId,DateOfJoining,Name,DOB,Qualification,AdharNo,MobileNo,EmailId,BankAccountNo,IFSC,BankName,PresentlyWorking,AppointCenter,NameCenter,CenterBrand,CenterFor,CenterLocation,PostOffice,PoliceStation,District,State,CenterContactNo,filename,CurrentTime)
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
	count = 0
	mycursor.execute("SELECT areamanager.EmployeeId,areamanager.DateOfJoining,areamanager.Name,areamanager.MobileNo,salesmanager.Name FROM areamanager LEFT JOIN salesmanager ON areamanager.UserID=salesmanager.AddedBy where areamanager.UserID=salesmanager.AddedBy")
	row=mycursor.fetchall()
	for i in row:
		EmployeeId = i[0]
		DateOfJoining = i[1]
		AreaManagerName = i[2]
		MobilNo = i[3]
		SalesManagerName = i[4]
		count = count + 1
		data = {'Id':count,'EmployeeId':EmployeeId,'DateOfJoining':DateOfJoining,'AreaManagerName':AreaManagerName,'MobilNo':MobilNo,'SalesManagerName':SalesManagerName}
		new.append(data)
		
	return render_template('viewam.php', result = new)

@app.route('/seadmin/viewsm')	
def viewsm():
	new = []
	count = 0
	mycursor.execute("SELECT salesmanager.EmployeeId,salesmanager.DateOfJoining,salesmanager.Name,salesmanager.MobileNo,vehiclecontract.OwnerName,vehiclecontract.AddedBy,salesmanager.UserID FROM vehiclecontract LEFT JOIN salesmanager ON vehiclecontract.AddedBy=salesmanager.UserID WHERE vehiclecontract.AddedBy=salesmanager.UserID")
	row=mycursor.fetchall()
	for i in row:
		EmployeeId = i[0]
		DateOfJoining = i[1]
		salesmanagername = i[2]
		MobileNo = i[3]
		CustomerName = i[4]
		count = count + 1
		data = {'Id':count,'EmployeeId':EmployeeId,'DateOfJoining':DateOfJoining,'salesmanagername':salesmanagername,'MobileNo':MobileNo,'CustomerName':CustomerName}
		new.append(data)
		
	return render_template('viewsm.php', result = new)	

	
@app.route('/seadmin/vc',methods = ['GET','POST'])
def vc():
	new = []
	count = 0
	if (request.method == 'POST'):
		
		if request.form['submit_button'] == 'Submit':
			start_dates = str(request.form.get('start'))
			start_ends = str(request.form.get('End'))
			sql="SELECT user.Name,user.RoleID,vehiclecontract.VehicleNo,vehiclecontract.OwnerName,vehiclecontract.	VehicleCategory,vehiclecontract.OnDate FROM user LEFT JOIN vehiclecontract ON user.UserID=vehiclecontract.AddedBy"
			
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
						count +=  1
						designation = i[0]
						data = {'slno':count,'Name':Name,'VehicleNo':VehicleNo,'OwnerName':OwnerName,'VehicleCategory':VehicleCategory,'OnDate':OnDate,'designation':designation}
						new.append(data)
		return render_template('vc.php',result = new)
	else:
		
		mycursor.execute("SELECT user.Name,user.RoleID,vehiclecontract.VehicleNo,vehiclecontract.OwnerName,vehiclecontract.	VehicleCategory,vehiclecontract.OnDate FROM user LEFT JOIN vehiclecontract ON user.UserID=vehiclecontract.AddedBy ORDER BY vehiclecontract.AddedBy desc limit 10")
		row=mycursor.fetchall()
		print(row)
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
				count += 1
				designation = i[0]
				data = {'slno':count,'Name':Name,'VehicleNo':VehicleNo,'OwnerName':OwnerName,'VehicleCategory':VehicleCategory,'OnDate':OnDate,'designation':designation}
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
	mycursor.execute("SELECT claim.DateOfClaim,claim.ClaimNo,claim.UserID,claiminspection.ClaimStatus,claim.MoneyReceiptPhoto FROM claim LEFT JOIN claiminspection ON claiminspection.ClaimID=claim.ClaimID ")
	rowcursor=mycursor.fetchall()
	if len(rowcursor) > 0:
		for i in rowcursor:
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
			data = {'DateOfClaim':DateOfClaim,'ClaimNo':ClaimNo,'name':name,'ClaimStatus':ClaimStatus,'MoneyReceiptPhoto':MoneyReceiptPhoto}
			new.append(data)

	return render_template('claim.php',result = new)
	
@app.route('/seadmin/Requestcustomer')
def Requestcustomer():
	new = []
	count = 0
	mycursor.execute("SELECT DateOfRegistration,Name ,Mobile ,VehicleCategory,DateOfPurchase,UserID FROM `customerrequest` order by DateOfRegistration desc")
	rowcursor=mycursor.fetchall()
	if len(rowcursor) > 0:
		for i in rowcursor:
			DateOfRegistration = i[0]
			Name = i[1]
			Mobile = i[2]
			VehicleCategory = i[3]
			DateOfPurchase = i[4]
			UserID = i[5]
			count = count + 1
			DateOfRegistration = DateOfRegistration.strftime("%m-%d-%Y")
			data = {'Slno':count,'DateOfRegistration':DateOfRegistration,'Name':Name,'Mobile':Mobile,'VehicleCategory':VehicleCategory,'DateOfPurchase':DateOfPurchase,'UserID':UserID}
			new.append(data)
							
	return render_template('viewcustomer.php',result = new)	
	
@app.route('/Requestcustomer_update/<string:id>')
def Requestcustomer_update(id):
	row = []
	mycursor.execute("SELECT UserID FROM customerrequest WHERE UserID= %s",[id])
	new = mycursor.fetchall()
	for j in new:
		id = j[0]
		
		data = {'id':id}
		row.append(data)
	return render_template('viewcustomer.php', row = row)


@app.route('/seadmin/Registercustomer')
def Registercustomer():
	row = []
	count = 0
	mycursor.execute("SELECT vehiclecontract.DateOfContract,vehiclecontract.VehicleNo,vehiclecontract.Mobile,vehiclecontract.OwnerName,vehiclecontract.Po,vehiclecontract.Ps,user.Name,user.RoleID,user.EmployeeId,vehiclecontract.VehicleCategory FROM user LEFT JOIN vehiclecontract ON user.UserID = vehiclecontract.AddedBy")
	new = mycursor.fetchall()
	for i in new:
		DateOfContract = i[0]
		VehicleNo = i[1]
		Mobile = i[2]
		OwnerName = i[3]
		Po = i[4]
		Ps = i[5]
		Name = i[6]
		RoleID = i[7]
		EmployeeId = i[8]
		VehicleCategory = i[9]
		count = count + 1
		mycursor.execute("SELECT RoleName from role WHERE RoleID = '"+str(RoleID)+"'")
		rowcursor=mycursor.fetchall()
		for i in rowcursor:
			Role=i[0]
			data = {'count':count,'DateOfContract':DateOfContract,'VehicleNo':VehicleNo,'Mobile':Mobile,'OwnerName':OwnerName,'Po':Po,'Ps':Ps,'Name':Name,'Role':Role,'EmployeeId':EmployeeId,'VehicleCategory':VehicleCategory}
			row.append(data)
	return render_template('registercustomer.php', result = row)


@app.route('/seadmin/Vehiclereport')
def Vehiclereport():
	arraynew = []
	new = []
	count = 0
	mycursor.execute("SELECT SUM( CASE WHEN VehicleCategory = 'car' THEN 1 ELSE 0 END ) AS carcount, SUM( CASE WHEN VehicleCategory = 'motorcycle' THEN 1 ELSE 0 END ) AS motorcyclecount,date(OnDate) FROM `vehiclecontract` GROUP BY DATE(`OnDate`)  DESC ")
	row=mycursor.fetchall()
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
	return render_template('index.php')

if __name__ == '__main__':
	app.run(port='7000',host='0.0.0.0',debug=False)
