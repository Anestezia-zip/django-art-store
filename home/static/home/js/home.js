// Object containing DOM elements
const elements = {
  track: document.getElementById("image-track"),
  images: document.querySelectorAll('.image'),
  fullscreenView: document.getElementById('fullscreen-view'),
  fullscreenImage: document.getElementById('fullscreen-image'),
  closeBtn: document.querySelector('.close-btn'),
  arrowLeft: document.querySelector('.arrow-left'),
  arrowRight: document.querySelector('.arrow-right')
};

// Index of the current image
let currentIndex = 0;

// Function to open fullscreen mode with a specified image source
function openFullscreen(imageSrc) {
  elements.fullscreenImage.src = imageSrc;
  elements.fullscreenView.classList.add('show');
}

// Function to close fullscreen mode
function closeFullscreen() {
  elements.fullscreenView.classList.remove('show');
}

// Function to display the previous image
function prevImage() {
  currentIndex = (currentIndex - 1 + elements.images.length) % elements.images.length;
  openFullscreen(elements.images[currentIndex].src);
}

// Function to display the next image
function nextImage() {
  currentIndex = (currentIndex + 1) % elements.images.length;
  openFullscreen(elements.images[currentIndex].src);
}

// Function to handle click on an image
function handleImageClick(image, index) {
  image.addEventListener('click', () => {
    currentIndex = index;
    openFullscreen(image.src);
  });
}

// Adding click event listeners to images
elements.images.forEach(handleImageClick);

// Adding click event listeners to navigation arrows
elements.arrowLeft.addEventListener('click', prevImage);
elements.arrowRight.addEventListener('click', nextImage);
elements.closeBtn.addEventListener('click', closeFullscreen);

// Listening for the 'Escape' key to close fullscreen mode
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closeFullscreen();
  }
});

// To track mouse and touchscreen events)
const handleOnDown = e => {
  elements.track.dataset.mouseDownAt = e.clientX;
};

const handleOnUp = () => {
  elements.track.dataset.mouseDownAt = "-30";
  elements.track.dataset.prevPercentage = elements.track.dataset.percentage;
};

const handleOnMove = e => {
  if (elements.track.dataset.mouseDownAt === "-30") return;

  const mouseDelta = parseFloat(elements.track.dataset.mouseDownAt) - e.clientX,
    maxDelta = window.innerWidth / 2;

  const percentage = (mouseDelta / maxDelta) * -100,
    nextPercentageUnconstrained = parseFloat(elements.track.dataset.prevPercentage) + percentage,
    nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, -30), -70);

  elements.track.dataset.percentage = nextPercentage;

  elements.track.animate({
    transform: `translate(${nextPercentage}%, -50%)`
  }, { duration: 1200, fill: "forwards" });

  for (const image of elements.track.getElementsByClassName("image")) {
    image.animate({
      objectPosition: `${100 + nextPercentage}% center`
    }, { duration: 1200, fill: "forwards" });
  }
};

const isTouchDevice = 'ontouchstart' in window || navigator.msMaxTouchPoints;
if (isTouchDevice) {
  window.onmousedown = null;
  window.onmouseup = null;
  window.onmousemove = null;

  window.ontouchstart = e => handleOnDown(e.touches[0]);
  window.ontouchend = e => handleOnUp(e.touches[0]);
  window.ontouchmove = e => handleOnMove(e.touches[0]);
} else {
  window.ontouchstart = null;
  window.ontouchend = null;
  window.ontouchmove = null;

  window.onmousedown = e => handleOnDown(e);
  window.onmouseup = e => handleOnUp(e);
  window.onmousemove = e => handleOnMove(e);
}
window.ontouchmove = e => handleOnMove(e.touches[0]);

// Adding a click handler to close fullscreen mode when clicking on the darkened background
elements.fullscreenView.addEventListener('click', (event) => {
  if (event.target === elements.fullscreenView) {
    closeFullscreen();
  }
});
