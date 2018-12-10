// var i = document.getElementById("url").value;
//
// chrome.extension.onMessage.addListener(
//     function(request, sender, sendResponse) {
//         chrome.extension.getBackgroundPage().console.log("requ: ", request.directive);
//         switch (request.directive) {
//         case "sendURL":
//           this_url = request.data;
//           chrome.extension.getBackgroundPage().console.log("grabbedurl: ", this_url);
//           i=this_url;
//           sendResponse({backgroundResponse: "urlgrabbed!"});
//           break;
//         default:
//             chrome.extension.getBackgroundPage().console.log("requ: ");
//             alert("Requset cannot be performed");
//         }
//     }
// );
