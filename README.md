# Flask-Online-Shop

An online exotic animal shop built with Python, Flask, SQLite, HTML and CSS for the Web Applications module of my Computer Science BSc at Cardiff University, 2023

![Screenshot of the shop]()

## Features
- Product pages for six unique animals, loaded from an SQLite database
- A shopping basket stored in SQLite so items stay between webpages
- Checkout with card-number validation

## Run Locally
```bash
git clone https://github.com/tim-s-huang/Flask-Online-Shop.git
cd Flask-Online-Shop
python -m venv .venv
source .venv/Scripts/activate    # Windows (Git Bash); use source .venv/bin/activate on Mac/Linux
pip install -r requirements.txt
python main.py
```
Then open http://127.0.0.1:5000 in a rbowser

All images are from [Unsplash](https://unsplash.com/). No animals were harmed in the making of this website.
