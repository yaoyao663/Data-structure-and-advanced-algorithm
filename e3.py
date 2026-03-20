class CommentNode:
    def __init__(self, comment_id, user_id, content, timestamp, likes):
        self.comment_id = comment_id
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.likes = likes
        self.replies = []
        
    def add_comment(self, reply_node):
        self.replies.append(reply_node)
        
    def flatten_recursive(self):
        results = []
        results.append(self)
        for reply in self.replies:
            results.extend(reply.flatten_recursive())
        return results
    
    def flatten_iterative(self):
        # define the state of the node, state_start means we just visit the node, state_replies_done means we have visited all the children nodes
        state_start = 0
        state_replies_done = 1
        resutls = []
        stack = [(self, state_start)] #initialize
        
        while stack:
            current_node, state = stack.pop()
            if state == state_start:
                resutls.append(current_node)
                stack.append((current_node, state_replies_done))
                
                #deal with the children node
                for reply in reversed(current_node.replies):
                    stack.append((reply, state_start))
            
            elif state == state_replies_done:
                pass
                
        return resutls
    
    
    def count_comments_tail(self, comments_to_process, accumulator = 0):
        if not comments_to_process:
            return accumulator
        current_comment = comments_to_process.pop()
        accumulator += 1
        comments_to_process.extend(current_comment.replies)
        return self.count_comments_tail(comments_to_process, accumulator)
    
    def count_comments_loop(self, comments_to_process):
        accumulator = 0
        while comments_to_process: 
            current_comment = comments_to_process.pop()
            accumulator += 1
            comments_to_process.extend(current_comment.replies)
        return accumulator




    
a = CommentNode(1, 101, "This is the first comment", "2024-06-01 10:00:00", 5)
b = CommentNode(2, 102, "This is a reply to the first comment", "2024-06-01 10:05:00", 3)
c = CommentNode(3, 103, "This is another reply to the first comment", "2024-06-01 10:10:00", 2)
d = CommentNode(4, 104, "This is a reply to the second comment", "2024-06-01 10:15:00", 1)
a.add_comment(b)
a.add_comment(c)
b.add_comment(d)
print(a.count_comments_loop([a]))