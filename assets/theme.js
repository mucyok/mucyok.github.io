// Bouton clair / sombre. Par défaut, le site suit le réglage du système
// (qui peut lui-même basculer au coucher du soleil). Un choix manuel ne vaut
// que pour la visite en cours : à la visite suivante, retour à l'automatique.
document.addEventListener("click", e => {
  if (!e.target.closest(".theme-toggle")) return;
  const root = document.documentElement;
  const systemDark = matchMedia("(prefers-color-scheme: dark)").matches;
  const dark = root.dataset.theme ? root.dataset.theme === "dark" : systemDark;
  const next = dark ? "light" : "dark";
  try {
    if ((next === "dark") === systemDark) {  // retour au réglage du système
      delete root.dataset.theme; sessionStorage.removeItem("theme");
    } else {
      root.dataset.theme = next; sessionStorage.setItem("theme", next);
    }
  } catch (err) { root.dataset.theme = next; }
});
