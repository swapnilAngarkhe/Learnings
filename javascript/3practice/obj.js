// key value pair shit
//---------------------------------------------
//blank obj= let a={}
//----------------------------------------
// filled obj = let a= {
//     key1:value1,
//     key2:value2,
//     "key3":value2,
    
// }
//--------------------------------------
// to update it:
// a.key1="updated value"

//------------------------------------

// to access it... 2 methods
// 1-console.log(a.key1);
// 2-console.log(a["key3"]);
// 2nd one is situatonal / if the key is in string

//----------------------------------------------------------------

// objects can be declared in 2 methods the I did was litral object other one is constructor obj

//-------------------------------------------------------------------------

// Symbol
// to declare symbol and print it, use []
// eg:
const mysymbol=Symbol("key1")
let a={
    nigga:"man",
    [mysymbol]:"hawgridaaa"
}

console.log(a[mysymbol]) 