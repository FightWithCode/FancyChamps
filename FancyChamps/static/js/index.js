  $(function () {
    $("#DateOfBirth").datepicker({
      format:'mm/dd/yyyy',
    });
  });

//   $(".signup_button").click(function(){

//   })

  $(".close").click(function(){
      console.log("Heloo")
      $('.alert').css("display","none");
  })
  var abc
  var xyz
  var a = false
  var b = false
  $('.signup_button').click(function(event){
    if(a != true && b != true){
      event.preventDefault();
      $('.InfoProvider').fadeIn(1000);
      $('.InfoProvider').html("<center>Please Verify your Email Address and Mobile Number.</center>")
      $('.InfoProvider').delay(3000).fadeOut();
    }
    else if (a != true && b == true){
      event.preventDefault();
      $('.InfoProvider').fadeIn(1000);
      $('.InfoProvider').html("<center>Please Verify your Mobile Number also.</center>")
      $('.InfoProvider').delay(3000).fadeOut();
    }
    else if(a == true && b != true){
      event.preventDefault();
      $('.InfoProvider').fadeIn(1000);
      $('.InfoProvider').html("<center>Please Verify your Email Address also.</center>")
      $('.InfoProvider').delay(3000).fadeOut();
    }
    else{
        $('#id_phone_number').val(xyz)
        $('#id_email').val(abc)
    }
    var username = $( "div.username" ).find( "#id_username" ).val();
    console.log(username)
	$.ajax({
        url: '/check/',
        data: {
            username: username,
        },
        dataType: 'json',
        success: function (data) {
            console.log(data)
 			if(data.is_taken){
 			    console.log("heif")
                event.preventDefault();
                $('.InfoProvider').html("<center>Username is Taken Already!</center>")
                $('.InfoProvider').delay(3000).fadeOut();
            }
        }
    })
  });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  $(".InfoProvider").on('click', '.verify_button_mobile', function () {
      verify_otp = $('#verify_input').val()
      var csrftoken = getCookie('csrftoken');
      console.log($(this).attr('verify-input'))
      console.log("I got clicked"+verify_otp)
      $.ajax({
          url: $(this).attr('verify-input'),
          type: "POST",
          data:{
            verify_otp: verify_otp,
            verify_this_mobile: verify_this_mobile,
            csrfmiddlewaretoken : csrftoken,
          },
          dataType: 'json',
          success: function (data) {
            console.log(data)
            if (data.otp_matched_status){
                a = true
                xyz = verify_this_mobile
                $('.InfoProvider').html("<center>Thank You! Mobile Verified Successfuly.</center>")
                $('.InfoProvider').delay(2500).fadeOut(1000);
            }
            else{
                a = false
                $('#id_phone_number').removeAttr("readonly");
                $('.InfoProvider').html("<center>Wrong OTP Entered. Try Again!</center>")
                $('.InfoProvider').delay(2500).fadeOut(1000);
            }
          }
      });
  });

  $(".InfoProvider").on('click', '.verify_button_email', function () {
      verify_otp = $('#verify_input').val()
      var csrftoken = getCookie('csrftoken');
      console.log($(this).attr('verify-input'))
      console.log("I got clicked"+verify_otp)
      $.ajax({
          url: $(this).attr('verify-input'),
          type: "POST",
          data:{
            verify_otp: verify_otp,
            verify_this_email: verify_this_email,
            csrfmiddlewaretoken : csrftoken,
          },
          dataType: 'json',
          success: function (data) {
            console.log(data)
            if (data.otp_matched_status){
                b = true
                abc = verify_this_email
                $('.InfoProvider').html("<center>Thank You! Email Verified Successfuly.</center>")
                $('.InfoProvider').delay(2500).fadeOut(1000);
            }
            else{
                b = false
                $('#id_phone_number').removeAttr("readonly");
                $('.InfoProvider').html("<center>Wrong OTP Entered. Try Again!</center>")
                $('.InfoProvider').delay(2500).fadeOut(1000);
            }
          }
      });
  });

  var verify_this_mobile=""
  var verify_this_email=""

  $(".custom_verify_email").click(function () {
      verify_this_email = $('#id_email').val()
      var csrftoken = getCookie('csrftoken');
      incorrect_input_data = "<center>Please Enter a valid Gamil Account<b>(youname@gamil.com)</b></center>";
      correct_input_data = "OTP sent to Email : "+verify_this_email+". Please Enter the OTP in below box.<center><input type=\"input\" id=\"verify_input\"><input class=\"verify_button_email btn\" type=\"button\" name=\"verify\" value=\"Verify\" verify-input=\"/verify_email_otp/\"></center>"
      $.ajax({
          url: $(this).attr('verify-input'),
          type: "POST",
          data:{
            verify_it: verify_this_email,
            csrfmiddlewaretoken : csrftoken,
          },
          dataType: 'json',
          success: function (data) {
            console.log(data)
            if (data.email_valid){
                a = false
                $('#id_email').attr("readonly", "readonly");
                $('.InfoProvider').html(correct_input_data)
                $('.InfoProvider').fadeIn(1000);
            }
            if(data.email_taken){
                a = false
                $('.InfoProvider').html("<center>Account with this email already Exists!</center>")
                $('.InfoProvider').fadeIn(1000);
                $('.InfoProvider').delay(3000).fadeOut();
            }
            else if(!data.email_valid){
                a = false
                $('.InfoProvider').html(incorrect_input_data)
                $('.InfoProvider').fadeIn(1000);
                $('.InfoProvider').delay(3000).fadeOut();
            }
          }
      });
  });

  $(".custom_verify_phone").click(function () {
      verify_this_mobile = $('#id_phone_number').val()
      var csrftoken = getCookie('csrftoken');
      incorrect_input_data = "<center>Please Enter a valid Mobile Number</center>";
      correct_input_data = "OTP sent to Mobile No : "+verify_this_mobile+". Please Enter the OTP in below box.<center><input type=\"input\" id=\"verify_input\"><input class=\"verify_button_mobile btn\" type=\"button\" name=\"verify\" value=\"Verify\" verify-input=\"/verify_mobile_otp/\"></center>"
      $.ajax({
          url: $(this).attr('verify-input'),
          type: "POST",
          data:{
            verify_it: verify_this_mobile,
            csrfmiddlewaretoken : csrftoken,
          },
          dataType: 'json',
          success: function (data) {
            console.log(data)
            if (data.digits_valid){
                a = false
                $('#id_phone_number').attr("readonly", "readonly");
                $('.InfoProvider').html(correct_input_data)
                $('.InfoProvider').fadeIn(1000);
            }
            else if(data.mobile_taken){
                $('.InfoProvider').html("<center>Account with this Mobile Number already Exists!</center>")
                $('.InfoProvider').delay(3000).fadeIn();
            }
            else if(!data.digits_valid){
                a = false
                $('.InfoProvider').html(incorrect_input_data)
                $('.InfoProvider').fadeIn(1000);
                $('.InfoProvider').delay(3000).fadeIn();
            }
          }
      });
  });
