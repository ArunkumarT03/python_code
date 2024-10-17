let item1={id:1,img:"https://tse2.mm.bing.net/th?id=OIP.Q4f5lR46RdwAqe9hXJ7dlAHaF7&pid=Api&P=0&h=220",name:'chiken Biriyani',price:150,qty:1}
let item2={id:2,img:"https://up.yimg.com/ib/th?id=OIP.4RwEkWIDE9xm5-cBTGJBmgHaEK&pid=Api&rs=1&c=1&qlt=95&w=206&h=115",name:'mutton Biriyani',price:260,qty:2}
let item3={id:3,img:"https://tse2.mm.bing.net/th?id=OIP.Q4f5lR46RdwAqe9hXJ7dlAHaF7&pid=Api&P=0&h=220",name:'Beef Biriyani',price:100,qty:3}
let item4={id:4,img:"https://tse2.mm.bing.net/th?id=OIP.Q4f5lR46RdwAqe9hXJ7dlAHaF7&pid=Api&P=0&h=220",name:'Prawn Biriyani',price:230,qty:4}

let items=[item1,item2,item3,item4];

function displayitems(products){
    if(products.length!=0){

        let eachproduct=``

        for (let product of products){

            eachproduct+=`<div class="col-md-3">
            <div class="card">
                <div class="card-header">
                    <img src="${products.img}" alt=""
                    class="img-fluid">
                </div>
                <div class="card-body ">
                 <h2>${products.name}</h2>
                 <h3>${products.price}.00 &#8377</h3>
                 <h5>
                     <i class="bi bi-dash-circle-fill"></i>
                     <span>
                    ${products.qty}</span>
                     <i class="bi bi-plus-circle-fill"></i>
                 </h5>

                </div>
             </div>
        </div>`
        }
        document.getElementById('display-task').innerHTML=eachproduct
    }
}
displayitems(items);
