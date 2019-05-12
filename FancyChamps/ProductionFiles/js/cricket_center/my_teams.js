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

$('.Preview').click(function () {
    var match_slug = $('#match_slug').attr('value')
    $.ajax({
        url: $(this).attr('go-to'),
        type: "GET",
        data: {match_slug: match_slug},
        dataType: 'json',
        success: function (data) {
                console.log("Data : ")
                console.log(data)

                if (data.keeper_count == 1){
                    KeepersDivWidth = 100/data.keeper_count+"%"
                    $(".KeepersPreview").html("<div class=\"PlayerView\" style=\"position:relative; margin-top:0px; width: " + KeepersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/keeper.png\"></center>" + data.keeper + "</div>")
                }

                if (data.bat_count == 3){
                    BatsmenDivWidth = 100/data.bat_count+"%"
                    $(".BatsmenPreview").html("")
                    for(var i=0; i<3; i++){
                        $(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + data["bat"+(i+1)] + "</span></div>")
                    }
                }
                if (data.bat_count == 4){
                    BatsmenDivWidth = 100/data.bat_count+"%"
                    $(".BatsmenPreview").html("")
                    for(var i=0; i<4; i++){
                        $(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + data["bat"+(i+1)] + "</span></div>")
                    }
                }
                if (data.bat_count == 5){
                    BatsmenDivWidth = 100/data.bat_count+"%"
                    $(".BatsmenPreview").html("")
                    for(var i=0; i<5; i++){
                        $(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + data["bat"+(i+1)] + "</span></div>")
                    }
                }

                if (data.allrounder_count == 1){
                    AllrounderDivWidth = 100/data.allrounder_count+"%"
                    $(".AllrounderPreview").html("<div class=\"PlayerView\" style=\"width: " + AllrounderDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/allrounder.png\"></center><span class=\"PlayerNameView\">" + data["allrounder"+(data.bat_count+1)] + "</span></div>")
                }

                if (data.allrounder_count == 2){
                    AllrounderDivWidth = 100/data.allrounder_count+"%"
                    $(".AllrounderPreview").html("")
                    for(var i=0; i<2; i++){
                        $(".AllrounderPreview").append("<div class=\"PlayerView\" style=\"width: " + AllrounderDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/allrounder.png\"></center><span class=\"PlayerNameView\">" + data["allrounder"+(data.bat_count+i+1)] + "</span></div>")
                    }
                }
                if (data.allrounder_count == 3){
                    AllrounderDivWidth = 100/data.allrounder_count+"%"
                    $(".AllrounderPreview").html("")
                    for(var i=0; i<3; i++){
                        $(".AllrounderPreview").append("<div class=\"PlayerView\" style=\"width: " + AllrounderDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/allrounder.png\"></center><span class=\"PlayerNameView\">" + data["allrounder"+(data.bat_count+i+1)] + "</span></div>")
                    }
                }

                if (data.bowl_count == 3){
                    BolwersDivWidth = 100/data.bowl_count+"%"
                    $(".BowlerPreview").html("")
                    for(var i=0; i<3; i++){
                        $(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + data["bowl"+(data.bat_count+data.allrounder_count+1+i)] + "</span></div>")
                    }
                }
                if (data.bowl_count == 4){
                    BolwersDivWidth = 100/data.bowl_count+"%"
                    $(".BowlerPreview").html("")
                    for(var i=0; i<4; i++){
                        $(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + data["bowl"+(data.bat_count+data.allrounder_count+1+i)] + "</span></div>")
                    }
                }
                if (data.bowl_count == 5){
                    BolwersDivWidth = 100/data.bowl_count+"%"
                    $(".BowlerPreview").html("")
                    for(var i=0; i<5; i++){
                        $(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + data["bowl"+(data.bat_count+data.allrounder_count+1+i)] + "</span></div>")
                    }
                }

                $('.CaptainVicePrivew').html("")
                $('.CaptainVicePrivew').append("<div class=\"PlayerView\" style=\"width: 50%;\"><center><span class=\"PlayerNameView\">Captain</span><img class=\"player_image\" src=\"/static/images/2x.png\"><span class=\"PlayerNameView\">" + data["captain"] + "</span></center></div>")

                $('.CaptainVicePrivew').append("<div class=\"PlayerView\" style=\"width: 50%;\"><center><span class=\"PlayerNameView\">Vice Captain</span><img class=\"player_image\" src=\"/static/images/15x.png\"><span class=\"PlayerNameView\">" + data["vice"] + "</span></center></div>")
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
























