// 3types of arrow functions
    // fat arrow function
    // arrow function with parameter
    // arrow function with return value

// fat arrow function
const add = (num1, num2) => {
    const sum = num1 + num2;
    return sum;
}
console.log(add(12, 12))

// arrow function with parameter
const add2 = (num1, num2) => {
    const sum = num1 + num2;
    return sum;
}

console.log(add2(12, 12))
// arrow function with implicet return 
const add3 = (num1,num2)=>num1 + num2;
console.log(add3(12, 12))
