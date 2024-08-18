import pandas as pd

schools = pd.read_csv("schools.csv")

best_math_schools = schools[schools["average_math"] >= 640][["school_name","average_math"]].sort_values(by="average_math",ascending = False)

print(best_math_schools.head())

total_SAT = schools['average_math'] + schools['average_reading'] + schools['average_writing']

schools['total_SAT'] = total_SAT

top_10_schools = schools[["school_name","total_SAT"]].sort_values(by="total_SAT",ascending = False).head(10)

print(top_10_schools)

boroughs = schools.groupby("borough")["total_SAT"].agg(["count","mean","std"]).round(2)

maximum_std = boroughs['std'].max()

largest_std_dev = boroughs[boroughs['std'] == maximum_std]

largest_std_dev = largest_std_dev.rename(columns={"count":"num_schools","mean":"average_SAT","std":"std_SAT"})

print(largest_std_dev)