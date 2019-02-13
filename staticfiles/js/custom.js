// datatable js start here

$('.myTable').dataTable( {
  "columns": [
    null,
    null,
    null,
    null,
    {
      "data": "office", // can be null or undefined
      "defaultContent": ""
    }
  ]
} );

$('.email-table').dataTable( {
  "columns": [
    null,
    null,
    {
      "data": "office", // can be null or undefined
      "defaultContent": ""
    }
  ]
} );

// datatable js end here

$(document).ready(function(){
  $("#cards").click(function(){
    $("#cards_list").slideToggle();
  });
});

// const audio = new Audio();

//     .then(stream => {
//     const mediaRecorder = new MediaRecorder(stream);
//     mediaRecorder.start();
// });