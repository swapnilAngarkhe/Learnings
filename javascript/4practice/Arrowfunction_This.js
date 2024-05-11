//This keyword
//If we use "this" keyword in a object it will show undefined

const user={
    username:"Dan",
    Price:999,
    wellcomeUser:function(){
        console.log(`${this.username}, to the website`);
    }
    

}

//this
console.log(this);
//this in a function
function kuchbhi(){
    console.log(this);
}
kuchbhi()

//ARROW FUNCTION

const bruh=() =>{
    let username="samosa"
    console.log(this.username);
}
//the this username will still show undefined here as well.

//Alternate arrow funciton
()=>{
    console.log("bruh")
}

//with curly braces
const add=(num1,num2)=>{
    return num1+num2
}
console.log(add(1,2))
//with paranthesis also used in "react"
const addem=(num1,num2)=>(num1+num2)
console.log(addem(1,1));

//with nothing lol
const add2=(num1,num2)=>num1+num2
console.log(add2(1,0));

//arrow and this done.
