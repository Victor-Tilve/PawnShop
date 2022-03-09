// There are many ways to pick a DOM node; here we get the form itself and the celular2
// input box, as well as the span element into which we will place the error message.
// const form  = document.getElementById('client_form');

const celular2 = document.getElementById('id_telefono_ref1');
const celular2Error = document.querySelector('#id_telefono_ref1 + span.errorcelularref1');
// const validationcelular2 = parseInt(celular2.value)
console.log("Valor:")
// console.log(/^\d{10}$/.test(celular2.value))

celular2.addEventListener('input', function (event) {
    // Each time the user types something, we check if the
    // form fields are valid.

  if ((/^\d{10}$/.test(celular2.value))) {
      // If there is still an error, show the correct error
      celular2Error.textContent = ''; // Reset the content of the message
      celular2Error.className = 'errorcelular2ref1'; // Reset the visual state of the message
    } else {
      // In case there is an error message visible, if the field
      // is valid, we remove the error message.
      showCelular2Error();
  }
});

form.addEventListener('submit', function (event) {
  // if the celular2 field is valid, we let the form submit

  if(!celular2.validity.valid || !(/^\d{10}$/.test(celular2.value))) {
    // If it isn't, we display an appropriate error message
    showCelular2Error();
    // Then we prevent the form from being sent by canceling the event
    event.preventDefault();
    // console.log("No es valido - 2")
  }
});

function showCelular2Error() {
    if(!(/^\d{10}$/.test(celular2.value))) {
    // If the field is empty,
    // display the following error message.
    celular2Error.textContent = 'El número debe ser de 10 dígitos.';
    // console.log('Necesitas ingresar celular2 de 10 digitos.')
  } else {
    // If the field doesn't contain an celular2 address,
    // display the following error message.
    // celular2Error.textContent = 'Debe ser un númer de 8 a 10 dígitos';
    // console.log('Debe ser un digito de 10 números')
  } 

  // Set the styling appropriately
  celular2Error.className = 'error active';
}