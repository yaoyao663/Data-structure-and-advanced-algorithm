class Binary_Tree:
    def __init__ (self,category_id,name,post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None

    def calculate_height(self):
        if self is None:
            return 0
        
        else:
            left_height = self.left.calculate_height() if self.left else 0
            right_height = self.right.calculate_height() if self.right else 0
            return max(left_height, right_height) + 1
    
    def find_target(self, target_id):
        if self.category_id == target_id:
            return self
        
        if self.left:
            found = self.left.find_target(target_id)
            if found:
                return found 
        if self.right:
            found = self.right.find_target(target_id)
            if found:
                return found
        
        return None
    
    def add_child(self, child_node, position):
        child_node.parent = self
        if position == 'left':
            self.left = child_node
        
        elif position == 'right':
            self.right = child_node

        else:
            raise ValueError('Position must be either "left" or "right"')

    
    def calculate_node_height(self, target_id):
        target_node = self.find_target(target_id)
        if target_node:
            return target_node.calculate_height()

        return -1
    
    def count_nodes(self):
        if self is None:
            return 0
        else:
            left_count = self.left.count_nodes() if self.left else 0
            right_count = self.right.count_nodes() if self.right else 0
            return left_count + right_count + 1
    
    def count_leaves(self):
        if self is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        else:
            left_leaves = self.left.count_leaves() if self.left else 0
            right_leaves = self.right.count_leaves() if self.right else 0
            return left_leaves + right_leaves
        
    def is_balanced(self):
        if self is None:
            return True
        
        left_height = self.left.calculate_height() if self.left else 0
        right_height = self.right.calculate_height() if self.right else 0

        if abs(left_height - right_height) > 1:
            return False
        
        left_balanced = self.left.is_balanced() if self.left else True
        right_balanced = self.right.is_balanced() if seld.right else True

        return left_balanced and right_balanced
    
    def is_full_binary_tree(self):
        if self is None:
            return True
        if (self.left is None and self.right is not None) or (self.left is not None and self.right is None):
            return False
        
        left_full = self.left.is_full_binary_tree() if self.left else True
        right_full = self.right.is_full_binary_tree() if self.right else True

        return left_full and right_full
    
    def is_perfect_binary_tree(self):
        if self is None:
            return True
        
        left_height = self.left.calculate_height() if self.left else 0
        right_height = self.right.calculate_height() if self.right else 0
        if left_height != right_height:
            return False
        
        left_perfect = self.left.is_perfect_binary_tree() if self.left else True
        right_perfect = self.right.is_perfect_binary_tree() if self.right else True
        return left_perfect and right_perfect
    
    def is_complete_binary_tree(self):
        if self is None:
            return True
        
        if self.left is None and self.right is not None:
            return False
        
        left_complete = self.left.is_complete_binay_tree() if self.left else True
        right_complete = self.right.is_complete_binary_tree() if self.right else True

        return left_complete and right_complete
    
    def find_catergory(self, target_id):
        if self.category_id == target_id:
            return self
        
        if self.left:
            found = self.left.find_category(target_id)
            if found:
                return found
            
        if self.right:
            found = self.right.find_category(target_id)
            if found:
                return found
            
        return None
    
    def find_path_to_root(self,target_id):
        if self.category_id == target_id:
            return[self.category_id]
        
        if self.left:
            left_path = self.left.find_path_to_root(target_id)
            if left_path:
                return [self.category_id] + left_path
            
        if self.right:
            right_path = self.right.find_path_to_root(target_id)
            if right_path:
                return [self.category_id] + right_path
            
        return None
    
    def lowest_common_ancestor(self, id1, id2):
        if self is None:
            return None
        
        if self.category_id == id1 or self.category_id == id2:
            return self
        
        left_lca = self.left.lowest_common_ancestor(id1, id2) if self.left else None
        right_lca = self.right.lowest_common_ancestor(id1, id2) if self.right else None

        if left_lca and right_lca:
            return self
        
        return left_lca if left_lca else right_lca
    
    def display_tree(self, level=0):
        print(' ' * 4 * level + '-> ' + self.name + f' (ID: {self.category_id}, Posts: {self.post_count})')
        if self.left:
            self.left.display_tree(level + 1)
        if self.right:
            self.right.display_tree(level + 1)



example_tree = Binary_Tree(1, "Technology", 150)
example_tree.add_child(Binary_Tree(2, "Programming", 80), 'left')
example_tree.add_child(Binary_Tree(3, "Design", 65), 'right')
example_tree.left.add_child(Binary_Tree(4, "Python", 50), 'left')
example_tree.left.add_child(Binary_Tree(5, "Java", 30), 'right')
example_tree.right.add_child(Binary_Tree(6, "UI/UX", 40), 'left')
example_tree.right.add_child(Binary_Tree(7, "Graphic Design", 25), 'right')
example_tree.left.left.add_child(Binary_Tree(8, "Django", 20), 'left')
example_tree.left.left.add_child(Binary_Tree(9, "Flask", 15), 'right')
example_tree.display_tree()
        
        


