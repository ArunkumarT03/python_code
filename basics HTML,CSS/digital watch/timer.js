let minTage=document.getElementById('min')
let secTag=document.getElementById('sec')
let msecTag=document.getElementById('m-sec')

let startBtn=document.getElementById('start-btn')
let stopBtn=document.getElementById('stop-btn')
let resetBtn=document.getElementById('reset-btn')

let seconds=60;
let milliseconds=1000;
let minutes=15;

let flag=true

function timer()
{
    milliseconds-=10
    if (milliseconds==0)
    {
        seconds-=1
        milliseconds=1000
        if(seconds==0)
        {
            minutes-=1
            seconds=60
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

let interval=null
startBtn.addEventListener('click',function(){
   if(flag)
   {
    interval=setInterval(timer,10)
    flag=false
   }
})

stopBtn.addEventListener('click',function(){
    if(!flag){
        clearInterval(interval)
        flag=true
    }
})

resetBtn.addEventListener('click',function(){

        clearInterval(interval)
        flag=true
        
        minTage.textContent='00';
        secTag.textContent='00';
        msecTag.textContent='00';
        
        milliseconds=1000;
        seconds=60
        minutes=15

})