
  $.ajax({
    method: "GET",
    url: 'http://127.0.0.1:8000/api/v1/refuels/',
    success: function (data) {
      $.each(data, function (index, val) {
        val.totale = +val.fuel_quantity * +val.fuel_unit_price;
      });
      const result = [...data.reduce((r, o) => {
        const key = o.gaz_station + '-' + o.vehicle;
        const refuel = r.get(key) || Object.assign({}, o, {
          totale: 0
        });
        refuel.totale += +o.totale;
        return r.set(key, refuel);
      }, new Map).values()];
      const gasoil_station = [...data.reduce((r, o) => {
        const key = o.gaz_station;
        const refuel = r.get(key) || Object.assign({}, o, {
          totale: 0
        });
        refuel.totale += +o.totale;
        return r.set(key, refuel);
      }, new Map).values()];
      console.log(result);
      console.log(gasoil_station);
      drawLineGraph(gasoil_station, 'refuelChart');
    },
    error: function (error_data) {
      console.log(error_data);
    }
  });
  $.ajax({
    method: "GET",
    url: 'http://127.0.0.1:8000/api/v1/consumption/',
    success: function (data) {
      let consumption = Object.create(null);
      $.each(data, function (index, val) {
        val.vehicle in consumption ? consumption[val.vehicle].push(val.consumption) : consumption[val
          .vehicle] = [val.consumption];
      });
      $.each(consumption, function (index, value) {
        const canvas = document.createElement('canvas');
        const div_container = document.createElement('div');
        const div_card = document.createElement("div");
        const div_row = document.createElement("div");
        const graphs = document.getElementById("consumption");
        div_container.classList.add('col');
        div_card.classList.add("card", "mb-3");
        div_row.classList.add("row", "g-0");
        graphs.appendChild(div_container);
        div_container.appendChild(div_card);
        div_card.appendChild(div_row);
        div_row.appendChild(canvas);
        canvas.id = index;
        const vehicle_data = Object.create(null);
        vehicle_data[index] = value;
        drawBarGraph(vehicle_data, index);
      });
    },
    error: function (error_data) {
      console.log(error_data);
    }
  });

  function drawLineGraph(data, id) {
    var labels = [];
    var chartdata = [];
    $.each(data, function (index, val) {
      labels.push(val.gaz_station);
      chartdata.push(val.totale);
    });
    var chartLabel = 'Coût Totale Gasoil par Station';
    var ctx = document.getElementById(id).getContext('2d');
    var chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: chartLabel,
          data: chartdata,
        }]
      },

      // Configuration options go here
      options: {
        scales: {
          xAxes: [{
            display: true
          }],
          yAxes: [{
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: 'Coùt gasoil '
            }
          }]
        },
        plugins: {

          colorschemes: {

            scheme: 'brewer.SetOne3'

          }

        }
      }
    });
  };

  function drawBarGraph(data, id) {
    var chartdata = Object.values(data)[0];
    var labels = [1, 2, 3, 4, 5];
    var ctx = document.getElementById(id).getContext('2d');
    var chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: Object.keys(data),
          data: chartdata,
        }]
      },

      // Configuration options go here
      options: {
        scales: {
          xAxes: [{
            display: true
          }],
          yAxes: [{
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: 'consomation %'
            }
          }]
        },
        plugins: {
            title: {
                display: true,
                text: Object.keys(data)
            },
            colorschemes: {
                scheme: 'brewer.PRGn8'
            }
        }
      }
    });
  };