# Website Workflow Guide

How to make changes to this Jekyll website and deploy it to GitHub Pages.

---

## 🖥️ Local Development

### Build & Serve
```bash
bundle exec jekyll serve --port 4001 --host 0.0.0.0
```
- Site at **http://localhost:4001**
- If port 4001 is busy, try another: `--port 4002`
- Add `--drafts` to include draft posts (in `_drafts/` folder)

### Build only (no server)
```bash
bundle exec jekyll build
```
Output goes to `_site/` folder.

---

## 📝 Making Changes (Common Scenarios)

### Adding a new paper
1. Add the BibTeX entry to `_bibliography/papers.bib`
2. Add `year = {YYYY}` in the entry
3. **Check** `_pages/papers.md` — the `years:` list on line 9 must include the paper's year
4. Add the PDF to `assets/pdf/papers/` (if referenced in the bib entry)
5. Add the HTML detail page to `_papersgallery/` (if referenced via `html=` field)

### Adding a new publication year
Edit `_pages/papers.md` and add the year to the `years:` list (line 9).

### Adding a blog post
Add a markdown file to `_posts/` with format: `YYYY-MM-DD-title.md`

### Adding a project
Edit `_data/projects.yml` and add images to `assets/img/projects/`.

---

## 🚀 Deploying to GitHub Pages

> ⚠️ **Important:** The deploy repo is at `~/Website/WebsiteTemplate/` (branch `gh-pages`).
> It is a *separate git repo* — it does NOT push the source code, only the built static site.

### Step-by-step deploy

```bash
cd ~/Website/PersonalWebsite

# 1. Build the site fresh
bundle exec jekyll build

# 2. Clean the deploy repo (preserve .git)
cd ~/Website/WebsiteTemplate
git rm -r --cached . 2>/dev/null
find . -not -path './.git/*' -not -name '.git' -delete

# 3. Copy built files to deploy repo
cp -r ~/Website/PersonalWebsite/_site/* .

# 4. Prevent GitHub Pages from re-building
touch .nojekyll

# 5. Commit and push
git add .
git commit -m "update site $(date +%Y-%m-%d)"
git push
```

---

## ⚠️ Troubleshooting

### Port already in use
```bash
fuser -k 4001/tcp
# or kill the process using the port
```

### Site is stale / not updating on GitHub
- Wait **1-10 minutes** — GitHub Pages has a cache
- Make sure `.nojekyll` exists at the root of the deploy repo
- Check that `git push` completed successfully

### "nothing to commit, working tree clean"
You missed a step in the deploy process — likely didn't rebuild or recopy. Re-run from step 1.

### Page not showing a paper
1. Is the year in the BibTeX `year = {YYYY}` correct?
2. Is that year included in `_pages/papers.md` → `years:` list?
3. Did you rebuild before deploying?

### "directory is already being watched" warning
Add the offending directory to `exclude:` in `_config.yml`. E.g.:
```yaml
exclude:
  - coding
```

---

## 📁 Key Files & Their Locations

| File | Purpose |
|---|---|
| `_config.yml` | Main site configuration |
| `_bibliography/papers.bib` | All publication entries |
| `_pages/papers.md` | Papers page template + years list |
| `_data/` | YAML data files for projects, news, etc. |
| `_posts/` | Blog posts |
| `_papersgallery/` | Individual paper detail pages |
| `assets/img/papers/cover/` | Paper cover images |
| `assets/img/papers/extract/` | Paper extract images |
| `assets/pdf/papers/` | Paper PDFs |
