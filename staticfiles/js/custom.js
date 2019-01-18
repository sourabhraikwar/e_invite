// $('.invi_card').animateCss('bounce');
$(document).ready(()=>{
  $('.text_2').addClass('animated slideInLeft ');
  $('.text_1').addClass('animated slideInRight');
})


var test = $("#html").get(0);
var img = new Array();
for (var i = 0; i < 5; i++) {
  html2canvas(test).then(canvas => {
    return data = canvas.toDataURL()
  }).then((data, i)=>{
    data_loop(data, i);
  })
}

function data_loop(data, i){
  img[i] = data;
  // console.log(img)
}


