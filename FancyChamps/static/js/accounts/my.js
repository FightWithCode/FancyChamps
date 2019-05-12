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