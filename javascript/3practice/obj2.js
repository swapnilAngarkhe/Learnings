// Construtive or singleton objects
//Objects within objects
 const regular={
    id: 123,
    fullname:{
        user_fullname:{
            firstName: 'nigga',
            lastName: 'Tron'
        }
    }
 }

 console.log(regular.fullname);
 console.log(regular.fullname.user_fullname);
 console.log(regular.fullname.user_fullname.firstName);
//---------------------------------------------
//combaining two objects

const obj1={1:'a', 2:'b'}
const obj2={3:'c', 4:'d'}
// first way
obj3=Object.assign(obj1, obj2)
console.log(obj3);
//2nd way (optimal)
obj4={...obj1, ...obj2}
console.log(obj4);

//-------------------------------------------------------
// checking if value or key is present in the obj (boolen return)
//using Object.hasOwnPropertey
console.log(obj1.hasOwnProperty('1'));
console.log(obj1.hasOwnProperty('bruh'));
//--------------------------------------------------------------
//getting all the keys or values of an object 
//using Object.key/value here Object is the keyword
//Make sure to write "Object.values"
console.log(Object.keys('regular'));
console.log(Object.values('obj1'));