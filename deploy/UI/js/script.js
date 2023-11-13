const host_name = "http://127.0.0.1:5000";

const sendImage = document.getElementById("send-image");
const imageFile = document.getElementById("image-file");
const formUpload = document.getElementById("form-upload");
const changeModel = document.getElementById("changeModelButton");

formUpload.addEventListener("submit", e => {
    e.preventDefault();

    const formData = new FormData();
    console.log(imageFile.files);
    formData.append("image", imageFile.files[0])
    var requestOptions = {
        method: 'POST',
        body: formData,
    };
    fetch(host_name + '/upload', requestOptions)
        .then(response => response.blob())
        .then(blob => {
            const imageUrl = URL.createObjectURL(blob);
            console.log(imageUrl)
            // Hiển thị hình ảnh trong thẻ img
            const img = document.getElementById('hrImage');
            img.src = imageUrl;
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });;
});

changeModel.addEventListener("click", e => {
    e.preventDefault();

    console.log(modelName);
    var requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ modelName: modelName }),
    }
    fetch(host_name + '/change_model', requestOptions)
        .then(response => response.json())
        .then(msg => {
            console.log('Response from host:', msg);
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
});


const defaultImageURL = 'download.jpg';
function showMyImage(fileInput) {
    var files = fileInput.files;
    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        var imageType = /image.*/;
        if (!file.type.match(imageType)) {
            continue;
        }
        var img = document.getElementById("thumbnil");
        img.file = file;
        var reader = new FileReader();
        reader.onload = (function (aImg) {
            return function (e) {
                aImg.src = e.target.result;
            };
        })(img);
        reader.readAsDataURL(file);
    }
    hrImage.src = defaultImageURL;
}

// Get the download button
const downloadButton = document.querySelector('.button-download');

// Add an event listener to the download button
downloadButton.addEventListener('click', () => {
    // Get the image URL
    const imageUrl = document.getElementById('hrImage').src;

    // Create a new anchor element
    const anchor = document.createElement('a');
    anchor.href = imageUrl;
    anchor.download = 'enhanced-image.jpg';

    // Append the anchor element to the body
    document.body.appendChild(anchor);

    // Click the anchor element to download the image
    anchor.click();

    // Remove the anchor element from the body
    document.body.removeChild(anchor);
});













