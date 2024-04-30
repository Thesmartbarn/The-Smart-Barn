var counter = 0;

var chartCanvasMin;
var chartCanvasHour;
var chartCanvasDay;

var graphListMin = { "temp": [], "hum": [] };
var graphListHour = { "temp": [], "hum": [] };
var graphListDay = { "temp": [], "hum": [] };

function renderGraphs() {
    chartCanvasMin.render();
    chartCanvasHour.render();
    chartCanvasDay.render();
}

function getData() {
    $.getJSON("http://172.16.111.217:5000", function (data) {
        // console.log(data);
        graphListMin = rebuildGraphList(data["min"], graphListMin);
        // graphListHour = rebuildGraphList(data["hour"], graphListHour);
        // graphListDay = rebuildGraphList(data["day"], graphListDay);
        console.log(graphListMin);
        renderGraphs();

        setTimeout(() => {
            getData();
        }, 200);
    });
}

function rebuildGraphList(data, graphList) {
    graphList = { temp: [], hum: [] };
    for (let i = 0; i < data.length; i++) {
        graphList["temp"].push({
            x: counter,
            y: parseInt(data[i][1]),
            label: data[i][0],
        });
        graphList["hum"].push({
            x: counter,
            y: parseInt(data[i][2]),
            label: data[i][0],
        });
        counter += 1;
    }
    return graphList
}
