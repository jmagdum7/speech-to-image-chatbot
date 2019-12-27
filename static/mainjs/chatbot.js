
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
    var fake = fakeMessage();
  }, 1000 + (Math.random() * 20) * 100);
}

$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    var ins = insertMessage();
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
  link=0;
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
                    if (response['link']!=0 || response['length']>=3) {
                      link = response['link'];
                      length = response['length'];
                      sentence = response['location'];
                      title = response['title'];
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
    $('.message.loading.new').remove();
    if(length > 1)
    {
      sentence = sentence.toString().split(",");
      title = title.toString().split(",");
      for(i=0;i<title.length;i++)
      {
        temp = title[i].toString().split("|");
        title[i] = temp[0];
      }
      console.log(sentence.length);
      ind = 0;
      var string = "";

      for (i=0; i<sentence.length-1; i++)
      {
        // $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure>' + '<button type="button" class="btn btn-danger">' + sentence[i] + '</button>' + '</div>').appendTo($('.mCSB_container')).addClass('new');    
        string = string +'<div class="card"><div class="card__bg"></div><div class="card__overlay cover"></div><div class="card__info"><div class="card__title">'+title[i]+'</div><a href="'+sentence[i]+'"><button class="card__cta">'+'View Link'+'<span class="icon">&rarr;</span></button></a></div></div>';
        // '<a href="'+sentence[i]+'"><button type="button" class="btn btn-success" >' + sentence[i] + '</button/></a>';
        // string = string + "<a href='/singlecourse/c01'><img src='/static/images/c"+(i+1)+".png' width=100 height=100 style='padding:5px;'></a>";
        //'<img src="{{url_for("static", filename= "images/c" + (i+1) + ".png" width="100" height="100">';
       //{{url_for('static',filename = 'images/icons/iconsmall.jpg')}}
        ind = ind + 1;
      }
      // $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif"/></figure>'+'<div class="main-carousel">'+ string +'</div>'+'</div>').appendTo($('.mCSB_container')).addClass('new');    
      // $('.scrolling-wrapper').remove();
      $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif"/></figure><div id="info"></div>'
      +'<div class="scrolling-wrapper" id="scrolling-wrapper" onmouseenter="pauseDiv()" onmouseleave="resumeDiv()">'+ string +'</div>'+'<img src="data:image/jpeg;base64,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" onload="scrollDiv_init()" width="0" height="0"></div>').appendTo($('.mCSB_container'));


      length = 0;
    }
    else{
      // if (link==1)
      // {
      //  sentence = sentence.toString().split(",");
      //  $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure>' + ' <div class="carousel" data-flickity="{ "groupCells": 1, "autoPlay":true, "wrapAround":true }"><div class="carousel-cell">hey</div></div> ' + '</div>').appendTo($('.mCSB_container')).addClass('new'); 
      //  // '<a href="'+sentence[0]+'"><button type="button" class="btn btn-success" >' + sentence[0] + '</button/></a>'
      //  link=0;
      // }
      // else
      // {
      //   $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure>' + sentence + '</div>').appendTo($('.mCSB_container')).addClass('new');
      // }
      $('<div class="message new"><figure class="avatar"><img src="http://algom.x10host.com/chat/img/icon-oracle.gif" /></figure>' + sentence + '</div>').appendTo($('.mCSB_container')).addClass('new');    
    }
    setDate();
    updateScrollbar();
    i++;
  }, 1000 + (Math.random() * 20) * 100);

}






                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  


