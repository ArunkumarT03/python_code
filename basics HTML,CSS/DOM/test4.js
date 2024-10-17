let obj1={
      id:101,
      img:"https://up.yimg.com/ib/th?id=OIP.fbmteUWIfkCuXM7a5Ex7rQHaHa&pid=Api&rs=1&c=1&qlt=95&w=121&h=121",
      name:'shawarma',
      price:40.00,
      Qty:1,
      totalprice:40.00

}
let htmlcode=`<tr>
                <td>${obj1.id}</td>
                <td>
                   <img src=${obj1.img}  alt="" width="40px" height="30px">
                </td>
                <td>${obj1.name}</td>
                <td>${obj1.price}&#8377</td>
                <td>
                    <i class="bi bi-plus-circle-fill" onclick="incre()"></i>
                    <span id="display-qty">${obj1.Qty}</span>
                    <i class="bi bi-dash-circle-fill" onclick="decre()"></i>
                </td>
                <td>${obj1.totalprice} &#8377</td>
            </tr>`
let objdisplay=document.getElementById('display-item')
objdisplay.innerHTML=htmlcode
let disply=1
   let displayqty=document.getElementById('display-qty')
   displayqty.textContent=disply
 function incre(){
 
    ++disply
    displayqty.textContent=disply
}
function decre(){
     if(disply>1){
        --disply
        displayqty.textContent=disply
     }
}