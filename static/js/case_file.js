// Initialize the SpeechRecognition object
const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
recognition.lang = "en-US"; // Set the recognition language to English

// Handle recognition results
recognition.onresult = function (event) {
  const spokenText = event.results[0][0].transcript;
  document.getElementById("spokenText").value = spokenText;
  translateText(spokenText);
};

// Handle errors
recognition.onerror = function (event) {
  console.error("Speech recognition error:", event.error);
};

// Start listening when the Start button is clicked
function startListening() {
  recognition.start();
  document.getElementById("startButton").setAttribute("disabled", "true");
  document.getElementById("stopButton").removeAttribute("disabled");
}

// Stop listening when the Stop button is clicked
function stopListening() {
  recognition.stop();
  document.getElementById("startButton").removeAttribute("disabled");
  document.getElementById("stopButton").setAttribute("disabled", "true");
}

// Translate text using a translation API (you need to implement this part)
async function translateText(text) {
  // You would typically use a translation API like Google Translate here.
  // For this example, we'll just display the same text.
  var inputLanguage = "hi";
  var outputLanguage = "en";
  var translateScript = "";
  const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${inputLanguage}&tl=${outputLanguage}&dt=t&q=${encodeURI(
    text
  )}`;
  await fetch(url)
    .then((response) => response.json())
    .then((json) => {
      console.log(json);
      console.log(json[0].map((item) => item[0]).join(""));
      translateScript = json[0].map((item) => item[0]).join("");
      console.log(`Translated Script ${translateScript}`);
    })
    .catch((error) => {
      console.log(error);
    });

  inputLanguage = "en";
  outputLanguage = "hi";

  var final_text = "";
  const url1 = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${inputLanguage}&tl=${outputLanguage}&dt=t&q=${encodeURI(
    translateScript
  )}`;
  await fetch(url1)
    .then((response) => response.json())
    .then((json) => {
      console.log(json);
      console.log(json[0].map((item) => item[0]).join(""));
      final_text = json[0].map((item) => item[0]).join("");
      // console.log(`Translated Script ${translateScript}` )
    })
    .catch((error) => {
      console.log(error);
    });

  document.getElementById("case_description").textContent = final_text;
}
