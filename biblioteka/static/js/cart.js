var updateBtns = document.getElementsByClassName("update-cart"); //Ta linia kodu pobiera wszystkie elementy HTML, które posiadają klasę "update-cart" i zapisuje je do zmiennej     updateBtns. Metoda getElementsByClassName() zwraca listę elementów pasujących do określonej klasy.

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener("click", function () {
		var productId = this.dataset.product;
		var action = this.dataset.action;
		console.log("productId:", productId, "Action:", action);

		if (user == "AnonymousUser") {
			console.log("nie zalogowany");
			addCookieItem(productId, action);
		} else {
			updateUserOrder(productId, action);
		}
	});
}
//iteruje przez wszystkie elementy, które zostały znalezione z klasą "update-cart". Każdy znaleziony element jest przechowywany w tablicy updateBtns.
//Dodaje ona zdarzenie "click" do każdego z tych elementów. Oznacza to, że kod wewnątrz funkcji anonimowej zostanie wykonany po kliknięciu na każdy element z klasą "update-cart".
//var productID = this.dataset.product;: Wewnątrz funkcji anonimowej, ta linia kodu pobiera wartość atrybutu data-product z elementu, który został kliknięty (this wskazuje na kliknięty element). Wartość ta jest przechowywana w zmiennej productID.
//var action = this.dataset.action;:  jak powyżej, ta linia kodu pobiera wartość atrybutu data-action z klikniętego elementu i zapisuje ją w zmiennej action.

function updateUserOrder(productId, action) {
	console.log("zalogowany, lecą dane");
	var url = "/update_item/";

	fetch(url, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"X-CSRFToken": csrftoken,
		},
		body: JSON.stringify({ productId: productId, action: action }),
	})
		.then((response) => {
			return response.json();
		})
		/* (response) => { return response.json(); } to funkcja zwrotna (callback), która przetwarza odpowiedź z serwera.
            response jest odpowiedzią zwróconą przez serwer.
            response.json() jest metodą JavaScript używaną do parsowania odpowiedzi z serwera w formacie JSON. Odpowiedź serwera jest przekształcana z formatu JSON na obiekt JavaScriptu.*/
		.then((data) => {
			console.log("data: ", data);
			location.reload();
		});
}
/* 
jest odpowiedzialna za wysłanie żądania do serwera, zaktualizowanie danych zamówienia i ponowne załadowanie strony
Definiuje zmienną url zawierającą adres docelowy, do którego zostanie wysłane żądanie POST.
Wywołuje funkcję fetch, która wysyła żądanie POST pod adres url. Zawiera ono informacje o produkcie (productId) oraz akcji (action), które są przekazane jako dane w formacie JSON.
method: "POST" - definiuje, że to jest żądanie typu POST.
headers - zawiera informacje nagłówkowe, w tym typ treści (JSON) oraz CSRF Token (X-CSRFToken), który jest wymagany w wielu aplikacjach Django w celu zapobieżenia atakom CSRF.
body - zawiera dane żądania w formacie JSON, reprezentujące productId i action. 
*/
