$('.LeagueName').click(function(){
	$('.PayoutDiv').toggle()
	$('.PayoutDiv').html("")
	//$('.PayoutDiv'+$(this).attr('pay-view').replace("/cricket_center/view_payout/", '')).toggle()
	//$('.LiContainer'+$(this).attr('pay-view').replace("/cricket_center/view_payout/", '')).html("")
	//class_is = '.LiContainer'+$(this).attr('pay-view').replace("/cricket_center/view_payout/", '')
	$.ajax({
        url: $(this).attr('pay-view'),
        dataType: 'json',
        success: function (data) {
			console.log(typeof(data))
			$('.PayoutDiv').append("<center><div style=\"position:relative;width:130%;left:-15%;line-height:14px;\"><span>NOTE : In case of the contest does not get filled then the total prize will be distributed to First Rank(Rank 1)</span><br>&nbsp;</center>")
			for (var key in data) {
    			if (data.hasOwnProperty(key) && key!="id") {
					console.log(typeof(key))
					new_rank = key.replace('Rank', '')
					new_rank = new_rank.replace('To', '-')
        			console.log(new_rank + " : " + data[key]+"₹");
					$('.PayoutDiv').append("<li style=\"list-style-type:none\">Rank " + new_rank + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + "<span style=\"float:right\">" + data[key] + "₹" + "</span></li>")
    			}
			}
        }
    })
})


$('.ProceedToPay').click(function (){
	$('.ChoosePaymentTypeContainer').css("display", "block")
    $('.ConentOfJoiningDetail').css("display", "none")
});


// var add_obj = {type:"Fiat", model:"500", color:"white"};
$('.JoinNowClass').click(function () {
	console.log("I got Called")
	$("#PayAndJoinNow").attr('id', 'PayAndJoinNowID')
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

    $.ajax({
        url: $(this).attr('check-teams'),
        dataType: 'json',
        success: function (data) {
        	if(data.profile_error){
		    	$('#sub_max').css('display','block');
		        $('#sub_max').html("Something went Wrong...");
		        $('#sub_max').delay(3000).fadeOut(1000);
		    	var div = $(".JoinNowContainer");
			    var height = div.height();
			    div.css({
			        overflow: "hidden",
			        marginTop: 0,
			        height: height,
			    }).animate({
			        marginBottom: height,
			        height: 0
			    }, 0, function () {
			        $(this).css({
			            display: "none",
			            overflow: "",
			            height: "",
			            marginTop: ""
			        });
			    });
		    }

    		else if(data.already_joined_or_filled){
    		    $('#sub_max').css('display','block');
		        $('#sub_max').html("Contest is Filled or You Have already Joined the Contest");
		        $('#sub_max').delay(3000).fadeOut(3000);
    			var div = $(".JoinNowContainer");
			    var height = div.height();
			    div.css({
			        overflow: "hidden",
			        marginTop: 0,
				        height: height,
			    }).animate({
			        marginBottom: height,
			        height: 0
			    }, 0, function () {
			        $(this).css({
			            display: "none",
			            overflow: "",
			            height: "",
			            marginTop: ""
			        });
			    });
			}
			if(data.add_money > 0 && data.low_balance == 1){

				$('.ConentOfJoiningDetail').css("display", "block")
				$('.PayAndJoinNow').css("display", "none")
				$('.ProceedToPay').css("display", "inline-block")
				$('.ProceedToPay').html("Proceed to Pay " + data.add_money)
				$('.JoinNowHeader').html("Join " + data.contest_name+ " Contest")
	   // 		$('#ContestPrice').html("₹"+data.contest_prize)
	   // 		$('#ContestFee').html("₹"+data.contest_fee)
	   // 		$('#UserMainBalance').html("₹"+data.user_balance)
	   // 		$('#UserBonus').html("₹"+data.user_bonus)
	    		$('#MainDeduction').html("₹"+data.user_balance)
	    		$('#BonusDeduction').html("₹"+data.contest_fee)
	    		$('#match_slug').val(data.match_slug)
	    		$('#contest_slug').val(data.contest_slug)
	    		$('.ChoosePaymentTypeContainer').css("display", "none")

				$('.ChoosePaymentTypePaytm').click(function(){
					console.log("Got Clicked")
					$('.ConentOfJoiningDetail').append("<a id=\"MoneyPayButton\" href=\"/payments/payment/?money_to_add=" + data.add_money + "\">Pay</a>")
					document.getElementById('MoneyPayButton').click();
				})

				// var csrftoken = getCookie('csrftoken');
	    		// var options = {
				//     "key": "rzp_test_C4Ohgv6Fhh2piC",
				//     "amount": data.add_money*100, // 2000 paise = INR 20
				//     "name": "Merchant Name",
				//     "description": "Purchase Description",
				//     "handler": function (response){
				//     	$.ajax({
				// 	        url: '/cricket_center/capture_payment/',
				// 	        type: 'POST',
				// 	        data: {csrfmiddlewaretoken: csrftoken, razorpay_payment_id: response.razorpay_payment_id, amt: data.add_money*100},
				// 	        dataType: 'json',
				// 	        success: function (data) {
				// 	        	console.log(data)
				// 				}
				// 	    });
				//         console.log(response);
				//     },
				//     "prefill": {
				//         "name": "Gaurav Kumar",
				//         "email": "test@test.com"
				//     },
				//     "notes": {
				//         "address": "Hello World"
				//     },
				//     "theme": {
				//         "color": "#F37254"
				//     }
				// };
				// var rzp1 = new Razorpay(options);

				// document.getElementById('rzp-button').onclick = function(e){
				//     rzp1.open();
				//     e.preventDefault();

				// }
    		}
    		else{
    			$('.ConentOfJoiningDetail').css("display", "block")
    			$('.ProceedToPay').css("display", "none")
    			$('.PayAndJoinNow').css("display", "inline-block")
    			$('.JoinNowHeader').html("Join " + data.contest_name+ " Contest")
	   // 		$('#ContestPrice').html("₹"+data.contest_prize)
	   // 		$('#ContestFee').html("₹"+data.contest_fee)
	   // 		$('#UserMainBalance').html("₹"+data.user_balance)
	   // 		$('#UserBonus').html("₹"+data.user_bonus)
	    		$('#MainDeduction').html("₹"+data.user_balance)
	    		$('#BonusDeduction').html("₹"+data.contest_fee)
	    		$('#match_slug').val(data.match_slug)
	    		$('#contest_slug').val(data.contest_slug)
	    		$('.ChoosePaymentTypeContainer').css("display", "none")
	        }
        }
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
});


//For getting CSRF token
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

$('.PayAndJoinNow').click(function () {
	var match_slug = $('#match_slug').attr('value')
	var contest_slug = $('#contest_slug').attr('value')
	var csrftoken = getCookie('csrftoken');
	if ($('input[name=SelectTeam]:checked').length == (1 || 2 || 3)){
		team_no = $('input[name=SelectTeam]:checked').val();
	    console.log(team_no)
	    $.ajax({
	        url: $(this).attr('pay-and-join'),
	        type: "POST",
	        data: {csrfmiddlewaretoken : csrftoken, match_slug: match_slug, contest_slug: contest_slug, team_no: team_no},
	        dataType: 'json',
	        success: function (data) {
	        	console.log(data)
			    if(data.already_joined_or_filled){
	    		    $('#sub_max').css('display','block');
		            $('#sub_max').html("Contest is Filled or You Have already Joined the Contest");
		            $('#sub_max').delay(3000).fadeOut(3000);
	    			var div = $(".JoinNowContainer");
				    var height = div.height();
				    div.css({
				        overflow: "hidden",
				        marginTop: 0,
				        height: height,
				    }).animate({
				        marginBottom: height,
				        height: 0
				    }, 0, function () {
				        $(this).css({
				            display: "none",
				            overflow: "",
				            height: "",
				            marginTop: ""
				        });
				    });
				}
				else if(data.error==true || data.contest_error==true){
				    $('#sub_max').css('display','block');
		            $('#sub_max').html("Something went wrong! Try another contest.");
		            $('#sub_max').delay(3000).fadeOut(1000);
				}
				else{
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
				    $('#sub_max').css('display','block');
		            $('#sub_max').html("Contest Joined");
		            $('#sub_max').delay(3000).fadeOut(1000);
				    location.reload(true);
				}
	        }
	    });
	}
	else{
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select a Team");
		$('#sub_max').delay(3000).fadeOut(1000);
	}
});
