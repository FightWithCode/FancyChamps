function openCity(e, a) {
    var t, l, s;
    for (l = document.getElementsByClassName("tabcontent"), t = 0; t < l.length; t++) l[t].style.display = "none";
    for (s = document.getElementsByClassName("tablinks"), t = 0; t < s.length; t++) s[t].className = s[t].className.replace(" active", "");
    document.getElementById(a).style.display = "block", e.currentTarget.className += " active"
}

function openEvent(e, a) {
    var t, l, s;
    for (l = document.getElementsByClassName("tabcontents"), t = 0; t < l.length; t++) l[t].style.display = "none";
    for (s = document.getElementsByClassName("tablinksMain"), t = 0; t < s.length; t++) s[t].className = s[t].className.replace(" active", "");
    document.getElementById(a).style.display = "block", e.currentTarget.className += " active"
}

function resetForms() {
    for (i = 0; i < document.forms.length; i++) document.forms[i].reset()
}

function KeeperFunction() {
    captain_id = $(this).attr("name") + "_1", vice_id = $(this).attr("name") + "_2", $("#" + captain_id).prop("checked", !1), $("#" + vice_id).prop("checked", !1);
    var e = $(".keeper:checkbox:checked");
    for (players_input = $(".CustomInput"), team_one = $(".TeamOneText").text(), team_two = $(".TeamTwoText").text(), selected_players = $(".CustomInput:checkbox:checked"), global_team_one_player = 0, global_team_two_player = 0, i = 0; i < selected_players.length; i++) id = selected_players[i].id, team = $("#" + id).next().find(".CustomField").find(".PlayerTeam").text(), team === team_one ? global_team_one_player += 1 : global_team_two_player += 1;
    for (var a = 0, t = 0; t < players_input.length; t++) $(players_input[t]).is(":checked") && (a += 1);
    global_keeper_count = a > 11 ? e.length - 1 : e.length, CheckCredit() > 100 && ($(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Opps! You don't have enough<strong> Points</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)), global_keeper_count > 4 && ($(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select Only <strong>4 Defenders</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)), a > 7 && ($(this).prop("checked", !1), $("#max").css("display", "block"), $("#max").html("Please Select Only <strong>7 Players</strong>"), $("#max").delay(3e3).fadeOut(1e3)), global_team_one_player > 5 && ($(this).prop("checked", !1), $("#max").css("display", "block"), $("#max").html("Select Only <strong>5 Players</strong> from each Team"), $("#max").delay(3e3).fadeOut(1e3)), global_team_two_player > 5 && ($(this).prop("checked", !1), $("#max").css("display", "block"), $("#max").html("Select Only <strong>5 Players</strong> from each Team"), $("#max").delay(3e3).fadeOut(1e3))
}

function BatsmanFunction() {
    captain_id = $(this).attr("name") + "_1", vice_id = $(this).attr("name") + "_2", $("#" + captain_id).prop("checked", !1), $("#" + vice_id).prop("checked", !1);
    var e = $(".batsmen:checkbox:checked");
    for (players_input = $(".CustomInput"), team_one = $(".TeamOneText").text(), team_two = $(".TeamTwoText").text(), selected_players = $(".CustomInput:checkbox:checked"), global_team_one_player = 0, global_team_two_player = 0, i = 0; i < selected_players.length; i++) id = selected_players[i].id, team = $("#" + id).next().find(".CustomField").find(".PlayerTeam").text(), team === team_one ? global_team_one_player += 1 : global_team_two_player += 1;
    for (var a = 0, t = 0; t < players_input.length; t++) $(players_input[t]).is(":checked") && (a += 1);
    global_batsmen_count = a > 11 ? e.length - 1 : e.length, CheckCredit() > 100 && ($(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Opps! You don't have enough<strong> Points</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)), global_batsmen_count > 3 && ($(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select Only <strong>3 Raiders</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)), a > 7 && ($(this).prop("checked", !1), $("#max").css("display", "block"), $("#max").html("Please Select Only <strong>7 Players</strong>"), $("#max").delay(3e3).fadeOut(1e3)), global_team_one_player > 5 && ($(this).prop("checked", !1), $("#max").css("display", "block"), $("#max").html("Select Only <strong>5 Players</strong> from each Team"), $("#max").delay(3e3).fadeOut(1e3)), global_team_two_player > 5 && ($(this).prop("checked", !1), $("#max").css("display", "block"), $("#max").html("Select Only <strong>5 Players</strong> from each Team"), $("#max").delay(3e3).fadeOut(1e3))
}

function AllrounderFunction() {
    captain_id = $(this).attr("name") + "_1", vice_id = $(this).attr("name") + "_2", $("#" + captain_id).prop("checked", !1), $("#" + vice_id).prop("checked", !1);
    var e = $(".allrounders:checkbox:checked");
    for (players_input = $(".CustomInput"), team_one = $(".TeamOneText").text(), team_two = $(".TeamTwoText").text(), selected_players = $(".CustomInput:checkbox:checked"), global_team_one_player = 0, global_team_two_player = 0, i = 0; i < selected_players.length; i++) id = selected_players[i].id, team = $("#" + id).next().find(".CustomField").find(".PlayerTeam").text(), team === team_one ? global_team_one_player += 1 : global_team_two_player += 1;
    for (var a = 0, t = 0; t < players_input.length; t++) $(players_input[t]).is(":checked") && (a += 1);
    global_allrounder_count = a > 11 ? e.length - 1 : e.length, CheckCredit() > 100 && ($(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Opps! You don't have enough<strong> Points</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)), global_allrounder_count > 2 && ($(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select Only <strong>2 Allrounders</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)), a > 7 && ($(this).prop("checked", !1), $("#max").css("display", "block"), $("#max").html("Please Select Only <strong>7 Players</strong>"), $("#max").delay(3e3).fadeOut(1e3)), global_team_one_player > 5 && ($(this).prop("checked", !1), $("#max").css("display", "block"), $("#max").html("Select Only <strong>5 Players</strong> from each Team"), $("#max").delay(3e3).fadeOut(1e3)), global_team_two_player > 5 && ($(this).prop("checked", !1), $("#max").css("display", "block"), $("#max").html("Select Only <strong>5 Players</strong> from each Team"), $("#max").delay(3e3).fadeOut(1e3))
}

function CheckCredit() {
    credits = 0, selected_players = $(".CustomInput:checkbox:checked");
    for (var e = 0; e < selected_players.length; e++) player = $("#" + selected_players[e].id), credits += +player.next("label").find(".PlayerCredits").html(), player_team = player.next("label").find(".PlayerTeam").html();
    return $("#total_credits_points").val(credits), $(".CreditPointsClass").html(100 - credits + "/100"), $(".TotalPlayersClass").html(selected_players.length + "/7"), credits
}

function TeamCollector() {
    for (credits = 0, selected_players = $(".CustomInput:checkbox:checked"), team_one = $(".TeamOneText").text(), team_two = $(".TeamTwoText").text(), global_team_one_player = 0, global_team_two_player = 0, i = 0; i < selected_players.length; i++) id = selected_players[i].id, team = $("#" + id).next().find(".CustomField").find(".PlayerTeam").text(), team === team_one ? global_team_one_player += 1 : global_team_two_player += 1;
    $(".TeamOneSelected").text(global_team_one_player), $(".TeamTwoSelected").text(global_team_two_player);
    for (var e = 0; e < selected_players.length; e++) player = $("#" + selected_players[e].id), credits += +player.next("label").find(".PlayerCredits").html(), player_team = player.next("label").find(".PlayerTeam").html();
    $("#total_credits_points").val(credits), $(".CreditPointsClass").html(100 - credits + "/100"), $(".TotalPlayersClass").html(selected_players.length + "/7")
}
$(".CloseTeamPreviewContainer").click(function() {
    var e = $(".TeamPreviewContainer"),
        a = e.height();
    e.css({
        overflow: "hidden",
        marginTop: 0,
        height: a
    }).animate({
        marginTop: a,
        height: 0
    }, 500, function() {
        $(this).css({
            display: "none",
            overflow: "",
            height: "",
            marginTop: ""
        })
    })
}), $(".TeamPreviewClass").click(function() {
    if (selected_batsmen = $(".batsmen:checkbox:checked"), selected_allrounders = $(".allrounders:checkbox:checked"), selected_keepers = $(".keeper:checkbox:checked"), selected_captain = $(".captain_class:checkbox:checked"), selected_vicecaptain = $(".vice_class:checkbox:checked"), team_one = $(".TeamOneText").text(), team_two = $(".TeamTwoText").text(), 1 == selected_keepers.length) {
        $(".KeepersPreview").html("");
        for (var a = 0; a < 1; a++) {
            var t = selected_keepers[a].name.split("_");
            id = selected_keepers[a].id, team_one === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() ? $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:red;margin:10px;">' + t[0] + " " + t[1] + "</span></div>") : team_two === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() && $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:green;margin:10px;">' + t[0] + " " + t[1] + "</span></div>")
        }
    } else {
        $(".KeepersPreview").html("");
        for (var l = 0; l < 4; l++) $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/question.png"></center><span class="PlayerNameView">Defender</span></div>')
    }
    if (2 === selected_keepers.length) {
        $(".KeepersPreview").html("");
        for (a = 0; a < 2; a++) {
            t = selected_keepers[a].name.split("_");
            id = selected_keepers[a].id, team_one === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() ? $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:red;margin:10px;">' + t[0] + " " + t[1] + "</span></div>") : team_two === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() && $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:green;margin:10px;">' + t[0] + " " + t[1] + "</span></div>")
        }
    }
    if (3 === selected_keepers.length) {
        $(".KeepersPreview").html("");
        for (a = 0; a < 3; a++) {
            t = selected_keepers[a].name.split("_");
            id = selected_keepers[a].id, team_one === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() ? $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:red;margin:10px;">' + t[0] + " " + t[1] + "</span></div>") : team_two === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() && $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:green;margin:10px;">' + t[0] + " " + t[1] + "</span></div>")
        }
    }
    if (4 === selected_keepers.length) {
        $(".KeepersPreview").html("");
        for (a = 0; a < 4; a++) {
            t = selected_keepers[a].name.split("_");
            id = selected_keepers[a].id, team_one === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() ? $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:red;margin:10px;">' + t[0] + " " + t[1] + "</span></div>") : team_two === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() && $(".KeepersPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:green;margin:10px;">' + t[0] + " " + t[1] + "</span></div>")
        }
    }
    if (1 == selected_batsmen.length) {
        $(".BatsmenPreview").html("");
        for (a = 0; a < 1; a++) {
            t = selected_batsmen[a].name.split("_");
            id = selected_batsmen[a].id, team_one === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() ? $(".BatsmenPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:red;margin:10px;">' + t[0] + " " + t[1] + "</span></div>") : team_two === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() && $(".BatsmenPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:green;margin:10px;">' + t[0] + " " + t[1] + "</span></div>")
        }
    } else {
        $(".BatsmenPreview").html("");
        for (l = 0; l < 4; l++) $(".BatsmenPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/question.png"></center><span class="PlayerNameView">Raider</span></div>')
    }
    if (2 === selected_batsmen.length) {
        $(".BatsmenPreview").html("");
        for (a = 0; a < 2; a++) {
            t = selected_batsmen[a].name.split("_");
            id = selected_batsmen[a].id, team_one === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() ? $(".BatsmenPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:red;margin:10px;">' + t[0] + " " + t[1] + "</span></div>") : team_two === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() && $(".BatsmenPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:green;margin:10px;">' + t[0] + " " + t[1] + "</span></div>")
        }
    }
    if (3 === selected_batsmen.length) {
        $(".BatsmenPreview").html("");
        for (a = 0; a < 3; a++) {
            t = selected_batsmen[a].name.split("_");
            id = selected_batsmen[a].id, team_one === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() ? $(".BatsmenPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:red;margin:10px;">' + t[0] + " " + t[1] + "</span></div>") : team_two === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() && $(".BatsmenPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:green;margin:10px;">' + t[0] + " " + t[1] + "</span></div>")
        }
    }
    if (1 == selected_allrounders.length) {
        $(".AllrounderPreview").html("");
        for (a = 0; a < 1; a++) {
            t = selected_allrounders[a].name.split("_");
            id = selected_allrounders[a].id, team_one === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() ? $(".AllrounderPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:red;margin:10px;">' + t[0] + " " + t[1] + "</span></div>") : team_two === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() && $(".AllrounderPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:green;margin:10px;">' + t[0] + " " + t[1] + "</span></div>")
        }
    } else
        for ($(".AllrounderPreview").html(""), l = 0; l < 2; l++) $(".AllrounderPreview").append('<div class="PlayerView" style="width: 50%"><center><img class="player_image" src="/static/images/question.png"></center><span class="PlayerNameView">Allrounder</span></div>');
    if (2 === selected_allrounders.length) {
        $(".AllrounderPreview").html("");
        for (a = 0; a < 2; a++) {
            t = selected_allrounders[a].name.split("_");
            id = selected_allrounders[a].id, team_one === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() ? $(".AllrounderPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:red;margin:10px;">' + t[0] + " " + t[1] + "</span></div>") : team_two === $("#" + id).next().find(".CustomField").find(".PlayerTeam").text() && $(".AllrounderPreview").append('<div class="PlayerView" style="width: 25%"><center><img class="player_image" src="/static/images/defender.png"></center><span class="PlayerNameView" style="background-color:green;margin:10px;">' + t[0] + " " + t[1] + "</span></div>")
        }
    }
    1 == selected_captain.length ? ($(".CaptainVicePrivew").html(""), e = selected_captain[0].value.split("_"), $(".CaptainVicePrivew").append('<div class="PlayerView" style="width: 50%;"><center><span class="PlayerNameView">Captain</span><img class="player_image" src="/static/images/2x.png"><span class="PlayerNameView">' + e[0] + " " + e[1] + "</span></center></div>")) : 0 == selected_captain.length ? ($(".CaptainVicePrivew").html(""), $(".CaptainVicePrivew").append('<div class="PlayerView" style="width: 50%;"><center><span class="PlayerNameView">Captain</span><img class="player_image" src="/static/images/2x.png"><span class="PlayerNameView">Select</span></center></div>')) : ($(".CaptainVicePrivew").html(""), $(".CaptainVicePrivew").append('<div class="CaptainClass"><center>Something Went Wrong...</center></div>')), 1 == selected_vicecaptain.length ? (e = selected_vicecaptain[0].value.split("_"), $(".CaptainVicePrivew").append('<div class="PlayerView" style="width: 50%;"><center><span class="PlayerNameView">Vice Captain</span><img class="player_image" src="/static/images/15x.png"><span class="PlayerNameView">' + e[0] + " " + e[1] + "</span></center></div>")) : 0 == selected_vicecaptain.length ? $(".CaptainVicePrivew").append('<div class="PlayerView" style="width: 50%;"><center><span class="PlayerNameView">Vice Captain</span><img class="player_image" src="/static/images/15x.png"><span class="PlayerNameView">Select</span></center></div>') : $(".CaptainVicePrivew").append('<div class="ViceClass"><center>Something Went Wrong...</center></div>');
    var s = $(".TeamPreviewContainer"),
        i = s.css({
            display: "inline"
        }).height();
    s.css({
        overflow: "hidden",
        marginTop: i,
        height: 0
    }).animate({
        marginTop: 0,
        height: i
    }, 0, function() {
        $(this).css({
            display: "inline-block",
            overflow: "",
            height: "",
            marginTop: ""
        })
    })
}), $(".captain_class").change(function() {
    var e = $(this).is(":checked"),
        a = $(this).next().next().is(":checked");
    $(".captain_class").prop("checked", !1), e && ($(this).prop("checked", !0), a && $(this).next().next().prop("checked", !1))
}), $(".vice_class").change(function() {
    var e = $(this).is(":checked");
    $(".vice_class").prop("checked", !1);
    var a = $(this).prev().prev().is(":checked");
    e && ($(this).prop("checked", !0), a && $(this).prev().prev().prop("checked", !1))
}), $(document).ready(function() {
    resetForms()
}), ajaxComplete = !1, $(document).ready(function() {
    var e = $("#match_slug").attr("value"),
        a = $("#team").attr("value");
    $("#get_team_info").attr("value"), $.ajax({
        url: $("#get_team_info").attr("url-is"),
        type: "GET",
        data: {
            team_no: a,
            match_slug: e
        },
        dataType: "json",
        success: function(e) {
            captain_id = e.team_captain.replace(/ /g, "_") + "_1", $("#" + captain_id).prop("checked", !0), vice_id = e.team_vice.replace(/ /g, "_") + "_2", $("#" + vice_id).prop("checked", !0), $(".CreditPointsClass").html(100 - e.total_credits_points + "/100"), 3 == e.total_defenders_in_team && (id = "id_" + e.def1.replace(/ /g, "_"), $("#" + id).prop("checked", !0), id1 = "id_" + e.def2.replace(/ /g, "_"), $("#" + id1).prop("checked", !0), id2 = "id_" + e.def3.replace(/ /g, "_"), $("#" + id2).prop("checked", !0)), 2 == e.total_defenders_in_team && (id = "id_" + e.def1.replace(/ /g, "_"), $("#" + id).prop("checked", !0), id1 = "id_" + e.def2.replace(/ /g, "_"), $("#" + id1).prop("checked", !0)), 4 == e.total_defenders_in_team && (id = "id_" + e.def1.replace(/ /g, "_"), $("#" + id).prop("checked", !0), id1 = "id_" + e.def2.replace(/ /g, "_"), $("#" + id1).prop("checked", !0), id2 = "id_" + e.def3.replace(/ /g, "_"), $("#" + id2).prop("checked", !0), id3 = "id_" + e.def4.replace(/ /g, "_"), $("#" + id3).prop("checked", !0)), 1 == e.total_allrounders_in_team && (id = "id_" + e.allrounder1.replace(/ /g, "_"), $("#" + id).prop("checked", !0)), 2 == e.total_allrounders_in_team && (id = "id_" + e.allrounder1.replace(/ /g, "_"), $("#" + id).prop("checked", !0), id1 = "id_" + e.allrounder2.replace(/ /g, "_"), $("#" + id1).prop("checked", !0)), 3 == e.total_raiders_in_team && (id = "id_" + e.raider1.replace(/ /g, "_"), $("#" + id).prop("checked", !0), id1 = "id_" + e.raider2.replace(/ /g, "_"), $("#" + id1).prop("checked", !0), id2 = "id_" + e.raider3.replace(/ /g, "_"), $("#" + id2).prop("checked", !0)), 2 == e.total_raiders_in_team && (id = "id_" + e.raider1.replace(/ /g, "_"), $("#" + id).prop("checked", !0), id1 = "id_" + e.raider2.replace(/ /g, "_"), $("#" + id1).prop("checked", !0)), 1 == e.total_raiders_in_team && (id = "id_" + e.raider1.replace(/ /g, "_"), $("#" + id).prop("checked", !0)), KeeperFunction(), BatsmanFunction(), AllrounderFunction(), TeamCollector()
        }
    })
}), global_team_one_player = 0, global_team_two_player = 0, global_keeper_count = 0, global_batsmen_count = 0, global_bowler_count = 0, global_allrounder_count = 0, temp_global = 0, $(".keeper").on("click", KeeperFunction), $(".batsmen").on("click", BatsmanFunction), $(".allrounders").on("click", AllrounderFunction), $(".btn-sm").click(function(e) {
    players_input = $(".CustomInput");
    for (var a = 0, t = 0; t < players_input.length; t++) $(players_input[t]).is(":checked") && (a += 1);
    a < 7 ? (e.preventDefault(), $(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select At Least <strong>7 Players</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)) : global_keeper_count < 1 ? (e.preventDefault(), $(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select At Least <strong>1 Defender</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)) : global_batsmen_count < 1 ? (e.preventDefault(), $(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select At Least <strong>1 Raider</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)) : global_allrounder_count < 1 ? (e.preventDefault(), $(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select At Least <strong>1 Allrounder</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)) : $(".captain_class").is(":checked") ? $(".captain_class").is(":checked") ? $(".vice_class").is(":checked") || (e.preventDefault(), $(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select Your <strong>Vice Captain</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)) : (e.preventDefault(), $(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select Your <strong>Captain</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)) : (e.preventDefault(), $(".vice_class").is(":checked") ? ($(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select Your <strong>Captain</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)) : ($(this).prop("checked", !1), $("#sub_max").css("display", "block"), $("#sub_max").html("Please Select Your <strong>Captain and Vice Captain</strong>"), $("#sub_max").delay(3e3).fadeOut(1e3)))
}), $(".CustomInput").click(function() {
    for (credits = 0, selected_players = $(".CustomInput:checkbox:checked"), team_one = $(".TeamOneText").text(), team_two = $(".TeamTwoText").text(), global_team_one_player = 0, global_team_two_player = 0, i = 0; i < selected_players.length; i++) id = selected_players[i].id, team = $("#" + id).next().find(".CustomField").find(".PlayerTeam").text(), team === team_one ? global_team_one_player += 1 : global_team_two_player += 1;
    $(".TeamOneSelected").text(global_team_one_player), $(".TeamTwoSelected").text(global_team_two_player);
    for (var e = 0; e < selected_players.length; e++) player = $("#" + selected_players[e].id), credits += +player.next("label").find(".PlayerCredits").html(), player_team = player.next("label").find(".PlayerTeam").html();
    $("#total_credits_points").val(credits), $(".CreditPointsClass").html(100 - credits + "/100"), $(".TotalPlayersClass").html(selected_players.length + "/7")
});
