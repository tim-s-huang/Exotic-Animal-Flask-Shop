# Exotic Animal Flask Shop

An online exotic animal shop built with Python, Flask, SQLite, HTML and CSS for the Web Applications module of my Computer Science BSc at Cardiff University, 2023.

<img width="1860" height="943" alt="Flask Shop" src="https://github.com/user-attachments/assets/49691cea-648a-4a11-b13d-bf1b7554edf1" />

## Features
- Product pages for six unique animals, loaded from an SQLite database
- A shopping basket stored in SQLite so items stay between webpages
- Checkout with card-number validation

## Run Locally
```bash
git clone https://github.com/tim-s-huang/exotic-animal-flask-shop.git
cd exotic-animal-flask-shop
python -m venv .venv
source .venv/Scripts/activate    # Windows (Git Bash)
pip install -r requirements.txt
python main.py
```
Then open http://127.0.0.1:5000 in a browser

All images are from [Unsplash](https://unsplash.com/). No animals were harmed in the making of this website.
