size = int(input("Enter the maximum users of the matrix: "))
matrix = [[0]*size for _ in range(size)]   

n = int(input("Enter the number of actual users: "))
for i in range(n):
    for j in range(n):
        matrix[i][j] = False

def is_valid_user(user):
    return 1 <= user <= n

def Follow(follower, following):
    if not (is_valid_user(follower) and is_valid_user(following)):
        print("Invalid user ID")
        return
    if follower == following:
        print("User cannot follow themselves")
        return
    matrix[follower-1][following-1] = True

def Unfollow(follower, following):
    if not (is_valid_user(follower) and is_valid_user(following)):
        print("Invalid user ID")
        return
    matrix[follower-1][following-1] = False

def is_following(follower, following):
    if not (is_valid_user(follower) and is_valid_user(following)):
        return False
    return matrix[follower-1][following-1]

def get_followers(user):
    if not is_valid_user(user):
        print("Invalid user ID")
        return []
    user -= 1
    followers = []
    for i in range(n):
        if matrix[i][user]:
            followers.append(i+1)
    return followers


def get_following(user):
    if not is_valid_user(user):
        print("Invalid user ID")
        return []
    user -= 1
    following = []
    for i in range(n):
        if matrix[user][i] == True:
            following.append(i+1)
    return following

def get_mutual_followers(matrix):
    mutual_followers = list()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == True and matrix[j][i] == True:
                mutual_followers.append((i+1,j+1)) 
    return mutual_followers

def influence_score(user):
    if not is_valid_user(user):
        print("Invalid user ID")
        return 0
    followers = get_followers(user)
    following = get_following(user)
    return (len(followers) + len(following)) / n
   
            
 
Follow(1,2)
Unfollow(1,3)
Follow(2,1)
Follow(2,3)
Unfollow(3,1)
Unfollow(3,2)
print(matrix)
print(get_mutual_followers(matrix))
print(influence_score(1))
print(influence_score(2))   
print(influence_score(3))

    
    
