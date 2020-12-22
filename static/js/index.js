
//Ajax scheduled server query
function fetchdata(){
    $.ajax({
        url: "_fetch_data",
        type: "GET",
        success: function(response){
            var ajax_length = response.ajax_data.length;
            console.log("Received number: " + response.ajax_data);
            for (var i = 0; i < ajax_length; i++){                
                $("#ajax_response" + i.toString()).text(response.ajax_data[i]);
        }}
    })
}

//Runs once the document is ready and published in the browser.
$(document).ready(function(){

//schedule the ajax query
//    setInterval(fetchdata, 1000);
    
//connect the socket to the server.

    //This is used for https transfers when deployed to online server
    // var socket = io.connect('https://' + document.domain + ':' + location.port + '/test', {secure: true});
    
    //This is used for http transfers when deployed to local network
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

//Create Chart Object and initialize
    //Initialize chart object with blank data
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: [],
        options: {
            title: {
                display: true,
                text: "House Temperature and humidity",
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        suggestedMax: 30,
                        fontColor: '#c45850'
                    },
                    id: 'A',
                    type: 'linear',
                    position: 'left',
                    scaleLabel: {
                        labelString: 'Temperature [C]',
                        display: true
                    }
                },{
                    ticks: {
                        beginAtZero: true,
                        suggestedMax: 100,
                        fontColor: "#3e95cd"
                    },
                    id: 'B',
                    type: 'linear',
                    position: 'right',
                    scaleLabel: {
                        labelString: 'Relative Humidity [%]',
                        display: true
                    }
                }],
                xAxes: [{
                    ticks: {
                        maxTicksLimit: 24,
                        maxRotation: 45,
                        minRotation: 45
                    },
                    scaleLabel: {
                        labelString: 'Time of day',
                        display: true
                    }
                }]
            },
            elements: {
                point: {
                    radius: 0
                }
            }
        }
    }); 
   //Update charge with data from server once received from ajax call
    function successinitialized(myChart, record_data){
            myChart.data = {
                labels: record_data.time,
                datasets: [{
                    data: record_data.temp,
                    label: "Temperature [C]",
                    borderColor: "#c45850",
                    fill: false,
                    yAxisID: 'A'
                },{
                    data: record_data.hum,
                    label: "Humidity [%]",
                    borderColor: "#3e95cd",
                    fill: false,
                    yAxisID: 'B'
                }]
            }
            myChart.update();        
            return myChart;
        };           
    //asynchronous call to server for unitial chart data
    function initializedata(myChart){
        $.ajax({
            url: "_initialize_data",
            type: "GET",
            success: function(response){
                var temp_data = response.temp;
                var hum_data = response.hum;
                var time_data = response.time;
                var record_data = {temp: temp_data, hum: hum_data, time: time_data};
                successinitialized(myChart, record_data); //update chart with data
        }
        });  
    };

    //initiate the data retrieval process
    initializedata(myChart);

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