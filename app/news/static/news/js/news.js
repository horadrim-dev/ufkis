(function($) {

    var original_onPageLoad = $.fn.onPageLoad;
    $.fn.onPageLoad = function () {
        original_onPageLoad();

        function setCookie(cName, cValue, expDays, path="/") {
            let date = new Date();
            date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
            const expires = "expires=" + date.toUTCString();
            document.cookie = cName + "=" + cValue + "; " + expires + "; path=" + path;
        }

        $(".news-container button.layout-toggler").click(function(){
            setCookie('news_list_layout', $(this).attr("data"), 7, path=$(this).attr("path"));
            window.location.reload();
        });

        $('#news-filter input.autoapply').on('change', function() {
            $(this).closest("form").submit();
            
        });
        $('#news-filter input#filter-reset').on('click', function() {
            $(this).closest("form").reset();
            //$(this).closest("form").find('input:not([type="submit"])').val('');
        });
        $(".news-container #filter-toggler").click(function(){
            // setCookie('news_list_layout', $(this).attr("data"), 7, path=$(this).attr("path"));
            // window.location.reload();
            $("#news-filter").animate({width: 'toggle'});
        });
    };
})(jQuery || django.jQuery);
