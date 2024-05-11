// suppose you fetch a request into a var
// the request has been sent 
// now the request will be in pending state 
// if the response is recived then it will be in resolve state 
// if the response is not recived it will be in reject state 

// overall request can be in 3 states pending, resovle, reject 

//if its resolved continue with "then function"
//if its rejected continue with "catch function"
//Promise is a constructor function which is invoked with new thats why we write new before writting Promise




// example 1:

let ans1= new Promise(function(res, rej){
    if(true){
        return res();
    }else{
        return rej();
    }

})

ans1
 .then(function(){console.log('resolved');})
 .catch(function(){console.log('rejected');})


/////////////////////////////////////////////
//  example 2:
//note we are taking number randomly from math.random

let ans2=new Promise((res,rej)=>{
    let a=Math.floor(Math.random()*10)

    if(a>5){
        return res();
    }else{
        return rej();
    }

})

ans2
 .then (()=>{
    console.log('number resolved');
 })
 .catch(()=>{
    console.log('number rejected');
 })

