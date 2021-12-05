let date_created_ = document.getElementById("id_date_created");
let deadline = document.getElementById("id_deadline");
let _meses = document.getElementById("id_num_meses");

date_created_.addEventListener("input", updateValue);
_meses.addEventListener("input", updateValue);

function updateValue(e)
{
    var day, month, year;
    var d = (date_created_.value);
    // console.log(typeof d);
    result = d.match("[0-9]{4}([\-/ \.])[0-9]{2}[\-/ \.][0-9]{2}");
    if(null != result) {
        dateSplitted = result[0].split(result[1]);
        day = parseInt(dateSplitted[2]);
        month = parseInt(dateSplitted[1]) - 1;
        year = parseInt(dateSplitted[0]);
    }
    // console.log(year);
    // console.log(month);
    // console.log(day);

    var theDate = new Date(year, month, day);        
    // console.log(theDate)
    var myNewDate = new Date(theDate);


    myNewDate.setMonth(myNewDate.getMonth() + parseInt(_meses.value));
    // myNewDate.setDate(myNewDate.getDate() + 30 * parseInt(_meses.value));
    // console.log(myNewDate)
    
    day = myNewDate.getDate();
    month = myNewDate.getMonth() + 1;
    year = myNewDate.getFullYear();
    
    // console.log(year);
    // console.log(month);
    // console.log(day);
    // console.log(year+"-"+month+"-"+day);
    if(month < 10) {
        month = "0"+month;
    }
    if(day < 10) {
        day = "0"+day;
    }

    // console.log(year);
    // console.log(month);
    // console.log(day);
    // console.log(year+"-"+month+"-"+day);
    deadline.value = year+"-"+month+"-"+day;
}
