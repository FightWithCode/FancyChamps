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
  // var abc
  // var xyz
  // var a = false
  // var b = false

  function get_something( new_values = null ) {
      var verify_this_mobile = ""; // default values
      if ( typeof( new_values ) == 'object' ) {
          verify_this_mobile = new_values;
      } 
      else{
          return verify_this_mobile;
      }
  }
  // var verify_this_mobile = ""
  var original = ""
  $('#SignUpForm').on('submit', function(event){
    var username = $( "div.username" ).find( "#id_username" ).val();
    var phone_number = $( "div.phone_number" ).find( "#id_phone_number" ).val();
    var unique_user = false
    console.log(username)
    event.preventDefault();
    console.log(typeof(phone_number))
  	$.ajax({
        url: '/check/',
        data: {
            username: username,
        },
        dataType: 'json',
        success: function (data) {
            console.log(data)
       			if(data.is_taken){
       			    console.log("if")
                unique_user = data.is_taken
                console.log(unique_user)
                console.log($('.InfoProvider'))
                // $('.InfoProvider').style("display","block")
                $('.InfoProvider').html("<center>Username is Taken Already!</center>")
                $('.InfoProvider').fadeIn();
                $('.InfoProvider').delay(3000).fadeOut();      
            }
            else{
              console.log(phone_number.length)
              console.log(parseInt(phone_number))
              if(phone_number.length==10 && phone_number.match(/^\d+$/)){
                console.log("If")
                $('#some_input_id').attr('name', 'submit_btn');
                $('#some_input_id').attr('value', 'Continue');
                //var form = document.getElementById("SignUpForm")
                get_something(phone_number)
                verify_this_mobile = phone_number
                console.log(verify_this_mobile)
                var csrftoken = getCookie('csrftoken');
                //correct_input_data = "OTP sent to Mobile No : "+verify_this_mobile+". Please Enter the OTP in below box.<center><input type=\"input\" id=\"verify_input\"><input class=\"verify_button_mobile btn\" type=\"button\" name=\"verify\" value=\"Verify\" verify-input=\"/verify_mobile_otp/\"></center>"
                $.ajax({
                    url: $('#SignUpForm').attr('verify-input'),
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
                          //original = $('.FormContainer').html()
                          //$('.FormContainer').html("<center><div class=\"input_field\"> <span><i aria-hidden=\"true\" class=\"fa fa-phone\"></i></span><input type=\"text\" name=\"otp\" placeholder=\"Enter 6 digit OTP\" class=\"custom_input\" id=\"otp_value\"></div><input type=\"button\" name=\"verify\" value=\"Verify\" class=\"btn signup_button verify_otp\" id=\"verify_otp\" verify-input=\"/verify_mobile_otp/\"></center>")
                          $('#SignUpForm').get(0).submit();
                          $('#some_input_id').remove()
                          // $('.InfoProvider').html(correct_input_data)
                          // $('.InfoProvider').fadeIn(1000);
                      }
                      else if(data.mobile_taken){
                          $('.InfoProvider').html("<center>Account with this Mobile Number already Exists!</center>")
                          $('.InfoProvider').fadeIn();
                          $('.InfoProvider').delay(3000).fadeOut()
                      }
                      else if(!data.digits_valid){
                          a = false
                          $('.InfoProvider').html("<center>Enter an valid Mobile no!</center>")
                          $('.InfoProvider').fadeIn();
                          $('.InfoProvider').delay(3000).fadeOut();
                      }
                    }
                });
              }
              else{
                $('.InfoProvider').html("<center>Enter an valid Mobile no!</center>")
                $('.InfoProvider').fadeIn();
                $('.InfoProvider').delay(3000).fadeOut();                  
              }
            }
        }
    });
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
  $(".FormContainer").on("click","#verify_otp", function(){
      console.log("hello World")
      verify_otp = $('#otp_value').val()
      var csrftoken = getCookie('csrftoken');
      console.log($(this).attr('verify-input'))
      console.log("I got clicked"+verify_otp)
      //console.log(get_something())
      someuser = $('#someuser').val()
      $.ajax({
          url: $(this).attr('verify-input'),
          type: "POST",
          data:{
            verify_otp: verify_otp,
            someuser:someuser,
            csrfmiddlewaretoken : csrftoken,
          },
          dataType: 'json',
          success: function (data) {
            console.log(data)
            if (data.otp_matched_status){
                $('.InfoProvider').html("<center>Thank You! Mobile Verified Successfuly.</center>")
                $('.InfoProvider').fadeIn();
                $('.InfoProvider').delay(3000).fadeOut();
                window.location.replace("/cricket_center/");
                // $('.FormContainer').html(original)
                // $('#SignUpForm').get(0).submit();
                // $('#some_input_id').remove()
            }
            else{
                console.log("JHere")
                $('.InfoProvider').html("<center>Wrong OTP Entered. Try Again!</center>")
                $('.InfoProvider').fadeIn();
                $('.InfoProvider').delay(3000).fadeOut();
            }
          }
      });
  });

  // $(".InfoProvider").on('click', '.verify_button_email', function () {
  //     verify_otp = $('#verify_input').val()
  //     var csrftoken = getCookie('csrftoken');
  //     console.log($(this).attr('verify-input'))
  //     console.log("I got clicked"+verify_otp)
  //     $.ajax({
  //         url: $(this).attr('verify-input'),
  //         type: "POST",
  //         data:{
  //           verify_otp: verify_otp,
  //           verify_this_email: verify_this_email,
  //           csrfmiddlewaretoken : csrftoken,
  //         },
  //         dataType: 'json',
  //         success: function (data) {
  //           console.log(data)
  //           if (data.otp_matched_status){
  //               b = true
  //               abc = verify_this_email
  //               $('.InfoProvider').html("<center>Thank You! Email Verified Successfuly.</center>")
  //               $('.InfoProvider').delay(2500).fadeOut(1000);
  //           }
  //           else{
  //               b = false
  //               $('#id_phone_number').removeAttr("readonly");
  //               $('.InfoProvider').html("<center>Wrong OTP Entered. Try Again!</center>")
  //               $('.InfoProvider').delay(2500).fadeOut(1000);
  //           }
  //         }
  //     });
  // });

  // var verify_this_mobile=""
  // var verify_this_email=""

  // $(".custom_verify_email").click(function () {
  //     verify_this_email = $('#id_email').val()
  //     var csrftoken = getCookie('csrftoken');
  //     incorrect_input_data = "<center>Please Enter a valid Gamil Account<b>(youname@gamil.com)</b></center>";
  //     correct_input_data = "OTP sent to Email : "+verify_this_email+". Please Enter the OTP in below box.<center><input type=\"input\" id=\"verify_input\"><input class=\"verify_button_email btn\" type=\"button\" name=\"verify\" value=\"Verify\" verify-input=\"/verify_email_otp/\"></center>"
  //     $.ajax({
  //         url: $(this).attr('verify-input'),
  //         type: "POST",
  //         data:{
  //           verify_it: verify_this_email,
  //           csrfmiddlewaretoken : csrftoken,
  //         },
  //         dataType: 'json',
  //         success: function (data) {
  //           console.log(data)
  //           if (data.email_valid){
  //               a = false
  //               $('#id_email').attr("readonly", "readonly");
  //               $('.InfoProvider').html(correct_input_data)
  //               $('.InfoProvider').fadeIn(1000);
  //           }
  //           if(data.email_taken){
  //               a = false
  //               $('.InfoProvider').html("<center>Account with this email already Exists!</center>")
  //               $('.InfoProvider').fadeIn(1000);
  //               $('.InfoProvider').delay(3000).fadeOut();
  //           }
  //           else if(!data.email_valid){
  //               a = false
  //               $('.InfoProvider').html(incorrect_input_data)
  //               $('.InfoProvider').fadeIn(1000);
  //               $('.InfoProvider').delay(3000).fadeOut();
  //           }
  //         }
  //     });
  // });

  // $(".custom_verify_phone").click(function () {
  //     verify_this_mobile = $('#id_phone_number').val()
  //     var csrftoken = getCookie('csrftoken');
  //     incorrect_input_data = "<center>Please Enter a valid Mobile Number</center>";
  //     correct_input_data = "OTP sent to Mobile No : "+verify_this_mobile+". Please Enter the OTP in below box.<center><input type=\"input\" id=\"verify_input\"><input class=\"verify_button_mobile btn\" type=\"button\" name=\"verify\" value=\"Verify\" verify-input=\"/verify_mobile_otp/\"></center>"
  //     $.ajax({
  //         url: $(this).attr('verify-input'),
  //         type: "POST",
  //         data:{
  //           verify_it: verify_this_mobile,
  //           csrfmiddlewaretoken : csrftoken,
  //         },
  //         dataType: 'json',
  //         success: function (data) {
  //           console.log(data)
  //           if (data.digits_valid){
  //               a = false
  //               $('#id_phone_number').attr("readonly", "readonly");
  //               $('.InfoProvider').html(correct_input_data)
  //               $('.InfoProvider').fadeIn(1000);
  //           }
  //           else if(data.mobile_taken){
  //               $('.InfoProvider').html("<center>Account with this Mobile Number already Exists!</center>")
  //               $('.InfoProvider').delay(3000).fadeIn();
  //           }
  //           else if(!data.digits_valid){
  //               a = false
  //               $('.InfoProvider').html(incorrect_input_data)
  //               $('.InfoProvider').fadeIn(1000);
  //               $('.InfoProvider').delay(3000).fadeIn();
  //           }
  //         }
  //     });
  // });

