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
                            <center><h4 style="margin-top:10px; text-decoration: underline;" class="pageheader-title">Claim Settle</h4></center>
							<form method="post" action="">

									<center><div class="form-group">
									<label style="width:150px;">ClaimNo-</label>
										<input name="ClaimNo" style="text-align:center" value= "{{result[0]['ClaimNo']}}" type="text" readonly>
									</div></center>

							<div class="col-sm-12">
							         {% if result[0]['BankName'] is not none or result[0]['BankName'] == ''  %}
							            <label>Bank Name</label>
									    <div class="form-group">
										    <input value= "{{result[0]['BankName']}}" type="text" class="welcome" readonly>
									    </div>

                                        <label>A/C Number</label>
                                        <div class="form-group">
                                            <input value= "{{result[0]['AccountNumber']}}" type="text" class="welcome" readonly>
                                        </div>

                                        <label>IFSC Code</label>
                                        <div class="form-group">
                                            <input value= "{{result[0]['IFSC']}}" type="text" class="welcome" readonly>
                                        </div>
                                     {% endif %}

                                     {% if result[0]['UPI'] is not none or result[0]['UPI'] == ''  %}
                                        <label>UPI Wallet Number</label>
                                        <div class="form-group">
                                            <input value= "{{result[0]['UPI']}}" type="text" class="welcome" readonly>
                                        </div>
                                        <label>Wallet Name</label>
                                        <div class="form-group">
                                            <input value= "{{result[0]['WalletName']}}" type="text" class="welcome" readonly>
                                        </div>
                                     {% endif %}
									<label>MoneyReceiptPhoto</label>
									<div class="form-group">
										<input value= "{{result[0]['MoneyReceiptPhoto']}}" type="text" class="welcome" readonly>
									</div>



									<div class="sub">
									    <input name="ClaimID" value="{{ result[0]['ClaimID'] }}" type="hidden">
                                        <button class="btn btn-primary"  type="submit" >Submit</button>
                                    </div>

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