window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;

const recognition = new SpeechRecognition();
const icon = document.querySelector('i.fa.fa-microphone');

icon.addEventListener('click', () => {
  // sound.play();
  dictate();
});
// const dictate = () => {
//   recognition.start();
// }

var inputtxt = "";
const dictate = () => {
  recognition.start();
  recognition.onresult = (event) => {
    const speechToText = event.results[0][0].transcript;
    inputtxt = speechToText;
    console.log(speechToText);
    insertVoiceMessage();
  }
}


var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

var sentence = 'hi, please enter a description and wait for the image.';

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

function insertVoiceMessage() {
  // msg = $('.message-input').val();
  msg = inputtxt;
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

function insertMessage() {
  msg = $('.message-input').val();
  // msg = inputtxt;
  sentence = msg;
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
  setTimeout(function() {
    fakeMessageTxt();
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

function fakeMessage() {
  // if ($('.message-input').val() != '') {
  //   return false;
  // }
  $('<div class="message loading new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure><span></span></div>').appendTo($('.mCSB_container'));
  updateScrollbar();
  $.ajax({
                type: "POST",
                url: "/postmethod",
                contentType: "application/json",
                data: JSON.stringify({location: sentence}),
                dataType: "json",
                success: function(response) {
                      sentence = response['location'];
                },
                error: function(err) {
                    console.log(err);
                }
            });
  
  setTimeout(function() {
    $('.message.loading.new').remove();
      // $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure>' + sentence + '</div>').appendTo($('.mCSB_container')).addClass('new');    
      $('<div class="message new">' + sentence + '</div>').appendTo($('.mCSB_container')).addClass('new');    
    setDate();
    updateScrollbar();
    i++;
  }, 1000 + (Math.random() * 20) * 100);

}

counter = 1;

function fakeMessageTxt() {
  if ($('.message-input').val() != '') {
    return false;
  }
  $('<div class="message loading new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure><span></span></div>').appendTo($('.mCSB_container'));
  updateScrollbar();
  $.ajax({
                type: "POST",
                url: "/postmethod",
                contentType: "application/json",
                data: JSON.stringify({location: sentence}),
                dataType: "json",
                success: function(response) {
                      sentence = response['location'];
                      console.log(sentence);

                },
                error: function(err) {
                    console.log(err);
                }
            });
  
  
  setTimeout(function() {
    $('.message.loading.new').remove();

    console.log(counter) ;
    
    $('<div class="message new"><img src="/static/images/' + counter + '.png" width="200px" height="200px"></div>').appendTo($('.mCSB_container')).addClass('new');    

    counter++ ;

    setDate();
    updateScrollbar();
    i++;
  }, 10000 + (Math.random() * 20) * 100);

}