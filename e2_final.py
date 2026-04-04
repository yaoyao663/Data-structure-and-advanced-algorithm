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
    def find_category(self, node, category_id):
        if node is None:
            return None
            
        if node.category_id == category_id:
            return node
        
        left = self.find_category(node.left, category_id)
        if left is not None:
            return left

        return self.find_category(node.right, category_id)
    
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
    
    # Part 1
    
    # Part A: In-order Traversal (Left → Root → Right) 
    def in_order_collect(self, node):
        if node is None:
            return []
        result = []
        if node.left is not None:
            result.extend(self.in_order_collect(node.left)) 
        result.append([node.name, node.post_count])
        if node.right is not None:
            result.extend(self.in_order_collect(node.right))
        return result
        
    def in_order_accumulate_posts(self, node):
        if node is None:
            return 0
        count = 0
        if node.left is not None:
            count += self.in_order_accumulate_posts(node.left)
        count += node.post_count
        if node.right is not None:
            count += self.in_order_accumulate_posts(node.right)
        return count
    
    def in_order_find_kth(self, node, k, counter=None):
        if counter is None:
            counter = [0]  
        if node is None:
            return None
        left_result = self.in_order_find_kth(node.left, k, counter)
        if left_result is not None:
            return left_result
        counter[0] += 1
        if counter[0] == k:
            return [node.category_id, node.name]
         
        return self.in_order_find_kth(node.right, k, counter)


    # Part B: Pre-order Traversal (Root → Left → Right) 
    def pre_order_export(self, node, depth=0):
        if node is None:
            return ""
        gap = "  " * depth
        result = f"{gap}{node.name}({node.post_count})\n" 
        if node.left is not None:
            result += self.pre_order_export(node.left,depth+1)
        if node.right is not None:
            result += self.pre_order_export(node.right,depth+1)       
        return result
    
    def pre_order_copy(self, node, is_root=True):
        if node is None:
            return None
        new_node = CategoryNode(node.category_id, node.name, node.post_count)
        
        if is_root: #is_root use to determine if we are copying the root node, if so, we need to set self.root to the new node
            self.root = new_node
            
        new_node.left = self.pre_order_copy(node.left, False)
        new_node.right = self.pre_order_copy(node.right, False)
        
        if new_node.left is not None:
            new_node.left.parent = new_node
        if new_node.right is not None:
            new_node.right.parent = new_node
            
        return new_node
    
    def pre_order_serialize(self, node):
        if node is None:
            return ""
        result = f" {node.category_id} {node.name}({node.post_count}) |" 
        if node.left is not None:
            result += self.pre_order_serialize(node.left)
        if node.right is not None:
            result += self.pre_order_serialize(node.right)       
        return result
    
    
    
    # Part C: Post-order Traversal (Left → Right → Root) 
    def post_order_total_posts(self, node):
        if node is None:
            return 0
        count = 0
        count += self.post_order_total_posts(node.left)
        count += self.post_order_total_posts(node.right)
        count += node.post_count
        return count
    
    def post_order_average_depth_helper(self, node, depth=0, leaves=0):
        if node is None:
            return 0, 0
        if node.left is None and node.right is None:
            return depth, 1
        
        left_depth, left_leaves = self.post_order_average_depth_helper(node.left, depth+1, leaves)
        right_depth, right_leaves = self.post_order_average_depth_helper(node.right, depth+1, leaves)
        total_depth = left_depth + right_depth
        total_leaves = left_leaves + right_leaves
        return total_depth, total_leaves
    
    def post_order_aeverage_depth(self, node):
        total_depth, total_leaves = self.post_order_average_depth_helper(node)
        if total_leaves == 0:
            return 0 
        return total_depth / total_leaves
    
    def post_order_collect_leaves(self, node):
        if node is None:
            return []
        result = []
        if node.left is None and node.right is None:
            result.append([node.category_id, node.name])
        result.extend(self.post_order_collect_leaves(node.left))
        result.extend(self.post_order_collect_leaves(node.right)) 
        return result
    
    
    
    # Part 2
    def find_most_popular_category(self, node):
        max_count = 0
        if node is None:
            return 0
        left_max = self.find_most_popular_category(node.left)
        right_max = self.find_most_popular_category(node.right)
        max_count = max(left_max, node.post_count, right_max)
        return max_count
    
    def category_with_most_subcategories(self, node):
        if node is None:
            return None
    
        best_state = [-1, None] 
        
        def traverse(current_node):
            if current_node is None:
                return
                
            child_count = 0
            if current_node.left is not None:
                child_count += 1
            if current_node.right is not None:
                child_count += 1
                
            if child_count > best_state[0]:
                best_state[0] = child_count
                best_state[1] = current_node.name
                
            traverse(current_node.left)
            traverse(current_node.right)

        traverse(node)

        return best_state[1]
        
            
    
    
    
    
    
    