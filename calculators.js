function italicElementsToColor(color) { 
            if (color == undefined) {
                color = 'black';
            }
            let italicElements = document.getElementsByTagName("i");
            for (let i = 0; i < italicElements.length; i++) {
                italicElements[i].style.color = color;
            }
        }
function paraToHeader(content) {
    if (content == undefined) {
        content = '<h2>None Given</h2>';
    }
    document.getElementById('demo').innerHTML = '<h2>'+ content + '</h2>';
}
