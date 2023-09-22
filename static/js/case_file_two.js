const languages = [
  {
    no: "0",
    name: "Auto",
    native: "Detect",
    code: "auto",
  },
  {
    no: "1",
    name: "Afrikaans",
    native: "Afrikaans",
    code: "af",
  },
  {
    no: "2",
    name: "Albanian",
    native: "Shqip",
    code: "sq",
  },
  {
    no: "3",
    name: "Arabic",
    native: "عربي",
    code: "ar",
  },
  {
    no: "4",
    name: "Armenian",
    native: "Հայերէն",
    code: "hy",
  },
  {
    no: "5",
    name: "Azerbaijani",
    native: "آذربایجان دیلی",
    code: "az",
  },
  {
    no: "6",
    name: "Basque",
    native: "Euskara",
    code: "eu",
  },
  {
    no: "7",
    name: "Belarusian",
    native: "Беларуская",
    code: "be",
  },
  {
    no: "8",
    name: "Bulgarian",
    native: "Български",
    code: "bg",
  },
  {
    no: "9",
    name: "Catalan",
    native: "Català",
    code: "ca",
  },
  {
    no: "10",
    name: "Chinese (Simplified)",
    native: "中文简体",
    code: "zh-CN",
  },
  {
    no: "11",
    name: "Chinese (Traditional)",
    native: "中文繁體",
    code: "zh-TW",
  },
  {
    no: "12",
    name: "Croatian",
    native: "Hrvatski",
    code: "hr",
  },
  {
    no: "13",
    name: "Czech",
    native: "Čeština",
    code: "cs",
  },
  {
    no: "14",
    name: "Danish",
    native: "Dansk",
    code: "da",
  },
  {
    no: "15",
    name: "Dutch",
    native: "Nederlands",
    code: "nl",
  },
  {
    no: "16",
    name: "English",
    native: "English",
    code: "en",
  },
  {
    no: "17",
    name: "Estonian",
    native: "Eesti keel",
    code: "et",
  },
  {
    no: "18",
    name: "Filipino",
    native: "Filipino",
    code: "tl",
  },
  {
    no: "19",
    name: "Finnish",
    native: "Suomi",
    code: "fi",
  },
  {
    no: "20",
    name: "French",
    native: "Français",
    code: "fr",
  },
  {
    no: "21",
    name: "Galician",
    native: "Galego",
    code: "gl",
  },
  {
    no: "22",
    name: "Georgian",
    native: "ქართული",
    code: "ka",
  },
  {
    no: "23",
    name: "German",
    native: "Deutsch",
    code: "de",
  },
  {
    no: "24",
    name: "Greek",
    native: "Ελληνικά",
    code: "el",
  },
  {
    no: "25",
    name: "Haitian Creole",
    native: "Kreyòl ayisyen",
    code: "ht",
  },
  {
    no: "26",
    name: "Hebrew",
    native: "עברית",
    code: "iw",
  },
  {
    no: "27",
    name: "Hindi",
    native: "हिन्दी",
    code: "hi",
  },
  {
    no: "28",
    name: "Hungarian",
    native: "Magyar",
    code: "hu",
  },
  {
    no: "29",
    name: "Icelandic",
    native: "Íslenska",
    code: "is",
  },
  {
    no: "30",
    name: "Indonesian",
    native: "Bahasa Indonesia",
    code: "id",
  },
  {
    no: "31",
    name: "Irish",
    native: "Gaeilge",
    code: "ga",
  },
  {
    no: "32",
    name: "Italian",
    native: "Italiano",
    code: "it",
  },
  {
    no: "33",
    name: "Japanese",
    native: "日本語",
    code: "ja",
  },
  {
    no: "34",
    name: "Korean",
    native: "한국어",
    code: "ko",
  },
  {
    no: "35",
    name: "Latvian",
    native: "Latviešu",
    code: "lv",
  },
  {
    no: "36",
    name: "Lithuanian",
    native: "Lietuvių kalba",
    code: "lt",
  },
  {
    no: "37",
    name: "Macedonian",
    native: "Македонски",
    code: "mk",
  },
  {
    no: "38",
    name: "Malay",
    native: "Malay",
    code: "ms",
  },
  {
    no: "39",
    name: "Maltese",
    native: "Malti",
    code: "mt",
  },
  {
    no: "40",
    name: "Norwegian",
    native: "Norsk",
    code: "no",
  },
  {
    no: "41",
    name: "Persian",
    native: "فارسی",
    code: "fa",
  },
  {
    no: "42",
    name: "Polish",
    native: "Polski",
    code: "pl",
  },
  {
    no: "43",
    name: "Portuguese",
    native: "Português",
    code: "pt",
  },
  {
    no: "44",
    name: "Romanian",
    native: "Română",
    code: "ro",
  },
  {
    no: "45",
    name: "Russian",
    native: "Русский",
    code: "ru",
  },
  {
    no: "46",
    name: "Serbian",
    native: "Српски",
    code: "sr",
  },
  {
    no: "47",
    name: "Slovak",
    native: "Slovenčina",
    code: "sk",
  },
  {
    no: "48",
    name: "Slovenian",
    native: "Slovensko",
    code: "sl",
  },
  {
    no: "49",
    name: "Spanish",
    native: "Español",
    code: "es",
  },
  {
    no: "50",
    name: "Swahili",
    native: "Kiswahili",
    code: "sw",
  },
  {
    no: "51",
    name: "Swedish",
    native: "Svenska",
    code: "sv",
  },
  {
    no: "52",
    name: "Thai",
    native: "ไทย",
    code: "th",
  },
  {
    no: "53",
    name: "Turkish",
    native: "Türkçe",
    code: "tr",
  },
  {
    no: "54",
    name: "Ukrainian",
    native: "Українська",
    code: "uk",
  },
  {
    no: "55",
    name: "Urdu",
    native: "اردو",
    code: "ur",
  },
  {
    no: "56",
    name: "Vietnamese",
    native: "Tiếng Việt",
    code: "vi",
  },
  {
    no: "57",
    name: "Welsh",
    native: "Cymraeg",
    code: "cy",
  },
  {
    no: "58",
    name: "Yiddish",
    native: "ייִדיש",
    code: "yi",
  },
  {
    no: "59",
    name: "Kannada",
    native: "ಕನ್ನಡ",
    code: "da",
  },
];
const dropdowns = document.querySelectorAll(".dropdown-container"),
  inputLanguageDropdown = document.querySelector("#input-language");

function populateDropdown(dropdown, options) {
  dropdown.querySelector("ul").innerHTML = "";
  options.forEach((option) => {
    const li = document.createElement("li");
    const title = option.name + " (" + option.native + ")";
    li.innerHTML = title;
    li.dataset.value = option.code;
    li.classList.add("option");
    dropdown.querySelector("ul").appendChild(li);
  });
}

populateDropdown(inputLanguageDropdown, languages);

dropdowns.forEach((dropdown) => {
  dropdown.addEventListener("click", (e) => {
    dropdown.classList.toggle("active");
  });

  dropdown.querySelectorAll(".option").forEach((item) => {
    item.addEventListener("click", (e) => {
      //remove active class from current dropdowns
      dropdown.querySelectorAll(".option").forEach((item) => {
        item.classList.remove("active");
      });
      item.classList.add("active");
      const selected = dropdown.querySelector(".selected");
      //   console.log("slected language is ", item.dataset.value);
      localStorage.setItem("lang", item.dataset.value);
      selected.innerHTML = item.innerHTML;
      selected.dataset.value = item.dataset.value;
      translate();
    });
  });
});
document.addEventListener("click", (e) => {
  dropdowns.forEach((dropdown) => {
    if (!dropdown.contains(e.target)) {
      dropdown.classList.remove("active");
    }
  });
});
