# MeloMix

**Content-based music discovery engine with audio feature analysis**

## Overview
MeloMix is a sophisticated music recommendation system that leverages track metadata and audio features to help users discover new music based on their preferences. Built with Flask and powered by TF-IDF vectorization and cosine similarity algorithms, this application analyzes a comprehensive dataset of popular tracks from Spotify to deliver personalized music recommendations. Whether you're searching for songs by a specific artist or looking to expand your musical horizons based on tracks you already love, MeloMix provides an intuitive interface for music exploration.

## Features

### Intelligent Search Functionality
- Search for songs and artists through a clean, user-friendly interface
- Get instant results as you type with case-insensitive matching
- Browse comprehensive track information including release dates and popularity metrics

### Data-Driven Recommendations
- Receive song recommendations based on content similarity
- Recommendations consider both metadata (artist, track name) and audio characteristics
- View similar songs with their corresponding audio feature profiles

### Audio Feature Analysis
- Explore music through quantifiable audio characteristics:
  - **Danceability**: How suitable the track is for dancing (0-100%)
  - **Energy**: The intensity and activity level of the track (0-100%)
  - **Tempo**: The speed of the track measured in beats per minute (BPM)
  - **Valence**: The musical positiveness conveyed by the track (0-100%)
  - **Acousticness**: The amount of acoustic sound in the track (0-100%)

### Visual Music Discovery
- View album artwork for all tracks
- Attractive and responsive design for seamless browsing
- Intuitive navigation between search results and recommendations

## Technical Implementation

### Data Processing
The application uses a curated dataset of popular music tracks with comprehensive metadata and audio features from Spotify. The dataset includes:
- Track and artist information
- Release dates
- Streaming and playlist metrics
- Audio features analyzed by Spotify's algorithms

### Recommendation Engine
MeloMix employs a content-based filtering approach using:
1. **TF-IDF Vectorization**: Converts track metadata into numerical vectors
2. **Cosine Similarity**: Measures the similarity between tracks based on these vectors
3. **Feature-Based Ranking**: Identifies the most similar tracks to recommend

### Technology Stack
- **Flask**: Lightweight Python web framework for the backend
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms for similarity calculations
- **HTML/CSS**: Frontend user interface
- **Responsive Design**: Optimized for both desktop and mobile devices

## Getting Started

### Prerequisites
- Python 3.6 or higher
- Required Python packages: Flask, pandas, scikit-learn

### Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/melomix.git
cd melomix
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage
1. **Search**: Enter an artist or song name in the search bar
2. **Browse Results**: View matching songs with their audio features
3. **Get Recommendations**: Click on any song to see similar tracks
4. **Explore Features**: Analyze the audio characteristics of each recommendation

## Dataset Information
The application is powered by a comprehensive dataset of popular tracks featuring:
- 950+ tracks from various artists and genres
- 25 different data points per track
- Audio features analyzed by Spotify's algorithms
- Popularity metrics across multiple streaming platforms (Spotify, Apple Music, Deezer, Shazam)

## Future Enhancements
- User accounts and personalized recommendation history
- Genre-based filtering options
- Advanced audio feature visualization
- Playlist generation based on mood and activity
- Integration with Spotify's API for real-time streaming

MeloMix demonstrates how data science and music analysis can come together to create an engaging music discovery experience, helping listeners break out of their usual patterns and find new artists and tracks to enjoy.
