const themeBtn = document.getElementById("theme-toggle");
const flagPL = document.getElementById("flag-pl");
const flagEN = document.getElementById("flag-en");

// --- LIGHT / DARK MODE ---
function setThemeClass(theme) {
  document.body.classList.remove("light-mode", "dark-mode");
  document.body.classList.add(theme + "-mode");
  localStorage.setItem("theme", theme);
  updateThemeIcon(theme);
}

function updateThemeIcon(theme) {
  const icon = document.getElementById("theme-icon");
  if (!icon) return;
  icon.classList.remove("bi-sun-fill", "bi-moon-stars-fill");

  if (theme === "dark") {
    icon.classList.add("bi-sun-fill");
    icon.title = "Przełącz na jasny tryb";
  } else {
    icon.classList.add("bi-moon-stars-fill");
    icon.title = "Przełącz na ciemny tryb";
  }
}

(function () {
  const savedTheme = localStorage.getItem("theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  setThemeClass(savedTheme || (prefersDark ? "dark" : "light"));
})();

themeBtn.addEventListener("click", () => {
  const darkActive = document.body.classList.contains("dark-mode");
  setThemeClass(darkActive ? "light" : "dark");
});

// FLAG LANGUAGE SWITCHER
function updateFlagIcon(activeLang) {
  if (!flagPL || !flagEN) return;

  if (activeLang === "pl") {
    flagPL.classList.add("flag-active");
    flagPL.classList.remove("flag-inactive");
    flagEN.classList.add("flag-inactive");
    flagEN.classList.remove("flag-active");
  } else {
    flagEN.classList.add("flag-active");
    flagEN.classList.remove("flag-inactive");
    flagPL.classList.add("flag-inactive");
    flagPL.classList.remove("flag-active");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const initialLang = document.documentElement.lang || "pl";
  updateFlagIcon(initialLang);
});