if (user != "AnonymousUser") {
	document.getElementById("user-info").innerHTML = "";
}
//chowa pola inputu jezeli jesteś zalogowany

var form = document.getElementById("form");

form.addEventListener("submit", function (eventObject) {
	eventObject.preventDefault(); //Ta metoda zapobiega domyślnemu zachowaniu przeglądarki, które polega na przeładowaniu strony lub wysłaniu żądania HTTP w przypadku zatwierdzenia formularza

	var userFormData = {
		//żeby na pewno były null by default
		name: null,
		email: null,
	};

	if (user == "AnonymousUser") {
		//jak nie jesteś zalogowany to pobiera z formularza
		userFormData.name = form.name.value;
		userFormData.email = form.name.email;
	}

	//wysyłamy na backend:
	var url = "/process_order/";
	fetch(url, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"X-CSRFToken": csrftoken,
		},
		body: JSON.stringify({ form: userFormData }),
	})
		.then((response) => response.json())
		.then((data) => {
			console.log("Success:", data);
			alert("ZAKONCZONA TRANZAKCJA");
			window.location.href = "/";
		})
		.catch((error) => console.error(error));

	console.log("form submitted");
	//console.log("CSRF token:", csrftoken);
});
