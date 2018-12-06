/**
	This popup.js file is used to receive the list of urls that the grabber content script has found
  and show them to the popup.html file.
**/

function init() {
	go_gallery();
	go_public_gallery();
	startLoading();
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
      listItem.innerHTML = "<a href= save_img.html><img src=" + picUrls[i].src + " width=50%, height=50%>" + "</a>";
      chrome.extension.getBackgroundPage().console.log( "src: ", picUrls[i].src );
      listElement.appendChild(listItem);
    }
    chrome.extension.getBackgroundPage().console.log("get_urls function ");
  }
  else{
    document.body.innerHTML = "Images unavilable";
  }
}

function go_public_gallery(){
	var pg_btn = document.getElementById('public_gallery_btn');
	pg_btn.addEventListener('click', function() {
			chrome.extension.getBackgroundPage().console.log("open publilc gallery");
	});
}

function go_gallery(){
	var g_btn = document.getElementById('my_gallery_btn');
	g_btn.addEventListener('click', function() {
			chrome.extension.getBackgroundPage().console.log("open my gallery");
	});
}

function startLoading(){
  //start loading the rest of the script
  chrome.extension.getBackgroundPage().console.log("popup clicked!");
  get_urls();
}

// when the page loads, remove the gif and execute the rest
//window.onload = startLoading()




// tracking code for analytics

// (function() {
//   var ga = document.createElement('script');
// 	ga.type = 'text/javascript';
// 	ga.async = true;
//   ga.src = 'https://ssl.google-analytics.com/ga.js';
//   var s = document.getElementsByTagName('script')[0];
// 	s.parentNode.insertBefore(ga, s);
// })();


document.addEventListener('DOMContentLoaded', init);
