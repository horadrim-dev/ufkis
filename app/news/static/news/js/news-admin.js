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
                success: function(data){
                    if (data.response) {
                        $("#publish-post").html("<i class=\"fa fa-check\"> Опубликовано<i>");
                    } else {
                        $("#publish-post").html("<h5>Ошибка. Попробуйте обновить страницу.</h5>");
                    }
                }
            });
        });
    });
})(jQuery || django.jQuery);
