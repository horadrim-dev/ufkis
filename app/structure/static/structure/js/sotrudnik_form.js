(function($) {
    $(document).ready(function () {
        // при выборе организации, подгружаем в поле "Отдел" список ее отделов через ajax
        $("#sotrudnik_form select[name='organization']").on('change', function(){
            var url = $(this).attr("data-otdels-url");  // получаем url переданный из forms.py и отрезаем последние 2 символа, "1/"
            var orgId = $(this).val();  // get the selected org
            if (!orgId) return;
            $.ajax({                       // initialize an AJAX request
                url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
                data: {
                'org_id': orgId       // add the country id to the GET parameters
                },
                success: function (res) {   // `data` is the return of the `load_cities` view function
                    let options='<option value="" selected="">---------</option>';
                    res.data.forEach(otdel => {
                        options += '<option value=\"' + otdel.id +'\">' + otdel.name + '</option>';
                    });
                    $("#sotrudnik_form select[name='otdel']").html(options);
                }
            });
        });
    });
})(jQuery || django.jQuery);