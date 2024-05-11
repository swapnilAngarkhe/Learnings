// in a sense Js is not async language

// js runs in two stacks Side stack (ss) and Main stack (ms)

// sync goes to ms and gets done and dusted
// async goes to ss and starts its work, after and only after the ms is empty it will ask 
// ss if there are any async done yet? if yes then it will put it in ms and complete it if no it will wait.

// the intaraction between ms and ss is called event loop, event loop takes the async in ss to ms

// the best example is:
//according to the code bellow the order expected is 1234, but will print 1243 because js is not async
//and it follows above structure to manage.

console.log('1')
console.log('2')
setTimeout(function(){
    console.log('3');
},0)
console.log('4');

//this is the single thread nature of js, its not multi-threaded