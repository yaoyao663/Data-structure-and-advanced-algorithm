# create a Post structrue
class Post:
    def __init__(self, post_id, user_id, content, timestamp, likes, comments, shares):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments
        self.shares = shares
        self.next = None
        
        self.engagement_score = self.calculate_engagement_score()
        
    def calculate_engagement_score(self):
        return self.likes * 1 + self.comments * 2 + self.shares * 3
        

# implement a PriorityQueue structrue
class PriorityQueue:
    def __init__(self):
        self.head = None
        
    def enqueue(self, post_id, user_id, content, timestamp, likes, comments, shares):
        new_post = Post(post_id, user_id, content, timestamp, likes, comments, shares)
        if self.head is None or self.head.engagement_score < new_post.engagement_score:
            new_post.next = self.head
            self.head = new_post
        else:
            temp = self.head
            while temp.next is not None and temp.next.engagement_score >= new_post.engagement_score:
                temp = temp.next
            new_post.next = temp.next
            temp.next = new_post
            
    def dequeue_max(self):
        highest_post = None
        if self.head is not None:
            if self.head.next is None:
                return self.head
            else:
                highest_post = self.head
                self.head = self.head.next
                return highest_post
        return False
    
    def peek_max(self):
        if self.head is not None:
            return self.head.post_id, self.head.user_id, self.head.content, self.head.timestamp, self.head.likes, self.head.comments, self.head.shares, self.head.engagement_score
        return False
    
    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def size(self):
        size = 0
        if self.head is None:
            return size
        temp = self.head
        while temp is not None:
            size += 1
            temp =temp.next
        return size
            
            

    def update_score(self, post_id, new_likes, new_comments, new_shares):
        if self.head is None:
            return False

        current = self.head
        prev = None
        
        while current is not None and current.post_id != post_id:
            prev = current
            current = current.next
        if current is None:
            return False
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        current.next = None 
        
        current.likes = new_likes
        current.comments = new_comments
        current.shares = new_shares
        current.calculate_score()
        
        self.enqueue(current)
        return True

    def refresh_all(self):
        if self.head is None or self.head.next is None:
            return 

        nodes = []
        current = self.head
        while current is not None:
            current.calculate_score()
            nodes.append(current)
            current = current.next
            
        nodes.sort(key=lambda x: x.engagement_score, reverse=True)
        
        self.head = nodes[0]
        current = self.head
        for i in range(1, len(nodes)):
            current.next = nodes[i]
            current = current.next
        current.next = None 
    
        
    def get_top_k(self, k):
        top_posts = []
        current = self.head
        count = 0
        
        while current is not None and count < k:
            top_posts.append(current)
            current = current.next
            count += 1
            
        return top_posts

    def decay_older_than(self, timestamp_limit, decay_rate=0.2):
        if self.head is None:
            return
        nodes = []
        current = self.head
        while current is not None:
            if current.timestamp < timestamp_limit:
                current.engagement_score *= (1 - decay_rate)
            nodes.append(current)
            current = current.next
            
        nodes.sort(key=lambda x: x.engagement_score, reverse=True)
        self.head = nodes[0]
        current = self.head
        for i in range(1, len(nodes)):
            current.next = nodes[i]
            current = current.next
        current.next = None
            
                
                    
                
     