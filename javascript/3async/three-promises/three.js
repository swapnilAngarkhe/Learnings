//A-4 
//TASK-6: with promise
response=fetch('https://jsonplaceholder.typicode.com/todos/1')
.then(function(response){

    if(response){
        console.log('data recived from api')
    const responseJson=response.json()
    console.log(responseJson)
    }else{
        console.log('else... data not  recived');
        reject()
    }
    
}).catch(function(){
    console.log('catch....data not recived')
})


//task-7: with async

async function apiAsync(){
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1')
    const jsonData= await response.json()
    console.log(jsonData);
}
apiAsync();