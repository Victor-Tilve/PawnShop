// Completa la tabla de la información de todos los abonos en el sistema. Es usada en el home de abonos
$( document ).ready(function() {
  // console.log("Dentro de documento")
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:8000/adicionales/get/ajax/validate/tabla_adicionales",
    success: function (response) {
      let tabla = response["_adicionales_informacion"];
      $("#id_tabla_prestamo").html("");
      //$("#id_codigo_prestamo").html( "<p>All new content. <em>You bet!</em></p>" );
      for (let i = 0; i < tabla.length; i++) {
        $("#id_tabla_prestamo").append(tabla[i]);
      }
  
    },
    error: function (response) {
      console.log("Hubo un error");
    },
  });
});
