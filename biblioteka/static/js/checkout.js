var form = document.getElementById("form");

form.addEventListener("submit", function (eventObject) {
	eventObject.preventDefault(); //Ta metoda zapobiega domyślnemu zachowaniu przeglądarki, które polega na przeładowaniu strony lub wysłaniu żądania HTTP w przypadku zatwierdzenia formularza

	//wysyłamy na backend:
	var url = "/process_order/";
	fetch(url, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"X-CSRFToken": csrftoken,
		},
	})
		.then((response) => response.json())
		.then((data) => {
			console.log("Success:", data);
			Swal.fire({
				title: "Sukces!",
				html:
					"Możesz odebrać książki w bibliotece :)<br> ID wypożyczenia: " +
					data.transaction_id,
				icon: "success",
				confirmButtonText: "Super",
			}).then((result) => {
				if (result.isConfirmed) {
					window.location.href = "/";
				}
			});
		})
		.catch((error) => console.error(error));

	console.log("form submitted");
	//console.log("CSRF token:", csrftoken);
});
