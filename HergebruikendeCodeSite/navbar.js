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
        tag.outerHTML = data
      });

      const netlifyIdentity =  document.createElement('script');
      netlifyIdentity.src = "https://identity.netlify.com/v1/netlify-identity-widget.js"
      document.body.appendChild(netlifyIdentity);

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

function onLogin(currentPage) {
  if (document.getElementById(currentPage) == null) {
    setTimeout(() => {
      onLogin(currentPage);
    }, 100);
  } else if (netlifyIdentity.currentUser()) {
    document.getElementById('login').innerHTML = 'Data';
    document.getElementById('login').setAttribute("onclick", "location.href='/Pages/Data.html'");
    document.getElementById('login2').innerHTML = 'Data';
    document.getElementById('login2').href = '/pages/Data.html';
  }
}

function onLoginData(currentPage) {
  if (document.getElementById(currentPage) == null) {
    setTimeout(() => {
      onLoginData(currentPage);
    }, 100);
  } else if (netlifyIdentity.currentUser()) {
    document.getElementById('login').innerHTML = 'Logout';
    document.getElementById('login2').innerHTML = 'Logout';
    document.getElementById('login').setAttribute("onclick", LogoutOnClick());


  }
}

function LogoutOnClick() {
  console.log("fucntie uitgzvoerd")
  netlifyIdentity.logout()
  window.href("index.html")
  console.log("logout ingedeudwd")
}
