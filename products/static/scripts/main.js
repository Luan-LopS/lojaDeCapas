document.addEventListener("DOMContentLoaded", function () {
    fetch("dados/dados.json")
        .then(response => response.json())
        .then(products => {
            const productList = document.getElementById("product-list");

            products.forEach(product => {
                const productCard = `
                    <div class="col-md-4">
                        <div class="card">
                            <img src="${product.image}" class="card-img-top" alt="${product.name}">
                            <div class="card-body">
                                <h5 class="card-title">${product.name}</h5>
                                <p class="fw-bold">R$ ${product.price.toFixed(2)}</p>
                                <p class=''>${product.description}</p>
                                <a href="whaqt" class="btn btn-danger w-100"></a>
                            </div>
                        </div>
                    </div>
                `;
                productList.innerHTML += productCard;
            });
        })
        .catch(error => console.error("Erro ao carregar os produtos:", error));

    // Carregar Header
    fetch("layout/header.html")
        .then(response => response.text())
        .then(data => {
            document.getElementById("header").innerHTML = data;
        })
        .catch(error => console.error("Erro ao carregar o header:", error));

    // Carregar Footer
    fetch("layout/footer.html")
        .then(response => response.text())
        .then(data => {
            document.getElementById("footer").innerHTML = data;
        })
        .catch(error => console.error("Erro ao carregar o footer:", error));

});



