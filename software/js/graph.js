var counter = 0;

var chartCanvasMin;
var chartCanvasHour;
var chartCanvasDay;


var graphTempMin = [];
var graphHumMin = [];
var graphTempHour = [];
var graphHumHour = [];
var graphTempDay = [];
var graphHumDay = [];


function renderGraphs() {
    chartCanvasMin.render();
    chartCanvasHour.render();
    chartCanvasDay.render();
}

function getData() {
    $.getJSON("http://172.16.111.217:5000", function (data) {
        // console.log(data);
        rebuildGraphList(data["min"], graphTempMin, graphHumMin);
        rebuildGraphList(data["hour"], graphTempHour, graphHumHour);
        rebuildGraphList(data["day"], graphTempDay, graphHumDay);

        console.log(graphTempMin);
        renderGraphs();

        setTimeout(() => {
            getData();
        }, 200);
    });
}

function rebuildGraphList(data, tempDataList, humDataList) {
    tempDataList.length = 0
    humDataList.length = 0

    for (let i = 0; i < data.length; i++) {
        tempDataList.push({
            x: counter,
            y: parseInt(data[i][1]),
            label: data[i][0],
        });
        humDataList.push({
            x: counter,
            y: parseInt(data[i][2]),
            label: data[i][0],
        });
        counter += 1;
    }
}
