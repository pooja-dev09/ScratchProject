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
                        <div class="page-header">
                            <h2 class="pageheader-title">View All Area Manager</h2>
                            
                           
                        </div>
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
                            <h5 class="card-header">List Of Area Manager Details</h5>
                            <div class="card-body">
                                <div class="table-responsive">
                                    <table class="table table-striped table-bordered first">
                                        <thead>

                                            <tr>
                                                <th>Id</th>
												<th>EmployeeId</th>
                                                <th>Name</th>
                                                <th>Email</th>
                                                <th>Mobile</th>
                                                <th>DateOfJoining</th>
												<th>DOB</th>
												<th>Qualification</th>
												<th>AdharNo</th>
												<th>BankAccountNo</th>
												<th>IFSC</th>
												<th>PresentlyWorking</th>
												<th>AppointCenter</th>
												<th>NameCenter</th>
												<th>CenterBrand</th>
												<th>Sales /Service Center</th>
												<th>CenterLocation</th>
												<th>CenterContctNo</th>
                                                <th>Police Station</th>
												<th>Post Office</th>
												<th>District</th>
												<th>State</th>
												<th>IdproofPhoto</th>
												
                                            </tr>
                                        </thead>
                                        <tbody>
										{% for r in result %}
                                            <tr>
                                                <td>{{r["Id"]}}</td>
                                                <td>{{r["EmployeeId"]}}</td>
                                                <td>{{r["Name"]}}</td>
                                                <td>{{r["EmailId"]}}</td>
                                                <td>{{r["MobileNo"]}}</td>	
												<td>{{r["DateOfJoining"]}}</td>
												<td>{{r["DOB"]}}</td>
												<td>{{r["Qualification"]}}</td>
												<td>{{r["AdharNo"]}}</td>
												<td>{{r["BankAccountNo"]}}</td>
												<td>{{r["IFSC"]}}</td>
												<td>{{r["PresentlyWorking"]}}</td>
												<td>{{r["AppointCenter"]}}</td>
												<td>{{r["NameCenter"]}}</td>
												<td>{{r["CenterBrand"]}}</td>
												<td>{{r["CenterFor"]}}</td>
												<td>{{r["CenterLocation"]}}</td>
												<td>{{r["CenterContctNo"]}}</td>
												<td>{{r["Ps"]}}</td>
												<td>{{r["Po"]}}</td>
												<td>{{r["District"]}}</td>
												<td>{{r["State"]}}</td>
												<td><img src=" video/{{ r["IdproofPhoto"]}} " width="100" height="100"></img></td>
												
                                            </tr>
											{% endfor %}
                                           
                                            
                                          
                                           
                                            
                                            
                                            
                                        </tbody>
                                        <tfoot>
                                            <tr>
												<th>Id</th>
												<th>EmployeeId</th>
                                                <th>Name</th>
                                                <th>Email</th>
                                                <th>Mobile</th>
                                                <th>DateOfJoining</th>
												<th>DOB</th>
												<th>Qualification</th>
												<th>AdharNo</th>
												<th>BankAccountNo</th>
												<th>IFSC</th>
												<th>PresentlyWorking</th>
												<th>AppointCenter</th>
												<th>NameCenter</th>
												<th>CenterBrand</th>
												<th>Sales /Service Center</th>
												<th>CenterLocation</th>
												<th>CenterContctNo</th>
                                                <th>Police Station</th>
												<th>Post Office</th>
												<th>District</th>
												<th>State</th>
												<th>IdproofPhoto</th>
												
                                            </tr>
                                        </tfoot>
                                    </table>
                                </div>
                            </div>
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