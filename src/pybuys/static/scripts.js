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
