$("#id_codigo_prestamo").bind("input change", function (e) {
  var _data = $(this).val();
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:8000/abonos/get/ajax/validate/prestamo_informacion",
    data: { id_prestamo: _data },
    success: function (response) {
      let prestamo_informacion = response["_prestamo_informacion"];
      let abono_informacion = response["_abono_informacion"];
      // console.log("id_prestamo: " + prestamo_informacion[0]["id"]); 
    //   console.log("date_created: " + prestamo_informacion[0]["date_created"]);
    //   console.log("deadline: " + prestamo_informacion[0]["deadline"]);
    //   console.log("cliente_id: " + prestamo_informacion[0]["cliente_id"]);
    //   console.log("interes: " + prestamo_informacion[0]["interes"]);
    //   console.log("monto_a_pagar: " + prestamo_informacion[0]["monto_a_pagar"]);
    //   console.log(
    //     "monto_prestado: " + prestamo_informacion[0]["monto_prestado"]
    //   );
    //   console.log("num_cuotas: " + prestamo_informacion[0]["num_cuotas"]);
    //   console.log("num_meses: " + prestamo_informacion[0]["num_meses"]);
    //   console.log("tipo_pago_id: " + prestamo_informacion[0]["tipo_pago_id"]);

      $("#id_ultimo_abono").val(abono_informacion[0]["abono"])
      $("#id_fecha_ultimo_abono").val(abono_informacion[0]["date_created"])
      $("#id_date_created_prestamo").val(prestamo_informacion[0]["date_created"])
      $("#id_deadline").val(prestamo_informacion[0]["deadline"])
      $("#id_monto_prestado").val(prestamo_informacion[0]["monto_prestado"])
      $("#id_interes").val(prestamo_informacion[0]["interes"])
      $("#id_num_meses").val(prestamo_informacion[0]["num_meses"])
      $("#id_num_cuotas").val(prestamo_informacion[0]["num_cuotas"])
      $("#id_tipo_pago").val(prestamo_informacion[0]["tipo_pago_id"])
      $("#id_monto_a_pagar").val(prestamo_informacion[0]["monto_a_pagar"])
      $("#id_date_created").val(prestamo_informacion[0]["date_created"])
      console.log(abono_informacion[0]["date_created"]);
    },
    error: function (response) {
      console.log("Hubo un error");
    },
  });
});
