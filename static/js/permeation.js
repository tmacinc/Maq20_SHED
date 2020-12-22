
//var allElements = document.querySelectorAll('*[id]')

function initialize_page_data(){
    var allElements = document.querySelectorAll('[id]');
    var variables = [];
    var vardict = {};
    for (var index = 0; index < allElements.length; index++){
        variables.push(allElements[index].id)
        vardict[allElements[index].id] = allElements[index].id;
    };
    console.log(vardict);
    $.getJSON($SCRIPT_ROOT + '/_initialize_page_data', 
        vardict, 
        function(data) {
        $("#result2").text(data.result2);
    });
    return false;
};

//Get current control values from server and update defaults.
function initializedata(){
    $.ajax({
        url: "_permeation_initialize",
        type: "GET",
        success: function(response){
            var response_length = response.ajax_data.length;
            console.log("Received initial data: " + response.ajax_data);

        }
    })
}

// Change the background color based on the temperature value
function changeBackgroundColor(input, value){
    $(input).removeClass();
    if (value < 15){
        $(input).addClass('range_low bold');
    }
    else if(value >= 15 && value <= 25){
        $(input).addClass('range_normal bold');
    }
    else{
        $(input).addClass('range_high bold');
    }
}


//Runs once the document is ready and published in the browser.
$(document).ready(function(){
initialize_page_data()


})