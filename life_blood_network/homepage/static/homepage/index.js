let bloodBankDetails = document.getElementById('listTable');
bloodBankDetails.addEventListener('click', function (event){
    let link = event.target.dataset.listid;
    if (!link) return;
    window.open(link, '_self');
});


