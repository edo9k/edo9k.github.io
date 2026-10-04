# eeff.com.br

Source for my GitHub Pages site, live at **[eeff.com.br](https://eeff.com.br/)**
(served from the `CNAME` file).

## The site

A bilingual curriculum vitae for **Eduardo França** — software and cloud engineer.

- `index.html` — the CV: summary, work experience, other work, education,
  technologies and languages.
- `assets/style.css` — layout, theming (light/dark), responsive and print rules.
- `assets/site.js` — language toggle, print button and nav highlighting.

### Languages

The CV is available in **English** and **Portuguese**, switched by the pill
toggle in the header. The visitor's choice is stored in `localStorage`
(`cv-lang`) and defaults to the browser language.

Content is translated inline: every translatable fragment is a
`<span lang="en">` / `<span lang="pt">` pair, and the stylesheet shows only the
pair matching `<html lang>`. The swap therefore works even before JavaScript
runs, and degrades to English with JS disabled.

### Other content

- `slides/` — lecture notes, exercises and quizzes.
- `archive/` — previous version of the landing page plus unused images
  (`cat.jpg`, `cheetos-security.jpg`, `self-qr.png`).

## Local preview

Any static server works, but absolute asset paths (`/assets/…`) need one that
resolves them from the site root:

```sh
python3 -m http.server 8000
# then open http://localhost:8000/
```

## Deploy

The site is published by GitHub Pages from this repository — nothing to build,
the HTML is served as-is. To publish changes, push to `main`.

## License

Copyleft — see `LICENSE`.