$(function () {
    "use strict";

    $(".popup #myIMG").click(function () {
        var $src = $(this).attr("src");
        $(".show").fadeIn();
        $(".img-show img").attr("src", $src);
    });

    $("#mySPAN, .overlay").click(function () {
        $(".show").fadeOut();
    });

});
