var counter = 0;
var fanCounter = 0;

var chartCanvasMin;
var chartCanvasHour;
var chartCanvasDay;
var fanCanvas;

var graphTempMin = [];
var graphHumMin = [];
var graphTempHour = [];
var graphHumHour = [];
var graphTempDay = [];
var graphHumDay = [];

var graphFan = [];

let graphType = {
    graph1temp: true,
    graph1hum: true,
    graph2temp: true,
    graph2hum: true,
    graph3temp: true,
    graph3hum: true,
};

var root = document.querySelector(":root");

function renderGraphs() {
    chartCanvasMin.options.data[1].visible = graphType["graph1temp"];
    chartCanvasMin.options.data[0].visible = graphType["graph1hum"];
    chartCanvasMin.render();

    chartCanvasHour.options.data[1].visible = graphType["graph2temp"];
    chartCanvasHour.options.data[0].visible = graphType["graph2hum"];
    chartCanvasHour.render();

    chartCanvasDay.options.data[1].visible = graphType["graph3temp"];
    chartCanvasDay.options.data[0].visible = graphType["graph3hum"];
    chartCanvasDay.render();

    fanCanvas.render();
}

function checkBox(graphID) {
    graphType[graphID] = !graphType[graphID];
    renderGraphs();
}

function getData() {
    // $.getJSON("http://172.16.111.217:5000", function (data) {
    // fetch('/software/graphData.json')
    fetch(
        "https://raw.githubusercontent.com/elmooooooooooo/The-Smart-Barn/website/software/graphData.json"
    )
        .then((response) => response.json())
        .then(function (data) {
            rebuildGraphList(data["min"], graphTempMin, graphHumMin);
            rebuildGraphList(data["hour"], graphTempHour, graphHumHour);
            rebuildGraphList(data["day"], graphTempDay, graphHumDay);
            rebuildFanList(data["fanDay"], graphFan);
            setVisualFanSpeed(parseInt(data["currentFanSpeed"]));

            renderGraphs();

            setTimeout(() => {
                getData();
            }, 30000);
        });
}

function rebuildGraphList(data, tempDataList, humDataList) {
    tempDataList.length = 0;
    humDataList.length = 0;
    counter = 0;

    for (let i = 0; i < data.length; i++) {
        tempDataList.push({
            x: counter,
            y: parseInt(data[i][1]),
            label: data[i][0],
            color: "red",
        });
        humDataList.push({
            x: counter,
            y: parseInt(data[i][2]),
            label: data[i][0],
            color: "blue",
        });
        counter++;
    }
}

function rebuildFanList(data, fanList) {
    fanList.length = 0;

    for (let i = 0; i < data.length; i++) {
        fanList.push({
            x: fanCounter,
            y: parseInt(data[i][1]),
            label: data[i][0],
            color: "green",
        });
        fanCounter++;
    }
}

function setVisualFanSpeed(currentFanSpeed) {
    let reversedFanSpeed = Math.abs(currentFanSpeed - 100);

    let fanSpeedFrequencyInSeconds =
        currentFanSpeed == 0 ? 0 : Math.max(reversedFanSpeed / 10, 1);
    root.style.setProperty("--fanSpeed", `${fanSpeedFrequencyInSeconds}s`);
}
