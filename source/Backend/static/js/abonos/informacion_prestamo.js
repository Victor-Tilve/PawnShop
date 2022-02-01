// Se completa la información del prestamo al que se le realizará el abono

  $("#id_codigo_prestamo").bind("input change", function (e) {
    var _data = $(this).val();
    $.ajax({
      type: "GET",
      url: "http://127.0.0.1:8000/abonos/get/ajax/validate/prestamo_informacion",
      data: { id_prestamo: _data },
      success: function (response) {
        let prestamo_informacion = response["_prestamo_informacion"];
        let abono_informacion = response["_abono_informacion"];
      // console.log(prestamo_informacion)

        // hay momentos en los que ciertos clientes no tienen prestamos, al cambiar 
        // el valor a una linea con dash, se colocan los valores por defecto
        if ( prestamo_informacion != "---------"){
          $("#id_ultimo_abono").val(abono_informacion[0]["abono"])
          $("#id_fecha_ultimo_abono").val(abono_informacion[0]["date_created"])
          $("#id_date_created_prestamo").val(prestamo_informacion[0]["date_created"])
          $("#id_deadline").val(prestamo_informacion[0]["deadline"])
          $("#id_monto_adeudado").val(prestamo_informacion[0]["monto_adeudado"])
          $("#id_interes").val(prestamo_informacion[0]["interes"])
          $("#id_num_meses").val(prestamo_informacion[0]["num_meses"])
          $("#id_num_cuotas").val(prestamo_informacion[0]["num_cuotas"])
          $("#id_tipo_pago").val(prestamo_informacion[0]["tipo_pago_id"])
          $("#id_monto_a_pagar").val(prestamo_informacion[0]["monto_a_pagar"])
          // console.log(abono_informacion[0]["date_created"]);
        }
        else{
          $("#id_ultimo_abono").val("0")
          $("#id_fecha_ultimo_abono").val("mm/dd/yyyy")
          $("#id_date_created_prestamo").val("mm/dd/yyyy")
          $("#id_deadline").val("mm/dd/yyyy")
          $("#id_monto_adeudado").val("0")
          $("#id_interes").val("0")
          $("#id_num_meses").val("1")
          $("#id_num_cuotas").val("1")
          $("#id_tipo_pago").val("")
          $("#id_monto_a_pagar").val("0")
          // console.log("Dentro del else");
        }


      },
      error: function (response) {
        console.log("Hubo un error");
      },
    });
  });



