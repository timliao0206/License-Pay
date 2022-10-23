
var curUser = ""

function setCuruser(username) {
	curUser = username;
}

if(document.getElementById("signinSubmit") != null) {
	document.getElementById("signinSubmit").addEventListener("click", (event) => {
		event.preventDefault();
		var userType = document.getElementById("signinUserType").value;
		var username = document.getElementById("signinUsername").value;
		var password = document.getElementById("signinPassword").value;
		
		fetch(`http://10.107.7.8:3000/login?username=${username}&psw=${password}&isPayer=${(Boolean)(userType == "payer")}`)
		.then((res) => {
			return res.json();
		})
		.then((data) => {
			console.log(data)
			if(data.success == true) {
				if(userType == "payer") {
					console.log("TEST")
					document.getElementById("signedInUser").innerHTML = username;
					window.location.replace("./payer.html");
				}
				else {
					window.location.replace("./receiver.html");
				}
			}
		})
		.catch((err) => {
			console.log(err);
		})
	})
}

if(document.getElementById("signupSubmit") != null) {
	document.getElementById("signupSubmit").addEventListener("click", (event) => {
		event.preventDefault();
		var userType = document.getElementById("signupUserType").value;
		var phone_number = document.getElementById("phone_number").value;
		var username = document.getElementById("signupUsername").value;
		var password = document.getElementById("signupPassword").value;
		var license_plate = document.getElementById("license_plate").value;

		console.log("A signup request : ", userType, phone_number, username, password, license_plate)
		fetch(`http://10.107.7.8:3000/payer?username=${username}&\
			psw=${password}&license_plate=${license_plate}&\
			phone_number=${phone_number}&balance=0`, { method: 'POST'})
		.then((res) => {
			return res.json();
		})
		.then((data) => {
			console.log(data)
		})
		.catch((err) => {
			console.log(err);
		})
	})

}

function buildTable(data) {
	var table = document.getElementById('myTable');
	table.innerHTML = "";
	for (var i = 0; i < data.length; i++) {
		var row = `<tr>
						<td>${data[i].payer_username}</td>
						<td>${data[i].receiver_username}</td>
						<td>${data[i].time}</td>
						<td>${data[i].money_diff}</td>
						<td>${data[i].permission}</td>
				  </tr>`;
		table.innerHTML += row;
	}
}

if(document.getElementById("refreshButton") != null) {
	document.getElementById("refreshButton").addEventListener("click", (event) => {
		event.preventDefault();
		console.log("test")

		console.log(curUser)

		fetch(`http://10.107.7.8:3000/transaction?payer=${curUser}`)
		.then((res) => {
			return res.json();
		})
		.then((data) => {
			console.log(data)
		})
		.catch((err) => {
			console.log(err);
		})
	})
}