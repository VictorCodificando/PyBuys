function mostrarNotificacion(message) {
  // Verificar si el navegador soporta la API de Notificaciones
  if ("Notification" in window) {
    // Pedir permiso al usuario para mostrar notificaciones
    Notification.requestPermission().then(function (permission) {
      if (permission === "granted") {
        // Crear una nueva notificación
        var notification = new Notification(message);
        // Mostrar la notificación
        setTimeout(notification.close.bind(notification), 5000);
      }
    });
  }
}
class Contador {
  constructor(id_elemento, inicial, maximo, minimo = 0) {
    this.id_elemento = id_elemento;
    this.valor = inicial;
    this.maximo = maximo;
    this.minimo = minimo;
  }

  modificarCantidad(cantidadASumar) {
    cantidadASumar = parseInt(cantidadASumar);
    const elemento = document.getElementById(this.id_elemento);
    let valorActual = parseInt(elemento.textContent || elemento.value);
    let puedeSumar = (valorActual + cantidadASumar >= this.minimo && cantidadASumar<0) || (valorActual + cantidadASumar <= this.maximo && cantidadASumar>0);
    if (puedeSumar) {
      this.valor += cantidadASumar;
      if (elemento.tagName === 'INPUT') {
        elemento.value = this.valor;
      } else {
        elemento.textContent = this.valor;
      }
    }
  }  
}
class ListaHovered {
  constructor(id_elemento, destacado, normal, especificacion = "*") {

    // destacado se agrega al elemento cuando el mouse entra
    // normal se agrega al elemento cuando el mouse sale
    // id_elemento es el id del elemento que contiene los elementos a los que se les agregará el hover
    document.addEventListener('DOMContentLoaded', function () {
      const lista = document.getElementById(id_elemento);
      const elementos = lista.querySelectorAll(especificacion);
      elementos.forEach(elemento => {
        elemento.addEventListener('mouseenter', function () {
          destacado.forEach(clase => {
            this.classList.add(clase);
          });
          normal.forEach(clase => {
            this.classList.remove(clase);
          });
        });

        elemento.addEventListener('mouseleave', function () {
          destacado.forEach(clase => {
            this.classList.remove(clase);
          });
          normal.forEach(clase => {
            this.classList.add(clase);
          });
        });
      });
    });
  }

}
