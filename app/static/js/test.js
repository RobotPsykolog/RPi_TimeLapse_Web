
/*  JS program to do a poor mans livevideo.
    Got help from my meetup group to fix this! Thanks! */

var picLink = 'static/pictures/livevideo/live_video_pic.jpg';
var tid = 100;
var bildElement = document.getElementById('test');
var counter = 0;
setInterval(function(){ counter++;	bildElement.src = picLink + '?' + counter; } , tid);