// const promise1= new Promise()
// const date= new Date();


//The keyword new is a constructor
//the problem that OOP fixed in JS
function User(username, ID, isloggedIn){
    this.username = username;
    this.ID=ID;
    this.isloggedIn=isloggedIn;

    return this
}

const userOne= new User("samosa",11,true);
const userTwo=new User("vadapav",22,false);
console.log(userOne);
console.log(userTwo);
//NOW WHEN YOU LOG THE ABOVE IT WILL OVERWRITE THE USER ONE WITH THE INFO OF USERTWO to 
    //avoid this we have constructors
    //simply put the keyword "new" in front of the User fucntion when being called
    //in similary way if you dont use the new keyword while using the Promise function things will get messy.

    // when you use the keyword "new" it will create a new object.
        //then it calls the constructor func
        // thirdly it will take in all the info