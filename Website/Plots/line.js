Highcharts.chart('line', {

    title: {
      text: 'Number of UFO Sightings in the US, 1973-2022',
      align: 'center'
    },
    subtitle: {
      text: "Source: National UFO Reporting Center",
      align:'center'
    },
  
    yAxis: {
      title: {
        text: 'Number of Sightings',
        style: {
          fontWeight: 'bold'
        }
      }
    },
  
    xAxis: {
      title: {
        text:"Year",
        style: {
          fontWeight: 'bold'
        }
      }
    }
    ,
  
    plotOptions: {
      series: {
        label: {
          connectorAllowed: false
        },
        pointStart: 1973
      }
    },
  
    series: [{
      name: "UFO Sightings",
      data: [267,  299,  345,  316,  299,  371,  274,  275,  193,  212,  185,
          193,  238,  202,  239,  262,  288,  267,  252,  285,  321,  444,
          569,  577, 1263, 1784, 2734, 2653, 2935, 2929, 3478, 3835, 3772,
         3443, 4060, 4645, 4230, 4204, 5128, 7354, 7046, 7998, 6399, 5300,
         4723, 3070, 5281, 5966, 2764, 3594],
      color:'#2C0BB0'
    }],
  
    responsive: {
      rules: [{
        condition: {
          maxWidth: 500
        }
      }]
    }
  
  });