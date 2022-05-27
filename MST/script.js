//Sarvesh Rembhoktar
// UTA ID: 1001966297
//Date : 10-Apr-2022


// This function returns array by splitting the given string
function get_edges(){
    
    var edges = document.getElementById("edges").value;
    var arr = edges.split("\n");
    return arr;
}

//This function creates a JSON object and returns it to the calling function
function get_Json(){
    
    var k_val = "N";
    var p_val = "N";
    var kruskal_chk = document.getElementById('kruskal');
    var prims_chk = document.getElementById('prims');
    if (kruskal_chk.checked){
        k_val = document.getElementById('kruskal').value;
    }
    if (prims_chk.checked){
        p_val = document.getElementById('prims').value;
    }
    var text = ' { "numnodes" :"' + document.getElementById("nodenum").value + '","numedges" : "' + document.getElementById("edgenum").value + '","k_algo":"' + k_val + '","p_algo" :"' + p_val + '"}' 
        
    text = JSON.stringify(text);
    try{
        var obj = JSON.parse(text);
    } catch(e){
        alert("Invalid data");
    }
    return obj;
}

//This function is called from the HTML page. It calls the python function exposed by eel and displays the output returned by Python function
async function run(){
    var obj1 = get_Json();
    var edge_lst = get_edges();
    //alert(edge_lst);
    if (obj1 == null){
        return;
    }
    var obj2 = JSON.parse(obj1);
    if (obj2.k_algo=="N" && obj2.p_algo=="N"){
        alert("Please select at least one algorithm to run");
        return;
    }
   
    let n = await eel.run_MST_algo(obj1,edge_lst )(function(n){
    var obj = JSON.parse(n);
    document.querySelector(".K_running_time").innerHTML = obj.K_runtime;
    var x = obj.K_MST;
    var txt="";
    for (var i = 0; i < x.length; i++) {
        txt += x[i];
        if ((i+1) != x.length){
            txt += "\n";
        }
    }
    document.getElementById("kruskal_output").value = txt;

    document.querySelector(".P_running_time").innerHTML = obj.P_runtime;
    var x = obj.P_MST;
    var txt="";
    for (var i = 0; i < x.length; i++) {
        txt += x[i];
        if ((i+1) != x.length){
            txt += "\n";
        }
    }
    document.getElementById("prims_output").value = txt;
    document.querySelector(".RT_diff").innerHTML = obj.rt_diff;
})
}


//This function is called for adding the edge to the text area on the HTML screen
var x="";

function addEdge(){
    
    x += document.getElementById("node1").value + "," + document.getElementById("node2").value + "," + document.getElementById("weight").value + "\n";
    document.getElementById("edges").value = x;
    document.getElementById("node1").value = "";
    document.getElementById("node2").value = "";
    document.getElementById("weight").value = "";
}
/*
document.querySelector("button").onclick = async function () {  
    // Call python's random_python function
    eel.kruskal_MST()(function(n){                      
      // Update the div with a random number returned by python
      
      var obj = JSON.parse(n);
      document.querySelector(".running_time").innerHTML = obj.runtime;
      var x = obj.MST;
      var txt="";
      for (var i = 0; i < x.length; i++) {
            txt += x[i] + "\n"
        }
      document.getElementById("output").value = txt
    })
  }
*/