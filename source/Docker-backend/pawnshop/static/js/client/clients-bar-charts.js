var config2 = {
    type: 'bar',
    data: {
      datasets: [{
        data: [46, 22,5,19],
        backgroundColor: [
          '#ff0000', '#0000ff', '#ff0080', '#73ffff'
        ],
        label: 'Meses'
      }],
      labels: ['Enero', 'Febrero','Marzo','Abril']
    },
    options: {
      responsive: true,
    //   plugins: {
    //     legend: {
    //       position: 'top',
    //     },
    //     title: {
    //       display: true,
    //       text: 'Chart.js Bar Chart'
    //     }
    //   }
    }
  };

  window.onload = function() {
    var ctx2 = document.getElementById('bar-chart').getContext('2d');
    window.myPie = new Chart(ctx2, config2);
  };