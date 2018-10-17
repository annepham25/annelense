$('#toggle').click(function() {
   $(this).toggleClass('active');
   $('#overlay').toggleClass('open');
  });

  $('.hover').mouseover(function() {
  $('.text').css("visibility","visible");
});

$('.hover').mouseout(function() {
  $('.text').css("visibility","hidden");
});
