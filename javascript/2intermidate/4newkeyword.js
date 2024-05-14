// we used this "new" keyword in constrotor.
//new keyword creats a blank objects which is filled by the values of this.

function moojik(artist, song, gener){
    this.song=song;
    this.artist=artist;
    this.gener=gener;

}

let moojik1= new moojik("baby_dont_hurt_me", "niqqa", "pop");
console.log(moojik1);

//here the new keyword will create a blank object called moojik
{
    // and fill it with
    //song: baby_dont_hurt_me;
    //artist: niqqa;
    //gener: pop;
}