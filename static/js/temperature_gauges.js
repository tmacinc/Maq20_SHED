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
    var fScale2 = gauge_T_shed3_cold.scale();
    var fScale3 = gauge_T_shed2_hot.scale();
    var fScale4 = gauge_T_shed2_cold.scale();
    var fScale5 = gauge_T_main_hot.scale();
    var fScale6 = gauge_T_main_hot.scale();
    var fScale7 = gauge_T_shed3_hot.scale();
    var fScale8 = gauge_T_shed3_hot.scale();

    // set the minimum and maximum values of the Fahrenheit scale
    fScale1.minimum(-40);
    fScale1.maximum(122);
    fScale2.minimum(-40);
    fScale2.maximum(122);
    fScale3.minimum(-40);
    fScale3.maximum(122);
    fScale4.minimum(-40);
    fScale4.maximum(122);
    fScale5.minimum(-40);
    fScale5.maximum(122);
    fScale6.minimum(-40);
    fScale6.maximum(122);
    fScale7.minimum(-40);
    fScale7.maximum(122);
    fScale8.minimum(-40);
    fScale8.maximum(122);

    // set the intervals of major and minor ticks on the Fahrenheit scale
    fScale1.ticks().interval(10);
    fScale1.minorTicks().interval(2);
    fScale2.ticks().interval(10);
    fScale2.minorTicks().interval(2);    
    fScale3.ticks().interval(10);
    fScale3.minorTicks().interval(2);    
    fScale4.ticks().interval(10);
    fScale4.minorTicks().interval(2);    
    fScale5.ticks().interval(10);
    fScale5.minorTicks().interval(2);    
    fScale6.ticks().interval(10);
    fScale6.minorTicks().interval(2);    
    fScale7.ticks().interval(10);
    fScale7.minorTicks().interval(2);    
    fScale8.ticks().interval(10);
    fScale8.minorTicks().interval(2);        

    // add an axis on the left side of the gauge
    var axisLeft1 = gauge_T_shed3_hot.axis(0);
    var axisLeft2 = gauge_T_shed3_cold.axis(0);
    var axisLeft3 = gauge_T_shed2_hot.axis(0);
    var axisLeft4 = gauge_T_shed2_cold.axis(0);
    var axisLeft5 = gauge_T_main_hot.axis(0);
    var axisLeft6 = gauge_T_main_cold.axis(0);
    var axisLeft7 = gauge_T_shed1_cold.axis(0);
    var axisLeft8 = gauge_T_shed1_hot.axis(0);

    // configure minor ticks on the left axis
    axisLeft1.minorTicks(true)
    axisLeft1.minorTicks().stroke('#cecece');
    axisLeft1.width('0');
    axisLeft1.offset('-0.18%');
    axisLeft1.scale(fScale1);
    axisLeft2.minorTicks(true)
    axisLeft2.minorTicks().stroke('#cecece');
    axisLeft2.width('0');
    axisLeft2.offset('-0.18%');
    axisLeft2.scale(fScale2);
    axisLeft3.minorTicks(true)
    axisLeft3.minorTicks().stroke('#cecece');
    axisLeft3.width('0');
    axisLeft3.offset('-0.18%');
    axisLeft3.scale(fScale3);
    axisLeft4.minorTicks(true)
    axisLeft4.minorTicks().stroke('#cecece');
    axisLeft4.width('0');
    axisLeft4.offset('-0.18%');
    axisLeft4.scale(fScale4);
    axisLeft5.minorTicks(true)
    axisLeft5.minorTicks().stroke('#cecece');
    axisLeft5.width('0');
    axisLeft5.offset('-0.18%');
    axisLeft5.scale(fScale5);
    axisLeft6.minorTicks(true)
    axisLeft6.minorTicks().stroke('#cecece');
    axisLeft6.width('0');
    axisLeft6.offset('-0.18%');
    axisLeft6.scale(fScale6);
    axisLeft7.minorTicks(true)
    axisLeft7.minorTicks().stroke('#cecece');
    axisLeft7.width('0');
    axisLeft7.offset('-0.18%');
    axisLeft7.scale(fScale7);
    axisLeft8.minorTicks(true)
    axisLeft8.minorTicks().stroke('#cecece');
    axisLeft8.width('0');
    axisLeft8.offset('-0.18%');
    axisLeft8.scale(fScale8);
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