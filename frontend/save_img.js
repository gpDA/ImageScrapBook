console.log("sssup");

console.log(window.localStorage.getItem('clickedone'));


var tv = document.getElementById('url');
tv.value = window.localStorage.getItem('clickedone');
