const images = document.querySelectorAll('.slideshow img');
let currentImageIndex = 0;

function nextImage() {
  images[currentImageIndex].classList.remove('active');
  currentImageIndex = (currentImageIndex + 1) % images.length;
  images[currentImageIndex].classList.add('active');
}

setInterval(nextImage, 3000); // Change image every 3 seconds
