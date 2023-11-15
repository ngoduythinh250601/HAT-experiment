document.getElementById('download_example').addEventListener('click', function () {
    var imageUrl1 = this.getAttribute('data-image-url1');
    var imageUrl2 = this.getAttribute('data-image-url2');
    
    alert("Image URL 1: " + imageUrl1);
    alert("Image URL 2: " + imageUrl2);
    
    downloadImages(imageUrl1, imageUrl2);
});

function downloadImages(imageUrl1, imageUrl2) {
    alert("Downloading images...");
    
    var a1 = document.createElement('a');
    a1.href = imageUrl1;
    a1.download = 'image1.png';
    document.body.appendChild(a1);
    a1.click();
    document.body.removeChild(a1);

    var a2 = document.createElement('a');
    a2.href = imageUrl2;
    a2.download = 'image2.png';
    document.body.appendChild(a2);
    a2.click();
    document.body.removeChild(a2);
}
