let stu_1={id:'101',name:'Arun kumar',email:'arun@gmail.com',gender:'male',marks:[87,78,85,90,96],role:'student',pw:1234}
let stu_2={id:'102',name:'kalim basha',email:'kalim@gmail.com',gender:'male',marks:[97,80,90,89,76],role:'student',pw:4567}
let stu_3={id:'103',name:'subash abi',email:'subash@gmail.com',gender:'male',marks:[92,88,75,85,86],role:'student',pw:7890}
let stu_4={id:'104',name:'Mano freaky',email:'mano@gmail.com',gender:'male',marks:[83,98,75,85,76],role:'student',pw:2345}
let stu_5={id:'105',name:'vijay poomalai',email:'vijay@gmail.com',gender:'male',marks:[83,88,95,75,86],role:'student',pw:3456}

let students=[stu_1,stu_2,stu_3,stu_4,stu_5];

console.log(students);

//create username
function createusername(student){

    student.username=student.name.tolowercase().split(" ").map((name)=>
    {return name[0]}).join("");
    console.log(student)
}
// total marks
function totalmarks(marks){
    let sum=0
    for(let m of marks)
    {
        sum+=m
    }
    return sum
}
// calc percentage
let maxmarks=500
function calcpercentage(marks){
    let percentage=(marks/maxmarks)*100
    return percentage
}

// display students
function displaystudents(student){
    if(student.length!=0)
        {
        let eachstu=``;
        student.forEach(function(stu)
        {
            let tmarks=totalmarks(stu.marks)
            let per=calcpercentage(tmarks)
            let res=per>=40 ?'pass':'fail'
            eachstu+=`<tr>
                        <td>${stu.id}</td>
                        <td>${stu.name}</td>
                        <td>${stu.email}</td>
                        <td>${stu.gender}</td>
                        <td>${tmarks}</td>
                        <td>${res}</td>
                                
                     </tr>`
        })
        document.getElementById('display-data').innerHTML=eachstu;
    }
}
displaystudents(students);

//display student details

function studentdata(student)
{
    console.log(student);
    let tmarks=totalmarks(student.marks);
    let per=(calcpercentage(tmarks)).toFixed(0);
    let htmlTemplate=`<h2>${student.name}</h2>
                      <h2>arun@gmail.com</h2>
                      <h2>392</h2>
                      <h2>pass</h2>`
}
//login functionallity

let logInBtn=document.getElementById('log=in')
let usernameBox=document.getElementById('usn')
let passwordBox=document.getElementById('pw')
logInBtn.addEventListener('submit',function(e)
{
    e.preventDefault();
    let usn=usernameBox.value.tolowercase().trim();
    let pw=Number(passwordBox.value.trim());

    let student=students.find(function(stu){
        return stu.username==usn
    })

})

