/**
	This is the background script.
  It coordinates passing of data between the grabber.js (which saves the images it scrapes to a variable here for the popup to acces),
  the save.js (a content script that saves the pictures in the tab) and the popup.js script that writes to the popup.html and handles the button listener which fires
  off the download of save.js.
**/

console.log("starting!");

var IMAGE_URLS = []


// listen to request directives sent by grabber.js
chrome.extension.onMessage.addListener(
    function(request, sender, sendResponse) {
      console.log(request.Dir)
        switch (request.directive) {
          case "setImages":
            //grab the urls sent from the grabber.js
            IMAGE_URLS = request.data;
            chrome.extension.getBackgroundPage().console.log("pic grabbed");
            sendResponse({backgroundResponse: "Pictures grabbed! (seding_from_background)"});
            break;
            //getImages case after saving
          default:
              // helps debug when request directive doesn't match
              alert("Unmatched request of '" + request.directive + "' from script to background.js from " + sender);
          }
    }
);

// when the active tab is changed,
// execute the grabber script on the changed tab to grab new images
// chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
//   chrome.tabs.executeScript(tabId, {file: "grabber.js"})
// });

//worksss:====================

//but...TODO: works on a single tab but doesn't load new images when opening up new tab.
chrome.tabs.onActivated.addListener(function(info) {
    var tab = chrome.tabs.get(info.tabId, function(tab) {
      chrome.tabs.executeScript(null, {file: "grabber.js"});
    });
});


//====1===============

// var currentURL;
//
// chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
//   function(tabs){
//   	getCurrentURL(tabs[0].url);
//   });
//
// function getCurrentURL(tab){
// 	currentURL = tab;
// }
//
//===2====================
// chrome.windows.getCurrent(function (currentWindow) {
//       chrome.tabs.query({ active: true, windowId: currentWindow.id }, function (activeTabs) {
//         chrome.tabs.executeScript(activeTabs[0].id, { file: "grabber.js", allFrames: true });
//       });
//     });
//============

/*
onActivated: Fires when the active tab in a window changes. Note that the tab's URL may not be set at the time this event fired,
but you can listen to onUpdated events so as to be notified when a URL is set.

onUpdated: Fired when a tab is updated.
*/
