let textTag=document.getElementById('text')
let minTag=document.getElementById('min')
let secTag=document.getElementById('sec')
let msecTag=document.getElementById('m-sec')
let Display=document.getElementById('display')

let value=textTag.value

let firstBtn=document.getElementById('btn-1')
let secondBtn=document.getElementById('btn-2')
let thirdBtn=document.getElementById('btn-3')
let fourthBtn=document.getElementById('btn-4')
let fifthBtn=document.getElementById('btn-5')

let seconds=0;
let milliseconds=0;
let minutes=0;

let flag=true

function timer()
{
    milliseconds+=10
    if (milliseconds==0)
    {
        seconds+=1
        milliseconds=0
        if(seconds==60)
        {
            minutes+=1
            seconds=0
        }
    }
    minTage.textContent=concatzero(minutes)
    secTag.textContent=concatzero(seconds)
    msecTag.textContent=concatzero(milliseconds)
}

function concatzero(time){
    if(time<=9) return 0+time;
    else return time;
}

textTag.addEventListener('keyup',function()
{
   let id=setInterval(time,10);
});

let disarr=['hello world!','hii everyone','welcome back','evryone should attend mock','i have new car']

disarr.addEventListener('click',function(ele,ind))
{
    if(ind==0)
    {
        firstBtn.addEventListener('click',function(){
            Display.innerHTML=ele
        })
    }
    else if(ind==1)
    {
        secondBtn.addEventListener('click',function()
    {
        Display.innerHTML=ele
    })
    }
}