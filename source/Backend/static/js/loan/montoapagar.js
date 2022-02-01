// const input = document.querySelector('input');
let monto = document.getElementById('id_monto_prestado');
let interes = document.getElementById('id_interes');
let meses = document.getElementById('id_num_meses');

monto.addEventListener('input', updateValue_);
interes.addEventListener('input', updateValue_);
meses.addEventListener('input', updateValue_);

function updateValue_(e) {

document.getElementById('id_monto_adeudado').value = parseInt(monto.value) + parseInt(monto.value * interes.value/100 * meses.value) ;;
}
