// datatable js start here

$(document).ready(function(){
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

  $("#cards").click(function(){
    $("#cards_list").slideToggle();
  });
});

$(document).ready(function(){
  $('.card_slider').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
  });
});

