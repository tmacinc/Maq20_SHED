anychart.onDocumentReady(function () {
    var T_vars = ["T_shed3_hot", "T_shed3_cold", "T_shed2_hot", "T_shed2_cold", "T_main_hot", "T_main_cold","T_shed1_cold","T_shed1_hot"];
    // create data
    var data_T = [[22],[22],[22],[22],[22],[22],[22],[22]];
    var data_title = ["T_shed3_hot", "T_shed3_cold", "T_shed2_hot", "T_shed2_cold", "T_main_hot", "T_main_cold","T_shed1_cold","T_shed1_hot"];

    
    // set the gauge type
    var gauge_T_shed3_hot = anychart.gauges.thermometer();
    var gauge_T_shed3_cold = anychart.gauges.thermometer();
    var gauge_T_shed2_hot = anychart.gauges.thermometer();
    var gauge_T_shed2_cold = anychart.gauges.thermometer();
    var gauge_T_main_hot = anychart.gauges.thermometer();
    var gauge_T_main_cold = anychart.gauges.thermometer();
    var gauge_T_shed1_cold = anychart.gauges.thermometer();
    var gauge_T_shed1_cold = anychart.gauges.thermometer();

    // set the data for the gauge
    gauge_T_shed3_hot.data(data_T[0]);
    gauge_T_shed3_cold.data(data_T[1]);
    gauge_T_shed2_hot.data(data_T[2]);
    gauge_T_shed2_cold.data(data_T[3]);
    gauge_T_main_hot.data(data_T[4]);
    gauge_T_main_cold.data(data_T[5]);
    gauge_T_shed1_cold.data(data_T[6]);
    gauge_T_shed1_cold.data(data_T[7]);


    // set the title of the gauge
    gauge_T_shed3_hot.title(data_title[0]);
    gauge_T_shed3_cold.title(data_title[1]);
    gauge_T_shed2_hot.title(data_title[2]);
    gauge_T_shed2_cold.title(data_T[3]);
    gauge_T_main_hot.title(data_title[4]);
    gauge_T_main_cold.title(data_title[5]);
    gauge_T_shed1_cold.title(data_title[6]);
    gauge_T_shed1_cold.title(data_title[7]);

    //gauge.title('Thermometer with Fahrenheit and Celsius Scales');

    // add a thermometer pointer
    gauge_T_shed3_hot.addPointer(0);
    gauge_T_shed3_cold.addPointer(0);
    gauge_T_shed2_hot.addPointer(0);
    gauge_T_shed2_cold.addPointer(0);
    gauge_T_main_hot.addPointer(0);
    gauge_T_main_cold.addPointer(0);
    gauge_T_shed1_cold.addPointer(0);
    gauge_T_shed1_cold.addPointer(0);
   

    // use the primary scale a Fahrenheit scale
    var fScale1 = gauge_T_shed3_hot.scale();

    // set the minimum and maximum values of the Fahrenheit scale
    fScale.minimum(-40);
    fScale.maximum(122);

    // set the intervals of major and minor ticks on the Fahrenheit scale
    fScale.ticks().interval(10);
    fScale.minorTicks().interval(2);    

    // add an axis on the left side of the gauge
    var axisLeft = gauge.axis(0);

    // configure minor ticks on the left axis
    axisLeft.minorTicks(true)
    axisLeft.minorTicks().stroke('#cecece');

    // set the width of the left axis
    axisLeft.width('0');

    // set the offset of the left axis (as a percentage of the gauge width)
    axisLeft.offset('-0.18%');

    // bind the left axis to the Fahrenheit scale
    axisLeft.scale(fScale);

    // configure a Celsius scale
    var cScale = anychart.scales.linear();
    cScale.minimum(-40);
    cScale.maximum(50);
    cScale.ticks().interval(10);
    cScale.minorTicks().interval(1);

    // configure an axis on the right side of the gauge
    var axisRight = gauge.axis(1);
    axisRight.minorTicks(true);
    axisRight.minorTicks().stroke('#cecece');
    axisRight.width('0');
    axisRight.offset('3.15%');
    axisRight.orientation('right');

    // bind the right axis to the Celsius scale
    axisRight.scale(cScale);

    // set the container id
    gauge.container('container');

    // initiate drawing the gauge
    gauge.draw();
});