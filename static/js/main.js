const themeBtn = document.getElementById("theme-toggle");
const flagPL = document.getElementById("flag-pl");
const flagEN = document.getElementById("flag-en");

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
    icon.title = "Switch to light mode";
  } else {
    icon.classList.add("bi-moon-stars-fill");
    icon.title = "Switch to dark mode";
  }
}

function updateFlagIcon(activeLang) {
  if (!flagPL || !flagEN) return;

  const lang = (activeLang || "pl").toLowerCase();
  const isPl = lang.startsWith("pl");

  if (isPl) {
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

function initPortfolioExpand() {
  const grid = document.getElementById("portfolio-grid");
  if (!grid) return;

  const items = Array.from(grid.querySelectorAll(".portfolio-item"));

  const closeAll = () => {
    grid.classList.remove("has-expanded");
    document.body.classList.remove("portfolio-expanded");
    items.forEach((item) => item.classList.remove("is-expanded"));
  };

  const expandItem = (item) => {
    const alreadyExpanded = item.classList.contains("is-expanded");
    closeAll();
    if (!alreadyExpanded) {
      item.classList.add("is-expanded");
      grid.classList.add("has-expanded");
      document.body.classList.add("portfolio-expanded");
      item.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  };

  grid.addEventListener("click", (event) => {
    const closeBtn = event.target.closest(".portfolio-close");
    if (closeBtn) {
      event.preventDefault();
      closeAll();
      return;
    }

    const preview = event.target.closest(".portfolio-preview");
    if (!preview) return;

    const item = preview.closest(".portfolio-item");
    if (item) {
      expandItem(item);
    }
  });

  grid.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") return;

    const preview = event.target.closest(".portfolio-preview");
    if (!preview) return;

    event.preventDefault();
    const item = preview.closest(".portfolio-item");
    if (item) {
      expandItem(item);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeAll();
    }
  });
}

(function () {
  const savedTheme = localStorage.getItem("theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  setThemeClass(savedTheme || (prefersDark ? "dark" : "light"));
})();

if (themeBtn) {
  themeBtn.addEventListener("click", () => {
    const darkActive = document.body.classList.contains("dark-mode");
    setThemeClass(darkActive ? "light" : "dark");
  });
}

function initPage() {
  const initialLang = document.documentElement.lang || "pl";
  updateFlagIcon(initialLang);
  initPortfolioExpand();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initPage);
} else {
  initPage();
}
