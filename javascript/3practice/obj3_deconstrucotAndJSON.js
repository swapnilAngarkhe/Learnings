//Destructering Object

const course={
    name:'Dan',
    course:'cs50',
    instructor:'David J'
}

const {instructor}=course
console.log(instructor);

const {name:n}=course
console.log(n);

//--------------------------------------------------------
//JSON
//JSON is basically object without name and key value both are strings
{
    "name":"samosa",
    "game":"litrally zero"
    "age": "23"
}
