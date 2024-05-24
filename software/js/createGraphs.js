window.onload = function () {
    chartCanvasMin = new CanvasJS.Chart("chartCanvasMin", {
        title: {
            text: "Temperatuur en luchtvochtigheid van het afgelopen uur",
        },
        data: [
            {
                type: "line",
                dataPoints: graphTempMin,
            },
            {
                type: "line",
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
                dataPoints: graphTempHour,
            },
            {
                type: "line",
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
                dataPoints: graphTempDay,
            },
            {
                type: "line",
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
