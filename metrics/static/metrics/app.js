var dates = globalData.map(function (d) {
  return d.timestamp;
});

var yVals = globalData.map(function (d) {
  return d.temperature;
});

var data = [
  {
    x: dates,
    y: yVals,
    type: 'line'
  }
];

Plotly.newPlot('chart', data);
