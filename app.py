from flask import Flask, render_template, request, jsonify
import pandas as pd
import random

app = Flask(__name__)

# --- Load datasets ---
def load_dataset(file):
    df = pd.read_csv(file)
    df.columns = [c.strip().lower() for c in df.columns]
    if 'mood' in df.columns:
        df['mood'] = df['mood'].astype(str).str.strip().str.lower()
    return df

music = load_dataset('data/music_clean.csv')
books = load_dataset('data/books_clean.csv')

datasets = {
    'music': music,
    'books': books,
}

# --- Routes ---
@app.route('/')
def home():
    print("✅ Home route loaded")
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form['mood'].strip().lower()
    category = request.form['category'].strip().lower()
    print(f"User selected: Mood={mood}, Category={category}")

    df = datasets.get(category)
    if df is None:
        print("❌ Invalid category")
        return jsonify([])

    if 'mood' not in df.columns or len(df) == 0:
        print("❌ Dataset is empty or missing 'mood'")
        return jsonify([])

    filtered = df[df['mood'] == mood]

    if len(filtered) == 0:
        print("⚠️ No matches for this mood")
        return jsonify([])

    results = filtered.sample(min(5, len(filtered)))
    suggestions = results[['title', 'description']].to_dict(orient='records')

    print(f"✅ Returning {len(suggestions)} suggestions")
    return jsonify(suggestions)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
