import pandas as pd

# Load dataset
movies = pd.read_csv('movies.csv')

def recommend_movies_by_genre(genre):
    # Filter berdasarkan genre
    result = movies[movies['genres'].str.contains(genre, case=False, na=False)]
    return result[['title', 'genres']].head(10)

if __name__ == "__main__":
    user_genre = input("Suka genre apa? ")
    recs = recommend_movies_by_genre(user_genre)

    if recs.empty:
        print("Maaf, tidak ada film dengan genre tersebut.")
    else:
        print("Film yang direkomendasikan:")
        print(recs.to_string(index=False))
