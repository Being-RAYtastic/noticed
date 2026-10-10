import json
from pathlib import Path

from flask import Flask, render_template, redirect, request, url_for, send_from_directory

import uuid
from datetime import date,  datetime

from photo import save_clean_photo
from caption import make_caption

APP_NAME = "Noticed"

BASE = Path(__file__).parent
DIARY = BASE / "data" / "diary.json"
PHOTOS = BASE / "data" / "photos"

PHOTOS.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)

def load_diary():
    if not DIARY.exists():
        return[]
    return json.loads(DIARY.read_text())

def save_diary(entries):
    DIARY.write_text(json.dumps(entries, indent=2))


@app.route("/")
def index():
    entries = sorted(load_diary(), key=lambda e: e["date"], reverse=True)

    today = date.today().isoformat()
    done_today = any(e["date"] == today for e in entries)

    return render_template("index.html", app_name=APP_NAME, entries=entries, today=today, done_today=done_today)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("photo")

    if not file or file.filename == "":
        return redirect(url_for("index"))

    today = date.today().isoformat()   # 2026-10-10 => iso format date
    name = f"{today}--{uuid.uuid4().hex[:8]}.jpg"

    color = save_clean_photo(file, PHOTOS / name)  
    caption = make_caption(str(PHOTOS / name))

    entries = load_diary()
    entries.append({
        "date": today,
        "photo": name,
        "caption": caption or "",
        "color": color 
    })  

    save_diary(entries)

    return redirect(url_for("index"))

@app.template_filter("format_date")
def format_date(day):
    d = datetime.strptime(day, "%Y-%m-%d")
    return f"{d:%a} {d.day} {d:%b}, {d:%Y}"

@app.route("/photo/<name>")
def serve_photo(name):
    return send_from_directory(PHOTOS, name)


if __name__ == "__main__":
    app.run(debug=True)