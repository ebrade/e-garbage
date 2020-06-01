
$("#id_province").change(function(){
    // var url = {% url 'load_district' %};
    var province = $(this).val();

    $.ajax({
        url: "url",
        data: {
            'province': province
        },
        success: function (data) {
            $("#id_district").html(data);
            alert("I got it")
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


