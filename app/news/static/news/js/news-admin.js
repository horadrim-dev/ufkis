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
                    $("#publish-post button").css("display", "none");
                    $("#publish-post").append("<div class=\'loading\"><i class=\"fa fa-refresh fa-spin fa-1x fa-fw\"> Выполнение</i></div>");
                },
                success: function(data){

                    switch (data.response) {
                        case "success":
                            $("#publish-post").html("<i class=\"fa fa-check\"> " + data.message + "<i>");
                            break;
                        case "error":
                            alert(data.message);
                            $("#publish-post .loading").html("");
                            $("#publish-post button").css("display", "block");
                            // $("#publish-post").html("<i class=\"fa fa-warning\"> " + data.message + "<i>");
                            break;
                        default:
                            $("#publish-post").html("<i class=\"fa fa-warning\"> Ошибка. Попробуйте обновить страницу.</i>");
                            break;
                    }
                    // if (data.response === "success") {
                    //     $("#publish-post").html("<i class=\"fa fa-check\"> " + data.message + "<i>");
                    // } else if (data.response === "error") {
                    //     $("#publish-post").html("<i class=\"fa fa-warning\"> " + data.message + "<i>");
                    // } else {
                    //     $("#publish-post").html("<span class=\"text-s\">Ошибка. Попробуйте обновить страницу.</span>");
                    // }
                }
            });
        });
    });
})(jQuery || django.jQuery);
