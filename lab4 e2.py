import random
random.seed(42)

class PostStructure:
    def __init__(self, post_id, user_id, content_preview, timestamp, likes, comments, shares):
        self.post_id = post_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments
        self.shares = shares
        self.engagement_score = likes + comments * 2 + shares * 3

post_1 = PostStructure(1,'liu','novel','10:20',1,2,3)
post_2 = PostStructure(2,'Jing','romance','11:20',5,5,5)
post_3 = PostStructure(3,'yao','drama','9:20',8,8,1)
post_4 = PostStructure(4, "le", "scf",'22:15',9,1,7)

posts = [post_1,post_2,post_3,post_4]

#Part A

def max_engagement(posts, left, right):
    if left > right:
        print("left should equal or less than right")
        return (0,None)
    elif left == right:
        return posts[left].engagement_score , posts[left].post_id
    else:
        mid = (left + right)//2
        left_max = max_engagement(posts,left,mid)
        right_max = max_engagement(posts, mid + 1, right)
        return max(left_max,right_max)
    
score, postid = max_engagement(posts, 0, len(posts) - 1)
print(f"the maximal engagement post is: post_id{postid} with scores{score}")

#Part B

def sum_engagement(posts, left, right):
    if left > right:
        print('left should equal or less than right')
        return 0
    elif left == right:
        return posts[left].engagement_score
    else:
        sum = sum_engagement(posts, left, right-1) + posts[right].engagement_score
        return sum
    
total_score = sum_engagement(posts, 0, len(posts)-1)
print(f'the sum of the engagement score is {total_score}.')

def average_engagement(posts, left, right):
    length = len(posts)
    average = sum_engagement(posts, left, right) / length
    return average

average_score = average_engagement(posts, 0, len(posts)-1)
print(f"the average engagement score is {average_score}")

#Part C
def count_above_threshold(posts, left, right, threshold):
    if left > right:
        print('left should equal or less than right')
        return 0
    elif left == right:
        if posts[left].engagement_score > threshold:
            return 1
        else:
            return 0
    else:
        mid = (left + right)//2
        left_part = count_above_threshold(posts, left, mid, threshold)
        right_part = count_above_threshold(posts, mid+1, right, threshold)
        return left_part + right_part

number_above_threshold = count_above_threshold(posts, 0, len(posts)-1, 26)
print(f'the number of posts above the threshold is {number_above_threshold}.')

#Part D
def merge_sort(posts, left, right):
    if left > right:
        print('left should equal or less than right')
        return []
    if left == right:
        return [posts[left]]
    
    mid = (left + right)//2
    left_part = merge_sort(posts, left, mid)
    right_part = merge_sort(posts, mid+1, right)
    return merge(left_part, right_part)

def merge(left_part, right_part):
    result = []
    i = j = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i].engagement_score < right_part[j].engagement_score:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1
        
    result.extend(left_part[i:])
    result.extend(right_part[j:])

    return result

sort_by_engagement = merge_sort(posts, 0, len(posts)-1)
sorted_list = []
for p in sort_by_engagement:
    sorted_list.append(p.post_id)
print(sorted_list)

time_like = [random.randint(1,100) for _ in range(24)]
print(time_like,len(time_like))

def find_peak_hour(likes, left, right):
    if left > right:
        print("left should equal or less than right")
        return 0 
    if left == right:
        return left
    
    mid = (left+right)//2
    if likes[mid] > likes[mid+1]:
        return find_peak_hour(likes, left, mid)
    else:
        return find_peak_hour(likes, mid+1, right)

time_peak = find_peak_hour(time_like,0,23)
print(time_peak)
 

