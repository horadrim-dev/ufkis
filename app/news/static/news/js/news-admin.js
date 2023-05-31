(function($) {
    
    var original_onPageLoad = $.fn.onPageLoad;
    $.fn.onPageLoad = function () {
        original_onPageLoad();

        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');

        $("#publish-post button").click(function(){
            var url = $(this).attr("url");
            var data = $(this).attr("data");
            $.ajax({
                url: url,
                method: 'post',
                headers: {'X-CSRFToken': csrftoken},
                dataType: 'json',
                data: data,
                beforeSend: function () {
                    $("#publish-post button").css("display", "none");
                    $("#publish-post").append("<div class=\'loading\"><i class=\"fa fa-refresh fa-spin fa-1x fa-fw\"> Выполнение</i></div>");
                },
                success: function(data){

                    $("#publish-post .loading").html("");

                    switch (data.result) {
                        case "success":
                            toastr.success(data.message);
                            break;
                        case "error":
                            toastr.warning(data.message);
                            $("#publish-post button").css("display", "block");
                            break;
                        default:
                            toastr.error("Ошибка. Попробуйте обновить страницу.")
                            break;
                    }
                }
            });
        });
    }
})(jQuery || django.jQuery);
