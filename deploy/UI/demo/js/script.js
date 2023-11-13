function displayImage(input) {
    // Get the <rect> and <text> elements
    var rect = document.getElementById('placeholder-rect');
    var text = document.getElementById('thumbnil');

    // Remove any existing patterns
    var existingPattern = document.getElementById('inputimage');
    if (existingPattern) {
      existingPattern.parentNode.removeChild(existingPattern);
    }

    // Get the selected file from the input
    var file = input.files[0];

    // Create a FileReader to read the selected file
    var reader = new FileReader();

    // Set up the FileReader to display the image when it's loaded
    reader.onload = function(e) {
      // Set the <rect> fill to the image
      rect.setAttribute('fill', 'url(#inputimage)');

      // Set the <text> content to be empty
      text.textContent = '';

      // Create a pattern element and an image element inside it
      var pattern = document.createElementNS('http://www.w3.org/2000/svg', 'pattern');
      pattern.setAttribute('id', 'inputimage');
      pattern.setAttribute('width', '100%');
      pattern.setAttribute('height', '100%');

      var image = document.createElementNS('http://www.w3.org/2000/svg', 'image');
      image.setAttribute('x', '0');
      image.setAttribute('y', '0');
      image.setAttribute('width', '100%');
      image.setAttribute('height', '100%');
      image.setAttribute('preserveAspectRatio', 'xMidYMid slice');

      // Set the image source to the data URL of the selected file
      image.setAttribute('href', e.target.result);

      // Append the image to the pattern, and the pattern to the SVG
      pattern.appendChild(image);
      rect.parentNode.appendChild(pattern);
    };

    // Read the selected file as a data URL
    reader.readAsDataURL(file);
  }






