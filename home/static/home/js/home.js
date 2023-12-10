
const track = document.getElementById("image-track");
const images = document.querySelectorAll('.image');
const fullscreenView = document.getElementById('fullscreen-view');
const fullscreenImage = document.getElementById('fullscreen-image');
const closeBtn = document.querySelector('.close-btn');
const arrowLeft = document.querySelector('.arrow-left');
const arrowRight = document.querySelector('.arrow-right');
let currentIndex = 0;

// Функция открытия изображения на полный экран
function openFullscreen(imageSrc) {
  fullscreenImage.src = imageSrc;
  fullscreenView.classList.add('show');
}

// Функция закрытия полноэкранного режима
function closeFullscreen() {
  fullscreenView.classList.remove('show');
}

fullscreenView.addEventListener('click', (event) => {
  // Проверяем, что клик произошел на затемненном фоне, а не на изображении или кнопках
  if (event.target === fullscreenView) {
    closeFullscreen();
  }
});

// Переключение на предыдущее изображение
function prevImage() {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  openFullscreen(images[currentIndex].src);
}

// Переключение на следующее изображение
function nextImage() {
  currentIndex = (currentIndex + 1) % images.length;
  openFullscreen(images[currentIndex].src);
}

// Обработчики событий для изображений
images.forEach((image, index) => {
  image.addEventListener('click', () => {
    currentIndex = index;
    openFullscreen(image.src);
  });
});

// Обработчики событий для стрелок
arrowLeft.addEventListener('click', prevImage);
arrowRight.addEventListener('click', nextImage);

// Обработчик события для закрытия полноэкранного режима
closeBtn.addEventListener('click', closeFullscreen);

// Закрыть полноэкранный режим при нажатии на Esc
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closeFullscreen();
  }
});

// Оставить ваш текущий код для отслеживания событий мыши и тачскрина
const handleOnDown = e => {
  track.dataset.mouseDownAt = e.clientX;
};

const handleOnUp = () => {
  track.dataset.mouseDownAt = "-30";
  track.dataset.prevPercentage = track.dataset.percentage;
};

const handleOnMove = e => {
  if (track.dataset.mouseDownAt === "-30") return;

  const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX,
    maxDelta = window.innerWidth / 2;

  const percentage = (mouseDelta / maxDelta) * -100,
    nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage,
    nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, -30), -70);

  track.dataset.percentage = nextPercentage;

  track.animate({
    transform: `translate(${nextPercentage}%, -50%)`
  }, { duration: 1200, fill: "forwards" });

  for (const image of track.getElementsByClassName("image")) {
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

// Добавление обработчика клика на затемненный фон
fullscreenView.addEventListener('click', (event) => {
  // Проверяем, что клик произошел на затемненном фоне, а не на изображении или кнопках
  if (event.target === fullscreenView) {
    closeFullscreen();
  }
});

