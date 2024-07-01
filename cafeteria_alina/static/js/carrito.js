/**
 * Generamos dinámicamente el carro, pero no se guarda nada hasta q se confirme
 */

var carro = []

/* Crea un pedido */
function createBox(producto, tipo, cantidad, precio, total) {
    let item = document.createElement('div');
    item.className = 'item';

    //Crear más bonita la caja
    var i;

    /* Producto */
    i = document.createElement('div');
    i.setAttribute('name', 'producto');
    i.setAttribute('value', producto.selectedOptions[0].value);
    i.textContent = producto.selectedOptions[0].textContent;
    item.appendChild(i);

    /* Tipo producto */
    i = document.createElement('div');
    i.setAttribute('name', 'tipo');
    i.setAttribute('value', tipo.selectedOptions[0].value);
    let kind = document.createElement('label');
    kind.textContent = tipo.selectedOptions[0].textContent;
    i.appendChild(kind);
    item.appendChild(i);

    /* Cantidad */
    i = document.createElement('div');
    i.setAttribute('name', 'cantidad');
    i.setAttribute('value', cantidad.value);
    let quant = document.createElement('label');
    quant.textContent = cantidad.value;
    i.appendChild(quant);
    item.appendChild(i);

    /* Precio del producto */
    i = document.createElement('div');
    i.setAttribute('name', 'precio');
    i.setAttribute('value', precio.id);
    let price = document.createElement('label');
    price.textContent = `\$${precio.precio}`;
    i.appendChild(price);
    item.appendChild(i);

    /* Subtotal */
    i = document.createElement('div');
    i.setAttribute('name', 'subtotal');
    let s = parseFloat(precio.precio) * parseInt(cantidad.value);
    i.setAttribute('value', s);
    let subtotal = document.createElement('label');
    subtotal.textContent = `\$${s}`;
    i.appendChild(subtotal);
    item.appendChild(i);

    total.value = parseFloat(total.value) + s;

    return item;
}

/**
 * Actualiza los tipos disponibles según el producto
 */
function changeTipo(producto, tipo) {
    let id_producto = producto.value;

    let i = tipo.options.length;
    while (i > 0) tipo.remove(--i)

    fetch(`tipos-por-producto/${id_producto}`)
        // Si la promesa es buena, lo hacemos json
        .then( response => {
            return response.json();
        })
        // Leemos el json como data
        .then( data => {
            data.forEach(rowTipo => {
                var option = document.createElement('option');
                option.value = rowTipo.id_tipo_producto;
                option.textContent = rowTipo.tipo_producto;
                tipo.appendChild(option);
            });
        })
        .catch( error => console.error('Error al buscar tipos: ' + error));   
}

/**
 * 
 * @param {id_producto} id_producto el producto que viene con categoria
 * @param {id_tipo_producto} id_tipo_producto con el cual se relaciono el precio
 */
async function getPrice(id_producto, id_tipo_producto){
    try {
        const response = await fetch(`get-precio/${id_producto}&${id_tipo_producto}`);
        return await response.json();
    } catch (error) {
        return console.error('Error al buscar tipos: ' + error);
    }
}

/**
 * Envia las compras agregadas anteriormente al cart.
 * Crea un JSON con la información colectada por el cart
 */
function sendCart(){
    //Convertir a JSON
    let cartData = carro.map(item => {
        return {
            cantidad: item.children['cantidad'].getAttribute('value'),  //cantidad
            precio: item.children['precio'].getAttribute('value'),      //precio
            subtotal: item.children['subtotal'].getAttribute('value')   //subtotal
        };
    });

    shop = {
        cart: cartData,
        total: total.value
    }

    //Enviar JSON
    fetch('nueva-venta', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(shop)
    })
    .then(response => {
        return response.text().then(text => {
            // return JSON.parse(text); // Todos coludos o todos rabones
            return text;
        });
    })
    .then(html => {
        // Por JSON
        // if (data.redirect) {
        //     // window.location.href = data.redirect;
        // } else {
        //     console.log('Success:', data);
        // }
        document.open();
        document.write(html);
        document.close();

    })
    .catch((error) => {
        console.log('Error:', error);
    });
}

// Main
window.onload = function (){
    let add_product = document.getElementById('agregar-carro');
    let cart = document.getElementById('cart');

    //Informacion del producto
    let producto = document.getElementById('producto');
    let tipo = document.getElementById('tipo');
    let cantidad = document.getElementById('cantidad');
    let total = document.getElementById('total');

    let submit = document.getElementById('comprar')

    producto.value = '';
    tipo.value = '';
    cantidad.value = '';
    total.value = '0';
    
    add_product.addEventListener('click', async function(){
        if (producto.value === '' || tipo.value === '' || cantidad.value === ''){
            alert('Rellena los campos de PRODUCTO, TIPO PRODUCTO Y CANTIDAD');
            return;
        }
        
        let precio;
        // Buscamos el precio de categoria-producto, tipo
        precio = await getPrice(producto.value, tipo.value);
    
        for (let item of carro){
            let id_precio = item.children['precio'].getAttribute('value');
            let q_value = item.children['cantidad'].getAttribute('value');
            if ( id_precio == precio.id){
                let cantidad_nueva = parseInt(cantidad.value) + parseInt(q_value);
                let subtotal_nuevo = parseFloat(precio.precio * cantidad_nueva);
                item.children['cantidad'].setAttribute('value', cantidad_nueva);
                /* No puede ser [0] */
                item.children['cantidad'].children[0].textContent = cantidad_nueva;
                item.children['subtotal'].setAttribute('value', subtotal_nuevo);
                item.children['subtotal'].children[0].textContent = `\$${subtotal_nuevo}`;
                total.value = parseFloat(total.value) + subtotal_nuevo;
                return;
            }
        }
        
        /* Si no existe creamos la caja */
        let nueva_transaccion = createBox(producto, tipo, cantidad, precio, total);
        carro.push(nueva_transaccion);
        cart.append(nueva_transaccion);

        producto.value = '';
        tipo.value = '';
        cantidad.value = '';
    });

    producto.addEventListener('change', function(){
        changeTipo(producto, tipo);
    });

    submit.addEventListener('click', function(){
        if (carro.length === 0)
            return;
        sendCart();
    });
}
