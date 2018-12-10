console.log("sssup");
console.log("grabbed src: ", window.localStorage.getItem('clickedone'));

var tv = document.getElementById('url');
tv.value = window.localStorage.getItem('clickedone');

var canvas = document.createElement('canvas');
var context = canvas.getContext('2d');
var img = document.getElementById('grabbed_img');

var myImg = new Image();
var d ;
img.onload = function() {
   context.drawImage(myImg, 0, 0);
   var theData = context.getImageData(0, 0, img.width, img.height);
   console.log("the Data : ", theData.data);
};

img.src = tv.value;
console.log("this not workin tho..why..:", theData.data);



const savebtn = document.getElementById('save')

savebtn.addEventListener('click', postImage())

const postImage = () => {
  fetch('https://www.gogle.com', {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json',
    },
    body: JSON.stringify({
      user: 1, //fake userId. After auth, we will have a "logged in" user Id
      title: document.getElementById('title').value,
      image: d,
      extension: 'jpg', //fake file format. Need to talk to Skye since ours is raw data
      privacy: false,
      thumbnail_url: '',
      imageurl: tv.value,
    })
  })
  .then(res => res.json())
  .then(res => console.log(res))
}
savebtn.addEventListener('click', postImage())
