fetch('https://raw.githubusercontent.com/elmooooooooooo/The-Smart-Barn/website/software/graphData.json')
    .then(response => response.json())
    .then(function(data) {
        console.log(data);
    })