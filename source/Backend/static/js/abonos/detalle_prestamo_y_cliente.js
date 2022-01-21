$(document).ready(function (){
    var codigo_prestamo = $("#id_codigo_prestamo").text();
    // console.log("El codigo es:" + codigo_prestamo)
    $.ajax({                                      
        type: "GET",
        url: "http://127.0.0.1:8000/abonos/get/ajax/validate/abono_detalle", 
        data: { id_prestamo: codigo_prestamo },
        success: function (response) {
          let prestamo_informacion = response["_prestamo_informacion"];
          let persona_informacion = response["_persona_informacion"];

          // Prestamo
          $("#id_monto_prestado").text(prestamo_informacion[0]["monto_prestado"])
          $("#id_interes").text(prestamo_informacion[0]["interes"])
          $("#id_num_meses").text(prestamo_informacion[0]["num_meses"])
          $("#id_tipo_pago").text(prestamo_informacion[0]["tipo_pago_id"])
          $("#id_fecha_prestamo").text(prestamo_informacion[0]["date_created"])
          $("#id_monto_a_pagar").text(prestamo_informacion[0]["monto_a_pagar"])
          $("#id_num_cuotas").text(prestamo_informacion[0]["num_cuotas"])
          $("#id_deadline").text(prestamo_informacion[0]["deadline"])
          
          
          // Cliente
          $("#id_client_id").text(persona_informacion[0]["id"]) //Ya está incluido
          $("#id_nombre_client").text(persona_informacion[0]["nombre"] + " " +persona_informacion[0]["apellido"])
          $("#id_identificacion_client").text(persona_informacion[0]["cedula"])
          // $("#id_").text(persona_informacion[0]["telefono"])
          // $("#id_").text(persona_informacion[0]["direccion"])

        },
        error: function (response) {
          console.log("Hubo un error");
        },
      });
});