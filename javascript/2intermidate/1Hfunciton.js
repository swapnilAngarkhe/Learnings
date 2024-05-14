//heigher functions: which accepts funcitons as parameters OR returns a Function , ether one of these condition should meet.
// example : forEach.

function abc(val){


}

abc(function(){
    console.log('hello');
})


//////////////////////////
function xyz(){
    return function (){
        console.log('bruh');
    }
}

xyz()



