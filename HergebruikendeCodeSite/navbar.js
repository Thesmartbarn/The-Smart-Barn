fetch("../HergebruikendeCodeSite/navbar.html")
  .then(response => {
    return response.text()
  })
  .then(data => {
    document.querySelector("navigatiebalk").innerHTML = data;
  });

window.onresize = function(e) {
  if (document.body.clientWidth > 1000) {
    document.getElementById("mobileMenu").style.display = "none";
    document.getElementById("hamburgerCheckBox").checked = false;
  }
}

function setActiveNavButton(currentPage)
{
    if (document.getElementById(currentPage) == null) {
        setTimeout(() => {
            setActiveNavButton(currentPage);
        }, 100);
    } else {
        document.querySelector(`#${currentPage}`).classList.remove("navbutton");
        document.querySelector(`#${currentPage}`).classList.add("navbutton_active");
        
    }
}

function CheckLogin(){
  window.href = "https://www.google.com"
  console.log('start functie');
  var button = document.getElementById('data');
  button.innerHTML = "Data";
  button.href = "/pages/Data.html";
  console.log('heyfyuehfuzhfuhzuhf');
}