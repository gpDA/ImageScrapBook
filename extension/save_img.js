$(function () {


  var tv = document.getElementById('url');
    
  var canvas = document.createElement('canvas');
  var context = canvas.getContext('2d');
  var img = document.getElementById('grabbed_img');
  
  var myImg = new Image();
  // var d ;
  // // data is not defined
  var theData;
  img.onload = function() {
     context.drawImage(myImg, 0, 0);
    //  var theData = context.getImageData(0, 0, img.width, img.height);
    theData = context.getImageData(0, 0, img.width, img.height);
    // undefined DATA
    //  console.log("the Data : ", theData.data);
  };
  
  var canvas = document.createElement('canvas');
  var context = canvas.getContext('2d');
  var img = document.getElementById('grabbed_img');
  
  // img.src = tv.value //set src of the image
  
context.drawImage(img, 10, 10);

var dataurl = canvas.toDataURL();
// base 64 encoded
// console.log("dataurl: ", dataurl);



$("#save").on('click', function(e){
  var title1 = $("#title").val();

  var formData = new FormData() 

  // formData.append('user', '1');
  formData.append('title', title1);
  formData.append('image', dataurl);
  formData.append('extension', 'jpeg')

  $.ajax({
    type: "POST",
    url: "http://localhost:8000/api/create",
    data: formData,
    // beforeSend : function(xhr){
    //   var cookie = credentials['COOKIE'];
    //   console.log('adding cookie'+ cookie);
    //   xhr.setRequestHeader('Cookie', cookie);
    // },

    xhrFields: { withCredentials: true },
    mimeType:"multipart/form-data",
    processData: false,
    contentType: false,
    // crossDomain: true, 

    // dataType: 'json',
    // contentType: "application/json; charset=utf-8;", // this
    error: function(errr){
      console.log(errr);
    },
    success: function(data, status, xhr){
      var token = data["token"];
      console.log(token)
      // console.log('successs,,,,' + xhr.getResponseHeader("Set-Cookie"));

      // window.location.href = "http://localhost:8000/gallery/public";
      // location.replace("http://localhost:8000/gallery/public");
    }

  })


})


});
