import random

import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()

NUM_CONTENT = 2000

GENRES = [
    "Drama",
    "Action",
    "Comedy",
    "Romance",
    "Thriller",
    "Documentary",
    "Sci-Fi",
    "Fantasy",
    "Crime",
    "Animation"
]

GENRE_WEIGHTS = [
    0.18,
    0.16,
    0.15,
    0.12,
    0.10,
    0.08,
    0.08,
    0.05,
    0.05,
    0.03
]

LANGUAGES = [
    "English",
    "Hindi",
    "Spanish",
    "French",
    "German",
    "Japanese",
    "Korean"
]

LANGUAGE_WEIGHTS = [
    0.45,
    0.20,
    0.10,
    0.08,
    0.06,
    0.06,
    0.05
]

CONTENT_TYPES = [
    "Movie",
    "Series"
]

AGE_RATINGS = [
    "U",
    "U/A 13+",
    "U/A 16+",
    "A"
]


def generate_content():

    records = []

    for content_id in range(1, NUM_CONTENT + 1):

        content_type = np.random.choice(
            CONTENT_TYPES,
            p=[0.70, 0.30]
        )

        duration = (
            random.randint(80, 180)
            if content_type == "Movie"
            else random.randint(250, 1200)
        )

        record = {
            "content_id": content_id,
            "title": fake.catch_phrase(),
            "content_type": content_type,
            "genre": np.random.choice(GENRES, p=GENRE_WEIGHTS),
            "language": np.random.choice(LANGUAGES, p=LANGUAGE_WEIGHTS),
            "release_year": random.randint(1995, 2025),
            "duration_minutes": duration,
            "imdb_rating": round(random.uniform(5.0, 9.8), 1),
            "age_rating": random.choice(AGE_RATINGS),
            "exclusive_content": random.choice([True, False]),
            "popularity_score": round(random.uniform(1, 100), 2)
        }

        records.append(record)

    return pd.DataFrame(records)


if __name__ == "__main__":

    df = generate_content()

    print(df.head())

    df.to_csv("02_data/dim_content.csv", index=False)

    print("\nContent Generated Successfully!")