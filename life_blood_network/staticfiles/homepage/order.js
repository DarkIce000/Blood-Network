function cancel(objID){
    fetch("/my-orders", {
        method: "PUT", 
        body: JSON.stringify({
            id : objID,  
            cancel_status: true
        })

    })
    .then((r) => {
        location.reload(true)
    })
}

document.addEventListener('DOMContentLoaded', () => {
    let buttons = document.querySelectorAll(".cancel-btn");
    buttons.forEach((element) => {
        element.addEventListener('click', (event) => {
            const objID = event.target.dataset.id;
            console.log(objID);
            cancel(objID);
        })
    })
})
