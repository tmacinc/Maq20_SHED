
//Ajax scheduled server query
function fetchdata(){
    $.ajax({
        url: "_maq20_fetch_data",
        type: "GET",
        success: function(response){
            var modules = [response.ajax_data.mod1_AI_MVDN, 
                response.ajax_data.mod2_AI_TTC, 
                response.ajax_data.mod3_AO_VO, 
                response.ajax_data.mod4_DI_DIV20, 
                response.ajax_data.mod5_DIO_DIOL, 
                response.ajax_data.mod6_DIO_DIOL, 
                response.ajax_data.mod7_DIO_DIOL, 
                response.ajax_data.mod8_DIO_DIOL];
                var modules_length = modules.length;
            for (var j = 0; j < modules_length; j++){
                var module_current = modules[j];
                console.log("Received number: " + module_current);                
                var module_length = module_current.length;
                for (var i = 0; i < module_length; i++){
//                    console.log("Received channel :" + i.toString() + " " + module_current[i].toString())                
                    $("#mod" + (j+1).toString() + "_" + i.toString()).text(module_current[i]);
        }}
    }
    })
}

//Runs once the document is ready and published in the browser.
$(document).ready(function(){

//schedule the ajax query
    setInterval(fetchdata, 1000);

    // update navbar with indicator of current page (currently color, can increase font etc.)
    $("[href]").each(function() {
        if (this.href == window.location.href) {
            $(this).addClass("currentLink");
        }
    });
//connect the socket to the server.

    //This is used for https transfers when deployed to online server
    // var socket = io.connect('https://' + document.domain + ':' + location.port + '/test', {secure: true});
    
    //This is used for http transfers when deployed to local network
/*    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');


//socket.io tasks. Performed when messages are received from the server.

    //receive details from server and update items using ID as definition.
    socket.on('newnumber', function(msg) {
        console.log("Received number: " + msg.number);
        var arrayLength = msg.number.length;       
        for (var i = 0; i < arrayLength; i++) {
            number_recieved = msg.number[i]
            number_string = '<p>' + number_recieved.toString() + '</p>';
            $('#log' + i.toString()).html(number_string);
        }  
    });
    socket.on('newmeasurement', function(msg) {
        console.log("Received measurement: " + msg.measurements);
        temperature_received = msg.measurements[0]
        humidity_received = msg.measurements[1]
        temperature_string = '<p>' + temperature_received.toString() + '</p>';
        humidity_string = '<p>' + humidity_received.toString() + '</p>';
        $('#temp').html(temperature_string);
        $('#humid').html(humidity_string)
        changeBackgroundColor('#temp', temperature_received)
    })
    // Update the chart when data is sent from server
    socket.on('newchartdata', function(msg) {
        var new_data = [msg.temperaturedata, msg.humiditydata, msg.timestamp]
        var time_stamp = new_data.pop(2)
        console.log("Received Chart Data :" + new_data + " with time stamp: " + time_stamp);
        //remove oldest once chart is 24hrs
        if (myChart.data.labels.length >= 60){
            myChart.data.labels.shift();
            myChart.data.datasets.forEach((dataset) => {
                dataset.data.shift();
            })
        }
        myChart.data.labels.push(time_stamp);
        myChart.data.datasets.forEach((dataset, index) => {
            dataset.data.push(new_data[index]);
        })
        myChart.update();
    }); 
*/
//Client side user interaction tasks

    //This function updates a display when a user input is changed (client side operation)

//    $("#input").on('change', function(){
//       var input_string = $("#input").val();
//        console.log('User input: ' + input_string)
//        $('#output').html('<p>' + input_string.toString() + '</p>');
//    })

//Ajax queries to server 

    //This function sends a user input to the server to perform an action and updates
    //the output with the response (server side operation at route /_add_numbers)    

//    $('input[name="b"]').on('change', function(){
//        $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
//            a: $('input[name=a]').val(),
//            b: $('input[name=b]').val()
//        }, function(data) {
//            $("#result2").text(data.result2);
//        });
//        return false;
//    });

//Additional client side functions

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

});