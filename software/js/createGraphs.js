window.onload = function () {
    chartCanvasMin = new CanvasJS.Chart("chartCanvasMin",
        {
            title: {
                text: "Data of the last hour",
            },
            data: [
                {
                    type: "line",
                    dataPoints: graphListMin["temp"],
                },
                {
                    type: "line",
                    dataPoints: graphListMin["hum"],
                },
            ],

            axisY: {
                minimum: 0,
                maximum: 60,
            },
    });

    chartCanvasHour = new CanvasJS.Chart("chartCanvasHour",
        {
            title: {
                text: "Data of the last 24 hours",
            },
            data: [
                {
                    type: "line",
                    dataPoints: graphListHour["temp"],
                },
                {
                    type: "line",
                    dataPoints: graphListHour["hum"],
                },
            ],
            axisY: {
                minimum: 0,
                maximum: 24,
            },
        });

    chartCanvasDay = new CanvasJS.Chart("charCanvasDay",
        {
            title: {
                text: "Data of the last year",
            },
            data: [
                {
                    type: "line",
                    dataPoints: graphListDay["temp"],
                },
                {
                    type: "line",
                    dataPoints: graphListDay["hum"],
                },
            ],
            axisY: {
                minimum: 0,
                maximum: 365,
            },
        });
    getData();
};
