function presentData(result) {
    let object = "";
    for (object of result) {
        let card = document.createElement('div');
        card.className = "card";
        card.innerHTML = f`<div class="card-body">
            <h5 class="card-title">${result.blood_bank}</h5>
            <p class="card-text"><i class="bi bi-geo-alt" style="size:2em; color:red;"></i><i class="bi bi-truck" style="size:2em; color:red;"></i>${result.blood_bank_address}</p>
            <p class="card-text"><small class="text-body-secondary">${result.timestamp}</small></p>
            <button type="button" class="btn btn-outline-danger" id="reject-btn data-id=${result.id}"><i class="bi bi-x-circle-fill" style=" color:crimson;"></i> Reject</button>
            <button type="button" class="btn btn-outline-success" id="approve-btn data-id=${result.id}"><i class="bi bi-check-circle-fill" style=" color: greenyellow;"></i>Approve</button>
            </div><img src="${result.prescription_img}" class="card-img-bottom" alt="prescription image"></img>`;
        let parentDiv = document.getElementById("parent-card");
        parentDiv.appendChild(card);

    }
}
