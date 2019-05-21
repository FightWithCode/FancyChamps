	// $('.PayoutDiv').toggle()
	// $('.PayoutDiv').html("HelloWorld")
	//$('.PayoutDiv'+$(this).attr('pay-view').replace("/cricket_center/view_payout/", '')).toggle()
	//$('.LiContainer'+$(this).attr('pay-view').replace("/cricket_center/view_payout/", '')).html("")
	//class_is = '.LiContainer'+$(this).attr('pay-view').replace("/cricket_center/view_payout/", '')
	// $.ajax({
    //     url: $(this).attr('pay-view'),
    //     dataType: 'json',
    //     success: function (data) {
	// 		console.log(typeof(data))
	// 		$('.PayoutDiv').append("<center><div style=\"position:relative;width:130%;left:-15%;line-height:14px;\"><span>NOTE : In case of the contest does not get filled then the total prize will be distributed to First Rank(Rank 1)</span><br>&nbsp;</center>")
	// 		for (var key in data) {
    // 			if (data.hasOwnProperty(key) && key!="id") {
	// 				console.log(typeof(key))
	// 				new_rank = key.replace('Rank', '')
	// 				new_rank = new_rank.replace('To', '-')
    //     			console.log(new_rank + " : " + data[key]+"₹");
	// 				$('.PayoutDiv').append("<li style=\"list-style-type:none\">Rank " + new_rank + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + "<span style=\"float:right\">" + data[key] + "₹" + "</span></li>")
    // 			}
	// 		}
    //     }
    // })
// })
$('.AddCash').click(function(){
	console.log("I got Called")
	var div = $(".JoinNowContainer");
    var height = div.css({
        display: "inline"
    }).height();

    div.css({
        overflow: "hidden",
        marginTop: height,
        height: 0
    }).animate({
        marginTop: 0,
        height: height
    }, 500, function () {
        $(this).css({
            display: "inline-block",
            overflow: "",
            height: "",
            marginTop: ""
        });
    });
});

$('.Widhdraw').click(function(){
	console.log("I got Called")
	var div = $(".WidhdrawMoney");
    var height = div.css({
        display: "inline"
    }).height();

    div.css({
        overflow: "hidden",
        marginTop: height,
        height: 0
    }).animate({
        marginTop: 0,
        height: height
    }, 500, function () {
        $(this).css({
            display: "inline-block",
            overflow: "",
            height: "",
            marginTop: ""
        });
    });
});

$(".CloseJoinNowContainer").click(function () {
	console.log("Print Me")
    var div = $(".JoinNowContainer");

    var height = div.height();

    div.css({
        overflow: "hidden",
        marginTop: 0,
        height: height
    }).animate({
        marginTop: height,
        height: 0
    }, 500, function () {
        $(this).css({
            display: "none",
            overflow: "",
            height: "",
            marginTop: ""
        });
    });

    var div = $(".WidhdrawMoney");

    var height = div.height();

    div.css({
        overflow: "hidden",
        marginTop: 0,
        height: height
    }).animate({
        marginTop: height,
        height: 0
    }, 500, function () {
        $(this).css({
            display: "none",
            overflow: "",
            height: "",
            marginTop: ""
        });
    });
});

/*Add Mooney*/
$('.AddCashButton').click(function(event){
    var cash = parseInt($('#CashAmount').val())
    if(isNaN(cash)){
        alert("Please valid Amount")
    }
    else{
        console.log("Right Value")
    }
    console.log(cash,typeof(cash))
})

$('.WidhdrawButton').click(function(event){
    event.preventDefault()
    console.log("I amWorkign")
    var cash = parseInt($('#WidhdrawCashAmount').val())
    if(isNaN(cash)){
        alert("Please valid Amount")
    }
    else{
        $.ajax({
            url: '/payments/check',
            dataType: 'json',
            success: function (data) {
                console.log(data)
                if(data.widhdrawable_balance>=cash){
                    console.log("ajax")
                    $.ajax({
                        url: '/payments/submit',
                        dataType: 'json',
                        data: {'cash': cash},
                        success: function(data){
                            if(data.request){
                                alert("Request Accepted")
                            }
                            else if(!data.request){
                                alert("Something Went Wrong")
                            }
                        }
                    })
                }
                else{
                    alert("Insufficient Balance")
                }
            }
        })
    }
    console.log(cash,typeof(cash))
})

// $('#widhdraw').click(function(event){
//     event.preventDefault()
//     var cash = parseInt($('#CashAmount').val())
//     if(isNaN(cash)){
//         alert("Please valid Amount")
//     }
//     else{
//         console.log("Right Value")
//     }
//     console.log(cash,typeof(cash))
// })

$('.CashButton').click(function(){
    console.log("Someting Went Good")
    console.log($(this).text())
    console.log($('#CashAmount').val())
    $('#CashAmount').val($(this).text())
})

$('.WidhdrawCashButton').click(function(){
    console.log("Someting Went Good")
    console.log($(this).text())
    console.log($('#CashAmount').val())
    $('#WidhdrawCashAmount').val($(this).text())
})

$('.ChoosePaymentTypePaytm').click(function(){
    money_to_add = $('#CashAmount').val()
    var cash = parseInt($('#CashAmount').val())
    if(isNaN(cash)){
        alert("Please valid Amount")
    }
    else{
        $('.JoinNowContainer').append("<a id=\"MoneyPayButton\" href=\"/payments/payment/?money_to_add=" + money_to_add + "\"></a>")
    document.getElementById('MoneyPayButton').click();
    }


//     $('#PaytmCashButton').click(function(event){
//     console.log("hello")
//     var cash = parseInt($('#CashAmount').val())

//     else{
//         window.location.href = "https://www.tutorialrepublic.com/";
//     }
//     console.log(cash,typeof(cash))
// })

})

window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove();
    });
}, 4000);

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

$(".AddEmailButton").click(function(event){
  event.preventDefault();
  console.log("Called")
  verify_this_email = $('#id_email').val()
  var csrftoken = getCookie('csrftoken');
  //incorrect_input_data = "<center>Please Enter a valid Gamil Account<b>(youname@gamil.com)</b></center>";
  //correct_input_data = "OTP sent to Email : "+verify_this_email+". Please Enter the OTP in below box.<center><input type=\"input\" id=\"verify_input\"><input class=\"verify_button_email btn\" type=\"button\" name=\"verify\" value=\"Verify\" verify-input=\"/verify_email_otp/\"></center>"
  $.ajax({
      url: $(this).attr('verify-input'),
      async: false,
      type: "POST",
      data:{
        verify_it: verify_this_email,
        csrfmiddlewaretoken : csrftoken,
      },
      dataType: 'json',
      success: function (data) {
        if (data.email_valid){
            // Check browser support
            if (typeof(Storage) !== "undefined") {
              // Store
              localStorage.setItem(data.variable, data.value_of);
              $('#VerifyEmailForm').get(0).submit();
            }
            else {
              aler("Sorry, your browser does not support Web Storage. Please update it.");
              window.location.href = "https://fancychamps.com/cricket_center";
            }            
        }
        if(data.email_taken){
            $('.AddEmailInfoProvider').html("<center>Account with this email already Exists!</center>")
            $('.AddEmailInfoProvider').fadeIn(1000);
            $('.AddEmailInfoProvider').delay(3000).fadeOut();
        }
        else if(!data.email_valid){
            $('.AddEmailInfoProvider').html("<center>Please enter a valid Email ending with @gamil.com</center>")
            $('.AddEmailInfoProvider').fadeIn(1000);
            $('.AddEmailInfoProvider').delay(3000).fadeOut();
        }
      }
  });  
})



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

