"""Génère les pages HTML du site à partir du contenu ci-dessous.

Usage : python3 build.py
Le contenu est repris de mucyo.net (pas à jour, septembre 2026).
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

# ---------------------------------------------------------------- contenu

NAME = "Mucyo Karemera"
ROLES = ["Senior Research Associate in Statistics"]
AFFILIATION = "University of Geneva"

# Micro bio de l'accueil
LAB = ("Data Analytics Lab", "https://stephaneguerrier.com/")
BIO_HTML = (  # HTML : contient un lien
    f'I work in the {LAB[0]} led by <a href="{LAB[1]}">Prof. Stéphane Guerrier</a>. '
    "My research develops statistical methodology for simulation-based inference and equivalence "
    "testing, applied to complex data problems in pharmaceutical sciences, robotics, and finance. "
    "I came to statistics from pure mathematics, with a Ph.D. in quantum topology."
)
AREAS = ("simulation-based inference, equivalence testing, fairness in AI, "
         "time series & signal processing, quantum topology")

# Page Research : (domaine, description courte)
RESEARCH_INTRO = (
    "My work sits between mathematical statistics and its applications. "
    "A common thread is inference that stays accurate when samples are small, "
    "models are complex, or the question is to show that two things are practically the same."
)
RESEARCH = [
    ("Simulation-based inference",
     "iterative bootstrap, bias correction in high dimensional settings, "
     "accurate parametric inference in finite samples."),
    ("Equivalence testing",
     "TOST procedures and their asymptotic theory, multivariate and adaptive designs, "
     "bioequivalence, and certification of algorithmic fairness."),
    ("Time series & signal processing",
     "wavelet variance methods, stochastic calibration of inertial sensors."),
    ("Quantum topology",
     "quantum invariants of 3-manifolds and links, 6j-symbols, the matrix dilogarithm."),
]

# Barre d'essai des photos sur l'accueil (mettre False pour le site final)
ESSAI_PHOTOS = False
PHOTO_CREDIT = "Aurélien Bergot"
PHOTO_CREDIT_URL = "https://www.aurelienbergot.com/"
EMAIL = "Mucyo.Karemera@unige.ch"
GITHUB = "https://github.com/mucyok"
SCHOLAR = "https://scholar.google.com/citations?hl=en&user=Ib6k-fgAAAAJ"
LINKEDIN = "https://www.linkedin.com/in/mucyo-karemera-80ab60377/"

INTERESTS = [
    "Quantum topology",
    "Representation theory",
    "Topological data analysis",
    "Quantum algorithms",
    "Mathematical statistics",
    "High-dimensional data analysis",
    "Signal processing",
    "Differential privacy and statistical disclosure control",
]

POSITIONS = [  # condensé (détail dans le CV)
    ("since 2026", "Senior Research Associate",
     "Faculty of Science, University of Geneva"),
    ("2022 to 2026", "Research Associate",
     "Geneva School of Economics and Management, then Faculty of Science, University of Geneva"),
    ("2018 to 2022", "Postdoctoral Scholar in Statistics & Lecturer in Mathematics",
     "Pennsylvania State University, University of Geneva, and Auburn University"),
    ("2016 to 2018", "Mathematics Teacher",
     "Centre de formation professionnelle arts (CFP Arts), Geneva"),
]

EDUCATION = [
    ("2016", "Ph.D., Mathematics", "University of Geneva, Switzerland"),
    ("2009", "M.Sc., Mathematics", "University of Geneva, Switzerland"),
    ("2006", "B.Sc., Mathematics", "University of Geneva, Switzerland"),
]

# (groupe, [(auteurs, titre, revue ou support, année, lien)])
# Source : Google Scholar, septembre 2026 (résumés de conférence omis).
PUBLICATIONS = [
    ("Journal articles", [
        ("Balbinot, F., Voirol, L., Guerrier, S., Karemera, M., Feser, R., Baroffio, A. & Gerbase, M. W.",
         "Unveiling empathy determinants across borders: a comparative analysis of medical students from two geo-sociocultural backgrounds",
         "BMC Medical Education, 25(1), 554", "2025", "https://doi.org/10.1186/s12909-025-07109-7"),
        ("Karemera, M., Voirol, L., Cucci, D. A., Chu, W., Molinari, R. & Guerrier, S.",
         "Accounting for vibration noise in stochastic measurement errors of inertial sensors",
         "IEEE Transactions on Signal Processing, 72", "2024", "https://doi.org/10.1109/tsp.2024.3387313"),
        ("Pfarrwaller, E., Voirol, L., Karemera, M., Guerrier, S. & Baroffio, A.",
         "Dynamics of career intentions in a medical student cohort: a four-year longitudinal study",
         "BMC Medical Education, 23(1), 131", "2023", "https://doi.org/10.1186/s12909-023-04102-w"),
        ("Miglioli, C., Bakalli, G., Orso, S., Karemera, M., Molinari, R., Guerrier, S. & Mili, N.",
         "Evidence of antagonistic predictive effects of miRNAs in breast cancer cohorts through data-driven networks",
         "Scientific Reports, 12(1), 5166", "2022", "https://doi.org/10.1038/s41598-022-08737-5"),
        ("Pfarrwaller, E., Voirol, L., Piumatti, G., Karemera, M., Sommer, J., Gerbase, M. W., Guerrier, S. & Baroffio, A.",
         "Students' intentions to practice primary care are associated with their motives to become doctors: a longitudinal study",
         "BMC Medical Education, 22(1), 30", "2022", "https://doi.org/10.1186/s12909-021-03091-y"),
        ("Guerrier, S., Jurado, J., Khaghani, M., Bakalli, G., Karemera, M., Molinari, R., Orso, S., Raquet, J., Schubert Kabban, C., Skaloud, J., Xu, H. & Zhang, Y.",
         "Wavelet-based moment-matching techniques for inertial sensor calibration",
         "IEEE Transactions on Instrumentation and Measurement, 69(10)", "2020", "https://doi.org/10.1109/tim.2020.2984820"),
        ("Xu, H., Guerrier, S., Molinari, R. & Karemera, M.",
         "Multivariate signal modeling with applications to inertial sensor calibration",
         "IEEE Transactions on Signal Processing, 67(19)", "2019", "https://doi.org/10.1109/tsp.2019.2935902"),
    ]),
    ("Conference proceedings", [
        ("Voirol, L., Guerrier, S., Zhang, Y., Karemera, M. & Radi, A.",
         "Optimally weighted wavelet variance-based estimation for inertial sensor stochastic calibration",
         "12th International Conference on Electrical Engineering (ICEENG), Cairo, Egypt", "2020", "https://doi.org/10.1109/iceeng45378.2020.9171715"),
        ("Zhang, Y., Xu, H., Radi, A., Molinari, R., Guerrier, S., Karemera, M. & El-Sheimy, N.",
         "An optimal virtual inertial sensor framework using wavelet cross covariance",
         "IEEE/ION Position, Location and Navigation Symposium (PLANS), Monterey, CA, USA", "2018", "https://doi.org/10.1109/plans.2018.8373525"),
    ]),
    ("Preprints", [
        ("Orso, S., Karemera, M., Victoria-Feser, M.-P. & Guerrier, S.",
         "An accurate percentile method for parametric inference based on asymptotically biased estimators",
         "arXiv:2405.05403", "2024", "https://arxiv.org/abs/2405.05403"),
        ("Zhang, Y., Ma, Y., Orso, S., Karemera, M., Victoria-Feser, M.-P. & Guerrier, S.",
         "Just identified indirect inference estimator: accurate inference through bias correction",
         "arXiv:2204.07907", "2022", "https://arxiv.org/abs/2204.07907"),
        ("Karemera, M.", "sl(3) matrix dilogarithm as a 6j-symbol",
         "arXiv:2010.14633", "2020", "https://arxiv.org/abs/2010.14633"),
        ("Molinari, R., Bakalli, G., Guerrier, S., Miglioli, C., Orso, S., Karemera, M. & Scaillet, O.",
         "SWAG: a wrapper method for sparse learning",
         "arXiv:2006.12837", "2020", "https://arxiv.org/abs/2006.12837"),
    ]),
    ("Working papers", [
        ("Guerrier, S., Hurlin, C., Karemera, M., Pérignon, C. & Saurin, S.",
         "A statistical certification framework for fairness testing", None, None, None),
        ("Karemera, M., Insolia, L. & Guerrier, S.",  # titre repris du CV
         "Optimal adjustment for bioequivalence assessment in heteroskedastic scenarios", None, None, None),
    ]),
    ("Ph.D. thesis", [
        ("Karemera, M.", "Quantum invariants of 3-manifolds from a quantum group related to U_q(sl_3)",
         "University of Geneva, advisor: Prof. R. Kashaev", "2016", "https://archive-ouverte.unige.ch/unige:143756"),
    ]),
]

TEACHING_INTRO = "Public courses and teaching materials."

# Du plus récent au plus ancien. "with" et "links" contiennent du HTML.
TEACHING = [
    dict(when="In development", title="Voir clair en mathématiques : intuition, approximation et optimisation",
         url=None, lang="en français", level="MOOC · University of Geneva · expected Spring 2027",
         desc="Open online course on mathematical intuition, approximation, and optimization, designed for a broad audience.",
         with_='Principal investigator · University of Geneva Rectorate grant, CHF&nbsp;50,000<br>'
               'With <a href="https://www.ihes.fr/~duminil/">Prof. H. Duminil-Copin</a> '
               '&amp; <a href="https://stephaneguerrier.com/">Prof. S. Guerrier</a>',
         links=[]),
    dict(when="September 2026", title="Descriptive Statistics and Statistical Inference",
         url="https://mucyok.github.io/das-clinical-trials-statistics/",  # adresse provisoire
         lang=None, level="Continuing education · DAS in Management of Clinical Trials, University of Geneva",
         desc="Four lectures on descriptive statistics, confidence intervals, hypothesis testing, and errors, power "
              "and multiple testing, built around a published randomised trial.",
         with_='With <a href="https://stephaneguerrier.com/">Prof. S. Guerrier</a>',
         links=[("slides", "https://mucyok.github.io/das-clinical-trials-statistics/")]),
    dict(when="Since 2025", title="Introduction à la Statistique",
         url="https://intro-statistique.netlify.app/", lang="en français", level="Undergraduate · University of Geneva",
         desc="First undergraduate course in statistics: probability, random variables, distributions, estimation, "
              "confidence intervals, and hypothesis testing. Built around an AI-powered interactive learning platform.",
         with_='With <a href="https://stephaneguerrier.com/">Prof. S. Guerrier</a>, Dr. S. Orso, '
               '<a href="https://lionelvoirol.com/">Dr. L. Voirol</a> &amp; <a href="https://sebastienfeser.ch/">S. Feser</a>',
         links=[("visit the platform", "https://intro-statistique.netlify.app/")]),
    dict(when="2020/2021", title="Mathematics I",
         url="https://mkaremera-math1.netlify.app", lang="en français",
         level="Undergraduate · Geneva School of Economics and Management, University of Geneva",
         desc="First-year calculus course for about 600 students in economics and management, "
              "with complete online material and video lectures.",
         with_='With <a href="https://stephaneguerrier.com/">Prof. S. Guerrier</a>',
         links=[("course materials", "https://mkaremera-math1.netlify.app"),
                ("videos on YouTube", "https://www.youtube.com/channel/UCwXJdhGBTzvvTlffkQv-Cjw")]),
]

SOFTWARE = [
    ("wv", "https://smac-group.github.io/wv/",
     "Methods related to the wavelet variance, including the multivariate approaches of Zhang et al. (2018) and Xu et al. (2019)."),
    ("cape", "https://stephaneguerrier.github.io/cape/",
     "Conditional prevalence estimation from random and non-random samples (Guerrier, Kuzmics and Victoria-Feser, 2020)."),
]

# ---------------------------------------------------------------- gabarits

PAGES = [  # (fichier, onglet)
    ("biography.html", "Biography"),
    ("publications.html", "Publications"),
    ("teaching.html", "Teaching"),
]
HIDDEN_PAGES = [("research.html", "Research"), ("software.html", "Software")]
CV_PDF = "assets/Mucyo_Karemera_CV.pdf"  # générées, mais absentes du menu

ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22,6 12,13 2,6"/></svg>'
ICON_SCHOLAR = '<svg viewBox="0 0 24 26" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5.242 13.769L0.5 9.5 12 1l11.5 9-5.242 3.769C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 1 0 0 14 7 7 0 0 0 0-14z"/></svg>'
ICON_LINKEDIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>'
THEME_BUTTON = (
    '<button class="theme-toggle" type="button" title="Light / dark mode" aria-label="Toggle dark mode">'
    '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
    '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
    '</button>'
)
ICON_GITHUB = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>'


def head(title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(NAME)}, {escape(' and '.join(ROLES))}, {escape(AFFILIATION)}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<script src="assets/theme.js" defer></script>
</head>
<body>
"""


def icons():
    return (f'<div class="icons"><a href="mailto:{EMAIL}" title="Email">{ICON_MAIL}</a>'
            f'<a href="{SCHOLAR}" title="Google Scholar">{ICON_SCHOLAR}</a>'
            f'<a href="{GITHUB}" title="GitHub">{ICON_GITHUB}</a>'
            f'<a href="{LINKEDIN}" title="LinkedIn">{ICON_LINKEDIN}</a></div>')


def nav(current=None):
    return "".join(
        f'<a href="{f}"{" class=on" if f == current else ""}>{label}</a>' for f, label in PAGES
    ) + f'<a href="{CV_PDF}" target="_blank" rel="noopener">CV</a>'


def cv(rows):
    items = "".join(
        f'<li><span class="cv-when">{when}</span><span><b>{escape(what)}</b><br>{escape(where)}</span></li>'
        for when, what, where in rows)
    return f'<ul class="cv">{items}</ul>'


def cv2(rows):
    items = "".join(
        f'<li><span class="cv-when">{when}</span><b>{escape(what)}</b><span>{escape(where)}</span></li>'
        for when, what, where in rows)
    return f'<ul class="cv2">{items}</ul>'


def pub(authors, title, venue, year, url):
    a = escape(authors).replace("Karemera, M.", "<strong>Karemera, M.</strong>")
    t = f'<a href="{url}">{escape(title)}</a>' if url else escape(title)
    v = ", ".join(escape(x) for x in (venue, year) if x)
    return (f'<li><span class="pub-t">{t}</span><span class="pub-a">{a}</span>'
            + (f'<span class="pub-v">{v}</span>' if v else "") + "</li>")


def teach(t):
    title = f'<a href="{t["url"]}">{escape(t["title"])}</a>' if t["url"] else escape(t["title"])
    lang = f' <span class="teach-lang">({t["lang"]})</span>' if t["lang"] else ""
    links = "".join(f' · <a href="{u}">{label} →</a>' for label, u in t["links"])
    return (f'<li><span class="cv-when">{t["when"]}</span><div>'
            f'<div class="teach-t">{title}{lang}</div>'
            f'<div class="teach-l">{escape(t["level"])}</div>'
            f'<p>{escape(t["desc"])}</p>'
            f'<div class="teach-w">{t["with_"]}{links}</div></div></li>')


def header(current=None):
    return (f'<header class="top"><a class="name" href="index.html">{NAME}</a>'
            f"<nav>{nav(current)}{THEME_BUTTON}</nav></header>")


def inner_page(filename, label, body):
    return (head(f"{label} · {NAME}")
            + f'<div class="wrap">{header(filename)}'
            + f"<main><h1>{label}</h1>{body}</main>"
            + "</div>\n"
            + "</body>\n</html>\n")


def build():
    home = (head(NAME)
            + f'<div class="wrap">{header()}<div class="home"><div class="hero">'
            + f'<figure class="photo"><img src="assets/portrait_carre.jpg" alt="{NAME}">'
            + f'<figcaption>Photo: <a href="{PHOTO_CREDIT_URL}">{PHOTO_CREDIT}</a></figcaption></figure>'
            + f'<div class="txt"><h1>{NAME}</h1>'
            + f'<p class="role">{", ".join(ROLES)}, {AFFILIATION}</p>'
            + f'<p class="bio">{BIO_HTML}</p>'
            + f'<p class="bio"><b>Research areas:</b> {escape(AREAS)}.</p>'
            + icons()
            + "</div></div></div></div>\n"
            + ('<script src="assets/essai.js"></script>\n' if ESSAI_PHOTOS else "")
            + "</body>\n</html>\n")

    bodies = {
        "research.html": f"<p>{escape(RESEARCH_INTRO)}</p><h2>Main research areas</h2><ul class=\"areas\">"
            + "".join(f"<li><b>{escape(a)}:</b> {escape(d)}</li>" for a, d in RESEARCH) + "</ul>",
        "biography.html": '<div class="bio-cols">'
            f"<section><h2>Positions</h2>{cv2(POSITIONS)}</section>"
            f"<section><h2>Education</h2>{cv2(EDUCATION)}</section></div>",
        "publications.html": "".join(
            f'<h2>{group}</h2><ul class="pubs">{"".join(pub(*p) for p in items)}</ul>'
            for group, items in PUBLICATIONS),
        "teaching.html": f"<p>{escape(TEACHING_INTRO)}</p>" + '<ul class="teach">' + "".join(teach(t) for t in TEACHING) + "</ul>",
        "software.html": '<ul class="soft">' + "".join(
            f'<li><a href="{url}"><code>{n}</code></a><span class="soft-tag">R package</span><p>{escape(d)}</p></li>'
            for n, url, d in SOFTWARE) + "</ul>",
    }

    (ROOT / "index.html").write_text(home, encoding="utf-8")
    for filename, label in PAGES + HIDDEN_PAGES:
        (ROOT / filename).write_text(inner_page(filename, label, bodies[filename]), encoding="utf-8")
    print("Pages générées :", ", ".join(["index.html"] + [f for f, _ in PAGES + HIDDEN_PAGES]))


if __name__ == "__main__":
    build()
