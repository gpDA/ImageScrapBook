// This popup.js file is the receive all the image urls data grabbed from the grabbed.js
// and show them on the popup.html
// var clickedUrl = {
// 	url:''
// }
//console.log("running:");

function init() {
	go_gallery();
	go_public_gallery();
	//grab_img();
	console.log("running:");
	startLoading();
	url_work();
}



function startLoading(){
  chrome.extension.getBackgroundPage().console.log("Popup clicked!");
}

var temp = document.getElementById('work');

function get_urls() {
  var picUrls = chrome.extension.getBackgroundPage().IMAGE_URLS;
  if (picUrls.length > 0){
  	var wholeList = document.createElement("div");
  	document.getElementById("ulContainer").appendChild(wholeList);
  	var listElement = document.createElement("ul");
    wholeList.appendChild(listElement);
    for (var i = 0; i < picUrls.length; i++){
      var listItem = document.createElement("li");
      //listItem.innerHTML = `<a href= save_img.html><img src=" + picUrls[i].src +  " width=30%, height=30% >" + "</a></div>`;
			listItem.innerHTML = `<a href= save_img.html><img name = ${i} src= ${picUrls[i].src} width=30% height=30% ></a>`;
      chrome.extension.getBackgroundPage().console.log( "src: ", picUrls[i].src , "name: ", i);
      listElement.appendChild(listItem);
    }
    chrome.extension.getBackgroundPage().console.log("get_urls function ");
		const ulContainer = document.getElementById('ulContainer');
		chrome.extension.getBackgroundPage().console.log("temp ", work);
		ulContainer.addEventListener('click', event => {
					var clicked =  picUrls[event.target.name].src;
					chrome.extension.getBackgroundPage().console.log("clicked: ", picUrls[event.target.name].src);

					temp.innerHTML+= clicked;



				})
  }
  else{
		console.log("Images unavailable");
    document.body.innerHTML = "Images unavilable";
  }
}
// when the page loads, show the images!
// onload:  used within the <body> element to execute a script once a
//      web page has **completely loaded** all content (including images, script files, CSS files, etc.).
window.onload = get_urls();

//=============BUTTONS on HTML===============

//TODO: direct to my gallery/public gallery
var newURL = "http://google.com";

function go_public_gallery(){
	var pg_btn = document.getElementById('public_gallery_btn');
	pg_btn.addEventListener('click', function() {
			chrome.extension.getBackgroundPage().console.log("open publilc gallery");
			//open the public gallery page
			chrome.tabs.create({url: newURL});
	});
}

function go_gallery(){
	var g_btn = document.getElementById('my_gallery_btn');
	g_btn.addEventListener('click', function() {
			chrome.extension.getBackgroundPage().console.log("open my gallery");
			//open the my gallery page
			chrome.tabs.create({url: newURL});
	});
}
// function url_work(){
// 	var temp_u = document.getElementById('work');
// 	temp_u.innerHTML += "44444";
// }


document.addEventListener('DOMContentLoaded', init);
