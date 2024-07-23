//A-3:task-4:

const k=new Promise(function(resolve,reject){
    setTimeout(() => {
        oopsie=false;
        if(!oopsie){
            console.log('oopsie set to false')
            resolve()
        }else{
            console.log('oopsie set to true')
            
        }
        
    }, 2000);
})

async function solvedPromise(){
    const response=await solvedPromise
    console.log(response);
}
solvedPromise();



//task-5:
const q=new Promise(function(resolve,reject){
    setTimeout(() => {
        oopsie=true;
        if(!oopsie){
            console.log('oopsie set to false')
            resolve()
        }else{
            console.log('oopsie set to true.')
            
        }
        
    }, 2000);
})

async function unSolved(){
    try{
        const response=await unSolved
    console.log(response);
    }catch{
        console.log(error);
    }
    
}
unSolved();
