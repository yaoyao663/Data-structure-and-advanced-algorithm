import numpy as np

interests = ["Sports", "Music", "Movies", "Tech", "Travel", "Art"]
num_users = 3
num_interests = len(interests)

user_info = np.zeros((num_users, num_interests))

print(f"Please enter {num_interests} the rate of each interest (0-9)，use ' ' as separator:")

for i in range(num_users):
    row = list(map(int, input(f"User {i} 's interest rate: ").split()))
    if len(row) == num_interests:
        user_info[i] = row

print("\n--- user's interest matrix ---")
print(f"{'':<10}", " | ".join(interests))
for i in range(num_users):
    print(f"User {i:<8}: {user_info[i]}")

def get_similarity(u1, u2):
    return np.dot(u1, u2) / (np.linalg.norm(u1) * np.linalg.norm(u2) + 1e-9)


print("\n--- The similarities of all users ---")
for i in range(num_users):
    for j in range(i + 1, num_users):
        sim = get_similarity(user_info[i], user_info[j])
        print(f"The similarity bewteen user {i} and user {j} : {sim:.4f}")

def recommend(user_index, top_k = 1):
    similarities = []
    for i in range(num_users):
        if i != user_index:
            sim = get_similarity(user_info[user_index], user_info[i])
            similarities.append((i, sim))
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_k]

print("\n--- Recommendations for each user ---")
for i in range(num_users):
    recs = recommend(i)
    print(f"Recommendations for user {i}:")
    for rec in recs:
        print(f"  User {rec[0]} with similarity {rec[1]:.4f}")



