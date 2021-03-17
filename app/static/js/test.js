/*
var picLink = '../static/pictures/livevideo/live_video_pic.jpg';
var time = 1500;

function wait(ms){
   var start = new Date().getTime();
   console.log(start);
   var end = start;
   while(end < start + ms) {
     end = new Date().getTime();
  }
}

function myFunc(){

    document.test.src = picLink;

    //setTimeout(console.log('Bajs'), 2000);

    //setTimeout('myFunc()', time);
}

console.log('Testning');

for (let i = 0; i < 5; i++){
    //console.log('Utskrift...');
    console.log(i);
    //setTimeout('myFunc()', 1000);
    myFunc();
    wait(1000);

}
console.log()
console.log('Slut!')
//setTimeout(myFunc(), 2000);
*/

var picLink = '../static/pictures/livevideo/live_video_pic.jpg';
var time = 1500; // 1.5 sekunder?
var bildElement = document.getElementById('test');
// <img src="" id="bildId">

setTimeout(function(){ 	bildElement.src = 'test'; } , time);