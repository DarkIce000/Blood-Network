function approveOrReject(arrayNode){
    arrayNode.forEach((element) => {
        element.addEventListener('click', function(event){
            let objectID = event.target.dataset.id;
            let objectBTN = event.target.dataset.btn;
            console.log(objectID);
            fetch("/approval", {
                method: "PUT",
                body: JSON.stringify({
                    id: objectID, 
                    status: objectBTN
                })
            })
            .then(response => response.json())
            .then(result => location.reload(true))
        })
    })
}

function presentData(result){
    let object;
    for (object of result){
        if (!object.approve_status && !object.cancelled_status && !object.rejected_status ){
            let forApproval = document.getElementById("for-approval");
            let card = document.createElement('div');
            card.className =  "card";
            card.innerHTML = `<div class="card-body">
                <h5 class="card-title">${object.blood_bank}</h5>
                <p class="card-text"><i class="bi bi-geo-alt" style="size:2em; color:red;"></i><i class="bi bi-truck" style="size:2em; color:red;"></i>${ object.blood_bank_address }</p>
                <p class="card-text"><small class="text-body-secondary">${object.timestamp}</small></p>
                <button type="button" class="btn btn-outline-danger reject" data-id="${object.id}" data-btn="reject"><i class="bi bi-x-circle-fill" style=" color:crimson;"></i> Reject</button>
                <button type="button" class="btn btn-outline-success approve" data-id="${object.id}" data-btn="approve"><i class="bi bi-check-circle-fill" style=" color: greenyellow;"></i>Approve</button>
                </div>
                <img src="${object.prescription_img}" class="card-img-bottom" alt="prescription image">`;
            forApproval.append(card);
        }else if (object.approve_status ){
            let card = document.createElement('div');
            card.className =  "card";
            card.innerHTML = `<div class="card-body">
                <h5 class="card-title">${object.blood_bank}</h5>
                <p class="card-text"><i class="bi bi-geo-alt" style="size:2em; color:red;"></i><i class="bi bi-truck" style="size:2em; color:red;"></i>${ object.blood_bank_address }</p>
                <p class="card-text"><small class="text-body-secondary">${object.timestamp}</small></p>
                </div>
                <img src="${object.prescription_img}" class="card-img-bottom" alt="prescription image">`;
            let approved = document.getElementById("approved");
            approved.append(card);
        }else if (object.rejected_status){
            let card = document.createElement('div');
            card.className =  "card";
            card.innerHTML = `<div class="card-body">
                <h5 class="card-title">${object.blood_bank}</h5>
                <p class="card-text"><i class="bi bi-geo-alt" style="size:2em; color:red;"></i><i class="bi bi-truck" style="size:2em; color:red;"></i>${ object.blood_bank_address }</p>
                <p class="card-text"><small class="text-body-secondary">${object.timestamp}</small></p>
                </div>
                <img src="${object.prescription_img}" class="card-img-bottom" alt="prescription image">`;
            let rejected = document.getElementById("rejected");
            rejected.append(card);
        }

    }

    // let approve = document.querySelectorAll(".approve");
    // let rejected = document.querySelectorAll(".reject");

    // approveOrReject(approve);
    // approveOrReject(rejected);

    // approve.forEach((element) => {
    //     element.addEventListener('click', function(event){
    //         let objectID = event.target.dataset.id;
    //         console.log(objectID);
    //         fetch("/approval", {
    //             method: "PUT",
    //             body: JSON.stringify({
    //                 id: objectID, 
    //                 approveStatus: true
    //             })
    //         })
    //         .then(response => response.json())
    //         .then(result => console.log(result))
    //     })
    // })

    // rejected.forEach((element) => {
    //     element.addEventListener('click', function(event){
    //         let objectID = event.target.dataset.id;
    //         console.log(objectID);
    //         fetch("/approval", {
    //             method: "PUT", 
    //             body: JSON.stringify({
    //                 id: objectID, 
    //                 rejectedStatus: true
    //             })
    //         })
    //         .then(response => response.json())
    //         .then(result => console.log(result))
    //     })
    // })
 
}

function putApprovalorRejection(){
    
    let approve = document.queryselectorall(".approve");
    let rejected = document.queryselectorall(".reject");

    approveOrReject(approve);
    approveOrReject(rejected);
}

document.addEventListener('DOMContentLoaded', event => {
    fetch("/approval", {
        method: "DATA", 
        body: JSON.stringify({})
    }) 
    .then(response => response.json())
    .then(function(result){
        console.log(result);
        presentData(result);
    })
})
   
