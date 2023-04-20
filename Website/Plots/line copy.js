Highcharts.chart('polar', {
  chart: {
      polar: true,
      type: 'column',
      width: 770,
      height: 670
  },
  title: {
      text: 'Total UFO Sightings per Hour of Day',
        style: {
      fontSize: '20px',
      fontWeight: 'bold'
  }
  },
  xAxis: {
      tickInterval: 1,
      categories: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'],
      labels: {
          formatter: function () {
              return this.value + ':00';
          }
      }
  },

  series: [{
      data: [
          {y: 6723, color: 'blue'},
          {y: 4414, color: 'blue'},
          {y: 3170, color: 'blue'},
          {y: 2937, color: 'black'},
          {y: 2382, color: 'black'},
          {y: 2800, color: 'black'},
          {y: 2173, color: 'black'},
          {y: 1482, color: 'black'},
          {y: 1284, color: 'black'},
          {y: 1567, color: 'black'},
          {y: 1796, color: 'black'},
          {y: 1695, color: 'black'},
          {y: 1920, color: 'black'},
          {y: 1827, color: 'black'},
          {y: 1812, color: 'black'},
          {y: 1937, color: 'black'},
          {y: 2357, color: 'black'},
          {y: 3772, color: '#8ACEF7'},
          {y: 6209, color: '#8ACEF7'},
          {y: 9052, color: '#8ACEF7'},
          {y: 13053, color: '#273E7B'},
          {y: 17241,color: '#273E7B'},
          {y: 15494,color: '#273E7B'},
          {y: 10732,color: '#273E7B'}
      ],
      pointPlacement: 'between',
    pointWidth: 0.19
  }]
});
