// There are many ways to pick a DOM node; here we get the form itself and the cedula
// input box, as well as the span element into which we will place the error message.
const form  = document.getElementById('client_form');

const cedula = document.getElementById('id_cedula');
const cedulaError = document.querySelector('#id_cedula + span.errorcedula');
// const validationCedula = parseInt(cedula.value)
// console.log("Valor:")
// console.log(/^\d{10}$/.test(cedula.value))

cedula.addEventListener('input', function (event) {
    // Each time the user types something, we check if the
    // form fields are valid.

  if ((/^\d{10}$/.test(cedula.value))) {
      // If there is still an error, show the correct error
      cedulaError.textContent = ''; // Reset the content of the message
      cedulaError.className = 'error'; // Reset the visual state of the message
      console.log("Es valido")
      console.log(cedula.value)
    } else {
      // In case there is an error message visible, if the field
      // is valid, we remove the error message.
      showError();
  }
});

form.addEventListener('submit', function (event) {
  // if the cedula field is valid, we let the form submit

  if(!cedula.validity.valid || !(/^\d{10}$/.test(cedula.value))) {
    // If it isn't, we display an appropriate error message
    showError();
    // Then we prevent the form from being sent by canceling the event
    event.preventDefault();
    // console.log("No es valido - 2")
  }
});

function showError() {
    if(!(/^\d{10}$/.test(cedula.value))) {
        // If the data is not a number,
        cedulaError.textContent = 'No se ingresaron 10 números';
        console.log('No es un número')
      }else if(cedula.validity.valueMissing) {
    // If the field is empty,
    // display the following error message.
    cedulaError.textContent = 'Necesitas ingresar Cedula de 10 digitos.';
    // console.log('Necesitas ingresar Cedula de 10 digitos.')
  } else if(cedula.validity.typeMismatch) {
    // If the field doesn't contain an cedula address,
    // display the following error message.
    cedulaError.textContent = 'Debe ser un digito de 10 números';
    // console.log('Debe ser un digito de 10 números')
  } else if(cedula.validity.tooShort) {
    // If the data is too short,
    // display the following error message.
    cedulaError.textContent = `cedula debe ser minimo ${ cedula.minLength } caracteres; ingresaste ${ cedula.value.length }.`;
    // console.log(`cedula debe ser minimo ${ cedula.minLength } caracteres; ingresaste ${ cedula.value.length }.`)
  }

  // Set the styling appropriately
  cedulaError.className = 'error active';
}