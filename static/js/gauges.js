var gauge_vars = ["T_shed3_hot", "T_shed3_cold","T_shed2_hot", "T_shed2_cold"]
google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(documentReady);

//get current values from server and update gauge display
// function update_gauge_data(data,chart,options){
//     var vardict = {}
//     for (var index = 0; index<)
// }