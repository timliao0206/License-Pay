fetch('http://10.107.7.8/')
    .then((response) => {
        return response.json();
    })
    .then( (response) => {
        console.log(response);
    })
    .catch((error) => {
        console.log(`Error: ${error}`);
    })


var jwt = localStorage.getItem("jwt");
if (jwt != null) {
    window.location.href = './index.html'
}

function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;








}    