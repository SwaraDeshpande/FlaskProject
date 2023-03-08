const updateCompany = (name) => {
    fetch('/company', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('company').innerHTML = data.name;
    });
}

document.getElementById("updateBtn").addEventListener("click", function(){
    let newName = document.getElementById("newName").value;
    updateCompany(newName);
});

fetch('/company')
  .then(response => response.json())
  .then(data => {
    document.getElementById('company').innerHTML = data.name;
  });
