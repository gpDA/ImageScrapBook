
// backgroud script.
// Grabs data of an actiavted tab using the grabber.js

var IMAGE_URLS = []

chrome.extension.onMessage.addListener(
    function(request, sender, sendResponse) {
      console.log(request.Dir)
        switch (request.directive) {
        case "setImages":
          //grabbing data sent from the grabber.js
          IMAGE_URLS = request.data;
          chrome.extension.getBackgroundPage().console.log("IMAGE_URLS grabbed by grabber.js: ", IMAGE_URLS);
          sendResponse({backgroundResponse: "Pictures grabbed!"});
          break;
        default:
            alert("Requset cannot be performed");
        }
    }
);

//execute the grabber script everytime the active tab is changed
chrome.tabs.onActivated.addListener(function(info) {
    var tab = chrome.tabs.get(info.tabId, function(tab) {
      chrome.tabs.executeScript(null, {file: "grabber.js"});
    });
});
