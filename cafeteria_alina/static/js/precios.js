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