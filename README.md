# Kelly Technologies — Official Website

Static one-pager for **Kelly Technologies Limited** (kellytec.io).

**Design language.** Dark aubergine base (`#1A1530`) with a soft orchid
accent (`#B89BE0`), punctuated by warm bone-white sections (`#F1ECEF`)
with a deep plum accent (`#5B2C6F`). Display type is Fraunces (serif),
body is Inter, monospace tags use JetBrains Mono — generous whitespace
and serif italics carry an editorial / institutional feel without being
visually loud.

The two light sections (Team, Contact) intentionally break the long dark
spine so the eye gets rhythm and the founders read as warm and
approachable.

A live palette study lives at `palettes.html` if we ever want to retheme.

## Stack

- Pure HTML / CSS / JS — no build step, no framework
- Google Fonts: Fraunces (display serif), Inter (sans), JetBrains Mono
- Hosted on GitHub Pages

## Local preview

```bash
cd kellytec-website
python3 -m http.server 8000
# open http://localhost:8000
```

## Project structure

```
kellytec-website/
├── index.html          # single-page site
├── assets/
│   ├── styles.css      # design system + components
│   └── script.js       # nav scroll state + reveal animations
├── CNAME               # custom domain → kellytec.io
├── .nojekyll           # disable Jekyll on Pages (we ship raw files)
└── README.md
```

## Deploying to GitHub Pages

1. Create a new repo on GitHub, e.g. `kelly-technologies/website`
   (or use a personal repo named `<user>.github.io` for root deployment).
2. Initialize and push:

   ```bash
   cd kellytec-website
   git init -b main
   git add .
   git commit -m "Initial site"
   git remote add origin git@github.com:<org>/<repo>.git
   git push -u origin main
   ```

3. In the repo on GitHub:
   - Settings → **Pages**
   - Source: **Deploy from a branch**
   - Branch: `main` / root (`/`)
   - Save.
4. Within ~1 minute the site is live at
   `https://<org>.github.io/<repo>/` (or at `https://<user>.github.io/`
   for a `<user>.github.io` repo).

### Custom domain (kellytec.io)

The `CNAME` file already contains `kellytec.io`. To point the domain:

- At your DNS provider, set:
  - **Apex** (`kellytec.io`): four `A` records pointing to GitHub Pages IPs:
    - `185.199.108.153`
    - `185.199.109.153`
    - `185.199.110.153`
    - `185.199.111.153`
  - **www** (`www.kellytec.io`): `CNAME` → `<org>.github.io`
- In GitHub repo Settings → Pages → Custom domain: enter `kellytec.io`
  and enable **Enforce HTTPS** once the cert provisions.

## Editing content

All copy lives in `index.html` in semantic sections:

| Section ID    | Purpose                                  |
| ------------- | ---------------------------------------- |
| `#company`    | Overview, edge, technology, discipline   |
| `#team`       | Founder bios (TS / XX / PX)              |
| `#research`   | Research pipeline (4 stages)             |
| `#execution`  | Execution stack (algo / clearing / data) |
| `#strategies` | ALGO3 + ALGO5 summary cards              |
| `#contact`    | Email & address                          |

Design tokens (colors, fonts, spacing) are defined as CSS variables
at the top of `assets/styles.css` under `:root` — change them in one
place to retheme the whole site.
