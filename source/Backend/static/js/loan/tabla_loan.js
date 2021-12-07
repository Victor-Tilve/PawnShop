$( document ).ready(function() {
  console.log("Dentro de documento")
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:8000/loans/get/ajax/validate/tabla",
    success: function (response) {
      let tabla = response["_prestamo_imformacion"];
      $("#id_tabla_prestamo").html("");
      for (let i = 0; i < tabla.length; i++) {
        $("#id_tabla_prestamo").append(tabla[i]);
      }
  
    },
    error: function (response) {
      console.log("Hubo un error");
    },
  });
});
