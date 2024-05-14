//parent childern type shi with prototype

function hooman(){
    naav='naam';
    canTalk="True";
    willDie="False";
    canWalk="True";
}

let hooman2={
    code: "True",
    Js: "True",
}

hooman2.__proto__=hooman;
console.log(hooman2);
//the above log will not show as its in the prototypes 
console.log(hooman2.canTalk);
hooman2.canTalk;
//see it in console

