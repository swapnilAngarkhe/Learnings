// asyinc - await came to replace .then  while writing any asyinc funciton 

// instead of the below
function abc(){
    fetch(`https://randomuser.me/api/`)
    .then((raw)=>{
        return raw.json();
    })
    .then((data)=>{
        console.log(data);
    });
}

////////////////////////////////////////////////
//we use
// lets get a response from randomuser api (typically used for simple stuff)
async function abc(){
    let raw =await fetch(`https://randomuser.me/api/`)
    
    let ans= await raw.json();
    console.log(ans);
}
