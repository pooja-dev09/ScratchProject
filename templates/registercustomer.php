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

    <style type="text/css">
		@media print {
			.noprintbtn {
				display :  none;
			}
		}
	</style>

</head>

<body>
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
                        <div class="page-header">
                            <center><h2 class="pageheader-title">Contract Record</h2></center>


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
                        <div class="card" >
                            <div class="card-body" >

                                <form method="post" action="/seadmin/Registercustomer">
									<div class="box" style="width:50%; margin-top:10px; margin-bottom:10px;" >
										<h4>Enter Your Date</h4>
										<input type="date" id ="start" name="start"/>
										<input type="date" id ="End" name="End"/>
										<input type="submit" value = "Submit" name ="submit_button" style="width:100px; ">
									</div>
								</form>
                                <div class="table-responsive" >
                                    <table class="table table-striped table-bordered first">
                                        <thead>

                                            <tr>
                                                <th>Slno</th>
												<th>Entry Date</th>
												<th>Expiry Date</th>
											    <th>Entry by ID</th>
											    <th>Vehicle Type</th>
                                                <th>Amount</th>
												<th>Contract No</th>
												<th>Money Receipt</th>

                                            </tr>
                                        </thead>
                                        <tbody>
										{% for r in result %}
                                            <tr>
                                                <td>{{r["count"]}}</td>
                                                <td>{{r["OnDate"]}}</td>
												<td>{{r["DateOfExp"]}}</td>
												<td>{{r["AddedEmployeeId"]}}</td>
                                                <td>{{r["VehicleCategory"]}}</td>
                                                <td>{{r["Package"]}}</td>
												<td><a style="color:#ff001a; text-decoration: underline;" href="/contractrecord/{{r.UserID}}">{{r["EmployeeId"]}}</a></td>
												<td><a href="/seadmin/Moneyreceipt/{{r.UserID}}"><input type="button" value="View"></a></td>
                                            </tr>
											{% endfor %}
                                        </tbody>
                                        <tfoot>
                                            <tr>
                                              <th>Slno</th>
												<th>Entry Date</th>
												<th>Expiry Date</th>
											    <th>Entry by ID</th>
											    <th>Vehicle Type</th>
                                                <th>Amount</th>
												<th>Contract No</th>
												<th>Money Receipt</th>


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

                {% for r in results %}
                    <div class="form-group"  style="padding-left: 350px; padding-top:20px; ">
                        <label style="width:150px";>Total Amount</label>
                           <input  value= "{{r['totalamt']}}" class="welcome" readonly required>

                    </div>
                {% endfor %}









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

	<script>
		$(document).ready(function () {
            $("button").click(function () {
    $(this).css("background-color", "#0cbd63");
                    });
    });
</script>

</body>

</html>


