<!doctype html>
<html lang="en">
 
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Data Tables</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='assets/vendor/bootstrap/css/bootstrap.min.css')}}">
    <link href="{{url_for('static',filename='assets/vendor/fonts/circular-std/style.css')}}" rel="stylesheet">
    <link rel="stylesheet" href="{{url_for('static',filename='assets/libs/css/style.css')}}">
    <link rel="stylesheet" href="{{url_for('static',filename='assets/vendor/fonts/fontawesome/css/fontawesome-all.css')}}">
    <link rel="stylesheet" type="text/css" href="{{url_for('static',filename='assets/vendor/datatables/css/dataTables.bootstrap4.css')}}">
    <link rel="stylesheet" type="text/css" href="{{url_for('static',filename='assets/vendor/datatables/css/buttons.bootstrap4.css')}}">
    <link rel="stylesheet" type="text/css" href="{{url_for('static',filename='assets/vendor/datatables/css/select.bootstrap4.css')}}">
    <link rel="stylesheet" type="text/css" href="{{url_for('static',filename='assets/vendor/datatables/css/fixedHeader.bootstrap4.css')}}">
</head>

<body>

<style>
.welcome, input[type="url"], #contact textarea {
	width:97%;
	border:1px solid #CCC;
	background:#FFF;
	margin:0 0 5px;
	border: 1px solid rgba(0,0,0,.12);
border-radius: .3rem;
    padding: 8px 10px;
color: rgba(0,0,0,.87);
font-size: 1rem;
}
</style>
    <!-- ============================================================== -->
    <!-- main wrapper -->
    <!-- ============================================================== -->
    <div class="dashboard-main-wrapper">
         <!-- ============================================================== -->

	  {% include 'header.php' %}
        <!-- ============================================================== -->

		{% include 'menu.php' %}
        <!-- ============================================================== -->
        <!-- wrapper  -->
        <!-- ============================================================== -->
        <div class="dashboard-wrapper">
            <div class="container-fluid  dashboard-content">
                <!-- ============================================================== -->
                <!-- pageheader -->
                <!-- ============================================================== -->
                <div class="row">
                    <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                    </div>
                </div>
                <!-- ============================================================== -->
                <!-- end pageheader -->
                <!-- ============================================================== -->
                <div class="row">
                    <!-- ============================================================== -->
                    <!-- basic table  -->
                    <!-- ============================================================== -->
                    <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                        <div class="card">
                          
							<form method="post" action="/viewsmdetails_update">
							
							
							<div class="col-sm-12">
							<center><h4 style="margin-top:10px; text-decoration: underline;" class="pageheader-title">Sales Manager Profile</h4></center>
									<div class="form-group">
										<td><center><img style="margin-top:10px" src="../static/video/{{ result[0]['IdproofPhoto']}}" width="100" height="100"></img></center></td>
									</div>
									
									<div class="form-group">
										<center><h5> {{result[0]['Name']}} </h5></center>
									</div>
									
										
									<div class="form-group">
										<center><h5><label for="date">Employee ID- {{result[0]['EmployeeId']}}</label></h5></center>
										
									</div>

									<label>Date Of Joining</label>
									<div class="form-group">
										<input name="Dateofjoining" value= "{{result[0]['Dateofjoining']}}" type="date" placeholder="Dateofjoining" class="welcome" required>
									</div>
								
									<h4 style="font-size:14px; color:#ff001a; text-decoration: underline; text-align:left;">Basic Details</h4>

									<label>D.O.B</label>
									<div class="form-group">
										<input name="DOB" value= "{{result[0]['DOB']}}"  type="date"  placeholder="Name" class="welcome" required>
									</div>

									
									<label>Qualification</label>
									<div class="form-group">				
										<input name="Qualification" value= "{{result[0]['Qualification']}}"  style = "text-transform:capitalize;" type="text"  placeholder="Qualification" class="welcome" required>
									</div>
									
									<label>AADHAR NO</label>
									<div class="form-group">										
										<input name="Adhar" value= "{{result[0]['Adhar']}}" type="number"  class="welcome"placeholder="Aadhar" required>
									</div>
									
									<label>Mobile Number</label>
									<div class="form-group">										
										<input name="Mobile" value= "{{result[0]['Mobile']}}" type="number"   class="welcome" placeholder="Mobile" required>
									</div>
									
									<label>E-mail Id</label>
									<div class="form-group">										
										<input name="Email" value= "{{result[0]['Email']}}" type="text" style = "text-transform:lowercase;" placeholder="Email" class="welcome" required>
									</div>
									
									<label for="date">Bank A/C Number</label>
									<div class="form-group">
										<input name="BankAccountNo" value= "{{result[0]['BankAccountNo']}}" type="number" placeholder="A/C Number" class="welcome" required>
									</div>
									
									<label for="date">IFSC Code</label>
									<div class="form-group">
										<input name="IFSC" value= "{{result[0]['IFSC']}}" type="text" placeholder="IFSC" style = "text-transform:uppercase;" class="welcome" required>
									</div>
									
									<label for="date">Bank Name</label>
									<div class="form-group">
										<input name="BankName" value= "{{result[0]['BankName']}}" type="text" placeholder="BankName" style = "text-transform:uppercase;" class="welcome" required>
									</div>
									
									<label for="date">Presently  working as</label>
									<div class="form-group">
										<input name="PresentlyWorking" value= "{{result[0]['PresentlyWorking']}}"  style = "text-transform:capitalize;" type="text" placeholder="PresentlyWorking" class="welcome" required>
									</div>
									<label for="date">Appoint for center</label>
									<div class="form-group">
										<input name="AppointCenter" value= "{{result[0]['AppointCenter']}}"  style = "text-transform:capitalize;" type="text" placeholder="AppointCenter" class="welcome" required>
									</div>
									
									<label for="date">Name of Center</label>
									<div class="form-group">
										<input name="NameCenter" value= "{{result[0]['NameCenter']}}"  style = "text-transform:capitalize;" type="text" placeholder="Name of Center" class="welcome" required>
									</div>
									
									<label for="date">Center Brand</label>
									<div class="form-group">
										<input name="CenterBrand" value= "{{result[0]['CenterBrand']}}"  style = "text-transform:capitalize;" type="text" placeholder="Center Brand" class="welcome" required>
									</div>
									<label for="date">This Center for</label>
									<div class="form-group">
										<input name="CenterFor" value= "{{result[0]['CenterFor']}}"  style = "text-transform:capitalize;" type="text" placeholder="This Center for" class="welcome" required>
									</div>
									<label for="date">Center Location</label>
									<div class="form-group">
										<input name="CenterLocation" value= "{{result[0]['CenterLocation']}}" style = "text-transform:capitalize;" type="text" placeholder="Center Location" class="welcome" required>
									</div>
									
									<label for="date">Police Office</label>
									<div class="form-group">
										<input name="Po" value= "{{result[0]['Po']}}" type="text" style = "text-transform:capitalize;" placeholder="Police Station" class="welcome" required>
									</div>
									
									<label for="date">Police Station</label>
									<div class="form-group">
										<input name="Ps" value= "{{result[0]['Ps']}}" type="text" style = "text-transform:capitalize;" placeholder="Police Station" class="welcome" required>
									</div>
									<label for="date">District</label>
									<div class="form-group">
										<input name="Dist" value= "{{result[0]['Dist']}}" type="text" style = "text-transform:capitalize;" placeholder="District" class="welcome" required>
									</div>
									<label for="date">State</label>
									<div class="form-group">
										<input name="state" value= "{{result[0]['state']}}" type="text" style = "text-transform:capitalize;" placeholder="District" class="welcome" required>
									</div>
									<label for="date">CenterContctNo</label>
										<div class="form-group">
											<input name="CenterContctNo" value= "{{result[0]['CenterContactNo']}}" type="number" placeholder="Center Contct No" class="welcome" required>
										</div>
								
								
									<input name="UserID" value="{{ result[0]['UserID'] }}" type="hidden">
									<input type="submit"  name="btn" value="Submit">

								

							</form>
                        </div>
                    </div>
                    <!-- ============================================================== -->
                    <!-- end basic table  -->
                    <!-- ============================================================== -->
                </div>
                
                
                
                
            </div>
            <!-- ============================================================== -->
            <!-- footer -->
            <!-- ============================================================== -->
            <div class="footer">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12 col-12">
                            Copyright &copy; 2019 Concept. All rights reserved. Dashboard by <a href="https://colorlib.com/wp/">Colorlib</a>.
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12 col-12">
                            <div class="text-md-right footer-links d-none d-sm-block">
                                <a href="javascript: void(0);">About</a>
                                <a href="javascript: void(0);">Support</a>
                                <a href="javascript: void(0);">Contact Us</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- ============================================================== -->
            <!-- end footer -->
            <!-- ============================================================== -->
        </div>
    </div>
    <!-- ============================================================== -->
    <!-- end main wrapper -->
    <!-- ============================================================== -->
    <!-- Optional JavaScript -->
    <script src="{{url_for('static',filename='assets/vendor/jquery/jquery-3.3.1.min.js')}}"></script>
    <script src="{{url_for('static',filename='assets/vendor/bootstrap/js/bootstrap.bundle.js')}}"></script>
    <script src="{{url_for('static',filename='assets/vendor/slimscroll/jquery.slimscroll.js')}}"></script>
    <script src="{{url_for('static',filename='assets/vendor/multi-select/js/jquery.multi-select.js')}}"></script>
    <script src="{{url_for('static',filename='assets/libs/js/main-js.js')}}"></script>
    <script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
    <script src="{{url_for('static',filename='assets/vendor/datatables/js/dataTables.bootstrap4.min.js')}}"></script>
    <script src="https://cdn.datatables.net/buttons/1.5.2/js/dataTables.buttons.min.js"></script>
    <script src="{{url_for('static',filename='assets/vendor/datatables/js/buttons.bootstrap4.min.js')}}"></script>
    <script src="{{url_for('static',filename='assets/vendor/datatables/js/data-table.js')}}"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/pdfmake.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/vfs_fonts.js"></script>
    <script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.html5.min.js"></script>
    <script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.print.min.js"></script>
    <script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.colVis.min.js"></script>
    <script src="https://cdn.datatables.net/rowgroup/1.0.4/js/dataTables.rowGroup.min.js"></script>
    <script src="https://cdn.datatables.net/select/1.2.7/js/dataTables.select.min.js"></script>
    <script src="https://cdn.datatables.net/fixedheader/3.1.5/js/dataTables.fixedHeader.min.js"></script>
    
</body>
 
</html>