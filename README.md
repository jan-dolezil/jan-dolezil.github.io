# Jan Doležil — personal homepage

Barebones static CV-style site (no blog) for `jan-dolezil.github.io`.

## Files

- `index.html` — the whole site, one page
- `style.css` — one tiny stylesheet, system fonts, no JavaScript anywhere
- `photo.jpg` — optimized portrait (~14 KB)
- `about.txt` — plain-text mirror of the facts (for humans, scrapers and LLMs)
- `robots.txt`, `sitemap.xml`, `favicon.ico`, `.nojekyll`

## Editing

Just edit `index.html` (and mirror key facts in `about.txt`). Keep it semantic:
one `<h1>`, section headings, real `<address>`, descriptive link text.

## Preview locally

```sh
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy

Push to `main` — `.github/workflows/deploy.yml` uploads the repo root directly
to GitHub Pages. No build step, no dependencies.
