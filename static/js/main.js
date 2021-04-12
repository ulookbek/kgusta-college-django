$(document).ready(function () {
  $("a.page-scroll").on("click", function (e) {
    var anchor = $(this);
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: $(anchor.attr("href")).offset().top - 50,
        },
        1500
      );
    e.preventDefault();
  });

  $(".bxslider").bxSlider();

  $(".menu-trigger").click(function () {
    $("#menu").fadeToggle(300);
    $(this).toggleClass("active");
  });

  $(".info-request, .get-contact").fancybox();

  $("select").crfs();

  $(".table td").mouseenter(function () {
    $(this).find(".holder").stop(true, true).fadeIn(600);
    $(this).find(">div").addClass("hover");
    return false;
  });
  $(".table td").mouseleave(function () {
    $(this).find(".holder").stop(true, true).fadeOut(400);
    $(this).find(">div").removeClass("hover");
    return false;
  });
  $(".table td .holder").click(function () {
    $(this).stop(true, true).fadeOut(400);
    $(this).parent().parent().removeClass("hover");
    return false;
  });

  var isBrowserOs = {
    Windows: function () {
      return navigator.userAgent.match(/Win/i);
    },
    MacOS: function () {
      return navigator.userAgent.match(/Mac/i);
    },
    UNIX: function () {
      return navigator.userAgent.match(/X11/i);
    },
    Linux: function () {
      return navigator.userAgent.match(/Linux/i);
    },
    iOs: function () {
      return navigator.userAgent.match(/(iPad|iPhone|iPod)/i);
    },
    Android: function () {
      return navigator.userAgent.match(/android/i);
    },
    BlackBerry: function () {
      return navigator.userAgent.match(/BlackBerry/i);
    },
    Chrome: function () {
      return window.chrome;
    },
    Firefox: function () {
      return navigator.userAgent.match(/Firefox/i);
    },
    IE: function () {
      return navigator.userAgent.match(/MSIE/i);
    },
    Opera: function () {
      return !!window.opera || navigator.userAgent.indexOf(" OPR/") >= 0;
    },
    SeaMonkey: function () {
      return navigator.userAgent.match(/SeaMonkey/i);
    },
    Camino: function () {
      return navigator.userAgent.match(/Camino/i);
    },
    Safari: function () {
      return (
        Object.prototype.toString
          .call(window.HTMLElement)
          .indexOf("Constructor") > 0
      );
    },
  };

  var html_class = "";
  //OS
  if (isBrowserOs.Windows()) html_class = "win";
  if (isBrowserOs.UNIX()) html_class = "unix";
  if (isBrowserOs.MacOS()) html_class = "mac";
  if (isBrowserOs.Linux()) html_class = "linux";
  if (isBrowserOs.iOs()) html_class = "ios mac";
  if (isBrowserOs.Android()) html_class = "android";
  if (isBrowserOs.BlackBerry()) html_class = "blackberry";

  //Browser
  if (isBrowserOs.Chrome()) html_class = html_class + " chrome";
  if (isBrowserOs.Firefox()) html_class = html_class + " firefox";
  if (isBrowserOs.IE()) html_class = html_class + " ie";
  if (isBrowserOs.Opera()) html_class = html_class + " opera";
  if (isBrowserOs.SeaMonkey()) html_class = html_class + " seamonkey";
  if (isBrowserOs.Camino()) html_class = html_class + " camino";
  if (isBrowserOs.Safari()) html_class = html_class + " safari";

  $("html").addClass(html_class);
});

const teacher_description = $(".teacher_description");

function kitcut(text, limit) {
  text = text.trim();
  if (text.length <= limit) return text;
  text = text.slice(0, limit);
  return text.trim() + "....";
}

document.addEventListener("DOMContentLoaded", function (event) {
  for (let i = 0; i < teacher_description.length; i++) {
    if (teacher_description[i].innerHTML.length > 100) {
      teacher_description[i].innerHTML = kitcut(
        teacher_description[i].innerHTML,
        50
      );
    }
  }

  $("#myCarousel .carousel-item img").on("click", function (e) {
    var src = $(e.target).attr("data-remote");
    if (src) $(this).ekkoLightbox();
  });

  // let aboutus = document.getElementById('aboutus')
  // let aboutusmenu = document.getElementById('aboutusmenu')
  // let aboutcollege = document.getElementById('aboutcollege')
  // let aboutcollegeMenu = document.getElementById('aboutcollegeMenu')
  // aboutus.addEventListener('mouseenter', () => {
  //     aboutusmenu.style.display = 'flex'
  // })
  // aboutus.addEventListener('mouseleave', () => {
  //     aboutusmenu.style.display = 'none'
  // })
  // aboutcollege.addEventListener('mouseenter', () => {
  //     aboutcollegeMenu.style.display = 'flex'
  // })
  // aboutcollege.addEventListener('mouseleave', () => {
  //     aboutcollegeMenu.style.display = 'none'
  // })
});

try {
  $("#myCarousel").carousel({
    interval: false,
  });
  $("#carousel-thumbs").carousel({
    interval: false,
  });
} catch (e) {
  console.log(e);
}

// handles the carousel thumbnails
// https://stackoverflow.com/questions/25752187/bootstrap-carousel-with-thumbnails-multiple-carousel
$("[id^=carousel-selector-]").click(function () {
  var id_selector = $(this).attr("id");
  var id = parseInt(id_selector.substr(id_selector.lastIndexOf("-") + 1));
  $("#myCarousel").carousel(id);
});
// Only display 3 items in nav on mobile.
if ($(window).width() < 575) {
  $("#carousel-thumbs .row div:nth-child(4)").each(function () {
    var rowBoundary = $(this);
    $('<div class="row mx-0">')
      .insertAfter(rowBoundary.parent())
      .append(rowBoundary.nextAll().addBack());
  });
  $("#carousel-thumbs .carousel-item .row:nth-child(even)").each(function () {
    var boundary = $(this);
    $('<div class="carousel-item">')
      .insertAfter(boundary.parent())
      .append(boundary.nextAll().addBack());
  });
}
// Hide slide arrows if too few items.
if ($("#carousel-thumbs .carousel-item").length < 2) {
  $("#carousel-thumbs [class^=carousel-control-]").remove();
  $(".machine-carousel-container #carousel-thumbs").css("padding", "0 5px");
}
// when the carousel slides, auto update
$("#myCarousel").on("slide.bs.carousel", function (e) {
  var id = parseInt($(e.relatedTarget).attr("data-slide-number"));
  $("[id^=carousel-selector-]").removeClass("selected");
  $("[id=carousel-selector-" + id + "]").addClass("selected");
});
// when user swipes, go next or previous
try {
  $("#myCarousel").swipe({
    fallbackToMouseEvents: true,
    swipeLeft: function (e) {
      $("#myCarousel").carousel("next");
    },
    swipeRight: function (e) {
      $("#myCarousel").carousel("prev");
    },
    allowPageScroll: "vertical",
    preventDefaultEvents: false,
    threshold: 75,
  });
} catch (e) {
  console.log(e);
}
/*
$(document).on('click', '[data-toggle="lightbox"]', function(event) {
  event.preventDefault();
  $(this).ekkoLightbox();
});
*/
