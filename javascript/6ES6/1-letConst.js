//es6 AKA Ecmascript released in 2015 is a standarizaiton of JS introduced 
    // let,const, arrow functions, template litrals (``),  and default paramters


//if you declare let without a value it will not throw an error but const will.

let a;
const k; 

//both are from es6, 
//both braces scoped
{
    let a=12;
    const k=12;
}
console.log(a);
console.log(k);