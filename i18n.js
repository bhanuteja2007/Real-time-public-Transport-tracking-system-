let userLang = localStorage.getItem("lang") || 'en';

function setLang(lang) {
  userLang = lang;
  localStorage.setItem("lang", lang);
  applyTranslations();
}

function applyTranslations() {
  let t = translations_en;  // default
  if (userLang === 'ta') t = translations_ta;
  // add other languages similarly

  document.documentElement.lang = userLang;

  document.querySelectorAll("[data-i18n]").forEach(elem => {
    const key = elem.getAttribute("data-i18n");
    if (t[key]) {
      elem.innerText = t[key];
    }
  });
}

window.addEventListener("DOMContentLoaded", () => {
  applyTranslations();
});
