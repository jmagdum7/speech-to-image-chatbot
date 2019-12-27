
var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

var sentence = 'hi';

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    fakeMessage();
  }, 100);
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}

function insertMessage() {
  msg = $('.message-input').val();
  sentence = msg;
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
  setTimeout(function() {
    fakeMessage();
  }, 1000 + (Math.random() * 20) * 100);
}

$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})

// var Fake = [
//   'Hi AlgoOracle at your service ',
//   'please enter the stock you\'d like to predict<input type="text" class="form-control oracle-search" name="query"  placeholder="Start typing something to search..."> ',
//   'Please Enter Your Target Price',
//   'good.....What is your comfortable level for investment loss (in %) <input type="range" value="50" min="0" max="100" step="10" />',
//   'we are Predicting... <div class="loading-img"><img src="http://algom.x10host.com/chat/img/chat.gif"  alt=""/></div>',
//   'great.. do you want to predict another? <button class="buttonx sound-on-click">Yes</button> <button class="buttony sound-on-click">No</button> ',
//   'Bye',
//   ':)'
// ]

function fakeMessage() {
  if ($('.message-input').val() != '') {
    return false;
  }
  $('<div class="message loading new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure><span></span></div>').appendTo($('.mCSB_container'));
  updateScrollbar();
  dictn = {'a': sentence}
  length = 0;
//   var cars = [
// 	{ "make":"Porsche", "model":"911S" },
// 	{ "make":"Mercedes-Benz", "model":"220SE" },
// 	{ "make":"Jaguar","model": "Mark VII" }
// ];
  $.ajax({
                type: "POST",
                url: "/postmethod",
                contentType: "application/json",
                data: JSON.stringify({location: sentence}),
                dataType: "json",
                success: function(response) {
                    if (response['length'] >= 3) {
                      length = response['length'];
                      sentence = response['location'];
                    }
                    else{
                      sentence = response['location'];
                    }
                },
                error: function(err) {
                    console.log(err);
                }
            });
  setTimeout(function() {
    $('.message.loading').remove();
    if(length > 0){
      sentence = sentence.toString().split(",");
      console.log(sentence.length);
      ind = 0;
      var string = "";
      for (i=0; i<sentence.length; i++){
        // $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure>' + '<button type="button" class="btn btn-danger">' + sentence[i] + '</button>' + '</div>').appendTo($('.mCSB_container')).addClass('new');    
        string = string + '<button type="button" class="btn btn-danger">' + sentence[i] + '</button>';
        ind = ind + 1;
      }
      $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure>' + string + '</div>').appendTo($('.mCSB_container')).addClass('new');    
      length = 0;
    }
    else{
      $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure>' + sentence + '</div>').appendTo($('.mCSB_container')).addClass('new');    
    }
    setDate();
    updateScrollbar();
    i++;
  }, 1000 + (Math.random() * 20) * 100);

}






                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  


