function cobrar_hoy() {
  var buscar_fecha = $("#id_buscar_fecha");
  // console.log("Esperando button")
  
  buscar_fecha.on('click', function(event) {
    // console.log("Dentro de button");
    var fecha_hoy= $('#id_fecha_hoy').val();
    event.preventDefault();
    
      $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/loans/get/ajax/validate/tabla_cobrar_hoy",
        data: { fecha_hoy: fecha_hoy },
        success: function (response) {
          let tabla = response["table_loan_date"];
          // console.log(tabla)
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
};
//Call it...
cobrar_hoy();