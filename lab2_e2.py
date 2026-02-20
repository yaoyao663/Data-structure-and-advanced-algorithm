#Intersection
def intersection(set1,set2):
    intersection_set = set()
    for element in set1:
        if element in set2:
            intersection_set.add(element)
    return intersection_set


#Difference
def difference(set1,set2):
    defference_set = set()
    for element in set1:
        if element not in set2:
            defference_set.add(element)
    return defference_set

#Union
def union(set1,set2):
    union_set = set()
    for element in set1:
        union_set.add(element)
    for element in set2:
        union_set.add(element)
    return union_set

#second_degree_friends, construct a social graph for users'network
def input_social_graph():
    graph = {}
    print("enter the social graph (type 'exit' to finish):")
    while True:
        user = input("Enter username: ")
        if user.lower() == 'exit':
            break
        friends = set(input(f"Enter friends of {user} (space separated): ").split())
        graph[user] = friends
    return graph


#get_suggestions function
def get_suggestions(user_id, graph):
    my_friends = graph.get(user_id, set())
    all_fof = set()
    
    # go through each friend of user_id and get their friends
    for friend_id in my_friends:
        if friend_id in graph:
            # get friends of friend
            friends_of_friend = graph[friend_id]
            all_fof = union(all_fof, friends_of_friend)

    # remove direct friends 
    potential_suggestions = difference(all_fof, my_friends)
    # 2. remove the user themselves
    final_suggestions = difference(potential_suggestions, {user_id})
    
    return final_suggestions

set1 = set(input("Enter friends of person A : ").split())
set2 = set(input("Enter friends of person B : ").split())
print("mutual friends:",intersection(set1,set2))
print("unique friends of person A:",difference(set1,set2))
print("unique friends of person B:",difference(set2,set1))
print("all friends:",union(set1,set2))
if len(union(set1,set2)) == 0:
    print("Jaccard similarity: 0")
else:
    jaccard_similarity = len(intersection(set1,set2)) / len(union(set1,set2))
    print("Jaccard similarity:", jaccard_similarity)

my_graph = input_social_graph()
user_id = input("Enter user ID to get suggestions: ")
suggestions = get_suggestions(user_id, my_graph)
print("Friend suggestions for", user_id, ":", suggestions)