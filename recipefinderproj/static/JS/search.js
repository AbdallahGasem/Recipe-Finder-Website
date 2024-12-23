document.addEventListener('DOMContentLoaded', function() {
    const option1 = document.getElementById('option1');
    const option2 = document.getElementById('option2');
    const input = document.getElementById('search-input');
    const dis = document.getElementById('display');
    let rdata = JSON.parse('{{ qs_json|escapejs }}'.replace(/&quot;/g, '"'));

    option1.addEventListener('click', function() {
        if (this.checked) {
            handleSearch();
        }
    });

    option2.addEventListener('click', function() {
        if (this.checked) {
            handleSearch();
        }
    });

    function debounce(func, delay) {
        let timer;
        return function() {
            const context = this;
            const args = arguments;
            clearTimeout(timer);
            timer = setTimeout(() => {
                func.apply(context, args);
            }, delay);
        };
    }

    function handleSearch() {
        input.addEventListener('input', debounce(function(e) {
            let query = e.target.value.trim().toLowerCase(); 
            dis.innerHTML = ""; 
            let filteredarr = [];

            if (option1.checked) {
                filteredarr = rdata.filter(recipe => 
                    recipe.name.toLowerCase().includes(query)
                );
            } else if (option2.checked) {
                filteredarr = rdata.filter(recipe => 
                    recipe.ingredients.toLowerCase().includes(query)
                );
            }

            console.log(filteredarr);

            let html = "";

            if (filteredarr.length > 0) {
                filteredarr.forEach(recipe => {
                    html += `
                    <div class="recipe">
                        <h2><a href="/display_recipe/${recipe.id}">${recipe.name}</a></h2>
                        ${recipe.image ? `<a href="/display_recipe/${recipe.id}"><img src="${recipe.image}" alt="${recipe.name}"></a>` : ''}
                        <form method="POST" action="/add_to_fav/${recipe.id}/">
                            {% csrf_token %}
                            <button class="sub" type="submit">ADD TO FAV</button>
                        </form>
                    </div>
                    `;
                });
            } else {
                html = "<b>No Results Found...</b>";
            }
            dis.innerHTML = html;
        }, 50));
    }

    // Initialize search with the default checked option
    handleSearch();
});
