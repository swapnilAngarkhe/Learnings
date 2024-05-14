// 4 pillrs of DOM Document Object Model
// while changing the STYLE/CSS of an element write the prop in  camel case ie: CamelCase

//SELECTION OF AN ELEMENT---
//CHANGING HTML
//CHANGING CSS
//EVENt LISTENER
 

// document.querySelector("h1") NAME 
// document.querySelector("#BOX") ID
// document.querySelector(".BOX") CLASS

//below is event listener 
//var.addEventListener("event", function(){

// })

// a.addEventListener("click", function(){
//     console.log("hey")
// })


var bulb = document.querySelector("#bulb");
var b = document.querySelector("button");

var flag = 0;

b.addEventListener("click", function(){
    if (flag == 0) {
        bulb.style.backgroundColor = "yellow";
        console.log("on");
        flag = 1;
    } else {
        bulb.style.backgroundColor = "black";
        console.log("off");
        flag = 0;
    }
});


