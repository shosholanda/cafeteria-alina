/**
 * Cambia el id del producto dinámicamente
 */
function changeID() {
    var producto = document.getElementById('producto');
    var url = document.getElementById('url');

    // Obtenemos la ruta renderizada por jinja 
    // de
    // {{ url_for('precios.create_precio', id='') }}
    // a
    // precios/agregar-precio/
    let baseUrl = url.getAttribute('data-url-base');

    // Concatenamos el producto id
    let newUrl = baseUrl + producto.value;
    url.setAttribute("href", newUrl);
}

document.addEventListener('DOMContentLoaded', function() {
    // Puros trucos.
    changeID();

    document.getElementById('producto').addEventListener('change', changeID);
});

/* The fuck is this sort */
window.onload = function(){
    const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;

    const comparer = (idx, asc) => (a, b) => ((v1, v2) => 
        v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
        )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

    // do the work...
    document.querySelectorAll('th').forEach(th => th.addEventListener('click', (() => {
        const table = th.closest('table');
        Array.from(table.querySelectorAll('tr:nth-child(n+2)'))
            .sort(comparer(Array.from(th.parentNode.children).indexOf(th), this.asc = !this.asc))
            .forEach(tr => table.appendChild(tr) );
    })));
}