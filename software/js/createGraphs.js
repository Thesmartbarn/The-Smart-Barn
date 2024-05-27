window.onload = function () {
    chartCanvasMin = new CanvasJS.Chart("chartCanvasMin", {
        title: {
            text: "Temperatuur en luchtvochtigheid van het afgelopen uur",
        },
        data: [
            {
                type: "line",
                lineColor: "red",
                dataPoints: graphTempMin,
            },
            {
                type: "line",
                lineColor: "blue",
                dataPoints: graphHumMin,
            },
        ],

        axisY: {
            minimum: 0,
            maximum: 100,
        },
    });

    chartCanvasHour = new CanvasJS.Chart("chartCanvasHour", {
        title: {
            text: "Temperatuur en luchtvochtigheid van de afgelopen 24 uur",
        },
        data: [
            {
                type: "line",
                lineColor: "red",
                dataPoints: graphTempHour,
            },
            {
                type: "line",
                lineColor: "blue",
                dataPoints: graphHumHour,
            },
        ],
        axisY: {
            minimum: 0,
            maximum: 100,
        },
    });

    chartCanvasDay = new CanvasJS.Chart("chartCanvasDay", {
        title: {
            text: "Temperatuur en luchtvochtigheid van het afgelopen jaar",
        },
        data: [
            {
                type: "line",
                lineColor: "red",
                dataPoints: graphTempDay,
            },
            {
                type: "line",
                lineColor: "blue",
                dataPoints: graphHumDay,
            },
        ],
        axisY: {
            minimum: 0,
            maximum: 100,
        },
    });

    fanCanvas = new CanvasJS.Chart("chartCanvasFan", {
        title: {
            text: "Snelheid van ventilator",
        },
        data: [
            {
                type: "line",
                lineColor: "green",
                dataPoints: graphFan,
            },
        ],
        axisY: {
            minimum: 0,
            maximum: 100,
        },
    });
    getData();
};
