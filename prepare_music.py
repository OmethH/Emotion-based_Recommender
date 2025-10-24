import pandas as pd
import random
import os

# Basic moods to assign
MOODS = ['happy', 'sad', 'angry', 'relaxed', 'excited']

RAW_PATH = 'data/music.csv'       # your original Kaggle CSV
CLEAN_PATH = 'data/music_clean.csv'

# --- 1️⃣ Load dataset ---
try:
    df = pd.read_csv(RAW_PATH)
    print(f"✅ Loaded raw dataset with {len(df)} rows")
except FileNotFoundError:
    print(f"❌ File not found: {RAW_PATH}")
    exit()

print("Available columns:", list(df.columns)[:10])

# --- 2️⃣ Select useful columns ---
# from your printout, these exist:
# ['Unnamed: 0', 'track_id', 'artists', 'album_name', 'track_name', 'popularity', ...]

# Create clean DataFrame
clean = pd.DataFrame()
clean['title'] = df['track_name'].astype(str)

# Build a readable description per row
clean['description'] = (
    "Artist: " + df['artists'].astype(str) + " | Album: " + df['album_name'].astype(str)
)

# --- 3️⃣ Assign moods ---
# We’ll map based on energy/danceability/popularity if possible
if {'energy', 'danceability', 'popularity'}.issubset(df.columns):
    def assign_mood(row):
        energy = row['energy']
        dance = row['danceability']
        pop = row['popularity']

        if energy > 0.7 and dance > 0.6:
            return 'excited'
        elif energy < 0.4 and dance < 0.4:
            return 'sad'
        elif dance > 0.6 and energy < 0.6:
            return 'happy'
        elif energy < 0.3:
            return 'relaxed'
        else:
            return random.choice(MOODS)

    clean['mood'] = df.apply(assign_mood, axis=1)
else:
    clean['mood'] = [random.choice(MOODS) for _ in range(len(clean))]

# --- 4️⃣ Save clean file ---
os.makedirs('data', exist_ok=True)
clean.to_csv(CLEAN_PATH, index=False)

print(f"✅ Saved cleaned file to {CLEAN_PATH}")
print(clean.head())
