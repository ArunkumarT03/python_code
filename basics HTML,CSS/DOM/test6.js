let likesbtn=document.getElementById('likes-btn')
let dislikesbtn=document.getElementById('dislikes-btn')
let displaylikes=document.getElementById('likes-display')
let displaydislikes=document.getElementById('dislikes-display')
let totaldisplay=document.getElementById('total')

let likes=localStorage.getItem('likes')?localStorage.getItem('likes'):0;
let dislikes=localStorage.getItem('dislikes')?localStorage.getItem('dislikes'):0;
let  total=localStorage.getItem('total')?localStorage.getItem('total'):0;

displaylikes.textContent=likes
displaydislikes.textContent=dislikes
totaldisplay.textContent=total

likesbtn.addEventListener('click',function()
{
    likes++;
    localStorage.setItem('likes',likes)
    displaylikes.textContent=localStorage.getItem('likes');
    total++;
    localStorage.setItem('total',total)
    totaldisplay.textContent=localStorage.getItem('total')
    
})
dislikesbtn.addEventListener('click',function()
{
    dislikes++;
    localStorage.setItem('dislikes',dislikes)
    displaydislikes.textContent=localStorage.getItem('dislikes');
    total++;
    localStorage.setItem('total',total)
    totaldisplay.textContent=localStorage.getItem('total')
    
})
//localStorage.clear()