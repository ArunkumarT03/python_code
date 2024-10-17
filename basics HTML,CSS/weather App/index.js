// let searchBtn=document.querySelector('.search')
// let formTag=document.querySelector('.form')
// let iconDiv=document.querySelector('.icon');
// let weatherInfo=document.querySelector('.info');

// formTag.addEventListener('submit',function(e){
//     e.preventDefault()
//     iconDiv.innerHTML=`<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSng5iGr1TB2UmRnLdjzCBVlhVuJ2nPzi1y9A&s" class="h-[80px] mx-[auto]" alt="">
//             <h4 class="mt-2">City Name</h4>
//             <h3>24 C</h3>`
//     weatherInfo.innerHTML=`<div class="ms-4 mb-2">
//                 <h3>Humidity</h3>
//                 <h3>74%</h3>
//             </div>
//             <div class="me-4 mb-2">
//                 <h3>Wind speed</h3>
//                 <h3>6 km/hr</h3>
//             </div>`
// })

// let url = "https://api.openweathermap.org/data/2.5/weather?q=karnataka&appid=6d44b4350d90ecb254cb31e745a94397&units=metric";

// fetch(url).then((res)=>res.json())
// .then((data)=>console.log(data))
// .catch((err)=>console.log(err))

let input=document.getElementById('city')
let searchBtn=document.querySelector('#search')

searchBtn.addEventListener('click',()=>{
    //console.log(input.value);
    let city=input.value
    if(!city .trim()){
        alert('write a city first then search ')
    }
    else{
        fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=6d44b4350d90ecb254cb31e745a94397&units=metric`)
        .then(response => {
            if (response.status==200){
                return response.json()
            }
            else{
                alert('enter valid city name')
            }
    })
        .then(data =>{ 
            console.log(data)
            if(data)
            {
                displayweather(data)
            }
        })
        .catch(error => console.log(error))
    }
})

function displayweather(data){
    document.getElementById('city-name').innerHTML= data.name
                document.getElementById('temp').innerHTML= Math.round(data.main.temp)+ '℃'
                document.getElementById('wind').innerHTML= Math.round(data.wind.speed)+ 'km/hr'
                document.getElementById('humid').innerHTML= Math.round(data.main.humidity)
               document.getElementById('display').classList.remove('hidden')
}