🧠 Emotion-Based Recommender System

A simple AI-powered web app that recommends music and books based on your selected mood 🎭.
Built using Python (Flask) for the backend and HTML/CSS/JS for the frontend.

🌟 Features

🎭 Choose from 5 moods — Happy, Sad, Angry, Relaxed, Excited

🎵 Get music recommendations based on mood

📚 Get book suggestions according to mood

🔄 Click Refresh to get 5 new suggestions

💡 Clean and minimal UI built with HTML, CSS, and Flask

⚠️ Current Status

✅ Working:

Music recommendations

Book recommendations

🚧 Planned (Not yet implemented):

Movie recommendations

Food recipe recommendations

If you want to add these, simply prepare new CSV files (similar to books_clean.csv or music_clean.csv)
and place them inside the data/ folder.

🏗️ Tech Stack
Component	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python (Flask)
Data	CSV datasets (from Kaggle)
Libraries	pandas, random, flask
📂 Project Structure
emotion_recommender/
│
├── app.py                   # Flask backend
├── templates/
│   └── index.html           # Main UI
├── static/
│   ├── style.css            # Styling
│   └── script.js            # Optional JS
├── data/
│   ├── books_clean.csv
│   ├── music_clean.csv
│   ├── movies_clean.csv     # (Optional – can add later)
│   └── food_clean.csv       # (Optional – can add later)
├── prepare_music.py         # Example script to clean raw music data
└── README.md

⚙️ Setup & Run
1️⃣ Clone this repo
git clone https://github.com/YOUR-USERNAME/emotion-recommender.git
cd emotion-recommender

2️⃣ Install dependencies
pip install flask pandas

3️⃣ Prepare datasets

Make sure you have books_clean.csv and music_clean.csv in the data/ folder.

To clean music data from Kaggle, run:

python prepare_music.py

4️⃣ Run the app
python app.py


If port 5000 is busy:

python app.py --port=5001


Then open your browser and go to:
👉 http://127.0.0.1:5000 (or the port you used)

💾 Example CSV Format

books_clean.csv

title,description,mood
Harry Potter,J.K. Rowling | Fantasy,excited
The Fault in Our Stars,John Green | Romance,sad


music_clean.csv

title,description,mood
Shape of You,Artist: Ed Sheeran | Album: Divide,excited
Someone Like You,Artist: Adele | Album: 21,sad


If you want to add more categories (movies, recipes),
just follow the same structure and ensure the CSV has:

title,description,mood

🚀 Future Improvements

Add emotion detection (AI model for automatic mood recognition)

Add movies & recipes support

Add user login and favorites

Enhance frontend with React or Tailwind CSS

👨‍💻 Author

Ometh Hettiarachchi
📧 omethhettiarachchi@gmail.com
]
💻 GitHub Profile

🪪 License

Open-source under the MIT License — free to use and modify.
