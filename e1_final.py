class StoryNode:
    def __init__(self, story_id, user_id, content_preview, timestamp, views):
        self.story_id = story_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = timestamp
        self.views = views
        self.prev = None
        self.next = None
        

class StoryLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0
        
    def add_story(self, story_id, user_id, content_preview, timestamp, views):
        new_node=StoryNode(story_id, user_id, content_preview, timestamp, views) 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        
    def remove_story(self, story_id) :
        temp = self.head
        while temp is not None:
            if temp.story_id == story_id:
                if temp == self.current: 
                    self.current = temp.next if temp.next else temp.prev 
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:   
                    self.head = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev
                self.size -= 1
                return True
            temp = temp.next
        return False
     
    def move_forward(self):        
        if self.current is not None:
            if self.current.next is not None:
                self.current = self.current.next
                return self.current.story_id, self.current.user_id, self.current.content_preview, self.current.timestamp, self.current.views
        return None
    
    def move_backward(self):
        if self.current is not None:
            if self.current.prev is not None:
                self.current = self.current.prev
                return self.current.story_id, self.current.user_id, self.current.content_preview, self.current.timestamp, self.current.views 
        return None
      
    def jump_to(self, story_id):
        temp = self.head
        while temp is not None:
            if temp.story_id == story_id:
                self.current = temp
                return True
            temp = temp.next
        return False
    
    def insert_after(self, current_id, story_id, user_id, content_preview, timestamp, views):
        new_node=StoryNode(story_id, user_id, content_preview, timestamp, views)
        temp = self.head
        while temp is not None:
            if temp.story_id == current_id:
                if temp.next is not None:
                    temp.next.prev = new_node
                    new_node.prev = temp
                    new_node.next = temp.next
                    temp.next = new_node
                else:
                    temp.next = new_node
                    new_node.prev = temp
                    self.tail = new_node
                self.size += 1
                return True
            temp = temp.next
        return False
    
    def display_around_current(self, k):
        result = []
        temp = self.current.prev
        for _ in range(k):
            if temp is not None:
                result.append((temp.story_id, temp.user_id, temp.content_preview, temp.timestamp, temp.views))
                temp = temp.prev
            else:
                break
            
        result.reverse() 
        result.append((self.current.story_id, self.current.user_id, self.current.content_preview, self.current.timestamp, self.current.views))
        
        temp = self.current.next
        for _ in range(k):
            if temp is not None:
                result.append((temp.story_id, temp.user_id, temp.content_preview, temp.timestamp, temp.views))
                temp = temp.next        
            else:                
                break
        return result   
    
    def track_view(self):
        if self.current is not None:
            self.current.views += 1
            return True
        return False
    
    def most_viewed(self):
        most_viewed = 0
        temp = self.head
        most_viewed_node = None
        while temp is not None:
            if most_viewed < temp.views:
                most_viewed = temp.views
                most_viewed_node = temp
            temp = temp.next
        return most_viewed_node if most_viewed_node else None
    
    def reorder_by_views(self):
        nodes = []
        temp = self.head
        while temp is not None:
            nodes.append(temp)
            temp = temp.next
        nodes.sort(key=lambda x: x.views, reverse=True)
        self.head = nodes[0]
        self.head.prev = None
        curr = self.head
        for node in nodes[1:]:
            curr.next = node
            node.prev = curr
            curr = curr.next
        self.tail = curr
        self.tail.next = None
        
        
        
      

    
    
# Initial feed (chronological)
test = StoryLinkedList()
test.add_story('Story1', 101, "Morning coffee", "2024-06-01 10:00:00", 0)
test.add_story('Story2', 102, "Workout complete", "2024-06-01 11:00:00", 0)
test.add_story('Story3', 103, "Sunset photo", "2024-06-01 12:00:00", 0)  
# After viewing Story2 twice and Story3 once
test.jump_to('Story2')
test.track_view()
test.track_view()
test.jump_to('Story3')
test.track_view()
print("Story1 views:", test.head.views)  
print("Story2 views:", test.head.next.views)  
print("Story3 views:", test.head.next.next.views)  
# After reorder_by_views()
test.reorder_by_views()
print("After reordering by views:")
print("First story:", test.head.story_id)  
print("Second story:", test.head.next.story_id)  
print("Third story:", test.head.next.next.story_id)  








