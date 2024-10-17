let formEl=document.getElementById('task-form')
let inputEl=document.getElementById('task-el')
 

formEl.addEventListener('submit',function(e){
    e.preventDefault()
    create()
    displaytask()
})

let tasklist=localStorage.getItem('tasks')?JSON.parse(localStorage.getItem('tasks')):[]

function create()
{
    let task=inputEl.value.trim();
    let taskobj={taskval:task,iscompleted:false}

    tasklist.unshift(taskobj);
    localStorage.setItem('tasks',JSON.stringify(tasklist));
    console.log(tasklist);
    inputEl.value='';
}

function displaytask()
{
    if(tasklist.length!=0)
    {
        let eachtask=``;
        tasklist.forEach((task,index)=> 
            {
            eachtask+=`<li class="list-group-item mt-3">
                        <span>${task.taskval}</span>
                        <button class="float-end ms-2 abc" >
                            <i class="bi bi-trash"  onclick="deleteTask (${index})"></i>
                        </button>
                        <button class="float-end abc">
                            <i class="bi bi-pen" onclick="updateTask (${index})"></i>
                        </button>
                    </li>`
        });
        document.getElementById('task-group').innerHTML=eachtask
    }
}
displaytask()


//delete task

function deleteTask(index)
{
    tasklist.splice(index,1);
    localStorage.setItem('tasks',JSON.stringify(tasklist));
    displaytask();
}



//updatetask

function updateTask(index){
    inputEl.value=tasklist[index].taskval;
    tasklist.splice(index,1);
    localStorage.setItem('tasks',JSON.stringify(tasklist));
    displaytask();
    
}