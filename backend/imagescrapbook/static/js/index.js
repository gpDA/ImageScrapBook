
const check = document.getElementById('check')
const gridContainer = document.getElementById('grid-container')

document.addEventListener('DOMContentLoaded', function() {
    var img_btn = document.getElementById('check')
    img_btn.addEventListener('click', function() {
        const gridItem = document.createElement("div");
        gridItem.className = 'grid-item';
        gridContainer.appendChild(gridItem)
    })
});

// console.log('hi')
