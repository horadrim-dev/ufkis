(function($) {
    $(document).ready(function() {

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

                    switch (data.result) {
                        case "success":
                            $("#publish-post").html("<i class=\"fa fa-check\"> " + data.message + "<i>");
                            break;
                        case "error":
                            alert(data.message);
                            $("#publish-post .loading").html("");
                            $("#publish-post button").css("display", "block");
                            break;
                        default:
                            $("#publish-post").html("<i class=\"fa fa-warning\"> Ошибка. Попробуйте обновить страницу.</i>");
                            break;
                    }
                }
            });
        });
    });
})(jQuery || django.jQuery);
