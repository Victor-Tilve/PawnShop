// There are many ways to pick a DOM node; here we get the form itself and the celular
// input box, as well as the span element into which we will place the error message.
// const form  = document.getElementById('client_form');

const celular = document.getElementById('id_telefono');
const celularError = document.querySelector('#id_telefono + span.errorcelular');
// const validationcelular = parseInt(celular.value)
// console.log("Valor:")
// console.log(/^\d{10}$/.test(celular.value))

celular.addEventListener('input', function (event) {
    // Each time the user types something, we check if the
    // form fields are valid.

  if ((/^\d{10}$/.test(celular.value))) {
      // If there is still an error, show the correct error
      celularError.textContent = ''; // Reset the content of the message
      celularError.className = 'errorcelular'; // Reset the visual state of the message
    } else {
      // In case there is an error message visible, if the field
      // is valid, we remove the error message.
      showCelularError();
  }
});

form.addEventListener('submit', function (event) {
  // if the celular field is valid, we let the form submit

  if(!celular.validity.valid || !(/^\d{10}$/.test(celular.value))) {
    // If it isn't, we display an appropriate error message
    showCelularError();
    // Then we prevent the form from being sent by canceling the event
    event.preventDefault();
    // console.log("No es valido - 2")
  }
});

function showCelularError() {
    if(!(/^\d{10}$/.test(celular.value))) {
    // If the field is empty,
    // display the following error message.
    celularError.textContent = 'El número debe ser de 10 dígitos.';
    // console.log('Necesitas ingresar celular de 10 digitos.')
  } else {
    // If the field doesn't contain an celular address,
    // display the following error message.
    // celularError.textContent = 'Debe ser un númer de 8 a 10 dígitos';
    // console.log('Debe ser un digito de 10 números')
  } 

  // Set the styling appropriately
  celularError.className = 'error active';
}