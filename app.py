from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the dataset and rename columns
df = pd.read_csv('updated_file.csv')
df.rename(columns={
    'track_name': 'song_name',
    'artist(s)_name': 'artist',
    'danceability_%': 'danceability',
    'energy_%': 'energy',
    'image_url': 'album_cover',
    'bpm': 'tempo'
}, inplace=True)

# Verify required columns are present
required_columns = ['song_name', 'artist', 'album_cover', 'danceability', 'energy', 'tempo']
for column in required_columns:
    if column not in df.columns:
        raise KeyError(f"Missing required column: {column}")

# Process dataset to include necessary information
df['combined_features'] = df['song_name'] + " " + df['artist']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for searching songs or artists
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    if query:
        results = df[df['combined_features'].str.contains(query, case=False, na=False)]
        songs = results.to_dict(orient='records')
        return render_template('results.html', songs=songs)
    return render_template('index.html', message="No results found")

# Route for song details and recommendations
@app.route('/song/<song_id>')
def song_details(song_id):
    song_id = int(song_id)
    song = df.iloc[song_id]
    song_features = tfidf_matrix[song_id:song_id+1]
    cosine_similarities = cosine_similarity(song_features, tfidf_matrix).flatten()
    similar_indices = cosine_similarities.argsort()[:-6:-1]
    similar_songs = df.iloc[similar_indices].to_dict(orient='records')
    
    return render_template('song.html', song=song, similar_songs=similar_songs)

if __name__ == '__main__':
    app.run(debug=True)
