// $('.invi_card').animateCss('bounce');
$(document).ready(()=>{
  $('.text_2').addClass('animated slideInLeft ');
  $('.text_1').addClass('animated slideInRight');
})


var test = $("#html").get(0);
var img = new Array();
html2canvas(test).then(canvas => {
  return data = canvas.toDataURL()
}).then(data=>{
  data_loop(data);
})

function data_loop(data){
  img[] = data;
  console.log(img)
}

