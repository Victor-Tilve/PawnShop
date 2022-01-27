// se le hace la solicitud al backend para que con el valor de id del cliente, se filtren todos los prestamos a su nombre.
$("#client-id").bind("input change", function (e) {
  var nick_name = $(this).val();
  // GET AJAX request
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:8000/abonos/get/ajax/validate/prestamos_cliente",
    data: { id_cliente: nick_name },
    success: function (response) {
      // if not valid user, alert the user
      let id_loans = response["id_loans"];
      if (id_loans == "---------"){
        console.log("Bingo");
      }
      $("#id_codigo_prestamo").html("");
      //$("#id_codigo_prestamo").html( "<p>All new content. <em>You bet!</em></p>" );
      for (let i = 0; i < id_loans.length; i++) {
        $("#id_codigo_prestamo").append(id_loans[i]);
      }
      $("#id_codigo_prestamo").trigger("change");
    },
    error: function (response) {
      console.log("Hubo un error");
    },
  });
});
