const cardDeck = document.getElementById('card-deck')
const addnew = document.getElementById('add-new')

let photoLists = [];
// function getBase64FromImageUrl(url) {
//     var img = new Image();
//
//     img.setAttribute('crossOrigin', 'anonymous');
//
//     img.onload = function () {
//         var canvas = document.createElement("canvas");
//         canvas.width =this.width;
//         canvas.height =this.height;
//
//         var ctx = canvas.getContext("2d");
//         ctx.drawImage(this, 0, 0);
//
//         var dataURL = canvas.toDataURL("image/png");
//
//         alert(dataURL.replace(/^data:image\/(png|jpg);base64,/, ""));
//     };
//
//     img.src = url;
//     console.log(img.src)
// }
//
// getBase64FromImageUrl("1-917b34c5-53cb-48ff-bb86-7e755cc56889.jpeg")
// let body = {
//   user: 1,
//   title: "Test",
//   image: getBase64FromImageUrl(url),
//   extension: url.split('.').slice(-1).join(''),
//   privacy: "false",
//   thumbnail_url: "",
//   imageurl: ""
//
// }
// const fetchPost = (body) => {
//   fetch('http://35.224.129.143/api/', {
//     method: 'PATCH',
//     headers: {
//       'Content-Type': 'application/json',
//       Accept: 'application/json',
//     },
//     body: JSON.stringify(body)
//   })
//   .then(res => res.json())
//   .then(res => console.log(res))
// }



const fetchReq = () => {
  fetch('http://35.224.129.143/api/')
  .then(res => res.json())
  .then(res => {
    photoLists.push(res);
    generateCards(photoLists[0])
  })
}

// const getUserName = () => {
//   fetch('http://35.224.129.143/user')
//   .then(res => res.json())
//   .then(res => {
//     console.log(res)
//   })
// }


const generateCards = (photoLists) => {
  for (let i = 0; i < photoLists.length; i++) {
    addCard(photoLists[i])
  }
}

const addCard = (photoObject) => {
  const cardFormat = document.createElement("div");
  cardFormat.className = 'col-sm-6 col-md-4 col-lg-3';
  cardDeck.appendChild(cardFormat)
  const card = document.createElement("div");
  card.className = 'card'
  cardFormat.appendChild(card)
  const cardHeader = document.createElement("h5");
  cardHeader.className = 'card-header'
  cardHeader.innerHTML = 'Chang'
  card.appendChild(cardHeader)
  const img = document.createElement('img')
  img.className = 'card-img-top'
  img.src = `http://35.202.153.173:9000/image/${photoObject.imageurl}`
  img.alt = alt="Card image cap"
  card.appendChild(img)
  const cardBody = document.createElement('div')
  cardBody.className = 'card-body'
  const cardTitle = document.createElement('h5')
  cardTitle.className = 'card-title'
  cardTitle.innerHTML = photoObject.title
  cardTitle.appendChild(cardBody)
  card.appendChild(cardTitle)
  const cardFooter = document.createElement('div')
  cardFooter.className = 'card-footer';
  const small = document.createElement('small')
  small.className = 'text-muted'
  small.innerHTML = 'Share With Me'
  const br = document.createElement('br')
  cardFooter.appendChild(br)
  const button = document.createElement('button')
  button.innerHTML = 'Share'
  cardFooter.appendChild(button)
  card.appendChild(cardFooter)
}

document.addEventListener('DOMContentLoaded', function() {
  fetchReq();
  // getUserName()





});
