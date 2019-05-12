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

$('.TeamPreviewClass').click(function () {
	selected_keepers = $('.keeper:checkbox:checked')
	selected_batsmen = $('.batsmen:checkbox:checked')
	selected_allrounders = $('.allrounders:checkbox:checked')
	selected_bowlers = $('.bowlers:checkbox:checked')
	selected_captain = $('.captain_class:checkbox:checked')
	selected_vicecaptain = $('.vice_class:checkbox:checked')
	if (selected_keepers.length == 1){
		var name_array = selected_keepers[0].name.split('_')
		KeepersDivWidth = 100/selected_keepers.length+"%"
		$(".KeepersPreview").html("<div class=\"PlayerView\" style=\"position:relative; margin-top:0px; width: " + KeepersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/keeper.png\"></center>" + name_array[0] + " " + name_array[1] + "</div>")
	}
	else{
		$(".KeepersPreview").html("")
		$(".KeepersPreview").append("<div class=\"PlayerView\" style=\"width: 25%\"><center><img class=\"player_image\" src=\"/static/images/question.png\"></center><span class=\"PlayerNameView\">Keeper</span></div>")
	}
	if (selected_batsmen.length == 1){
		var name_array = selected_batsmen[0].name.split('_')
		BatsmenDivWidth = 100/selected_batsmen.length+"%"
		$(".BatsmenPreview").html("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
	}
	else{
		$(".BatsmenPreview").html("")
		for(var i=0;i<4;i++){
			$(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: 25%\"><center><img class=\"player_image\" src=\"/static/images/question.png\"></center><span class=\"PlayerNameView\">Batsmen</span></div>")
		}
	}
	if (selected_batsmen.length === 2){
		BatsmenDivWidth = 100/selected_batsmen.length+"%"
		$(".BatsmenPreview").html("")
		for(var i=0; i<2; i++){
			var name_array = selected_batsmen[i].name.split('_')
			// var name = name_array[0] + ' ' + name_array[1]
			$(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}
	if (selected_batsmen.length === 3){
		BatsmenDivWidth = 100/selected_batsmen.length+"%"
		$(".BatsmenPreview").html("")
		for(var i=0; i<3; i++){
			var name_array = selected_batsmen[i].name.split('_')
			$(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}
	if (selected_batsmen.length === 4){
		BatsmenDivWidth = 100/selected_batsmen.length+"%"
		$(".BatsmenPreview").html("")
		for(var i=0; i<4; i++){
			var name_array = selected_batsmen[i].name.split('_')
			$(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}
	if (selected_batsmen.length === 5){
		BatsmenDivWidth = 100/selected_batsmen.length+"%"
		$(".BatsmenPreview").html("")
		for(var i=0; i<5; i++){
			var name_array = selected_batsmen[i].name.split('_')
			$(".BatsmenPreview").append("<div class=\"PlayerView\" style=\"width: " + BatsmenDivWidth + ";\"><center><img class=\"player_image\" src=\"/static/images/batsman.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}

	if (selected_allrounders.length == 1){
		var name_array = selected_allrounders[0].name.split('_')
		AllrounderDivWidth = 100/selected_allrounders.length+"%"
		$(".AllrounderPreview").html("<div class=\"PlayerView\" style=\"width: " + AllrounderDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/allrounder.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
	}
	else{
		$(".AllrounderPreview").html("")
		for(var i=0;i<2;i++){
			$(".AllrounderPreview").append("<div class=\"PlayerView\" style=\"width: 50%\"><center><img class=\"player_image\" src=\"/static/images/question.png\"></center><span class=\"PlayerNameView\">Allrounder</span></div>")
		}
	}
	if (selected_allrounders.length === 2){
		AllrounderDivWidth = 100/selected_allrounders.length+"%"
		$(".AllrounderPreview").html("")
		for(var i=0; i<2; i++){
			var name_array = selected_allrounders[i].name.split('_')
			$(".AllrounderPreview").append("<div class=\"PlayerView\" style=\"width: " + AllrounderDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/allrounder.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}
	if (selected_allrounders.length === 3){
		AllrounderDivWidth = 100/selected_allrounders.length+"%"
		$(".AllrounderPreview").html("")
		for(var i=0; i<3; i++){
			var name_array = selected_allrounders[i].name.split('_')
			$(".AllrounderPreview").append("<div class=\"PlayerView\" style=\"width: " + AllrounderDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/allrounder.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}

	if (selected_bowlers.length == 1){
		var name_array = selected_bowlers[0].name.split('_')
		BolwersDivWidth = 100/selected_bowlers.length+"%"
		$(".BowlerPreview").html("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
	}
	else{
		$(".BowlerPreview").html("")
		for(var i=0;i<4;i++){
			$(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: 25%\"><center><img class=\"player_image\" src=\"/static/images/question.png\"></center><span class=\"PlayerNameView\">Bowler</span></div>")
		}

	}
	if (selected_bowlers.length === 2){
		BolwersDivWidth = 100/selected_bowlers.length+"%"
		$(".BowlerPreview").html("")
		for(var i=0; i<2; i++){
			var name_array = selected_bowlers[i].name.split('_')
			$(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}
	if (selected_bowlers.length === 3){
		BolwersDivWidth = 100/selected_bowlers.length+"%"
		$(".BowlerPreview").html("")
		for(var i=0; i<3; i++){
			var name_array = selected_bowlers[i].name.split('_')
			$(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}
	if (selected_bowlers.length === 4){
		BolwersDivWidth = 100/selected_bowlers.length+"%"
		$(".BowlerPreview").html("")
		for(var i=0; i<4; i++){
			var name_array = selected_bowlers[i].name.split('_')
			$(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + "\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}
	if (selected_bowlers.length === 5){
		BolwersDivWidth = 100/selected_bowlers.length+"%"
		$(".BowlerPreview").html("")
		for(var i=0; i<5; i++){
			var name_array = selected_bowlers[i].name.split('_')
			$(".BowlerPreview").append("<div class=\"PlayerView\" style=\"width: " + BolwersDivWidth + ";\"><center><img class=\"player_image\" src=\"/static/images/bowlers.png\"></center><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></div>")
		}
	}
	if(selected_captain.length == 1){
		$('.CaptainVicePrivew').html("")
		var name_array = selected_captain[0].value.split('_')
		$('.CaptainVicePrivew').append("<div class=\"PlayerView\" style=\"width: 50%;\"><center><span class=\"PlayerNameView\">Captain</span><img class=\"player_image\" src=\"/static/images/2x.png\"><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></center></div>")
	}
	else if(selected_captain.length == 0){
		$('.CaptainVicePrivew').html("")
		$('.CaptainVicePrivew').append("<div class=\"PlayerView\" style=\"width: 50%;\"><center><span class=\"PlayerNameView\">Captain</span><img class=\"player_image\" src=\"/static/images/2x.png\"><span class=\"PlayerNameView\">Select</span></center></div>")
	}
	else{
		$('.CaptainVicePrivew').html("")
		$('.CaptainVicePrivew').append("<div class=\"CaptainClass\"><center>Something Went Wrong...</center></div>")
	}

	if(selected_vicecaptain.length == 1){
		var name_array = selected_vicecaptain[0].value.split('_')
		$('.CaptainVicePrivew').append("<div class=\"PlayerView\" style=\"width: 50%;\"><center><span class=\"PlayerNameView\">Vice Captain</span><img class=\"player_image\" src=\"/static/images/15x.png\"><span class=\"PlayerNameView\">" + name_array[0] + " " + name_array[1] + "</span></center></div>")
	}
	else if(selected_vicecaptain.length == 0){
		$('.CaptainVicePrivew').append("<div class=\"PlayerView\" style=\"width: 50%;\"><center><span class=\"PlayerNameView\">Vice Captain</span><img class=\"player_image\" src=\"/static/images/15x.png\"><span class=\"PlayerNameView\">Select</span></center></div>")
	}
	else{
		$('.CaptainVicePrivew').append("<div class=\"ViceClass\"><center>Something Went Wrong...</center></div>")
	}


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
	}, 0, function () {
		$(this).css({
			display: "inline-block",
			overflow: "",
			height: "",
			marginTop: ""
		});
	});

});

$(".captain_class").change(function() {
	var checked = $(this).is(':checked');
	var sibchecked = $(this).next().next().is(':checked');
	$(".captain_class").prop('checked',false);
	if(checked) {
		$(this).prop('checked',true);
		if(sibchecked){
			$(this).next().next().prop('checked',false);
		}
	}
});

$(".vice_class").change(function() {
	var checked = $(this).is(':checked');
	$(".vice_class").prop('checked',false);
	var sibchecked = $(this).prev().prev().is(':checked');
	if(checked) {
		$(this).prop('checked',true);
		if(sibchecked){
			$(this).prev().prev().prop('checked',false);
		}
	}
});

function openCity(evt, cityName) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
	document.getElementById(cityName).style.display = "block";
	evt.currentTarget.className += " active";
}

function openEvent(evt, BlockEvent) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("tabcontents");
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablinksMain");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}

	document.getElementById(BlockEvent).style.display = "block";
	evt.currentTarget.className += " active";
}

$(document).ready(function () {
	resetForms();
});

function resetForms() {
	// console.log("I have been Called.")
	for (i = 0; i < document.forms.length; i++) {
		document.forms[i].reset();
	}
}

ajaxComplete = false
console.log("first"+ajaxComplete)
$(document).ready(function () {
	var match_slug = $('#match_slug').attr('value')
	var team_no = $('#team').attr('value')
	var url_is = $('#get_team_info').attr('value')
	$.ajax({
		url: $('#get_team_info').attr('url-is'),
		type: "GET",
		data: {'team_no': team_no, match_slug: match_slug},
		dataType: 'json',
		success: function (data) {
			captain_id = data.team_captain.replace(/ /g,"_")+"_1"
			$('#'+captain_id).prop('checked', true)
			vice_id = data.team_vice.replace(/ /g,"_")+"_2"
			$('#'+vice_id).prop('checked', true)
			id = "id_"+data.keeper.replace(/ /g,"_");
			$("#"+id).prop("checked", true);
			$('.CreditPointsClass').html(100-data.total_credits_points+"/100")
			if(data.total_batsmen_in_team==3){
				id = "id_"+data.bat1.replace(/ /g,"_");
				$("#"+id).prop("checked", true);
				id1 = "id_"+data.bat2.replace(/ /g,"_");
				$("#"+id1).prop("checked", true);
				id2 = "id_"+data.bat3.replace(/ /g,"_");
				$("#"+id2).prop("checked", true);
			}

			if(data.total_batsmen_in_team==4){
				id = "id_"+data.bat1.replace(/ /g,"_");
				$("#"+id).prop("checked", true);
				id1 = "id_"+data.bat2.replace(/ /g,"_");
				$("#"+id1).prop("checked", true);
				id2 = "id_"+data.bat3.replace(/ /g,"_");
				$("#"+id2).prop("checked", true);
				id3 = "id_"+data.bat4.replace(/ /g,"_");
				$("#"+id3).prop("checked", true);
			}

			if(data.total_batsmen_in_team==5){
				id = "id_"+data.bat1.replace(/ /g,"_");
				$("#"+id).prop("checked", true);
				id1 = "id_"+data.bat2.replace(/ /g,"_");
				$("#"+id1).prop("checked", true);
				id2 = "id_"+data.bat3.replace(/ /g,"_");
				$("#"+id2).prop("checked", true);
				id3 = "id_"+data.bat4.replace(/ /g,"_");
				$("#"+id3).prop("checked", true);
				id4 = "id_"+data.bat5.replace(/ /g,"_");
				$("#"+id4).prop("checked", true);
			}

			if(data.total_allrounders_in_team==1){
				id = "id_"+data.allrounder1.replace(/ /g,"_");
				$("#"+id).prop("checked", true);
			}

			if(data.total_allrounders_in_team==2){
				id = "id_"+data.allrounder1.replace(/ /g,"_");
				$("#"+id).prop("checked", true);
				id1 = "id_"+data.allrounder2.replace(/ /g,"_");
				$("#"+id1).prop("checked", true);
			}

			if(data.total_allrounders_in_team==3){
				id = "id_"+data.allrounder1.replace(/ /g,"_");
				$("#"+id).prop("checked", true);
				id1 = "id_"+data.allrounder2.replace(/ /g,"_");
				$("#"+id1).prop("checked", true);
				id2 = "id_"+data.allrounder3.replace(/ /g,"_");
				$("#"+id2).prop("checked", true);
			}

			if(data.total_bowlers_in_team==3){
				id = "id_"+data.bowl1.replace(/ /g,"_");
				$("#"+id).prop("checked", true);
				id1 = "id_"+data.bowl2.replace(/ /g,"_");
				$("#"+id1).prop("checked", true);
				id2 = "id_"+data.bowl3.replace(/ /g,"_");
				$("#"+id2).prop("checked", true);
			}

			if(data.total_bowlers_in_team==4){
				id = "id_"+data.bowl1.replace(/ /g,"_");
				$("#"+id).prop("checked", true);
				id1 = "id_"+data.bowl2.replace(/ /g,"_");
				$("#"+id1).prop("checked", true);
				id2 = "id_"+data.bowl3.replace(/ /g,"_");
				$("#"+id2).prop("checked", true);
				id3 = "id_"+data.bowl4.replace(/ /g,"_");
				$("#"+id3).prop("checked", true);
			}

			if(data.total_bowlers_in_team==5){
				id = "id_"+data.bowl1.replace(/ /g,"_");
				$("#"+id).prop("checked", true);
				id1 = "id_"+data.bowl2.replace(/ /g,"_");
				$("#"+id1).prop("checked", true);
				id2 = "id_"+data.bowl3.replace(/ /g,"_");
				$("#"+id2).prop("checked", true);
				id3 = "id_"+data.bowl4.replace(/ /g,"_");
				$("#"+id3).prop("checked", true);
				id4 = "id_"+data.bowl5.replace(/ /g,"_");
				$("#"+id4).prop("checked", true);
			}
			KeeperFunction();
			BatsmanFunction();
			AllrounderFunction();
			BowlerFunction();
		}
	});
});
global_keeper_count = 0;
global_batsmen_count = 0;
global_bowler_count = 0;
global_allrounder_count = 0;
temp_global = 0

$('.keeper').on('click',KeeperFunction);
function KeeperFunction(){
	captain_id = $(this).attr("name")+"_1"
	vice_id = $(this).attr("name")+"_2"
	$("#"+captain_id).prop("checked", false)
	$("#"+vice_id).prop("checked", false)
	var keeper_inputs = $('.keeper:checkbox:checked');
	players_input = $('.CustomInput')
	global_keeper_count = keeper_inputs.length
	var players_count = 0;
	// for(var i = 0; i < keeper_inputs.length; i++){
	// 	if($(keeper_inputs[i]).is()){
// 	   	  	global_keeper_count = global_keeper_count+1;
// 	    }
	// }
	console.log(global_keeper_count)
	for(var i = 0; i < players_input.length; i++){
		if($(players_input[i]).is(':checked')){
			players_count = players_count+1;
		}
	}

	var points = CheckCredit()
	if (points>100){
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Opps! You don't have enough<strong> Points</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	if(global_keeper_count>1){
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select Only <strong>One Keeeper</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	if (players_count>11){
		$(this).prop( "checked", false );
		$('#max').css('display','block');
		$('#max').html("Please Select Only <strong>11 Players</strong>");
		$('#max').delay(3000).fadeOut(1000);
	}
	console.log("My Valie"+global_keeper_count)
};

$('.batsmen').on('click',BatsmanFunction);
function BatsmanFunction(){
	captain_id = $(this).attr("name")+"_1"
	vice_id = $(this).attr("name")+"_2"
	$("#"+captain_id).prop("checked", false)
	$("#"+vice_id).prop("checked", false)
	var batsmen_inputs = $('.batsmen:checkbox:checked');
	players_input = $('.CustomInput')
	global_batsmen_count = batsmen_inputs.length;
	var players_count = 0;
	for(var i = 0; i < players_input.length; i++){
		if($(players_input[i]).is(':checked')){
			players_count = players_count+1;
			console.log(players_count)
		}
	}

	var points = CheckCredit()
	if (points>100){
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Opps! You don't have enough<strong> Points</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	if(global_batsmen_count>5){
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select Only <strong>5 Batsmen</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	if (players_count>11){
		$(this).prop( "checked", false );
		$('#max').css('display','block');
		$('#max').html("Please Select Only <strong>11 Players</strong>");
		$('#max').delay(3000).fadeOut(1000);
	}
};

$('.allrounders').on('click',AllrounderFunction);
function AllrounderFunction(){
	captain_id = $(this).attr("name")+"_1"
	vice_id = $(this).attr("name")+"_2"
	$("#"+captain_id).prop("checked", false)
	$("#"+vice_id).prop("checked", false)
	var allrounder_inputs = $('.allrounders:checkbox:checked');
	players_input = $('.CustomInput')
	global_allrounder_count = allrounder_inputs.length
	var players_count = 0;
	for(var i = 0; i < players_input.length; i++){
		if($(players_input[i]).is(':checked')){
			players_count = players_count+1;
		}
	}

	var points = CheckCredit()
	if (points>100){
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Opps! You don't have enough<strong> Points</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	if(global_allrounder_count>3){
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select Only <strong>3 Allrounders</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	if (players_count>11){
		$(this).prop( "checked", false );
		$('#max').css('display','block');
		$('#max').html("Please Select Only <strong>11 Players</strong>");
		$('#max').delay(3000).fadeOut(1000);
	}
};

$('.bowlers').on('click', BowlerFunction);
function BowlerFunction(){
	captain_id = $(this).attr("name")+"_1"
	vice_id = $(this).attr("name")+"_2"
	$("#"+captain_id).prop("checked", false)
	$("#"+vice_id).prop("checked", false)
	var bowler_inputs = $('.bowlers:checkbox:checked');
	players_input = $('.CustomInput')
	global_bowler_count = bowler_inputs.length;
	var players_count = 0;
	for(var i = 0; i < players_input.length; i++){
		if($(players_input[i]).is(':checked')){
			players_count = players_count+1;
		}
	}

	var points = CheckCredit()
	if (points>100){
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Opps! You don't have enough<strong> Points</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	if(global_bowler_count>5){
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select Only <strong>5 Bowlers</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	if (players_count>11){
		$(this).prop( "checked", false );
		$('#max').css('display','block');
		$('#max').html("Please Select Only <strong>11 Players</strong>");
		$('#max').delay(3000).fadeOut(1000);
	}
};


console.log("Ji"+global_keeper_count)
$('.btn-sm').click(function(event){
	players_input = $('.CustomInput');
	var players_count = 0;
	for(var i = 0; i < players_input.length; i++){
		if($(players_input[i]).is(':checked')){
			players_count = players_count+1;
			console.log("Something")
		}
	}
	if(players_count<11){
		event.preventDefault();
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select At Least <strong>11 Players</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}
	else if(global_keeper_count<1){
		event.preventDefault();
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select At Least <strong>1 Keeeper</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}
	else if(global_batsmen_count<3){
		event.preventDefault();
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select At Least <strong>3 Batsmen</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}
	else if(global_allrounder_count<1){
		event.preventDefault();
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select At Least <strong>1 Allrounder</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}
	else if(global_bowler_count<3){
		event.preventDefault();
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select At Least <strong>3 Bowlers</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}
	else if(!$('.captain_class').is(':checked')){
		event.preventDefault();
		if(!$('.vice_class').is(':checked')){
			$(this).prop( "checked", false );
			$('#sub_max').css('display','block');
			$('#sub_max').html("Please Select Your <strong>Captain and Vice Captain</strong>");
			$('#sub_max').delay(3000).fadeOut(1000);
		}
		else{
			$(this).prop( "checked", false );
			$('#sub_max').css('display','block');
			$('#sub_max').html("Please Select Your <strong>Captain</strong>");
			$('#sub_max').delay(3000).fadeOut(1000);
		}
	}
	else if(!$('.captain_class').is(':checked')){
		event.preventDefault();
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select Your <strong>Captain</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	else if(!$('.vice_class').is(':checked')){
		event.preventDefault();
		$(this).prop( "checked", false );
		$('#sub_max').css('display','block');
		$('#sub_max').html("Please Select Your <strong>Vice Captain</strong>");
		$('#sub_max').delay(3000).fadeOut(1000);
	}

	console.log("Global Keeeper Count : "+global_keeper_count)
	console.log("Global Batsmen Count : "+global_batsmen_count)
})

$('.CustomInput').click(function(){
	credits = 0
	selected_players = $('.CustomInput:checkbox:checked')
	for(var i=0;i<selected_players.length;i++){
		player = $('#'+selected_players[i].id)
		credits = credits + +player.next('label').find('.PlayerCredits').html()
		player_team = player.next('label').find('.PlayerTeam').html()
		console.log("Name : " + selected_players[i].id + " Points : " + credits)
	}
	$('#total_credits_points').val(credits)
	$('.CreditPointsClass').html(100-credits + "/100")
	$('.TotalPlayersClass').html(selected_players.length + "/11")
	//console.log("IND : "+ ind + " WI : " + wi + " Total Credits : "+credits)
});

function CheckCredit(){
	credits = 0
	selected_players = $('.CustomInput:checkbox:checked')
	for(var i=0;i<selected_players.length;i++){
		player = $('#'+selected_players[i].id)
		credits = credits + +player.next('label').find('.PlayerCredits').html()
		player_team = player.next('label').find('.PlayerTeam').html()
	}
	$('#total_credits_points').val(credits)
	$('.CreditPointsClass').html(100-credits + "/100")
	$('.TotalPlayersClass').html(selected_players.length + "/11")
	return credits
}
