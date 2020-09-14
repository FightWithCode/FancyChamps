$(".Preview").click(function() {
    $(this).css("visibility", "hidden"), $(this).css("display", "none"), setTimeout(function() {
        $(".Preview").css("visibility", "visible"), $(".Preview").css("display", "block")
    }, 500)
}), $(".CloseTeamPreviewContainer").click(function() {
    var e = $(".TeamPreviewContainer"),
        i = e.height();
    e.css({
        overflow: "hidden",
        marginTop: 0,
        height: i
    }).animate({
        marginTop: i,
        height: 0
    }, 500, function() {
        $(this).css({
            display: "none",
            overflow: "",
            height: "",
            marginTop: ""
        })
    })
}), $(".Preview").click(function() {
    var e = $("#match_slug").attr("value");
    $.ajax({
        url: $(this).attr("go-to"),
        type: "GET",
        data: {
            match_slug: e
        },
        dataType: "json",
        success: function(e) {
            console.log(e)
            $(".KeepersPreview").html("");
            for (var i = 0; i < e.def_count; i++) $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView">' + e["def" + (i + 1)] + "</span></div>");
            $(".AllrounderPreview").html("");
            for (i = 0; i < e.allrounder_count; i++) $(".AllrounderPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView">' + e["allrounder" + (i + 1 + e.def_count)] + "</span></div>");
            $(".BatsmenPreview").html("");
            for (i = 0; i < e.raider_count; i++) $(".BatsmenPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView">' + e["raider" + (i + 1 + e.def_count + e.allrounder_count)] + "</span></div>");
            $(".CaptainVicePrivew").html(""), $(".CaptainVicePrivew").append('<div class="PlayerView" style="width: 50%;"><center><span class="PlayerNameView">Captain</span><img class="player_image" src="/static/images/2x.png"><span class="PlayerNameView">' + e.captain + "</span></center></div>"), $(".CaptainVicePrivew").append('<div class="PlayerView" style="width: 50%;"><center><span class="PlayerNameView">Vice Captain</span><img class="player_image" src="/static/images/15x.png"><span class="PlayerNameView">' + e.vice + "</span></center></div>")
        }
    });
    var i = $(".TeamPreviewContainer"),
        a = i.css({
            display: "inline"
        }).height();
    i.css({
        overflow: "hidden",
        marginTop: a,
        height: 0
    }).animate({
        marginTop: 0,
        height: a
    }, 500, function() {
        $(this).css({
            display: "inline-block",
            overflow: "",
            height: "",
            marginTop: ""
        })
    })
});