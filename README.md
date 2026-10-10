# Noticed
**Outside for a minute. Noticed for a day.**

Noticed is a small photo diary that runs on your own computer. You add a photo from your walk, and a local open-source vision model (Gemma 3 through Ollama) writes a short caption for it.

Once a day, step outside and take one photo of whatever catches your eye. Noticed keeps it with a short caption, so you build a gallery of small moments instead of a feed to scroll.

Built for the Hacktoberfest Open-Source AI Challenge, Week 1 ("Touch Grass").

## TechStack I used:
- **Model:** [Gemma 3 4B](https://ollama.com/library/gemma3) (open-weight vision model), run locally with [Ollama](https://ollama.com)
- **Backend:** Python, [Flask](https://flask.palletsprojects.com) (routes and Jinja templates)
- **Frontend:** plain HTML, CSS, and a little JavaScript, with no frameworks
- **Storage:** photos in a folder and entries in a JSON file, with no database

## Why it's local

- Photos and captions never leave your computer.
- Location data (EXIF/GPS) is stripped from every photo you upload.
- No accounts, no analytics, no API keys.
- The page loads its fonts from Google Fonts; everything else is local.



## Requirements

- Python 3.9+
- [Ollama](https://ollama.com)

## Setup

1. Download Model
```bash
ollama pull gemma3:4b
```
<br>

2. Clone this Repository and Install Python Modules
```bash
pip install flask pillow ollama
```
<br>

3. Run the App (from the project's root directory)
```bash
python3 app.py
```

Open http://127.0.0.1:5000 and click today's tile to add a photo. The first caption can take up to a minute while the model loads.



## How it works

1. `photo.py` fixes rotation, drops metadata, saves the photo as a JPG, and returns its average color.
2. `caption.py` sends the photo to the local model and returns a one-line caption.
3. `app.py` saves each entry to `data/diary.json` and serves the page.


## Notes

- Captions are AI-generated.
- To use another vision model, change `MODEL` in `caption.py`.
- `data/` directory contains your photos and diary.json (created on first run). So you can delete it if you want to reset everything.