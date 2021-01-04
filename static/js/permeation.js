

//Get current control values from server and update defaults. Not needed?
function update_page_data(allElements){
    var vardict = {};
    console.log(allElements);
    for (var index = 0; index < allElements.length; index++){
        vardict[allElements[index]] = allElements[index];
    };
//    console.log(vardict);
    $.ajax({
        url: $SCRIPT_ROOT + "/_update_page_data",
        type: "GET",
        data: vardict,
        success: function(response){
            var parsed_data = response.ajax_data;
            console.log(parsed_data);
            for (var i in parsed_data) {
                number_received = parsed_data[i];
                $('#' + i).html(number_received);
                $('#' + i).addClass('bold');                    //bold numbers when they are updated
            }
        }
    })
}

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

//Ajax send changed input to server
function senddata(data){
    $.ajax({
        type: "GET",
        url: "_set_control",
        data: data,
        success: function(response){
            console.log(response)
        },
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

// get page variables and separate into indicators and controls (inputs and outputs).
    function get_variables(){
        var allVariables = document.querySelectorAll('[id]');
        var inputs_html = [];
        var inputs = [];
        var inputs_dict = {};
        var outputs = [];
        for (var index = 0; index < allVariables.length; index++){
            var variable = allVariables[index].id;
            if (variable.includes('input_')){
              var input = variable.replace("input_", "");
              inputs_html.push(variable)
              inputs.push(input);
              inputs_dict[input] = variable;
            }else{
                outputs.push(variable);
            }}
        var variables = {"Inputs": inputs, "Outputs": outputs}
        return variables;
      }

// create string of input names to watch in .change function

    function generate_input_string(Inputs){
        var input_string = "";
        console.log(Inputs)
        console.log(Inputs.length)
        for (var i = 0; i < Inputs.length; i++){
            console.log(Inputs[i]);
            var str1 = "#";
            var str2 = "input_";
            var str3 = Inputs[i];
            var str4 = ", "
            input_string = input_string.concat(str1, str2, str3, str4);
        }
        input_string = input_string.slice(0, -2);
        console.log("String: " + input_string);
        return input_string
    }

// get initial list of inputs and store their values

    function initialize_inputs(Inputs){
        var inputs = {}
        for (var i = 0; i < Inputs.length; i++){
            var type = $("#input_" + Inputs[i]).attr('type');
            if (type == 'checkbox'){
                inputs[Inputs[i]] = $("#input_" + Inputs[i]).prop('checked');
            }
            else {
            inputs[Inputs[i]] = $("#input_" + Inputs[i]).val()
            }
        }
        return inputs
    }

//Runs once the document is ready and published in the browser.
$(document).ready(function(){

// update navbar with indicator of current page (currently color, can increase font etc.)
    $("[href]").each(function() {
        if (this.href == window.location.href) {
            $(this).addClass("currentLink");
        }
    });

// get list of variables used by page (tags which have and id="")

    var variables = get_variables()
    
// call the initialize page data function
    


// Set JQuery refresh interval.
  setInterval(update_page_data, 1000, variables.Outputs)

// monitor inputs for changes, trying to use variables.Inputs to automatically work with changing html

    var input_string = generate_input_string(variables.Inputs) //generate list of current inputs
    var inputs_prev = initialize_inputs(variables.Inputs)   //initialize list of current input values for tracking which input has changed
    

    $(input_string).on("change", function(){
        var inputs_current = {}
        var input_changed = {}
        for (var i = 0; i < variables.Inputs.length; i++){
            var input = variables.Inputs[i];
            var type = $("#input_" + input).attr('type');
            if (type == 'checkbox'){
                inputs_current[input] = $("#input_" + input).prop('checked')
            }
            else {
                inputs_current[input] = $("#input_" + input).val()
            }
//            console.log(inputs_current[input]);
            if (inputs_current[input] != inputs_prev[input]){
//                console.log("Input changed is: " + input);
//                console.log("current value: " + inputs_current[input]);
//                console.log("Previous value: " + inputs_prev[input]);
                inputs_prev[input] = inputs_current[input];
                input_changed[input] = inputs_current[input];
//                console.log(input_changed)
            }
        }
        senddata(input_changed)    // send new value to server
//        console.log(input_changed);
    })

})