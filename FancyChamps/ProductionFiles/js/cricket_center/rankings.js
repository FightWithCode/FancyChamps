$('.LeagueName').click(function(){
    var div = $(".PayoutDiv");
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

    // $('.PayoutDiv').toggle()
    $('.PayoutDivInfoContainer').html("")
    $('.PayoutDivContestTypes').html("")
    // //$('.PayoutDiv'+$(this).attr('pay-view').replace("/cricket_center/view_payout/", '')).toggle()
    //$('.LiContainer'+$(this).attr('pay-view').replace("/cricket_center/view_payout/", '')).html("")
    //class_is = '.LiContainer'+$(this).attr('pay-view').replace("/cricket_center/view_payout/", '')
    $.ajax({
        url: $(this).attr('pay-view'),
        dataType: 'json',
        success: function (data) {
            console.log(typeof(data))
            $('.PayoutDivInfoContainer').append("<center>NOTE : In case of the contest does not get filled then the total prize will be distributed to <b>First Rank(Rank 1)</b></center>")
            for (var key in data) {
                if (data.hasOwnProperty(key) && key!="multiple_entry" && key!="confirmed" && key!="id" && key!="bonus_contest") {
                    console.log(typeof(key))
                    new_rank = key.replace('Rank', '')
                    new_rank = new_rank.replace('To', '-')
                    console.log(new_rank + " : " + data[key]+"₹");
                    $('.PayoutDivInfoContainer').append("<li style=\"list-style-type:none\">Rank " + new_rank + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + "<span style=\"float:right\">" + data[key] + "₹" + "</span></li>")
                }
            }
            if(data.confirmed){
                $('.PayoutDivContestTypes').append("<span class=\"ContestTypesJs\">C</span><span class=\"ContestTypeInfo\">This is a confirmed contest.</span><br>")    
            }
            if(data.bonus_contest){
                $('.PayoutDivContestTypes').append("<span class=\"ContestTypesJs\">B</span><span class=\"ContestTypeInfo\">You can use bonus in this contest.</span><br>")  
            }
            if(data.multiple_entry){
                $('.PayoutDivContestTypes').append("<span class=\"ContestTypesJs\">M</span><span class=\"ContestTypeInfo\">You can join this contest with multiple teams.</span><br>")  
            }
        }
    })
})


$(".Message").click(function(){
    var message=$(this).attr("message")
    slug = $("#CS").attr("slug")
    $.ajax({
        url: $(this).attr('go-to'),
        type: "GET",
        data: {"message_no":message, "slug":slug},
        dataType: 'json',
        success: function (data) {
                if(!data[data.length-1]){
                    alert("Please wait for someone to reply")
                }
                else{
                    $('.MessagesDiv').html("")
                    for (i=0;i<data.length-2;i++){
                        if(data[i].user==data[data.length-2]){
                            $('.MessagesDiv').append("<p class=\"UserMessages\">"+data[i].message+":"+data[i].user+"</p><br><br>")
                        }
                        else{
                            $('.MessagesDiv').append("<p class=\"OtherMessages\">"+data[i].message+":"+data[i].user+"</p><br><br>")
                        }
                    }
                }
            }
    });
});

$(".CloseTeamPreviewContainer").click(function () {
    var div = $(".TeamPreviewContainer");

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

$(".CloseMessageContainer").click(function () {
    var div = $(".MessageContainer");

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

$('#MessageButton').click(function () {
    slug = $("#CS").attr("slug")
    $.ajax({
        url: $('.Message').attr('go-to'),
        type: "GET",
        data: {"message_no":0, "slug":slug},
        dataType: 'json',
        success: function (data) {
                $('.MessagesDiv').html("")
                for (i=0;i<data.length-2;i++){
                    if(data[i].user==data[data.length-2]){
                        $('.MessagesDiv').append("<p class=\"UserMessages\">"+data[i].message+":"+data[i].user+"</p><br><br>")
                    }
                    else{
                        $('.MessagesDiv').append("<p class=\"OtherMessages\">"+data[i].message+":"+data[i].user+"</p><br><br>")
                    }
                }
            }
    });
    var div = $(".MessageContainer");
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

$('.RankInfoCard').click(function () {
    // var match_slug = $('#match_slug').attr('value')
    // console.log(match_slug)
    $.ajax({
        url: $(this).attr('go-to'),
        type: "GET",
        dataType: 'json',
        success: function (data) {
                KeepersDivWidth = 100/1+"%"
                $(".KeepersPreview").html("<div class=\"PlayerView\" style=\"position:relative; margin-top:0px; width: " + KeepersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/keeper.png\"></center>" + data.Keeper + "<br>" + data.Keeper_Points + "</div>")
                if (data.total_batsmen == 3){
                    BatsmenDivWidth = 100/data.total_batsmen+"%"
                    $(".BatsmenPreview").html("")
                    for(var i=0; i<3; i++){
                        $(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + data["Player"+[i+2]] + "<br>" + data["Player"+[i+2]+"_Points"] + "</span></div>")
                    }
                }
                if (data.total_batsmen == 4){
                    BatsmenDivWidth = 100/data.total_batsmen+"%"
                    $(".BatsmenPreview").html("")
                    for(var i=0; i<4; i++){
                        $(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + data["Player"+[i+2]] + "<br>" + data["Player"+[i+2]+"_Points"] + "</span></div>")
                    }
                }
                if (data.total_batsmen == 5){
                    BatsmenDivWidth = 100/data.total_batsmen+"%"
                    $(".BatsmenPreview").html("")
                    for(var i=0; i<5; i++){
                        $(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + data["Player"+[i+2]] + "<br>" + data["Player"+[i+2]+"_Points"] + "</span></div>")
                    }
                }

                if (data.total_allrounders == 1){
                    AllrounderDivWidth = 100/data.total_allrounders+"%"
                    $(".AllrounderPreview").html("<div class=\"PlayerView\" style=\"width: " + AllrounderDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/allrounder.png\"></center><span class=\"PlayerNameView\">" + data["Player"+[data.total_batsmen+i+2]] + "<br>" + data["Player"+[data.total_batsmen+i+2]+"_Points"] + "</span></div>")
                }

                if (data.total_allrounders == 2){
                    AllrounderDivWidth = 100/data.total_allrounders+"%"
                    $(".AllrounderPreview").html("")
                    for(var i=0; i<2; i++){
                        $(".AllrounderPreview").append("<div class=\"PlayerView\" style=\"width: " + AllrounderDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/allrounder.png\"></center><span class=\"PlayerNameView\">" + data["Player"+[data.total_batsmen+i+2]] + "<br>" + data["Player"+[data.total_batsmen+i+2]+"_Points"] + "</span></div>")
                    }
                }
                if (data.total_allrounders == 3){
                    AllrounderDivWidth = 100/data.total_allrounders+"%"
                    $(".AllrounderPreview").html("")
                    for(var i=0; i<3; i++){
                        $(".AllrounderPreview").append("<div class=\"PlayerView\" style=\"width: " + AllrounderDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/allrounder.png\"></center><span class=\"PlayerNameView\">" + data["Player"+[data.total_batsmen+i+2]] + "<br>" + data["Player"+[data.total_batsmen+i+2]+"_Points"] + "</span></div>")
                    }
                }

                if (data.total_bowlers == 3){
                    BolwersDivWidth = 100/data.total_bowlers+"%"
                    $(".BowlerPreview").html("")
                    for(var i=0; i<3; i++){
                        $(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + data["Player"+[data.total_batsmen+data.total_allrounders+i+2]] + "<br>" + data["Player"+[data.total_batsmen+data.total_allrounders+i+2]+"_Points"] + "</span></div>")
                    }
                }
                if (data.total_bowlers == 4){
                    BolwersDivWidth = 100/data.total_bowlers+"%"
                    $(".BowlerPreview").html("")
                    for(var i=0; i<4; i++){
                        $(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + data["Player"+[data.total_batsmen+data.total_allrounders+i+2]] + "<br>" + data["Player"+[data.total_batsmen+data.total_allrounders+i+2]+"_Points"] + "</span></div>")
                    }
                }
                if (data.total_bowlers == 5){
                    BolwersDivWidth = 100/data.total_bowlers+"%"
                    $(".BowlerPreview").html("")
                    for(var i=0; i<5; i++){
                        $(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + data["Player"+[data.total_batsmen+data.total_allrounders+i+2]] + "<br>" + data["Player"+[data.total_batsmen+data.total_allrounders+i+2]+"_Points"] + "</span></div>")
                    }
                }

                $('.CaptainVicePrivew').html("")
                $('.CaptainVicePrivew').append("<div class=\"PlayerView\" style=\"width: 50%;\"><center><span class=\"PlayerNameView\">Captain</span><img class=\"player_image\" src=\"/static/images/2x.png\"><span class=\"PlayerNameView\">" + data.Captain + "<br>" + data.Captain_Points + "</span></center></div>")

                $('.CaptainVicePrivew').append("<div class=\"PlayerView\" style=\"width: 50%;\"><center><span class=\"PlayerNameView\">Vice Captain</span><img class=\"player_image\" src=\"/static/images/15x.png\"><span class=\"PlayerNameView\">" + data.Vice_Captain + "<br>" + data.Vice_Captain_Points + "</span></center></div>")
            }
    });

    var div = $(".TeamPreviewContainer");
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

$(".ClosePayoutDiv").click(function () {
	console.log("Print Me")
    var div = $(".PayoutDiv");

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
window.onload = function () {
	$(".ContestTypes").each(function(i) {
		if($(this).html()==""){
			$(this).removeClass("ContestTypes")
		}
    });
}