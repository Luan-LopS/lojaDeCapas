document.addEventListener("DOMContentLoaded", function () {
    const params = new URLSearchParams(window.location.search);
    const productId = params.get("id");

    fetch("scritp/dados.json")
        .then(response => response.json())
        .then(products => {
            const product = products.find(p => p.id == productId);

            if (product) {
                document.getElementById("product-name").textContent = product.name;
                document.getElementById("product-description").textContent = product.description;
                document.getElementById("product-price").textContent = `R$ ${product.price.toFixed(2)}`;
                document.getElementById("product-image").src = product.image;
            } else {
                document.querySelector(".container").innerHTML = "<h2 class='text-center'>Produto não encontrado!</h2>";
            }
        })
        .catch(error => console.error("Erro ao carregar os detalhes do produto:", error));
});
