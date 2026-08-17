# Gelana Abdisa — Personal Portfolio (Streamlit)

An interactive personal portfolio dashboard built with **Streamlit**,
showing education, experience, skills, and projects — meant to be shared as
a live link with anyone who wants to know more about me.

## Project structure

```
portfolio/
├── app.py              # Streamlit dashboard (all content is edited here)
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

## Before you run it: edit your content

Open `app.py` in any text editor and edit the values near the top, under the
`CONTENT` section — your name, title, about text, education, experience,
skills, projects, and contact links (email, LinkedIn, GitHub). Everything on
the page comes from those variables, so you don't need to touch any of the
layout code below it.

---

## Step-by-step: run it locally, then publish to GitHub

### 1. Install prerequisites (one-time setup)

- **Python 3.9+** — from [python.org](https://www.python.org/downloads/).
  On Windows, check "Add Python to PATH" during install.
- **Git** — from [git-scm.com](https://git-scm.com/downloads).
- A **GitHub account** (you already have one).

Check both are installed:
```bash
python --version
git --version
```

### 2. Create your project folder

Create a folder, e.g. `portfolio`, and put these files inside it:
- `app.py`
- `requirements.txt`
- `.gitignore`
- `README.md`

### 3. Open a terminal in that folder

```bash
cd path/to/portfolio
```

### 4. Create and activate a virtual environment

```bash
python -m venv venv
```

Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the app locally

```bash
streamlit run app.py
```

This opens the dashboard in your browser at `http://localhost:8501`. Check
that everything looks right — edit `app.py` and save to see changes (refresh
the browser tab, or click "Rerun" if Streamlit prompts you).

Press `Ctrl+C` in the terminal to stop the app.

### 7. Put your project on GitHub (public repo)

**a) Create the repository on GitHub:**
1. Go to [github.com](https://github.com) and log in.
2. Click **+** (top right) → **New repository**.
3. Name it, e.g. `portfolio`.
4. Set visibility to **Public**.
5. Leave "Add a README" unchecked (you already have one).
6. Click **Create repository**.

**b) Push your local project:**

```bash
git init
git add .
git commit -m "Initial commit: personal portfolio dashboard"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/portfolio.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If `origin` already
exists from a previous project in this same folder, skip the `git remote
add` line.

**c) Refresh your GitHub repo page** — your files should now be visible there.

### 8. Deploy it live (free) so you can share a link

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
2. Click **New app**.
3. Select your `portfolio` repository, branch `main`, main file `app.py`.
4. Click **Deploy**.

After a minute or two, Streamlit gives you a public URL (something like
`https://your-app-name.streamlit.app`) — that's the link you share with
anyone who wants to see your portfolio.

Any time you edit `app.py`, commit and push the change:
```bash
git add .
git commit -m "Update portfolio content"
git push
```
Streamlit Cloud automatically redeploys with your latest changes.

---

## Notes

- No dataset or model is needed for this app — it's pure content + layout.
- Keep your contact details (email, phone) truthful but only as public as
  you're comfortable with, since this page will be public on the internet.
