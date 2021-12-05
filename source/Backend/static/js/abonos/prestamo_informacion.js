$("#id_codigo_prestamo").bind("input change", function (e) {
  var _data = $(this).val();
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:8000/abonos/get/ajax/validate/prestamo_informacion",
    data: { id_prestamo: _data },
    success: function (response) {
      let prestamo_imformacion = response["_prestamo_imformacion"];
    //   console.log("id_prestamo: " + prestamo_imformacion[0]["id"]);
    //   console.log("date_created: " + prestamo_imformacion[0]["date_created"]);
    //   console.log("deadline: " + prestamo_imformacion[0]["deadline"]);
    //   console.log("cliente_id: " + prestamo_imformacion[0]["cliente_id"]);
    //   console.log("interes: " + prestamo_imformacion[0]["interes"]);
    //   console.log("monto_a_pagar: " + prestamo_imformacion[0]["monto_a_pagar"]);
    //   console.log(
    //     "monto_prestado: " + prestamo_imformacion[0]["monto_prestado"]
    //   );
    //   console.log("num_cuotas: " + prestamo_imformacion[0]["num_cuotas"]);
    //   console.log("num_meses: " + prestamo_imformacion[0]["num_meses"]);
    //   console.log("tipo_pago_id: " + prestamo_imformacion[0]["tipo_pago_id"]);
      $("#id_date_created_prestamo").val(prestamo_imformacion[0]["date_created"])
      $("#id_deadline").val(prestamo_imformacion[0]["deadline"])
      $("#id_monto_prestado").val(prestamo_imformacion[0]["monto_prestado"])
      $("#id_interes").val(prestamo_imformacion[0]["interes"])
      $("#id_num_meses").val(prestamo_imformacion[0]["num_meses"])
      $("#id_num_cuotas").val(prestamo_imformacion[0]["num_cuotas"])
      $("#id_tipo_pago").val(prestamo_imformacion[0]["tipo_pago_id"])
      $("#id_monto_a_pagar").val(prestamo_imformacion[0]["monto_a_pagar"])
      $("#id_date_created").val(prestamo_imformacion[0]["date_created"])
    },
    error: function (response) {
      console.log("Hubo un error");
    },
  });
});
