var autocollapse = function (menubar) {
    var logo_block = menubar.find(".navbar-header")
    var right_block = menubar.find(".navbar-right")
    var menu = menubar.find("#main-menu");
    var menu_items = menu.find(" > li:not(#more)");
    var more = menu.find(" > li#more");
    var available_space = menubar.width() - logo_block.width() - right_block.width() - more.width();
    
    // if (menu.width() > available_space){
        // menu.find(" > li:last-child")
        var cnt = 0;
        menu_items.each(function(){
            // if ($(this).hasClass("hidden"))
            $(this).removeClass("hidden");
            cnt += $(this).width();
            if (cnt > available_space) {
                // $(this).addClass("hidden");
                // console.log(menu_items.index(this))
                menu_items.slice( menu_items.index(this) )
                    .each(function(){$(this).addClass("hidden")});
                return false; //exiting loop
            }
            // console.log($(this).width());
        });
        console.log(menu_items.length, menubar.width(), available_space, menu.width());
    // }
    // menu_items.each
//     var nav = $(menu);
//     var navHeight = nav.innerHeight();
//     if (navHeight >= maxHeight) {
//         $(menu + ' .dropdown').removeClass('d-none');
//         while (navHeight > maxHeight) {
//             var children = nav.children(menu + ' li:not(:last-child)');
//             var count = children.length;
//             $(children[count - 1]).prependTo(menu + ' .dropdown-menu');
//             navHeight = nav.innerHeight();
//         }
//     }
//     else {
//         var collapsed = $(menu + ' .dropdown-menu').children(menu + ' li');
      
//         if (collapsed.length===0) {
//           $(menu + ' .dropdown').addClass('d-none');
//         }
      
//         while (navHeight < maxHeight && (nav.children(menu + ' li').length > 0) && collapsed.length > 0) {
//             collapsed = $(menu + ' .dropdown-menu').children('li');
//             $(collapsed[0]).insertBefore(nav.children(menu + ' li:last-child'));
//             navHeight = nav.innerHeight();
//         }

//         if (navHeight > maxHeight) { 
//             autocollapse(menu,maxHeight);
//         }
//     }
};


$(document).ready(function () {

    // when the page laods
    autocollapse( $('.navbar-main .container')); 

    
    // when the window is resized
    $(window).on('resize', function () {
        // autocollapse('#main-menu',50); 
        autocollapse( $('.navbar-main .container')); 
    });

});