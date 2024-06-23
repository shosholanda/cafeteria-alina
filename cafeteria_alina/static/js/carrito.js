/**
 * Generamos dinámicamente el carro, pero no se guarda nada hasta q se confirme
 */

var carro = []

/* Crea un pedido */
function createBox(producto, tipo, cantidad, total) {
    let item = document.createElement('div');
    item.className = 'item';

    //Crear más bonita la caja
    var i;

    /* Producto */
    i = document.createElement('div');
    i.setAttribute('name', 'producto');
    i.setAttribute('value', tipo.selectedOptions[0].getAttribute('id_producto'));
    let nombre = document.createElement('label');
    nombre.textContent = producto.selectedOptions[0].textContent;
    i.appendChild(nombre);
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
    i.setAttribute('value', tipo.selectedOptions[0].getAttribute('precio'));
    let price = document.createElement('label');
    price.textContent = `\$${tipo.selectedOptions[0].getAttribute('precio')}`;
    i.appendChild(price);
    item.appendChild(i);

    /* Subtotal */
    i = document.createElement('div');
    i.setAttribute('name', 'subtotal');
    let s = parseFloat(tipo.selectedOptions[0].getAttribute('precio')) * parseInt(cantidad.value);
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
                option.value = rowTipo.id_tipo;
                option.textContent = rowTipo.tipo;
                option.setAttribute('precio', rowTipo.precio);
                option.setAttribute('id_producto', rowTipo.id_producto);
                tipo.appendChild(option);
            });
        })
        .catch( error => console.error('Error al buscar tipos: ' + error));   
}

function sendCart(){
    //Convertir a JSON
    let cartData = carro.map(item => {
        return {
            producto: item.children['producto'].getAttribute('value'),  //id_producto
            tipo: item.children['tipo'].getAttribute('value'),          //id_tipo
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

// Call the addBoxes function when the page loads
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
    
    add_product.addEventListener('click', function(){
        if (producto.value === '' || tipo.value === '' || cantidad.value === ''){
                alert('Rellena los campos de PRODUCTO, TIPO PRODUCTO Y CANTIDAD');
                return;
        }
    
        for (let item of carro){
            let p_value = item.children['producto'].getAttribute('value');
            let t_value = item.children['tipo'].getAttribute('value');
            let c_value = item.children['cantidad'].getAttribute('value');
            let pr_value = item.children['precio'].getAttribute('value');
            if ( p_value === producto.value && t_value === tipo.value){
                let cantidad_nueva = parseInt(cantidad.value) + parseInt(c_value);
                let subtotal_nuevo = parseFloat(pr_value * cantidad_nueva);
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
        let nueva_transaccion = createBox(producto, tipo, cantidad, total);
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
