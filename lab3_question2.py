# Activity Stack Implementation
class ActivityStack:
    def __init__(self):
        self.activities = []
        self.undo_stack = []

    def push(self, activity):
        self.activities.append(activity)
        
    def pop(self):
        if not self.activities:
            print("No activities.")
            return None
        else:
            self.undo_stack.append(self.activities[-1])
            return self.activities.pop()
        
    def peek(self):
        if not self.activities:
            print("No activities.")
            return None
        return self.activities[-1]
    
    def is_empty(self):
        return len(self.activities) == 0
    
    def size(self):
        return len(self.activities)
    
    def recent(self,n):
        return self.activities[-n:] if n <= len(self.activities) else self.activities

    def undo_last(self):
        if not self.undo_stack:
            print("No activities to undo.")
            return None
        Last_activity = self.undo_stack.pop()
        self.activities.append(Last_activity)

# Example usage:
activity_stack = ActivityStack()
activity_stack.push("Like")
activity_stack.push("Comment")
activity_stack.push("Share")
activity_stack.push("follow")

print(activity_stack.peek())
print(activity_stack.pop())
print(activity_stack.size())
print(activity_stack.recent(1))
activity_stack.undo_last()
print(activity_stack.peek())
print(activity_stack.size())

print("----------------------------------")

# Notification Queue Implementation
class NotificationQueue:
    def __init__(self):
        self.notifications = []

    def enqueue(self, notification):
        self.notifications.append(notification)

    def dequeue(self):
        if not self.notifications:
            print("No notifications.")
            return None
        return self.notifications.pop(0)
    
    def front(self):
        if not self.notifications:
            print("No notifications.")
            return None
        return self.notifications[0]
    
    def is_empty(self):
        return len(self.notifications) == 0
    
    def size(self):
        return len(self.notifications)
    
    def display_pending(self):
        return self.notifications
    
    def priority_enqueue(self, notification):
        self.notifications.insert(0, notification)
    
# Example usage:
notification_queue = NotificationQueue()
notification_queue.enqueue("New message from Alice")
notification_queue.enqueue("Bob liked your post")   
notification_queue.enqueue("Charlie commented on your photo")
print(notification_queue.front())
print(notification_queue.dequeue()) 
print(notification_queue.size())
notification_queue.priority_enqueue("Urgent: New friend request from Dave")
print(notification_queue.display_pending())
    

class FeedProcessor:
    def __init__(self):
        self.recent_activities = ActivityStack()
        self.notification_queue = NotificationQueue()
        self.process_log = []
    
    def process_income(self):
        if not self.notification_queue.is_empty():
            notification = self.notification_queue.dequeue()
            self.recent_activities.push(notification)
        
        else:
            print('No notifications to process.')

    def batch_process(self, n ):
        for i in range(n+1):
            self.process_income()

    def clear_history(self):
        for i in range(self.recent_activities.size()):
            recent_acitvity = self.recent_activities.pop()
            self.process_log.append(recent_acitvity)
        
        print("Activity history cleared. Process log updated.")

    def get_stats(self):
        return{"recent_activities": self.recent_activities.size(), "notifications": self.notification_queue.size(), "process_log": len(self.process_log)}


# Example usage:
feed_processor = FeedProcessor()
feed_processor.notification_queue.enqueue("New follower")
feed_processor.notification_queue.enqueue("New like")    
feed_processor.notification_queue.enqueue("New comment")
feed_processor.recent_activities.push('shared a post')
feed_processor.recent_activities.push('comment on post')
feed_processor.recent_activities.push('like video')
feed_processor.process_income()
print(feed_processor.notification_queue.display_pending())
print(feed_processor.recent_activities.peek())


