//set time out syntax:
// setTimeout(callback, time in ms)
//here call back is a function that you are in need to run after the "time in ms" passes

// ex:
console.log('namaste');
setTimeout(function(){
    console.log('hello world');
},3000)


//note that the delayed response should be written in the callback funcion.

//what if:

console.log('//////////////////////')
setTimeout(function(){
    console.log('shantabai')
},2000)
console.log('samosa')

// here you can notice 'samosa' is printed after shantabai, indicating that it has to wait 
//for shantabai to print

//its called call back funciton because it will wait untill its time has come and
//he will be called back.