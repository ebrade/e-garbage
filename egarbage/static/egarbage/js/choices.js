$("#id_province").change(function(){
    var url = $("#registerForm").attr("data_load_district");
    var province = $(this).val();

    $.ajax({
        url: url,
        data: {
            'province': province
        },
        success: function (data) {
            $("#id_district").html(data);
        }

        // success: function (data) {
        //     $("id_sector").html(data);
        // },
        //
        // success: function (data) {
        //     $("id_cell").html(data);
        // },
        //
        // success: function (data) {
        //     $("id_village").html(data);
        // },

    });
});


