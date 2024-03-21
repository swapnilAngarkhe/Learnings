// for-each loops only works on array

var a=[12,2,3,22,34,72,17,13]

//suppose you have to loop through each value of a and add 2 to them:
//SYNTAX:
// var.forEach(funciton(value)){
//    console.log("val here represnts the value that is being looped" val+2);
// }



a.forEach(function(val){
    console.log(val+2);
})

// FOR IN LOOP
// used in loop for obejects
// ::: for (var key in )

var obj={
    name: "samosa",
    city: "Mumbai"

}

for (var key in obj){
    console.log(key);//here are keys
    console.log(obj[key]); // here will be the value
    console.log(key, obj[key]); // both

}