

//Get current values from server and update display. Activated at interval as set in document.ready function
function update_page_data(variables_to_update){
    var variables_to_update_dict = {};
    for (var index = 0; index < variables_to_update.length; index++){  // build dict object of name: value, to send to server.
        variables_to_update_dict[variables_to_update[index]] = variables_to_update[index];
    };
    $.ajax({
        url: $SCRIPT_ROOT + "/_update_page_data",
        type: "GET",
        data: variables_to_update_dict,
        success: function(response){
            var updated_variables = response.ajax_data;
            console.log(updated_variables);
            for (var i in updated_variables) {
                updated_variable = updated_variables[i];
                $('#' + i).html(updated_variable);               // update value at current id
                $('#' + i).addClass('bold');                    // bold numbers when they are updated
                //changeBackgroundColor("#" + i, number_received);// change background color based on value for alarming reasons
            }
        }
    })
}

// Ajax send changed input to server
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

// Change the background color based on the temperature value, could use range parameter for each value. eg, get info from config file on server for each variable, alarm enabled, alarm status, range high, range low.
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
        var allVariables = document.querySelectorAll('[id]');               // get all id names from html
        var inputs = [];
        var outputs = [];
        for (var index = 0; index < allVariables.length; index++){          // iterate through list, separating inputs and removing the input_tag from the names
            var variable = allVariables[index].id;
            if (variable.includes('input_')){
              var input = variable.replace("input_", "");
              inputs.push(input);
            }else{
                outputs.push(variable);
            }}
        var variables = {"Inputs": inputs, "Outputs": outputs}              // return object {dict} on input and output names
        console.log(variables)
        return variables;
      }

// create string of input names to watch in .change function. Uses the format for jquery of #input_id, etc
    function generate_input_string(Inputs){
        var input_string = "";
        for (var i = 0; i < Inputs.length; i++){
            var str1 = "#";
            var str2 = "input_";
            var str3 = Inputs[i];
            var str4 = ", "
            input_string = input_string.concat(str1, str2, str3, str4);
        }
        input_string = input_string.slice(0, -2);
        return input_string
    }

// get initial list of inputs and store their values
    function get_input_values(Inputs){                              // gets the current settings from all id's with prefix input_, currently working for checkbox and numeric, add others as needed.
        var input_values = {}
        for (var i = 0; i < Inputs.length; i++){
            var type = $("#input_" + Inputs[i]).attr('type');       // check input type
            if (type == 'checkbox'){
                input_values[Inputs[i]] = $("#input_" + Inputs[i]).prop('checked');
            }
            else {
            input_values[Inputs[i]] = $("#input_" + Inputs[i]).val()
            }
        }
        return input_values
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
    
// Set JQuery refresh interval.
  setInterval(update_page_data, 1000, variables.Outputs)

// monitor inputs for changes, trying to use variables.Inputs to automatically work with changing html
    var input_string = generate_input_string(variables.Inputs)      // generate list of current inputs as a string to monitor for changes
    var inputs_prev = get_input_values(variables.Inputs)           // initialize list of current input values for tracking which input has changed
    

    $(input_string).on("change", function(){                        // monitor input string for changes, run on change
        var inputs_current = {}
        var input_changed = {}
        inputs_current = get_input_values(variables.Inputs)
        for (var i = 0; i < variables.Inputs.length; i++){
            var input = variables.Inputs[i];
            if (inputs_current[input] != inputs_prev[input]){       // check if this input has changed, if so add to list of changes to send to server and update list of previous readings for next evaluation
                inputs_prev[input] = inputs_current[input];
                input_changed[input] = inputs_current[input];
            }
        }
        senddata(input_changed)                                     // send new value to server
    })

})