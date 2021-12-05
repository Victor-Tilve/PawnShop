// const input = document.querySelector('input');
let monto = document.getElementById('id_monto_prestado');
let interes = document.getElementById('id_interes');
let meses = document.getElementById('id_num_meses');
let monto_pagar = document.getElementById('id_monto_a_pagar');

monto.addEventListener('input', updateValue_);
interes.addEventListener('input', updateValue_);
meses.addEventListener('input', updateValue_);

function updateValue_(e) {
//   monto_pagar.value = (monto.value) * (1 + interes.value/100);
  monto_pagar.value = parseInt(monto.value) + parseInt(monto.value * interes.value/100 * meses.value) ;
}