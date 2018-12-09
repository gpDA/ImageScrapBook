// This popup.js file is the receive all the image urls data grabbed from the grabbed.js
// and show them on the popup.html

function init() {
	go_gallery();
	go_public_gallery();
	//grab_img();
}


function startLoading(){
  chrome.extension.getBackgroundPage().console.log("Popup clicked!");
}

function get_urls() {
  var picUrls = chrome.extension.getBackgroundPage().IMAGE_URLS;
  if (picUrls.length > 0){
  	var wholeList = document.createElement("div");
  	document.getElementById("ulContainer").appendChild(wholeList);
  	var listElement = document.createElement("ul");
    wholeList.appendChild(listElement);
    for (var i = 0; i < picUrls.length; i++){
      var listItem = document.createElement("li");
      listItem.innerHTML = "<a href= save_img.html><img src=" + picUrls[i].src + " width=30%, height=30%>" + "</a>";
      chrome.extension.getBackgroundPage().console.log( "src: ", picUrls[i].src );
      listElement.appendChild(listItem);
    }
    chrome.extension.getBackgroundPage().console.log("get_urls function ");
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


document.addEventListener('DOMContentLoaded', init);
