(function($) {
    $(document).ready(function() {
        $("#publish-post button").click(function(){
            // var post = $(this).attr("post");
            var url = $(this).attr("url");
            $.ajax({
                url: url,
                method: 'get',
                dataType: 'json',
                // data: {post: post},
                beforeSend: function () {
                    $("#publish-post").html("<i class=\"fa fa-refresh fa-spin fa-1x fa-fw\"></i> <span class=\"text-m\">Выполнение</span>");
                },
                success: function(data){
                    if (data.response) {
                        $("#publish-post").html("<i class=\"fa fa-check\"> Опубликовано<i>");
                    } else {
                        $("#publish-post").html("<span>Ошибка. Попробуйте обновить страницу.</span>");
                    }
                }
            });
        });
    });
})(jQuery || django.jQuery);
