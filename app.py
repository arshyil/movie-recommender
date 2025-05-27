from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data
movies = pd.read_csv('movies.csv')

# Daftar genre yang tersedia (bisa kamu sesuaikan)
genres_list = [
    "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
    "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance",
    "Sci-Fi", "Thriller", "War", "Western"
]

# Fungsi rekomendasi berdasarkan genre
def get_recommendations(genre):
    result = movies[movies['genres'].str.contains(genre, case=False, na=False)]
    return result[['title', 'genres']].head(10).values.tolist()

# Routing
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    selected_genre = ""
    if request.method == 'POST':
        selected_genre = request.form['genre']
        recommendations = get_recommendations(selected_genre)
    return render_template('index.html', recommendations=recommendations, genres=genres_list, selected=selected_genre)

if __name__ == '__main__':
    app.run(debug=True)
