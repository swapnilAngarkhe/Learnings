// this
// call 
// apply 
// bind 
//method
////////////////////////////////////

//anything out of {} these brackets are global and 
//anything inside {} these brackets are local

//METHOD: any funciton within an object is a method.


// when you log this in:
// global: window
// funciton: window
// method: obj

////////////////////////
// call apply bind=> the motive is when you have a object and a function, run that function but the 
    //the value of "this" should be something from that present object, instead of window
    //use "function.call(value)" to do so.
//CALL BELOW
function need(){
    console.log(this);
}
need();

let BJ ={
    i_want:"Blowjob",
}

need.call(BJ)

//APPLY
//in case you have parameters to take in use function.call(val, [parameters,parameter1,para2...])
function want(val1){
    console.log(this,val1);
}
want();

let Bj ={
    i_want:"Blowjob",
}

need.call(Bj,["Right now!"])

//BIND
//Used in React
function xyz(){
    console.log(this);
}

let anObject={age:22}
let binded=xyz.bind(anObject);
binded()