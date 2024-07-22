// spread and rest both have same syntax ie: ...
// spread is used to split up array elements or object properties
// rest is used to merge a list of function arguments into an array

// spread example
let a=[1,2,3,4]
let b=[...a]
console.log(b)

// rest example
let fnc = (a,b,c, ...d)=>console.log(a,b,c,d);
fnc(1, 2, 3, 4, 5, 6)
