import requests
import pandas as pd
string_filename = "theor_of.csv"
df = pd.read_csv(string_filename)
df_selection = df[df.freq >= 2]
query_strings = df_selection["theory"].values.tolist()
all_results_df = pd.DataFrame()
for query_string in query_strings:
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&utf8=1&srsearch={query_string}&srnamespace=14"
    r = requests.get(url)

    search_results = r.json()['query']['search']

    new_df = pd.DataFrame(search_results)
    new_df['query_string'] = query_string
    all_results_df = all_results_df.append(new_df)

    for result in search_results:
        print(result)

print(all_results_df)
all_results_df["category"] = all_results_df["title"].str.split("Category:").apply(lambda l: l[1])
all_results_df.to_csv("categories_wikipedia.csv")
