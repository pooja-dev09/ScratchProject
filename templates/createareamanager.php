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
</head>
<style> 
.fileUpload {
    position: relative;
    overflow: hidden;
}
.fileUpload input.upload {
    position: absolute;
    top: 0;
    right: 0;
    margin: 0;
    padding: 0;
    font-size: 20px;
    cursor: pointer;
    opacity: 0;
    filter: alpha(opacity=0);
}
</style> 

<body>
    <!-- ============================================================== -->
    <!-- main wrapper -->
    <!-- ============================================================== -->
    <div class="dashboard-main-wrapper">
       /*  <?php include_once('header.php')?> */
	   {% include 'header.php' %}
        <!-- ============================================================== -->
      /*  <?php include_once('menu.php')?> */
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
                            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
                                <div class="section-block" id="basicform">
									{%with messages = get_flashed_messages(with_categories=true)%}
									{%if messages%}
										<ul>
											{%for category, message in messages%}
											<div class="alert alert-success mb-3{{ category }}" role="alert"> 
											{{ message }}
											</div>
											
											{%endfor%}
										</ul>
									{%endif%}
								{%endwith%}
								
								
								
								
                                    <h3 class="section-title">Create Area Manager</h3>
                                    
                                </div>
                                <div class="card">
                                    <h5 class="card-header">Basic Details</h5>
                                    <div class="card-body">
                                        <form method="post" action="/seadmin/createareamanager" enctype=multipart/form-data>
                                             <div class="form-group">
												<label for="date">Date Of Joining</label>
												<input type="date" name="DateOfJoining" class="form-control" required />
											</div>
										  <div class="form-group">
												<label for="date"> Name </label>
												<input type="text" name="Name" class="form-control" required />
										  </div>
										  <div class="form-group">
												<label for="date">DOB </label>
												<input type="date" name="DOB" class="form-control" required  />
										  </div>
										  <div class="form-group">
												<label for="date"> Qualification  </label>
												<input type="text" name="Qualification" class="form-control" required />
										  </div>
										 <h4 style="font-size:14px; color:#FF9900; text-align:left;">ID Proof Address</h4>
										  <div class="form-group">
												<label for="centerid"> AdharNo </label>
												<input type="text"  class="form-control" name="AdharNo" required />
										   </div>
										  <div class="form-group">
												<label for="centerid"> Mobile No </label>
												<input type="text" class="form-control" name="Mobile" required />
										   </div>
										   <div class="form-group">
												<label for="centerid"> Email Id </label>
												<input type="email" class="form-control" name="Email" required />
										   </div>
										   
										   <h4 style="font-size:14px; color:#FF9900; text-align:left;">Bank Details</h4>
										   <div class="form-group">
												<label for="centerid"> Bank Account No </label>
												<input type="text" class="form-control" name="BankAccountNo" required />
										   </div>
										   <div class="form-group">
												<label for="centerid"> IFSC Code </label>
												<input type="text" class="form-control" name="IFSC" required />
										   </div>
										   <div class="form-group">
												<label for="centerid"> Bank Name </label>
												<input type="text" class="form-control" name="BankName" required />
											</div>
											<h4 style="font-size:14px; color:#FF9900; text-align:left;">Work Experience Details</h4>
										   <div class="form-group">
												<label for="centerid"> Presently  working as </label>
												<input type="text" class="form-control" name="PresentlyWorking" required />
										   </div>
										  
										  <div class="form-group">
											<label for="branchid">Appoint For </label>
											<select class="form-control" name="AppointCenter" required >
												<option value="SalesCenter">Sales Center</option>
												<option value="ServiceCenter">Service Center</option>
												<option value="SalesandService">Sales & Service Center</option>
											</select>
										  </div>
										  <div class="form-group">
											<label for="centerid"> Name of Sales /Service Center </label>
											<input type="text" class="form-control" name="NameCenter" required />
										   </div>
										  <div class="form-group">
											<label for="centerid"> Center Brand </label>
											<input type="text" class="form-control" name="CenterBrand" required />
										   </div>
											<div class="form-group">
											<label for="branchid">Sales /Service Center For </label>
											<select class="form-control" name="CenterFor" required >
												<option value="motorcycle">Two Wheeler</option>
												<option value="car">Four Wheeler</option>
												
											</select>
										  </div>
											<div class="form-group">
											<label for="centerid"> Center Location </label>
											<input type="text" class="form-control" name="CenterLocation" required />
										   </div>
										 <div class="form-group">
											<label for="centerid"> PO </label>
											<input type="text" class="form-control" name="PostOffice" required />
											
										   </div>
										  <div class="form-group">
											<label for="villageid"> PS  </label>
											<input type="text" class="form-control" name="PoliceStation" required />
											
										  </div> 
										   <div class="form-group">
											<label for="centerid"> Dist </label>
											<input type="text" class="form-control" name="District" required  />
										   </div>
										   <div class="form-group">
											<label for="centerid"> State </label>
											<input type="text" class="form-control" name="State" required />
										   </div>
										   <div class="form-group">
											<label for="centerid"> Sales/Service Center Contact No</label>
											<input type="text" class="form-control" name="CenterContactNo" required />
										   </div>
											 
										   <div class="form-group">
											<p style="font-weight:bold;">Upload a photo of candidates ID proof (Adhara card/ DL/ Voter ID)</p>
											</div>
												<div class="form-group">
												<div class="input-group-btn">
												<span class="fileUpload btn btn-success">
												  <span class="upl" id="upload">Upload from gallery</span>
												  <input type="file" class="upload up" id="inputfile" name="inputfile"  required />
												</span>
											   </div>
										  
											<div class="sub">
											<button class="btn btn-primary"  type="submit" >Create</button>
                                            </div>
										</div>
                                        </form>
                                    
                                </div>
                            </div>
                        </div>
                        <!-- ============================================================== -->
                        <!-- end basic form  -->
                        <!-- ============================================================== -->
                       
                    </div>
                   
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
    <script src="{{url_for('static',filename='assets/vendor/jquery/jquery-3.3.1.min.js')}}"></script>
    <script src="{{url_for('static',filename='assets/vendor/bootstrap/js/bootstrap.bundle.js')}}"></script>
    <script src="{{url_for('static',filename='assets/vendor/slimscroll/jquery.slimscroll.js')}}"></script>
    <script src="{{url_for('static',filename='assets/libs/js/main-js.js')}}"></script>
    <script src="{{url_for('static',filename='assets/vendor/inputmask/js/jquery.inputmask.bundle.js')}}"></script>
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