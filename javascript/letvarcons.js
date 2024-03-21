// var is function scoped: ie the var once declared can be used throughout the function

// let is curly-braces scoped {}: ie the let can be used within the curly brases
// =========================================================

// LET 
// in the code below the numbers printed will be till 11,
    // as "i" cannot be used after {}

function lett(){
    for (let i=1; i<12; i++){
        console.log(i)
    }
    // console.log(i) 
}

lett();
// ======================================================

// LET 
// in the code below the numbers printed will be till 12,
    // as "a" can be used after {} cuz its function scoped
function varr(){
    for(var a=1; a<12; a++){
        console.log(a)
    }
    console.log(a)
}

varr();

// Let cannot be seen in window, but var can. 
//Window object is something that Js doesnt have but can use it form the browsers
// few exampls are "print, prompt, scroll, fetch ..."
