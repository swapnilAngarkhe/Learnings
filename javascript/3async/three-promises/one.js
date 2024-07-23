let promiseOne = new Promise(function(resolve, reject){
    setTimeout(function(){
        console.log('async task complete')
        resolve()
    },2000)
})

promiseOne.then(function(){
    console.log('promise consumed')
})

new Promise (function(resolve, reject){
    setTimeout(() => {
        console.log('promise without variable')
        resolve()
    }, 2000);
}).then(function(){
    console.log('then without variable');
})

//passing value  through resolve

new Promise(function(resolve,reject){
    setTimeout(() => {
        console.log('passing value through resolve')
        resolve({username:"myusername", name:"samosa"})
    }, 2000);
}).then(function(obj){
    console.log(obj.username)

     
})