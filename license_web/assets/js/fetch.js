
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
					localStorage.setItem("username", username)
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
	for (var i = 0, j = 0; i < data.length; i++) {
		var obj = JSON.parse(data[i])
		if(obj.permission) {
			continue;
		}
		console.log(obj.money_diff)
		var row = `<tr id = row${j ++}>
						<td id = "row${i}payer">${obj.payer_username}</td>
						<td id = "row${i}receiver">${obj.receiver_username}</td>
						<td id = "row${i}time">${obj.time}</td>
						<td id = "row${i}money>${obj.money_diff}</td>
						<td id = "row${i}description">${obj.description}</td>
						<td><button value = ${i} onclick="handleModify(${i}, 1)">Accept</button></td>
						<td><button value = ${i} onclick="handleModify(${i}, 0)">Reject</button></td>
				  </tr>`;
		table.innerHTML += row;
	}
}

if(document.getElementById("refreshButton") != null) {
	document.getElementById("refreshButton").addEventListener("click", (event) => {
		event.preventDefault();
		
		var curUser = localStorage.getItem("username");

		fetch(`http://10.107.7.8:3000/transaction?payer_username=${curUser}`)
		.then((res) => {
			return res.json();
		})
		.then((data) => {
			console.log(data)
			buildTable(data)
		})
		.catch((err) => {
			console.log(err);
		})
	})
}

if(document.getElementById("signedInUser") != null) {
	document.getElementById("signedInUser").innerHTML = localStorage.getItem("username")
}

function handleModify(ind, state) {
	var payer = document.getElementById(`row${ind}payer`).innerHTML;
	var receiver = document.getElementById(`row${ind}receiver`).innerHTML;
	var time = document.getElementById(`row${ind}time`).innerHTML;
	console.log(payer, receiver, time, state)
	fetch(`http://10.107.7.8:3000/decide?payer_username=${payer}&receiver_username=${receiver}&time=${time}&permission=${state}`, {method: "POST"})
	.catch((err) => {
		console.log(err);
	})
}

if(document.getElementById("balance") != null) {
	fetch(`http://10.107.7.8:3000/payer?username=${localStorage.getItem("username")}`)
	.then((res) => {
		return res.json();
	})
	.then((data) => {
		console.log(data)
		document.getElementById("balance").innerHTML = data.balance;
	})
	.catch((err) => {
		console.log(err)
	})
}