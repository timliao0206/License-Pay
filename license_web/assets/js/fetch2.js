let form = new FormData();
if(document.getElementById("submitButton") != null) {
	document.getElementById("submitButton").addEventListener("click", (event) => {

		event.preventDefault();
		// var file = document.getElementById("carpic");
		// var t = encodeImageFileAsURL(file)
		// console.log(t)
		// var amount = document.getElementById("moneyReq").value;
		fetch('http://10.107.7.8:3000/license_plate', {
		  method: 'POST',
		  body: form
		})
	})
}


const fileUploader = document.querySelector('#file-uploader');

fileUploader.addEventListener('change', (e) => {
  	console.log(e.target.files); // get file object
	form.append("photo", e.target.files[0])

	// fetchAPI
});
