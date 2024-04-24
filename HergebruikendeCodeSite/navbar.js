// Wait for the document to finish loading
document.addEventListener('DOMContentLoaded', function () {
  // Find all custom tags in the document
  const customTags = document.querySelectorAll('navigatiebalk');

  // Loop through each custom tag
  customTags.forEach(function (tag) {
    // Replace the custom tag with its inner HTML content
    fetch("../HergebruikendeCodeSite/navbar.html")
      .then(response => {
        return response.text()
      })
      .then(data => {
        tag.outerHTML = data;
      });

      const netlifyCustom = document.createElement('script');
      netlifyCustom.src = "/software/js/netlify.js";
      document.body.appendChild(netlifyCustom);
  }); 

});


window.onresize = function (e) {
  if (document.body.clientWidth > 1000) {
    document.getElementById("mobileMenu").style.display = "none";
    document.getElementById("hamburgerCheckBox").checked = false;
  }
}

function setActiveNavButton(currentPage) {
  if (document.getElementById(currentPage) == null) {
    setTimeout(() => {
      setActiveNavButton(currentPage);
    }, 100);
  } else {
    document.querySelector(`#${currentPage}`).classList.remove("navbutton");
    document.querySelector(`#${currentPage}`).classList.add("navbutton_active");

  }
}