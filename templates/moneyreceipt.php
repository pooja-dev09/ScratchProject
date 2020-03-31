<!doctype html>
<html lang="en">
 
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Scratch Exponent Admin</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{{url_for('static',filename='assets/vendor/bootstrap/css/bootstrap.min.css')}}">
    <link href="{{url_for('static',filename='assets/vendor/fonts/circular-std/style.css')}}" rel="stylesheet">
    <link rel="stylesheet" href="{{url_for('static',filename='assets/libs/css/style.css')}}">
    <link rel="stylesheet" href="{{url_for('static',filename='assets/vendor/fonts/fontawesome/css/fontawesome-all.css')}}">
    <link rel="stylesheet" href="{{url_for('static',filename='assets/vendor/datepicker/tempusdominus-bootstrap-4.css')}}" />
    <link rel="stylesheet" href="{{url_for('static',filename='assets/vendor/inputmask/css/inputmask.css')}}" />
	<style>
		.table thead th{vertical-align:middle;}

	</style>
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
         {% include 'header.php' %}
        <!-- ============================================================== -->
       {% include 'menu.php' %}
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- wrapper  -->
        <!-- ============================================================== -->
        <div class="dashboard-wrapper">
            <div class="container-fluid dashboard-content">
                <div class="row">
                    <div class="col-xl-10">
                       
                       
                        <!-- ============================================================== -->
                        <!-- basic form  -->
                        <!-- ============================================================== -->
                        <div class="row">
                            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12" id="div_print">
                                <div class="section-block" id="basicform">
                                    <h3 class="section-title">Money Receipt</h3>
                                    
                                </div>
                                <div class="card">
                                    <h5 class="card-header" style="text-align:center; font-size:20px; font-weight:normal;">SCRATCH EXPONENT<br/>
									GSTIN No -21ADZFS5312F1Z0
									</h5>
                                    <div class="card-body">
                                        <form>
                                            <div class="form-group">
												<div class="row">

														<div class="col-xl-4">
															<div class="row">
																<label for="inputText3" class="col-xl-4 col-form-label">Date :</label>
																<input id="inputText3" type="date" value={{result[0]['DateOfContract']}} class="col-xl-8 form-control">
															</div>
														</div>
														<div class="col-xl-4">
														</div>
														<div class="col-xl-4">
															<div class="row">
																<label for="inputText3" class="col-xl-4 col-form-label">Sl No :</label>
																<input id="inputText3" type="text" value={{result[0]['slno']}} class="col-xl-8 form-control">
															</div>
														</div>
													
												</div>
                                            </div>
                                            <div class="form-group">
                                                <div class="row">
													
														<div class="col-xl-12">
															<div class="row">
																<label for="inputText3" class="col-xl-3 col-form-label">Customer Name :</label>
																<input id="inputText3" type="text" value={{result[0]['OwnerName']}} class="col-xl-6 form-control">
															</div>
														</div>
												</div>
                                               
                                            </div>
											<div class="form-group">
                                                <div class="row">
													
														<div class="col-xl-12">
															<div class="row">
																<label for="inputText3" class="col-xl-3 col-form-label">Vehicle No :</label>
																<input id="inputText3" type="text" value={{result[0]['VehicleNo']}} class="col-xl-6 form-control">
															</div>
														</div>
												</div>
                                               
                                            </div>
                                            <div class="table-responsive">
											<table class="table table-striped table-bordered first">
												<thead>

													<tr>
														<th rowspan="2">SI.No</th>
														<th rowspan="2">Service Particular</th>
														<th rowspan="2">Contract ID</th>
														<th rowspan="2">Quantity</th>
														<th colspan="2">Amount</th>
														
													</tr>
													<tr>
														<th>Rs. </th>

													</tr>
												</thead>
												<tbody>
													<tr>
														<td>1</td>
														<td>Vehicle Annual Maintenance Service</td>
														<td>{{result[0]['EmployeeId']}}</td>
														<td>1</td>
														<td>{{result[0]['Package']}}</td>

													</tr>
													<tr>
														<td colspan="3">Payment With Cash / Cheq / Online </td>
														<td>Total</td>
														<td colspan="2"></td>
														
													</tr>
													<tr>
														<td colspan="3"> </td>
														<td>S.GST 9%</td>
														<td colspan="2">{{result[0]['stategst']}}</td>
														
													</tr>
													<tr>
														<td colspan="3"> </td>
														<td>C.GST 9%</td>
														<td colspan="2">{{result[0]['centralgst']}}</td>
														
													</tr>
													<tr>
														<td colspan="3"> </td>
														<td>Round Off</td>
														<td colspan="2">{{result[0]['totalamt']}}</td>
													</tr>
													<tr>
														<td colspan="3"> </td>
														<td>Ground Total</td>
														<td colspan="2">{{result[0]['totalamt']}}</td>
														
													</tr>
													<tr>
														<td>For Scratch Exponent</td>
														<td colspan="5"></td>
													</tr>
												</tbody>
											</table>
											</div>
											<div class="form-group" style="margin-top:15px;">


												<a class="btn btn-primary" class = "noprintbtn" onClick="printdiv('div_print')" href="#">Print</a>

											</div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- ============================================================== -->
                        <!-- end basic form  -->
                        <!-- ============================================================== -->
                       
                    </div>
                     <script language="javascript">
                function printdiv(printpage)
                {
                var headstr = "<html><head><title></title></head><body>";
                var footstr = "</body>";
                var newstr = document.all.item(printpage).innerHTML;
                var oldstr = document.body.innerHTML;
                document.body.innerHTML = headstr+newstr+footstr;
                window.print();
                document.body.innerHTML = oldstr;
                return false;
                }
			</script>
                   
                </div>
            </div>
            <!-- ============================================================== -->
            <!-- footer -->
            <!-- ============================================================== -->
            <div class="footer">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12 col-12">
                            Copyright © 2018 Concept. All rights reserved. Dashboard by <a href="https://colorlib.com/wp/">Colorlib</a>.
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
    <script src="assets/vendor/jquery/jquery-3.3.1.min.js"></script>
    <script src="assets/vendor/bootstrap/js/bootstrap.bundle.js"></script>
    <script src="assets/vendor/slimscroll/jquery.slimscroll.js"></script>
    <script src="assets/libs/js/main-js.js"></script>
    <script src="assets/vendor/inputmask/js/jquery.inputmask.bundle.js"></script>
    <script>
    $(function(e) {
        "use strict";
        $(".date-inputmask").inputmask("dd/mm/yyyy"),
            $(".phone-inputmask").inputmask("(999) 999-9999"),
            $(".international-inputmask").inputmask("+9(999)999-9999"),
            $(".xphone-inputmask").inputmask("(999) 999-9999 / x999999"),
            $(".purchase-inputmask").inputmask("aaaa 9999-****"),
            $(".cc-inputmask").inputmask("9999 9999 9999 9999"),
            $(".ssn-inputmask").inputmask("999-99-9999"),
            $(".isbn-inputmask").inputmask("999-99-999-9999-9"),
            $(".currency-inputmask").inputmask("$9999"),
            $(".percentage-inputmask").inputmask("99%"),
            $(".decimal-inputmask").inputmask({
                alias: "decimal",
                radixPoint: "."
            }),

            $(".email-inputmask").inputmask({
                mask: "*{1,20}[.*{1,20}][.*{1,20}][.*{1,20}]@*{1,20}[*{2,6}][*{1,2}].*{1,}[.*{2,6}][.*{1,2}]",
                greedy: !1,
                onBeforePaste: function(n, a) {
                    return (e = e.toLowerCase()).replace("mailto:", "")
                },
                definitions: {
                    "*": {
                        validator: "[0-9A-Za-z!#$%&'*+/=?^_`{|}~/-]",
                        cardinality: 1,
                        casing: "lower"
                    }
                }
            })
    });
    </script>
</body>
 
</html>