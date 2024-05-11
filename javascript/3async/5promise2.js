// chain Promise
// if you want to run tasks by an order use chain Promise
//the result of previous Promise is stored in """data""" you can reuse it.
    //pass it in the then function or catch function

// TASK ORDER:
// GET WATER BOTTEL
// OPEN TAB 
// FILL WATER  
// CLOSE TAB  

let xyz= new Promise((res,rej)=>{
    return res('get water bottel')
})

let p2= xyz .then((data)=>{
    console.log(data);
    return new Promise((res,rej)=>{
        return res('OPEN TAB')
        
    })
 })


let p3=p2.then((data)=>{
    console.log(data);
    return new Promise((res,rej)=>{
        return res('Fill water')
    })
})

let p4=p3.then((data)=>{
    console.log(data);
    return new Promise((res,rej)=>{
        return res('Close Tab')
    })
})

p4.then((data)=>{
    console.log(data);
})
