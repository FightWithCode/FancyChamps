$(document).ready(function(){
    $('div.dropdown').each(function() {
      var $dropdown = $(this);

      $("a.dropdown-link", $dropdown).click(function(e) {
        e.preventDefault();
        $div = $("div.dropdown-container", $dropdown);
        $div.toggle();
        $("div.dropdown-container").not($div).hide();
        return false;
      });
  });
  $('html').click(function(){
    $("div.dropdown-container").hide();
  });
});

function openEvent(evt, BlockEvent) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("tabcontent");
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

$(window).on('load', function(){
    $(".GrandClass > div:gt(0)").hide();
    $(".HeadClass > div:gt(0)").hide();
    $(".4On1Class > div:gt(0)").hide();
    //$('.GrandClass > .LeagueArea').not('#FirstLeagueArea').hide();
})

$(".GrandClass > button").click(function(){
    $(this).siblings("div:gt(0)").slideToggle();
    $(this).text($(this).text() == "Show More Grand Leagues!" ? "Show Less" : "Show More Grand Leagues!");
});

$(".HeadClass > button").click(function(){
    $(this).siblings("div:gt(0)").slideToggle();
    $(this).text($(this).text() == "Show More Leagues!" ? "Show Less" : "Show More Leagues!");
});

$(".4On1Class > button").click(function(){
    $(this).siblings("div:gt(0)").slideToggle();
    $(this).text($(this).text() == "Show More Leagues!" ? "Show Less" : "Show More Leagues!");
});



