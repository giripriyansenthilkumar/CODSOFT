import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'user_id': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8],
    'item': ['Inception', 'Titanic', 'Avatar', 'Shrek', 'The Great Gatsby', '1984', 'Moby Dick', 'Pride and Prejudice',
             'The Catcher in the Rye', 'Harry Potter', 'The Hobbit', 'Titanic', 'Inception', 'Shrek', 
             'Matrix', 'iPhone', 'Samsung Galaxy', 'MacBook', 'Dell XPS', 'Sony TV', 'LG Refrigerator', 
             'Air Fryer', 'Instant Pot', 'Ninja Blender', 'PlayStation', 'Xbox', 'Nintendo Switch', 'Razer Mouse'],
    'rating': [5, 4, 5, 3, 4, 5, 3, 4, 2, 3, 5, 4, 4, 5, 5, 3, 3, 4, 5, 4, 4, 5, 3, 4, 4, 5, 4, 3]
}

df = pd.DataFrame(data)
user_item_matrix = df.pivot_table(index='user_id', columns='item', values='rating').fillna(0)
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def recommend_items(user_id, num_recommendations=3):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    similar_user_items = user_item_matrix.loc[similar_users].mean().sort_values(ascending=False)
    user_items = user_item_matrix.loc[user_id]
    recommended_items = similar_user_items[user_items == 0].head(num_recommendations)
    return recommended_items

user_id = int(input("Enter User ID: "))

if user_id not in user_item_matrix.index:
    print("Invalid User ID.")
else:
    recommendations = recommend_items(user_id=user_id)
    if not recommendations.empty:
        print("\nRecommended Items for User {}:".format(user_id))
        for item, rating in zip(recommendations.index, recommendations):
            print(f"{item}: {rating:.2f}")  # Print item name and its average rating
    else:
        print(f"No recommendations available for User {user_id}.")
