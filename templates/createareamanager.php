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
								
								
								
								
                                    <center><h3 class="section-title">Appoint Area Manager</h3></center>
                                    
                                </div>
                                <div class="card">
                                    
                                    <div class="card-body" style="width: 650px;">
                                        <form method="post" action="/seadmin/createareamanager" enctype=multipart/form-data>
											<div class="form-group"  >
												<label for="date">District Allocate</label>
												<input type="text" name="Districtallocation" class="form-control" style = "text-transform:uppercase;"  required />
											</div>
											<div class="form-group" style = "text-transform:capitalize;">
												<label for="date">Date Of Joining</label>
												<input type="date" name="DateOfJoining" class="form-control"   required />
											</div>

											 <h4 style="font-size:14px; color:#ff001a; text-align:left; text-decoration: underline; ">Basic Details</h4>
                                             
										  <div class="form-group">
												<label for="text"> Name of Candidate </label>
												<input type="text" name="Name" class="form-control" style = "text-transform:capitalize;"  required />
										  </div>
										  <div class="form-group">
												<label for="date">Date of Birth </label>
												<input type="date" name="DOB" class="form-control"  required  />
										  </div>
										  <div class="form-group">
												<label for="date"> Qualification  </label>
												<input type="text" name="Qualification" class="form-control" style = "text-transform:capitalize;" required />
										  </div>
										 
										  <div class="form-group">
												<label for="centerid"> Aadhar Card No </label>
												<input type="number"  Placeholder = "Please Enter 12 -digit numbers"class="form-control" name="AdharNo" required />
										   </div>
										   <div class="form-group">
												<label for="centerid"> PAN Card No </label>
												<input type="text"  class="form-control" name="Pancard" style = "text-transform:uppercase;" required />
										   </div>
										  <div class="form-group">
												<label for="centerid"> Mobile Number </label>
												<input type="number" class="form-control" Placeholder="Please Enter 10-digit numbers" name="Mobile" required />
										   </div>
										   <div class="form-group">
												<label for="centerid"> E-mail Id </label>
												<input type="email" class="form-control" name="Email" style = "text-transform:lowercase;" required />
										   </div>
										   <h4 style="font-size:14px; color:#ff001a; text-align:left; text-decoration: underline; ">Experience</h4>
										   <div class="form-group">
												<label for="centerid">Year of experience</label>
												<input type="text" class="form-control" name="Yearofexperience" style = "text-transform:capitalize;" required />
										   </div>
										   <div class="form-group">
												<label> Experience Sector</label>
												<input type="text" class="form-control" name="ExperienceSector" style = "text-transform:capitalize;" required />
										   </div>
										   <div class="form-group">
												<label> Presently  working as </label>
												<input type="text" class="form-control" name="PresentlyWorking" style = "text-transform:capitalize;" required />
										   </div>
										   <h4 style="font-size:14px; color:#ff001a; text-decoration: underline;  text-align:left;">Address(As per ID proof)</h4>
										   <div class="form-group">
												<label >Street/Village </label>
												<input type="text" class="form-control" name="StreetVillage" style = "text-transform:capitalize;" required />
										   </div>
										   <div class="form-group">
											<label > Post Office </label>
											<input type="text" class="form-control" name="PostOffice" style = "text-transform:capitalize;" required />
											
										   </div>
										  <div class="form-group">
											<label > Police Station  </label>
											<input type="text" class="form-control" name="PoliceStation" style = "text-transform:capitalize;" required />
											
										  </div> 
										   <div class="form-group">
											<label > District </label>
											<input type="text" class="form-control" name="District" style = "text-transform:capitalize;" required  />
										   </div>
										   <div class="form-group">
											<label > State </label>
											<input type="text" class="form-control" name="State" style = "text-transform:capitalize;" required />
										   </div>
										   <div class="form-group">
											<label > Pin code </label>
											<input type="number" Placeholder="Please enter 6-digit numbers"class="form-control" name="Pincode" required />
										   </div>
										   
										   
										   <h4 style="font-size:14px;color:#ff001a; text-decoration: underline;  text-align:left;">Bank Details</h4>
										    <div class="form-group">
												<label> Bank Name </label>
												<input type="text" class="form-control" name="BankName" style = "text-transform:uppercase;" required />
											</div>
										   <div class="form-group">
												<label > A/C Number </label>
												<input type="number" Placeholder="Please enter minimum 14 and maximum 16 digit number "class="form-control" name="BankAccountNo" required />
										   </div>
										   <div class="form-group">
												<label> IFSC Code </label>
												<input type="text" class="form-control" name="IFSC" placeholder="Please enter first 4-capital characters and rest 7-digits" style = "text-transform:uppercase;" required />
										   </div>
										   <div class="form-group">
											</div>
												<div class="form-group">
												<div class="input-group-btn">
												<span class="fileUpload btn btn-success">
												  <span class="upl" id="upload">Upload from gallery</span>
												  <input type="file" class="upload up" id="inputfile" name="inputfile" 
											
													onchange="readURL(this);" required />
												</span>
											   </div>
										  </div>
										  <div>
											<div class="sub">
											<button class="btn btn-primary"  type="submit" >Appoint</button>
                                            </div>
										<div>
                                        </form>
                                    
                                </div>
								
								
							<div class="card-body" >
								<div style="width:170px; height:170px; border:1px; position:absolute; right:10px; top:60px;">
								  <div id = "one"  >
									<img id="user_photo" style="width:170px; height:170px;"/>
								  </div>
								</div>
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
	<script type="text/javascript">
	function readURL(input) {
    $('#one').css("display","block");
    if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function(e) {
        $('#user_photo').attr('src', e.target.result);
      }

      reader.readAsDataURL(input.files[0]);
    }
  }

  $("#inputfile").change(function() {
    readURL(this);
  });
	</script>
	
</body>
 
</html>