/**
	This is the content script that scrapes the webpage for images and works with background.js
**/

function parseUrls() {
	// get the urls of the images
	var images = document.getElementsByTagName('img');
	var srcList = [];
	for(var i = 0; i < images.length; i++) {
	    srcList.push(images[i].src);
	}
	return srcList;
}

function checkImageSize(imageUrls) {
	var url_collection = [];
	for (var i = 0; i < imageUrls.length; i++){
		var img = new Image();
		img.src = imageUrls[i];
		//if the image isn't too small, add!
		if (img.width > 30){
			var slashIndex = imageUrls[i].lastIndexOf("/");
			var picName = imageUrls[i].substring(slashIndex+1, imageUrls[i].txt);
			imageObject = new Object();
			imageObject.name = picName;
			imageObject.width = img.width;
			imageObject.height = img.height;
			imageObject.src = img.src;
			url_collection.push(imageObject);
		}
	}
	return url_collection;
}

function noResponse(){
	chrome.runtime.sendMessage({greeting: null}, function(response) {
		  console.log(response.farewell);
	});
}

function removeDuplicates(url_collection){
	var unique = {};
	var uniqueOnes = [];
	for (var i = 0; i < url_collection.length; i++) {
		unique[url_collection[i].src] = i;
	};
	for(item in unique){
		uniqueOnes.push(url_collection[unique[item]]);
	}
	return uniqueOnes;
}

function main(){
	console.log("main called");
	var imageUrls = parseUrls();
	if (imageUrls){
		url_collection = checkImageSize(imageUrls);
		url_collection = removeDuplicates(url_collection);
		//if our url_collection is ready, send to background.js as data
		if(url_collection){
			chrome.extension.sendMessage(
				{directive: "setImages", data: url_collection},
				 function(response) {
		        console.log("main response: ", response.backgroundResponse);
						console.log("url_collection: ", url_collection);
		    });
		}
		else{
			noResponse();
		}
	}
	else{
		noResponse();
	}
}

main()
