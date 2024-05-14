function strucBiscut(){
    this.width=10;
    this.height=6;
    this.colour="brown";
    this.cream="coco";
}

var Bis1 = new strucBiscut();
var Bis2 = new strucBiscut();
var Bis3 = new strucBiscut();

console.log(Bis1);
///////////////////////////////////////////

function buttonStruc(color,shadow){
    this.radius=3;
    this.height=6;
    this.colour=color;
    this.cream=shadow;
}

let button1= new buttonStruc('green','box');
console.log(button1);


/////////////////////////////
function moojik(artist, song, gener){
    this.song=song;
    this.artist=artist;
    this.gener=gener;

}

let moojik1= new moojik("niqqa", "baby_dont_hurt_me", "pop");
console.log(moojik1);
