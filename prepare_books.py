import pandas as pd
import random

# Load your original Kaggle books dataset
books = pd.read_csv('data/books.csv', low_memory=False)

# Keep relevant columns
books = books[['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']]

# Create a simple description
books['description'] = (
    "Written by " + books['Book-Author'].astype(str) +
    " | Published by " + books['Publisher'].astype(str) +
    " (" + books['Year-Of-Publication'].astype(str) + ")"
)

# Define moods
moods = ['happy', 'sad', 'angry', 'relaxed', 'excited']

# Randomly assign a mood for now (you can later base this on genre, title, etc.)
books['mood'] = [random.choice(moods) for _ in range(len(books))]

# Rename for your Flask app’s expected format
books = books.rename(columns={'Book-Title': 'title'})

# Keep only the needed columns
books = books[['title', 'description', 'mood']]

# Save as the cleaned dataset
books.to_csv('data/books_clean.csv', index=False)

print("✅ data/books_clean.csv created successfully!")
print(books.head())
