function NumCuotas(e) {
    let num_meses = parseInt(document.getElementById("id_num_meses").value);
    let tipo_cuota = parseInt(e.target.value);

    if (tipo_cuota == 1) {
        document.getElementById("id_num_cuotas").value = num_meses;
        }else if (tipo_cuota == 2) {
            document.getElementById("id_num_cuotas").value = 2 * num_meses;
        }else if (tipo_cuota == 3) {
            document.getElementById("id_num_cuotas").value = 4 * num_meses;
        }else if (tipo_cuota == 4) {
            document.getElementById("id_num_cuotas").value = 30 * num_meses;
        }else{
            document.getElementById("id_num_cuotas").value = 0;
    }
}
