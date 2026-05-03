import math

class TrendingHeap:
    def __init__(self):
        self.heap = [] # use list to store the information of heap
        self.index_dict = {}
        
    def get_parent(self, index):
        return (index - 1) // 2
    
    def swap(self, i, j): # i is child index, j is parent index
        post_id_i = self.heap[i][1]
        post_id_j = self.heap[j][1]
        
        self.index_dict[post_id_i] = j
        self.index_dict[post_id_j] = i
        
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    # 1. Core heap operations
    
    # push and heapify up
    def push(self, likes, post_id, timestamp):
        new_node = (likes, post_id, timestamp)
        self.heap.append(new_node)
        curent_index = len(self.heap) - 1
        self.index_dict[new_node[1]] = curent_index
        
        self.heapify_up(curent_index)
        
    def heapify_up(self, index):
        while index > 0:
            parent_index = self.get_parent(index)
            if self.heap[index][0] > self.heap[parent_index][0]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break # early stop
        
        
    # pop max
    # time complexity is O(logn)
    def pop_max(self):
        # if the heap is empty, raise an error
        if not self.heap:
            raise IndexError("Heap is empty")
        
        # if the heap has only one element, pop it and return
        if len(self.heap) == 1:
            max_post = self.heap.pop()
            del self.index_dict[max_post[1]] 
            return max_post

        last_index = len(self.heap) - 1
        self.swap(last_index, 0)
        
        max_value = self.heap.pop()
        del self.index_dict[max_value[1]]
        
        self.heapify_down(0)
        return max_value
        
    def heapify_down(self, index):
        
        while 2*index + 1 <= len(self.heap)-1:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = left
            
            if right <= len(self.heap)-1 and self.heap[left][0] < self.heap[right][0]:
                largest = right
            
            if self.heap[index][0] < self.heap[largest][0]:
                self.swap(index, largest)
                index = largest
            else:
                break
            
            
    # peek max
    def peek_max(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        max_value = self.heap[0]
        return max_value
    
    
    # get top k
    # push的时间复杂度是O(logn), pop_max的时间复杂度也是O(logn),所以先pop k次，再push k次进行还原
    def get_top_k(self, k):
        k = min(k, len(self.heap))
        top_k_list = []
        
        for _ in range(k):
            top_k_list.append(self.pop_max())
        
        for post in top_k_list:
            self.push(post[0], post[1], post[2])
            
        return top_k_list
            
        
    # update likes
    def update_likes(self, new_likes, post_id, timestamp):
        target_index = self.index_dict[post_id]
        self.heap[target_index] = (new_likes, post_id, timestamp)
        
        parent_index = self.get_parent(target_index)
        if new_likes > self.heap[parent_index][0]:
            self.heapify_up(target_index)
        else:
            self.heapify_down(target_index)
            
    def size(self):
        return len(self.heap)
    
    
    
    # 2. Heap analytics
    
    # verify heap properly
    def is_valid_heap(self, index):
        if index >= len(self.heap):
            return True
        left = 2 * index + 1
        right = 2 * index + 2   
        if left < len(self.heap) and self.heap[left][0] > self.heap[index][0]:
            return False    
        if right < len(self.heap) and self.heap[right][0] > self.heap[index][0]:
            return False
        return self.is_valid_heap(left) and self.is_valid_heap(right)
    
    
    # get height
    def get_height(self):
        size = len(self.heap)
        
        if size == 0:
            return 0
            
        return math.ceil(math.log2(size + 1)) # ceil函数向上取整
    
    
    # get level order
    def get_level_order(self):
        """按层级返回堆的内容（二维列表）"""
        if not self.heap:
            return []
            
        result = []
        start_index = 0
        level_capacity = 1  # 第 0 层最多 1 个节点 (2^0)
        
        while start_index < len(self.heap):
            # 利用切片提取当前层的所有节点
            # 即使 start_index + level_capacity 超出数组总长度，Python 切片也会自动截断到末尾，不会报错
            current_level = self.heap[start_index : start_index + level_capacity]
            result.append(current_level)
            
            # 为下一层做准备
            start_index += level_capacity
            level_capacity *= 2  # 下一层容量翻倍 (2^1, 2^2, 2^3...)
            
        return result
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    testheap = TrendingHeap()
    testheap.push(10, "post1", 1)
    testheap.push(20, "post2", 2)
    testheap.push(15, "post3", 3)
    testheap.push(25, "post4", 4)
    testheap.push(40, "post5", 5)
    testheap.push(30, "post6", 6)
    testheap.push(50, "post7", 7)
    
    print(testheap.heap)
    
    testheap.pop_max()
    print(testheap.heap)
    
    print(testheap.peek_max())
    
    print(testheap.get_top_k(10))
    
    testheap.update_likes(55, "post2", 2)
    print(testheap.heap)
    
    print(testheap.size())
    
    print(testheap.is_valid_heap(0))
    print(testheap.get_height())
    print(testheap.get_level_order())