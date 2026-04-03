from logging import root

from numpy import rint

from LAB5_binarytree import Binary_Tree

class Generalized_Tree:
    def __init__ (self,category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def binary_to_generalized(self, binary_tree):
        if binary_tree is None:
            return None
        
        generalized_tree = Generalized_Tree(binary_tree.category_id, binary_tree.name, binary_tree.post_count)

        if binary_tree.left:
            left_child = self.binary_to_generalized(binary_tree.left)
            generalized_tree.children.append(left_child)
            left_child.parent = generalized_tree

        if binary_tree.right:
            right_child = self.binary_to_generalized(binary_tree.right)
            generalized_tree.children.append(right_child)
            right_child.parent = generalized_tree

        return generalized_tree
    
    def generalized_to_binary(self):
        if self is None:
            return None
        
        binary_tree = Binary_Tree(self.category_id, self.name, self.post_count)

        if self.children:
            binary_tree.left = self.children[0].generalized_to_binary()
            current_binary_node = binary_tree.left

            for child in self.children[2:]:
                current_binary_node.right = child.generalized_to_binary()
                current_binary_node = current_binary_node.right

            return binary_tree
            
    def display_tree(self, level=0):
        print(' ' * 4 * level + '-> ' + self.name + f' (ID: {self.category_id}, Posts: {self.post_count})')
        for child in self.children:
            child.display_tree(level + 1)
                               


    def pre_order_traversal(self):
        results = [self.category_id]
        for child in self.children:
            results.extend(child.pre_order_traversal())
        return results
            
    def post_order_traversal(self):
        results = []
        for child in self.children:
            results.extend(child.post_order_traversal())
        results.append(self.category_id)
        return results
    
    def level_order_traversal(self):
        results = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            results.append(current.category_id)
            queue.extend(current.children)
        return results

    def calculate_fan_out(self):
        max_fan_out = len(self.children)
        for child in self.children:
            child_fan_out = child.calculate_fan_out()
            max_fan_out = max(max_fan_out, child_fan_out)
        return max_fan_out
    
    def height(self):
        if self is None:
            return 0
        if not self.children:
            return 1
        
        child_heights = [child.height() for child in self.children]
        return max(child_heights) + 1
    
    def count_nodes(self):
        if self is None:
            return 0
        else:
            child_counts = [child.count_nodes() for child in self.children]
            return sum(child_counts) + 1
        
    def count_leaves(self):
        if self is None:
            return 0 
        if not self.children:
            return 1
        else:
            child_leaf = [child.count_leaves() for child in self.children]
            return sum(child_leaf)
        
    def calculate_branch_factor(self):
        total_nodes = self.count_nodes()
        total_leaves = self.count_leaves()
        if total_leaves == 0:
            return 0
        return (total_nodes - 1) / total_leaves
    
def run_edge_tests():
    print("--- Running Edge Case Tests ---")

    # Test Case 1: Single Node Tree
    root = Generalized_Tree(1, "Root Only", 10)
    assert root.count_nodes() == 1
    assert root.count_leaves() == 1
    assert root.height() == 1
    assert root.pre_order_traversal() == [1]
    print("Test 1 (Single Node): Passed")

    # Test Case 2: Broad "Flat" Tree (High Fan-out)
    flat_root = Generalized_Tree(100, "Flat", 0)
    for i in range(101, 111): # Add 10 children to one node
        flat_root.add_child(Generalized_Tree(i, f"Child {i}", 0))
    
    assert flat_root.calculate_fan_out() == 10
    assert flat_root.count_leaves() == 10
    assert flat_root.height() == 2        
    print("Test 2 (High Fan-out): Passed")

    # Test Case 3: Deeply Nested Tree (The "Vine")
    deep_root = Generalized_Tree(1, "Level 1", 0)
    current = deep_root
    for i in range(2, 6): # Create 5 levels
        new_node = Generalized_Tree(i, f"Level {i}", 0)
        current.add_child(new_node)
        current = new_node
    
    assert deep_root.height() == 5
    assert deep_root.count_leaves() == 1
    print("Test 3 (Deep Nesting): Passed")

    # Test Case 4: Branching Factor with Zero Leaves (Safety Check)
    # Note: A real tree always has at least 1 leaf (the root itself if empty)
    # but we check if our formula handles it.
    bf = deep_root.calculate_branch_factor()
    assert bf == (5 - 1) / 1  # (nodes - 1) / leaves
    print(f"Test 4 (Branching Factor): Passed (Value: {bf})")

# 执行测试
if __name__ == "__main__":
    try:
        run_edge_tests()
        print("\nAll Edge Cases Passed Successfully!")
    except Exception as e:
        print(f"\nTest Failed: {e}")

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

tree_tool = Generalized_Tree(0, "Root", 0)
generalized_tree = tree_tool.binary_to_generalized(example_tree)
generalized_tree.display_tree()
binary_tree = generalized_tree.generalized_to_binary()
binary_tree.display_tree()
print("Pre-order traversal:", generalized_tree.pre_order_traversal())
print("Post-order traversal:", generalized_tree.post_order_traversal())
print("Level-order traversal:", generalized_tree.level_order_traversal())  
print("Fan-out of the tree:", generalized_tree.calculate_fan_out())
print("Height of the tree:", generalized_tree.height())
print("Total number of nodes:", generalized_tree.count_nodes())
print("Total number of leaves:", generalized_tree.count_leaves())
print("Branch factor of the tree:", generalized_tree.calculate_branch_factor())
run_edge_tests()