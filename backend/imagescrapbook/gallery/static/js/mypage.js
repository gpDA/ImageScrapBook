const cardDeck = document.getElementById('card-deck')
const addnew = document.getElementById('add-new')
const shareButton = document.getElementById('share')
const userId = 1;
let myPhotos = [];
let sharedPhotos = [];



const fetchMyPhotos = (userId) => {
  fetch('http://localhost:8000/api/')
  .then(res => res.json())
  .then(res => {
    res.filter(photoObject => photoObject.user.id === userId);
    myPhotos.push(res);
    generateCards(myPhotos[0])
  })
}

const fetchSharedPhotos = (userId) => {
      fetch('http://localhost:8000/api/sharing')
      .then(res => res.json())
      .then(res => {
        res.filter(sharedObject => sharedObject.shared_by === userId);
        sharedPhotos.push(res);
        generateShareCards(sharedPhotos[0])
}

const generateShareCards = (sharedPhotos) => {
  sharedPhotos.forEach((obj) => addSharedCard(obj))
}

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
  cardHeader.innerHTML = `${photoObject.user.useername}`
  card.appendChild(cardHeader)
  const img = document.createElement('img')
  img.className = 'card-img-top'
  img.src = `${photoObject.imageurl}`
  img.alt = alt="Card image cap"
  card.appendChild(img)
  const cardBody = document.createElement('div')
  cardBody.className = 'card-body'
  const cardTitle = document.createElement('h5')
  cardTitle.className = 'card-title'
  cardTitle.innerHTML = `${photoObject.title}`
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

const addSharedCard = () => {

}

document.addEventListener('DOMContentLoaded', function() {
  fetchMyPhotos(userId)
  // getUserName()





});
