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




                                   <center><h4 style="margin-top:10px; text-decoration: underline;" class="pageheader-title">Customer Profile</h4></center>

                                </div>
                                <div class="card">
                                <div class="form-group">
                                {{result}}
									</div>

                                    <div class="card-body" style="width: 650px;">
                                        <form method="post" action="/viewcontract_update" enctype=multipart/form-data>
											<div class="form-group"  >
												<label >Date of Contract</label>
												<input type="text" name="DateOfContract" value= "{{result['DateOfContract']}}" placeholder="dateofcontract" class="form-control" style = "text-transform:capitalize;"  required />
											</div>
											<h4 style="font-size:14px; color:#ff001a; text-align:left; text-decoration: underline; ">Vehicle Information</h4>
											<div class="form-group" style = "text-transform:capitalize;">
												<label >Vehicle Category</label>
												<input type="text" name="VehicleCategory" value= "{{result['VehicleCategory']}}"placeholder="vehiclecategory" class="form-control" style = "text-transform:capitalize;"  required />
											</div>

										  <div class="form-group">
												<label> Model </label>
												<input type="text" name="Model" value= "{{result['Model']}}" placeholder="model" class="form-control" style = "text-transform:capitalize;"  required />
										  </div>
										  <div class="form-group">
												<label >Color</label>
												<input type="text" name="color" value= "{{result['color']}}" placeholder="color" class="form-control" style = "text-transform:capitalize;"  required  />
										  </div>
										  <h4 style="font-size:14px; color:#ff001a; text-align:left; text-decoration: underline; ">Owner Details</h4>
										  <div class="form-group">
												<label> Owner Name</label>
												<input type="text" name="ownername" value= "{{result['ownername']}}" placeholder="ownername" class="form-control" style = "text-transform:capitalize;" required />
										  </div>


										   <div class="form-group">
												<label> Email </label>
												<input type="text" name="email" value= "{{result['email']}}" class="form-control" placeholder="email" style = "text-transform:uppercase;" required />
										   </div>
										  <div class="form-group">
												<label> Po </label>
												<input type="text" name="po" value= "{{result['po']}}" class="form-control"  placeholder="po" required />
										   </div>
										   <div class="form-group">
												<label >District</label>
												<input type="text" name="district" value= "{{result['district']}}" class="form-control" placeholder="district" style = "text-transform:lowercase;" required />
										   </div>

										   <div class="form-group">
												<label >Date of Expiry</label>
												<input type="text" name="dateofexpiry" value= "{{result['dateofexpiry']}}" class="form-control" placeholder="dateofexpiry" style = "text-transform:capitalize;" required />
										   </div>
										   <div class="form-group">
												<label> Maker</label>
												<input type="text" name="maker" value= "{{result['maker']}}" class="form-control" placeholder="maker" style = "text-transform:capitalize;" required />
										   </div>
										   <div class="form-group">
												<label> Chassis No </label>
												<input type="text" name="chassis" value= "{{result['chassis']}}" class="form-control" placeholder="chassis" style = "text-transform:capitalize;" required />
										   </div>

										   <div class="form-group">
												<label >Date of Regd.</label>
												<input type="text" name="dateofregd" value= "{{result['dateofregd']}}" class="form-control" placeholder="dateofregd" style = "text-transform:capitalize;" required />
										   </div>

										  <div class="form-group">
											<label > Mobile No </label>
											<input type="text" name="mobile" value= "{{result['mobile']}}" class="form-control" placeholder="mobileno" style = "text-transform:capitalize;" required />
										  </div>

										   <div class="form-group">
											<label > Street/Village </label>
											<input type="text" name="streetvillage" value= "{{result['streetvillage']}}" class="form-control" placeholder="location" style = "text-transform:capitalize;" required  />
										   </div>
										   <div class="form-group">
											<label > PS </label>
											<input type="text" name="ps" value= "{{result['ps']}}" class="form-control" placeholder="ps" style = "text-transform:capitalize;" required />
										   </div>
										   <div class="form-group">
											<label > State </label>
											<input type="text" name="state" value= "{{result['state']}}" class="form-control" placeholder="state" required />
										   </div>

										   <div class="form-group">

										  </div>
										  <div>
											<div class="sub">
											<input name="UserID" value="{{ result['UserID'] }}" type="hidden">
											<button class="btn btn-primary"  type="submit" >Submit</button>
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