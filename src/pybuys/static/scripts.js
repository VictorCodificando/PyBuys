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
  constructor(id_elemento, inicial, maximo) {
    this.id_elemento = id_elemento;
    this.valor = inicial;
    this.maximo = maximo;
  }

  modificarCantidad(cantidadASumar) {
    cantidadASumar = parseInt(cantidadASumar);
    if (this.valor + cantidadASumar >= 0 && this.valor + cantidadASumar <= this.maximo) {
      this.valor += cantidadASumar;
      document.getElementById(this.id_elemento).textContent = this.valor;
    }
  }
}
class ListaHovered {
  constructor(id_elemento, destacado, normal, especificacion = "*") {

    // destacado y normal son arrays de clases
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
