from collections import deque

class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None  

class Categories:
    def __init__(self):
        self.root = None

    # build the tree
    def add_child(self, parent_id, category_id, name, post_count, position="left"):
        new_node = CategoryNode(category_id, name, post_count)

        if self.root is None:
            self.root = new_node
            print(f"Created root node: {name}")
            return True

        parent_node = self.find_category(self.root, parent_id)
        
        if parent_node is None:
            print(f"Error: Parent node with ID {parent_id} not found!")
            return False

        if position == "left":
            if parent_node.left is not None:
                print(f"Warning: {parent_node.name} already has a left child. It will be overwritten.")
            parent_node.left = new_node
            new_node.parent = parent_node  # Establish two-way connection
            print(f"Added '{name}' as the left child of '{parent_node.name}'")
            
        elif position == "right":
            if parent_node.right is not None:
                print(f"Warning: {parent_node.name} already has a right child. It will be overwritten.")
            parent_node.right = new_node
            new_node.parent = parent_node  # Establish two-way connection
            print(f"Added '{name}' as the right child of '{parent_node.name}'")
            
        else:
            print("Error: position must be 'left' or 'right'")
            return False
            
        return True
    
    
    # Implement tree metric calculations
    def calculate_height(self, node):
        if node is None:
            return -1
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        return 1 + max(left_height, right_height)
    
    def calculate_node_height(self, node, target_id):
        if node is None:
            return -1
        
        if node.category_id == target_id:
            return self.calculate_height(node)
        
        left = self.calculate_node_height(node.left, target_id)
        if left != -1:
            return left
        
        right = self.calculate_node_height(node.right, target_id)
        if right != -1:
            return right
        return -1
    
    def count_nodes(self, node):
        if node is None:
            return 0
        left_count = self.count_nodes(node.left)
        right_count = self.count_nodes(node.right)
        return 1 + left_count + right_count
    
    def count_leaves(self, node):
        if node is None:
           return 0
        count = 0
        if node.left is None and node.right is None:
            count = 1
       
        return count + self.count_leaves(node.left) + self.count_leaves(node.right)
    
    def is_balanced(self, node):
        if node is None:
            return True
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        
        return self.is_balanced(node.left) and self.is_balanced(node.right)
    # up-to-down, calculate the height repeatedly
    
    def is_balanced_optimized(self, node):
    
        def check_height(current_node):
            if current_node is None:
                return -1
            left_height = check_height(current_node.left)
            if left_height == -2:
                return -2 

            right_height = check_height(current_node.right)
            if right_height == -2:
                return -2

            if abs(left_height - right_height) > 1:
                return -2
                
            return 1 + max(left_height, right_height)
        return check_height(node) != -2
    
    
    # Implement tree property verification
    def is_full_binary_tree(self, node):
        if node is None:
            return True
        if node.left is None and node.right is not None:
            return False
        if node.left is not None and node.right is None:
            return False
        return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
    
    
    def is_perfect_binary_tree(self, node):
        if node is None:
            return True
        
        total_nodes = self.count_nodes(node)
        height = self.calculate_height(node)
        expected_nodes = (2 ** (height + 1)) - 1
        
        return total_nodes == expected_nodes
    
    
    def is_complete_binary_tree(self, node):
        if node is None:
            return True

        queue = deque([node])
        label = False
        
        while len(queue) > 0:
            current = queue.popleft()
            if current is None:
                label = True
            else:
                if label:
                    return False
                queue.append(current.left)
                queue.append(current.right)
        return True
                
                
    # Implement category search and navigation
    def find_category(self, node, category_id):
        if node is None:
            return None
            
        if node.category_id == category_id:
            return node
        
        left = self.find_category(node.left, category_id)
        if left is not None:
            return left

        return self.find_category(node.right, category_id)
    
    def find_path_to_root(self, node, category_id):
        current = self.find_category(node, category_id)
        if current is None:
            return None
        path = [] # list不可以作为变量名
        
        while current is not None:
            path.append([current.category_id, current.name])
            current = current.parent
                
        return path
    
    def lowest_common_ancestor(self, node, id1, id2):
        list1 = self.find_path_to_root(self.root, id1)
        list2 = self.find_path_to_root(self.root, id2)
        
        if list1 is None or list2 is None:
            return None
        
        for category in list1:
            if category in list2: 
                return category
        return None
        
    
        
        
    



