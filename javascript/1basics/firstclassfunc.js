// there is a featur of Js where, we can use a function as a value.

function xyz(a){
    (a);
}

var a=function(){
    console.log("this is a first class function");
}

a();