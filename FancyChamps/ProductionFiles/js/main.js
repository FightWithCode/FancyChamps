// AOS.init({
//   duration: 1200,
// })


$(function() {
  AOS.init();
});

$(window).on('load', function() {
  AOS.refresh();
});

$(function(){
  $('[time-counter]').each(function(i) {
    var temp = i+1
    $(this).attr('id', 'TimeCounter'+temp)
    total_tick = $(this).attr('time-counter')
    var now = Math.floor(new Date().getTime()/1000)
    var time_tick = total_tick - now;
    timer(time_tick, temp, $(this).attr('id'))
  });
});

var timerData = [];

function secondPassed(row, id) {
    var seconds = timerData[row].remaining;
    var minutes = Math.floor((seconds / 60) % 60);
    var hours = Math.floor(seconds / (60 * 60));
    var remainingSeconds = seconds % 60;
    if (remainingSeconds < 10) {
        remainingSeconds = "0" + remainingSeconds;
    }
    $('#'+id).html(hours + "H " + minutes + "M " + remainingSeconds + "S");
    if (seconds <= 0) {
        clearInterval(timerData[row].timerId);
        $('#'+id).html("Time-Over");
        console.log($('#'+id).next().next().attr('href', "#"))

    } else {
        seconds--;
    }
    timerData[row].remaining = seconds;
}

function timer(sec, row, id) {
    timerData[row] = {
        remaining: sec,
        timerId: setInterval(function () {
            secondPassed(row, id);
        }, 1000)
    };
}


$(document).ready(function(){
  // Add smooth scrolling to all links
  $(".innerA").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 600, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});
//here was event function









// var deadlineOne = new Date("September 12, 2018 19:00:00").getTime();
// var x = setInterval(function() {
// var now = new Date().getTime();
// var t = deadlineOne - now;
// var days = Math.floor(t / (1000 * 60 * 60 * 24));
// var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
// var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
// var seconds = Math.floor((t % (1000 * 60)) / 1000);
// document.getElementById("timerOne").innerHTML = days + ":"
// + hours + ":" + minutes + ":" + seconds + "s";
//     if (t < 0) {
//         clearInterval(x);
//         document.getElementById("timerOne").innerHTML = "EXPIRED";
//     }
// }, 1000);

// var deadlineTwo = new Date(" 19, 2018 15:00:00").getTime();
// var x = setInterval(function() {
// var now = new Date().getTime();
// var t = deadlineTwo - now;
// var days = Math.floor(t / (1000 * 60 * 60 * 24));
// var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
// var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
// var seconds = Math.floor((t % (1000 * 60)) / 1000);
// document.getElementById("timerTwo").innerHTML = days + ":"
// + hours + ":" + minutes + ":" + seconds + "s";
//     if (t < 0) {
//         clearInterval(x);
//         document.getElementById("timerTwo").innerHTML = "EXPIRED";
//     }
// }, 1000);

// var deadlineThree = new Date("July 20, 2018 15:00:00").getTime();
// var x = setInterval(function() {
// var now = new Date().getTime();
// var t = deadlineThree - now;
// var days = Math.floor(t / (1000 * 60 * 60 * 24));
// var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
// var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
// var seconds = Math.floor((t % (1000 * 60)) / 1000);
// document.getElementById("timerThree").innerHTML = days + ":"
// + hours + ":" + minutes + ":" + seconds + "s";
//     if (t < 0) {
//         clearInterval(x);
//         document.getElementById("timerThree").innerHTML = "EXPIRED";
//     }
// }, 1000);
// var deadlineFour = new Date("July 21, 2018 15:00:00").getTime();
// var x = setInterval(function() {
// var now = new Date().getTime();
// var t = deadlineFour - now;
// var days = Math.floor(t / (1000 * 60 * 60 * 24));
// var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
// var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
// var seconds = Math.floor((t % (1000 * 60)) / 1000);
// document.getElementById("timerFour").innerHTML = days + ":"
// + hours + ":" + minutes + ":" + seconds + "s";
//     if (t < 0) {
//         clearInterval(x);
//         document.getElementById("timerFour").innerHTML = "EXPIRED";
//     }
// }, 1000);

// var deadlineFive = new Date("July 22, 2018 15:00:00").getTime();
// var x = setInterval(function() {
// var now = new Date().getTime();
// var t = deadlineThree - now;
// var days = Math.floor(t / (1000 * 60 * 60 * 24));
// var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
// var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
// var seconds = Math.floor((t % (1000 * 60)) / 1000);
// document.getElementById("timerFive").innerHTML = days + ":"
// + hours + ":" + minutes + ":" + seconds + "s";
//     if (t < 0) {
//         clearInterval(x);
//         document.getElementById("timerFive").innerHTML = "EXPIRED";
//     }
// }, 1000);

// var deadlineFive = new Date("July 23, 2018 15:00:00").getTime();
// var x = setInterval(function() {
// var now = new Date().getTime();
// var t = deadlineThree - now;
// var days = Math.floor(t / (1000 * 60 * 60 * 24));
// var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
// var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
// var seconds = Math.floor((t % (1000 * 60)) / 1000);
// document.getElementById("timerSix").innerHTML = days + ":"
// + hours + ":" + minutes + ":" + seconds + "s";
//     if (t < 0) {
//         clearInterval(x);
//         document.getElementById("timerSix").innerHTML = "EXPIRED";
//     }
// }, 1000);

// var deadlineFive = new Date("July 23, 2018 15:00:00").getTime();
// var x = setInterval(function() {
// var now = new Date().getTime();
// var t = deadlineThree - now;
// var days = Math.floor(t / (1000 * 60 * 60 * 24));
// var hours = Math.floor((t%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
// var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
// var seconds = Math.floor((t % (1000 * 60)) / 1000);
// document.getElementById("timerSix").innerHTML = days + ":"
// + hours + ":" + minutes + ":" + seconds + "s";
//     if (t < 0) {
//         clearInterval(x);
//         document.getElementById("timerSix").innerHTML = "EXPIRED";
//     }
// }, 1000);











// <div class="col-sm-4 row wrapFeaturesLeft conatiner">
//   <div class="col-sm-12 featureSpecs">
//     <i class="fa fa-certificate fa-3x" aria-hidden="true"></i>
//     <h3>Signup Bonus<h3>
//   </div>
//   <div class="col-sm-12 featureSpecs">
//     <i class="fa fa-certificate fa-3x" aria-hidden="true"></i>
//     <h3>Variety of Leages<h3>
//   </div>
//   <div class="col-sm-12 featureSpecs">
//     <i class="fa fa-certificate fa-3x" aria-hidden="true"></i>
//     <h3>Win Real Cash Prizes<h3>
//   </div>
// </div>
// <div class="col-sm-4 container4">
//   <img src="{% static "images/testlogo.png" %}" alt="Sorry! LOGO Not Found" class="logo featuresLogo">
// </div>
// <div class="col-sm-4 wrapFeaturesRight">
//   <div class="col-sm-12 featureSpecs">
//     <i class="fa fa-certificate fa-3x" aria-hidden="true"></i>
//     <h3>24x7 Support<h3>
//   </div>
//   <div class="col-sm-12 featureSpecs">
//     <i class="fa fa-certificate fa-3x" aria-hidden="true"></i>
//     <h3>High Rewards<h3>
//   </div>
//   <div class="col-sm-12 featureSpecs">
//     <i class="fa fa-certificate fa-3x" aria-hidden="true"></i>
//     <h3>No Need of PAN Card Details<h3>
//   </div>
// </div>
//   Counter Script
