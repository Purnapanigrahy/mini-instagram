const errorBox = document.getElementById("error-box");
if (errorBox && errorBox.innerText.trim() !== "") {
  // Show animation
  errorBox.classList.add("show");
  // Hide after 3 seconds
  setTimeout(() => {
    errorBox.classList.remove("show");
  }, 3000);
}