// Bouton clair / sombre : par défaut le site suit le réglage du système.
document.addEventListener("click", e => {
  if (!e.target.closest(".theme-toggle")) return;
  const root = document.documentElement;
  const dark = root.dataset.theme
    ? root.dataset.theme === "dark"
    : matchMedia("(prefers-color-scheme: dark)").matches;
  root.dataset.theme = dark ? "light" : "dark";
  try { localStorage.setItem("theme", root.dataset.theme); } catch (err) {}
});
