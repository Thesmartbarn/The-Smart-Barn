fetch('https://github.com/elmooooooooooo/The-Smart-Barn/blob/website/software/graphData.json')
    .then(response => response.json())
    .then(function(data) {
        console.log(data);
    })