function NumCuotas(e) {
    let num_meses = parseInt(document.getElementById("id_num_meses").value);
    let tipo_cuota = parseInt(e.target.value);

    if (tipo_cuota == 1) {
        console.log("Condicion 1");
        document.getElementById("id_num_cuotas").value = num_meses;
        }else if (tipo_cuota == 2) {
            console.log("Condicion 2");
            document.getElementById("id_num_cuotas").value = 2 * num_meses;
        }else if (tipo_cuota == 3) {
            console.log("Condicion 3");
            document.getElementById("id_num_cuotas").value = 4 * num_meses;
        }else if (tipo_cuota == 4) {
            console.log("Condicion 4");
            document.getElementById("id_num_cuotas").value = 30 * num_meses;
        }else{
            console.log("Else");
            document.getElementById("id_num_cuotas").value = 0;
    }
}
