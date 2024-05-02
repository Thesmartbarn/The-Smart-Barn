// Wait for the document to finish loading
document.addEventListener("DOMContentLoaded", function () {
    // Find all custom tags in the document
    const customTags = document.querySelectorAll("navigatiebalk");

    // Loop through each custom tag
    customTags.forEach(function (tag) {
        // Replace the custom tag with its inner HTML content
        fetch("../HergebruikendeCodeSite/navbar.html")
            .then((response) => {
                return response.text();
            })
            .then((data) => {
                tag.outerHTML = data;
            });
    });

    // if user logs in: print msg in log & change which button is visible.
    netlifyIdentity.on("login", function (user) {
        console.log("Welcome,", user);
        window.location.href = "Pages/Data.html";
    });

    // if user logs out: print msg in log & change which button is visible.
    netlifyIdentity.on("logout", function () {
        window.location.href = "/index.html";
    });

    // Link the netlify events to the login buttons.
    addNetlifyButtonEvents();
});

window.onresize = function (e) {
    if (document.body.clientWidth > 1000) {
        document.getElementById("mobileMenu").classList.add("hideMobileMenu");
        document.getElementById("hamburgerCheckBox").checked = false;
    }
};

// Load in all needed netlify buttons and link to functions containing onclick events.
function addNetlifyButtonEvents() {
    const loginBtn = document.getElementById("login");
    const loginBtnMobile = document.getElementById("login2");

    if (loginBtn == null || loginBtnMobile == null) {
        console.log("netlify buttons nog niet geladen");
        setTimeout(() => {
            addNetlifyButtonEvents();
        }, 100);
    } else {
        console.log("netlify buttons geladen");
        const is_dataPage =
            window.location.href.toLowerCase().indexOf("data") > -1;
        if (netlifyIdentity.currentUser()) {
            // When on data page show logout option. On all other pages, link to data page.
            if (is_dataPage) {
                loginBtn.innerHTML = "Logout";
                loginBtnMobile.innerHTML = "Logout";
                loginBtn.onclick = onClickLogin;
                loginBtnMobile.onclick = onClickLogin;
            } else {
                loginBtn.innerHTML = "Data";
                loginBtnMobile.innerHTML = "Data";
                loginBtn.setAttribute(
                    "onclick",
                    "location.href='/Pages/Data.html'"
                );
                loginBtnMobile.href = "/pages/Data.html";
            }
        } else {
            if (is_dataPage) {
                // If unauthorised person goes to data page, send to home.
                window.location.href = "/index.html";
            }
            loginBtn.onclick = onClickLogin;
            loginBtnMobile.onclick = onClickLogin;
        }
    }
}

function onClickLogin() {
    if (netlifyIdentity) {
        output = netlifyIdentity.open(); // Important! Change the config in Netlify to make it so signing up is disabled.
        console.log(output);
    }
}

function onClickLogout() {
    if (netlifyIdentity) {
        output = netlifyIdentity.logout();
        console.log(output);
    }
}

function setActiveNavButton(currentPage) {
    if (document.getElementById(currentPage) == null) {
        setTimeout(() => {
            setActiveNavButton(currentPage);
        }, 100);
    } else {
        document.querySelector(`#${currentPage}`).classList.remove("navbutton");
        document
            .querySelector(`#${currentPage}`)
            .classList.add("navbutton_active");
    }
}

function hamburgerMenuActions() {
    document.getElementById("mobileMenu").style.display = "block";
    if (document.getElementById("hamburgerCheckBox").checked) {
        document
            .getElementById("mobileMenu")
            .classList.remove("hideMobileMenu");
    } else {
        document.getElementById("mobileMenu").classList.add("hideMobileMenu");
    }
}
