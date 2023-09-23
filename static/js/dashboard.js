const showPopupButton = document.getElementById("showPopup");
const closePopupButton = document.getElementById("closePopup");
const popupContainer = document.getElementById("popupContainer");
const overlay = document.getElementById("overlay");

showPopupButton.addEventListener("click", () => {
  popupContainer.style.display = "flex";
  overlay.style.display = "block";
  console.log("clicked");
});

closePopupButton.addEventListener("click", () => {
  popupContainer.style.display = "none";
  overlay.style.display = "none";
});
function openChat() {
  document.getElementById("chatbot").style.width = "250px";
}

function closeChat() {
  document.getElementById("chatbot").style.width = "0";
}
