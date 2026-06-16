function presentData(result){
    let object;
    const approved = document.getElementById(`approved`);
    let rejected = document.getElementById(`rejected`);
    let forApproval = document.getElementById(`for-approval`);
    forApproval.innerHTML = "";
    rejected.innerHTML = ""
    approved.innerHTML = "";

    for (object of result){
        if (!object.approve_status && !object.cancelled_status && !object.rejected_status ){
            let card = document.createElement('div');
            card.className =  "card my-3 rounded";
            card.innerHTML = `
                <div class="card-body">
                <h5 class="card-title">${object.blood_bank}</h5>
                <p class="card-text"><i class="bi bi-geo-alt" style="size:2em; color:red;"></i><i class="bi bi-truck" style="size:2em; color:red;"></i>${ object.blood_bank_address }</p>
                <p class="card-text"><small class="text-body-secondary">${object.timestamp}</small></p>
                <button type="button" class="btn btn-outline-danger reject" data-id="${object.id}" data-btn="reject"><i class="bi bi-x-circle-fill" style=" color:crimson;"></i> Reject</button>
                <button type="button" class="btn btn-outline-success approve" data-id="${object.id}" data-btn="approve"><i class="bi bi-check-circle-fill" style=" color: greenyellow;"></i>Approve</button>
                </div>
                <img src="${object.user_id_proof}" class="card-img-bottom img-fluid" alt="prescription image">
                `;
            forApproval.append(card);
        }else if (object.approve_status ){
            let card = document.createElement('div');
            card.className =  "card my-3 rounded";
            card.innerHTML = `<div class="card-body">
                <h5 class="card-title">${object.blood_bank}</h5>
                <p class="card-text"><i class="bi bi-geo-alt" style="size:2em; color:red;"></i><i class="bi bi-truck" style="size:2em; color:red;"></i>${ object.blood_bank_address }</p>
                <p class="card-text"><small class="text-body-secondary">${object.timestamp}</small></p>
                </div>
                <img src="${object.user_id_proof}" class="card-img-bottom img-fluid" alt="prescription image">`;
            approved.append(card);
        }else if (object.rejected_status){
            let card = document.createElement('div');
            card.className =  "card rounded";
            card.innerHTML = `<div class="card-body bg-danger">
                <h5 class="card-title">${object.blood_bank}</h5>
                <p class="card-text"><i class="bi bi-geo-alt" style="size:2em; color:red;"></i><i class="bi bi-truck" style="size:2em; color:red;"></i>${ object.blood_bank_address }</p>
                <p class="card-text"><small class="text-body-secondary">${object.timestamp}</small></p>
                </div>
                <img src="${object.user_id_proof}" class="card-img-bottom img-flui,d" alt="prescription image">`;
            rejected.append(card);
        }

    } 
}

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
            .then(function(result) {
                presentData(result);
                putApprovalOrRejection();
            });
        })
    })
}

function putApprovalOrRejection(){
    let approved = document.querySelectorAll(".approve");
    let rejected = document.querySelectorAll(".reject");

    approveOrReject(approved);
    approveOrReject(rejected);
}


document.addEventListener('DOMContentLoaded', event => {
    fetch("/approval", {
        method: "DATA", 
        body: JSON.stringify({})
    }) 
    .then(response => response.json())
    .then(function(result){
        presentData(result);
        putApprovalOrRejection();
    })
})

   
