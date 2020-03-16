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
      /* <?php include_once('header.php')?> */
	  {% include 'header.php' %}
        <!-- ============================================================== -->
        /* <?php include_once('menu.php')?> */
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
                          
							<form method="post" action="/viewamdetails_update">
							
							
							<div class="col-sm-12">
							<center><h4 style="margin-top:10px; text-decoration: underline;" class="pageheader-title">Area Manager Profile</h4></center>
									<div class="form-group">
										<td><center><img style="margin-top:10px" src="../static/video/{{ result[0]['IdproofPhoto']}}" width="100" height="100"></img></center></td>
									</div>
									
									<div class="form-group">
									{{result}}
										<center><h5> {{result[0]['Name']}} </h5></center>
									</div>
										
									<div class="form-group">
										<center><h5><label for="date">Employee ID- {{result[0]['EmployeeId']}}</label></h5></center>
										
									</div>
									
									
									
									<h4 style="font-size:14px; color:#ff001a; text-decoration: underline; text-align:left;">Basic Details</h4>
									<label for="date">District Allocate</label>
									<div class="form-group">
										<input name="Districtallocation" value= "{{result[0]['Districtallocation']}}" type="text"  placeholder="Districtallocation" class="welcome"  required>
									</div>
									
									<label for="date">Date Of Joining</label>
									<div class="form-group">
										<input name="Dateofjoining" value= "{{result[0]['Dateofjoining']}}" type="text" placeholder="Dateofjoining" class="welcome" required>
									</div>
									
									<label for="text">Name of Candidate</label>
									<div class="form-group">
										<input name="Name" value= "{{result[0]['Name']}}" type="text"  placeholder="Name" class="welcome" required>
									</div>
									
									<label for="date">Date of Birth</label>
									<div class="form-group">
										<input name="DOB" value= "{{result[0]['DOB']}}" type="text" placeholder="DOB" class="welcome" required>
									</div>
									
									<label for="date">Qualification</label>
									<div class="form-group">				
										<input name="Qualification" value= "{{result[0]['Qualification']}}" type="text"  placeholder="Qualification" class="welcome" required>
									</div>
									
									<label for="date">Adhar Card No</label>
									<div class="form-group">										
										<input name="Adhar" value= "{{result[0]['Adhar']}}" type="text"  class="welcome"placeholder="Adhar" required>
									</div>
									
									<label for="date">PAN Card No</label>
									<div class="form-group">										
										<input name="Pancard" value= "{{result[0]['Pancard']}}" type="text"  class="welcome"placeholder="Pan Card" required>
									</div>
									
									<label for="date">Mobile Number</label>
									<div class="form-group">										
										<input name="Mobile" value= "{{result[0]['Mobile']}}" type="text"   class="welcome" placeholder="Mobile" required>
									</div>
									
									<label for="date">E-mail Id</label>
									<div class="form-group">										
										<input name="Email" value= "{{result[0]['Email']}}" type="text" placeholder="Email" class="welcome" required>
									</div>
									<h4 style="font-size:14px; color:#ff001a; text-decoration: underline; text-align:left;">Experience</h4>
									<label for="date">Year of experience</label>
									<div class="form-group">
										<input name="YrsOfExp" value= "{{result[0]['YrsOfExp']}}" type="text" placeholder="Year of experience" class="welcome" required>
									</div>
									
									</div>
									<div class="col-sm-12">
									
									<label for="date">Experience Sector</label>
									<div class="form-group">
										<input name="StreetVillage" value= "{{result[0]['ExpSector']}}" type="text" placeholder="Experience Sector" class="welcome" required>
									</div>
									<label for="date">Presently  working as</label>
									<div class="form-group">
										<input name="PresentlyWorking" value= "{{result[0]['PresentlyWorking']}}" type="text" placeholder="PresentlyWorking" class="welcome" required>
									</div>
									 <h4 style="font-size:14px; color:#ff001a; text-decoration: underline;  text-align:left;">Address(As per ID proof)</h4>
									<label for="date">Street/Village</label>
									<div class="form-group">
										<input name="StreetVillage" value= "{{result[0]['StreetVillage']}}" type="text" placeholder="Street/Village" class="welcome" required>
									</div>
									<label for="date">Post Office</label>
									<div class="form-group">
										<input name="Po" value= "{{result[0]['Po']}}" type="text" placeholder="Post Office" class="welcome" required>
									</div>
									<label for="date">Police Station</label>
									<div class="form-group">
										<input name="Ps" value= "{{result[0]['Ps']}}" type="text" placeholder="Police Station" class="welcome" required>
									</div>
									<label for="date">District</label>
									<div class="form-group">
										<input name="Dist" value= "{{result[0]['Dist']}}" type="text" placeholder="District" class="welcome" required>
									</div>
									<label for="date">State</label>
									<div class="form-group">
										<input name="state" value= "{{result[0]['state']}}" type="text" placeholder="District" class="welcome" required>
									</div>
									<label for="date">Pin code</label>
									<div class="form-group">
										<input name="pincode" value= "{{result[0]['pincode']}}" type="text" placeholder="pincode" class="welcome" required>
									</div>
									<h4 style="font-size:14px;color:#ff001a; text-decoration: underline;  text-align:left;">Bank Details</h4>
									<label for="date">Bank Name</label>
									<div class="form-group">
										<input name="BankName" value= "{{result[0]['BankName']}}" type="text" placeholder="BankName" class="welcome" required>
									</div>
									<label for="date">A/C Number</label>
									<div class="form-group">
										<input name="BankAccountNo" value= "{{result[0]['BankAccountNo']}}" type="text" placeholder="A/C Number" class="welcome" required>
									</div>
									<label for="date">IFSC Code</label>
									<div class="form-group">
										<input name="IFSC" value= "{{result[0]['IFSC']}}" type="text" placeholder="IFSC" class="welcome" required>
									</div>
									
									</div>
								
								
									<input name="UserID" value="{{ result[0]['UserID'] }}" type="hidden">
									<input type="submit"  value="Submit">
								

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