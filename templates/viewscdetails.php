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
                            <center><h4 style="margin-top:10px; text-decoration: underline;" class="pageheader-title">Authorized Service Center</h4></center>
							<form method="post" action="/viewscdetails_update">

									<center><div class="form-group">
									<label style="width:150px;">Authorisation No-</label>
										<input name="EmployeeId" style="text-align:center" value= "{{result[0]['EmployeeId']}}" type="text" readonly>
									</div></center>

							<div class="col-sm-12">

									<label for="date">District of authorisation</label>
									<div class="form-group">
										<input name="DateOfAuthorize"  value= "{{result[0]['DateOfAuthorize']}}" type="date"  placeholder="DateOfAuthorize" class="welcome"  required>
									</div>

									<label for="date">Owner Name</label>
									<div class="form-group">
										<input name="OwnerName" style = "text-transform:capitalize;" value= "{{result[0]['OwnerName']}}" type="text" placeholder="OwnerName" class="welcome" required>
									</div>

									<label for="text">Center Location</label>
									<div class="form-group">
										<input name="CenterLocation" style = "text-transform:capitalize;" value= "{{result[0]['CenterLocation']}}" type="text"  placeholder="CenterLocation" class="welcome" required>
									</div>

									<label for="date">Po</label>
									<div class="form-group">
										<input name="Po" style = "text-transform:capitalize;" value= "{{result[0]['Po']}}" type="text" placeholder="Po" class="welcome" required>
									</div>

									<label for="date">District</label>
									<div class="form-group">
										<input name="District" style = "text-transform:capitalize;" value= "{{result[0]['District']}}" type="text"  placeholder="District" class="welcome" required>
									</div>
                                    <h4 style="font-size:14px; color:#ff001a; text-decoration: underline; text-align:left;">Facilities Available</h4>
									<label for="date">Denting & Painting</label>
									<div class="form-group">
									        {% if result[0]['DentingPainting'] == '0' %}
										        <input name="DentingPainting" value= "No" style = "text-transform:capitalize;" type="text" placeholder="DentingPainting" class="welcome" required>
										    {% else %}
										        <input name="DentingPainting" value= "Yes" style = "text-transform:capitalize;" type="text" placeholder="DentingPainting" class="welcome" required>
										    {% endif %}
									</div>
									<label for="date">WorkingFor</label>
									<div class="form-group">

									       <input name="WorkingFor" style = "text-transform:capitalize;" value= "{{result[0]['WorkingFor']}}" type="text" placeholder="WorkingFor" class="welcome" required>

									</div>
									<label for="date">Center Name</label>
									<div class="form-group">
										<input name="CenterName" style = "text-transform:capitalize;" value= "{{result[0]['CenterName']}}" type="text" placeholder="CenterName" class="welcome" required>
									</div>

									<label for="date">Mobile No</label>
									<div class="form-group">
										<input name="Mobile" value= "{{result[0]['Mobile']}}" type="number"  class="welcome"placeholder="Mobile" required>
									</div>

									<label for="date">GSTIN  Number</label>
									<div class="form-group">
										<input name="GSTINno" style = "text-transform:uppercase;" value= "{{result[0]['GSTINno']}}" type="text"   class="welcome" placeholder="GSTINno" required>
									</div>

									<label for="date">Town</label>
									<div class="form-group">
										<input name="Town" style = "text-transform:capitalize;" value= "{{result[0]['Town']}}" type="text" placeholder="Town" class="welcome" required>
									</div>

									<label for="date">Ps</label>
									<div class="form-group">
										<input name="Ps" style = "text-transform:capitalize;" value= "{{result[0]['Ps']}}" type="text" placeholder="Ps" class="welcome" required>
									</div>
									<label for="date">State</label>
									<div class="form-group">
										<input name="State" style = "text-transform:capitalize;" value= "{{result[0]['State']}}" type="text" placeholder="State" class="welcome" required>
									</div>

									<label for="date">Mechanical</label>
									<div class="form-group">
									    {% if result[0]['Mechanical'] == '0' %}
										<input name="Mechanical" value= "Yes" style = "text-transform:capitalize;" type="text" placeholder="Mechanical" class="welcome" required>
										{% else %}
										<input name="Mechanical" value= "No" style = "text-transform:capitalize;" type="text" placeholder="Mechanical" class="welcome" required>
										{% endif %}
									</div>

									</div>



									<input name="UserID" value="{{ result[0]['UserID'] }}" type="hidden">
									<input type="submit"   value="Submit">


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