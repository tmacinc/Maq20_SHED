var gauge_vars = ["T_shed3_hot", "T_shed3_cold","T_shed3"]
google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(documentReady);

function update_page_data(allElements, data, chart, options){
    var vardict = {};
    for (var index = 0; index < allElements.length; index++){  // build dict object of name: value, to send to server.
        vardict[allElements[index]] = allElements[index];
    };
    $.ajax({
        url: $SCRIPT_ROOT + "/_update_page_data",
        type: "GET",
        data: vardict,
        success: function(response){
            var parsed_data = response.ajax_data;
            // console.log(parsed_data);
            for (var i in parsed_data) {
                for (var j in gauge_vars){
                    var k = 0;
                    console.log(gauge_vars[k])
                    if (i == gauge_vars[j]) {
                        data.setValue(j, 1, parsed_data[i]);
                        chart.draw(data, options);
                    }
                if (parsed_data[i] != "chan_name_error"){
                number_received = parsed_data[i];
                $('#' + i).html(number_received);               // update value at current id
                $('#' + i).addClass('bold');                    // bold numbers when they are updated
                //changeBackgroundColor("#" + i, number_received);// change background color based on value for alarming reasons
                k += 1;
            }}}
        }
    })
}

