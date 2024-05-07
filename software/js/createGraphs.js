window.onload = function () {
    chartCanvasMin = new CanvasJS.Chart("chartCanvasMin",
        {
            title: {
                text: "Data of the last hour",
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

    chartCanvasHour = new CanvasJS.Chart("chartCanvasHour",
        {
            title: {
                text: "Data of the last 24 hours",
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

    chartCanvasDay = new CanvasJS.Chart("charCanvasDay",
        {
            title: {
                text: "Data of the last year",
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
    getData();
};
