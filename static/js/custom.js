// $('.invi_card').animateCss('bounce');
$(document).ready(()=>{
  $('.text_2').addClass('animated slideInLeft ');
  $('.text_1').addClass('animated slideInRight');
})


$(document).ready(function(){

    
var element = $("#html-content-holder"); // global variable
var getCanvas; // global variable
 
    $(window).on('load',setInterval(function () {
         html2canvas(element, {
         onrendered: function (canvas) {
                getCanvas = canvas;
                var imgageData = getCanvas.toDataURL("image/png");
                // Now browser starts downloading it instead of just showing it
                var newData += imgageData.replace(/^data:image\/png/, "data:application/octet-stream");
             }
         });
    },3000);
    $("#btn-Convert-Html2Image").on('click',(newData)=>{

        $("#btn-Convert-Html2Image").attr("download", "your_pic_name.png").attr("href", newData);
    })
});

    var i = 1;                   

    function myLoop () {          
       setTimeout(function () {   
          alert('hello');         
          i++;                
          if (i < 10) {          
             myLoop();         
          }                  
       }, 3000)
    }