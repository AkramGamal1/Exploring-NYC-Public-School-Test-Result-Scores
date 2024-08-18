import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

netflix_df = pd.read_csv("netflix_data.csv")

movies = netflix_df.query('type == "Movie"')

movies = movies.loc[:,['type','title','release_year','duration','genre']]

#Movies Duration throughout the years

colors = []

for lab, row in movies.iterrows() :
    if row['genre'] == "Children" :
        colors.append("red")
    elif row['genre'] == "Documentaries" :
        colors.append("blue")
    elif row['genre'] == "Stand-Up" :
        colors.append("green")
    else:
        colors.append("black")

plt.scatter(movies['release_year'],movies['duration'],c=colors,alpha=0.4)
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()

#Most frequent movie genre at each decade (according to Netflix)
movies['decade'] = (movies['release_year'] // 10) * 10

genre_counts = movies.groupby(['decade', 'genre']).size().unstack(fill_value=0)

genre_counts = genre_counts.reset_index()

genre_counts_long = genre_counts.melt(id_vars='decade', var_name='genre', value_name='count')

most_frequent_genre = genre_counts_long.loc[genre_counts_long.groupby('decade')['count'].idxmax()]

most_frequent_genre.reset_index(drop=True, inplace=True)

print(most_frequent_genre)

plt.figure(figsize=(12, 6))

for i, count in enumerate(most_frequent_genre['count']):
    plt.text(x=most_frequent_genre['decade'][i], y=count , s=most_frequent_genre['genre'][i], ha='center', va='bottom')

plt.bar(most_frequent_genre['decade'], most_frequent_genre['count'], color='skyblue',edgecolor='green')
plt.xlabel('Decade')
plt.ylabel('Number of Movies')
plt.title('Most Frequent Genre per Decade')
plt.tight_layout()

plt.show()
