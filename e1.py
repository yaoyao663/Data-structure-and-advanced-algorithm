class UserBST:
    def __init__(self, user_id, name, friends):
        self.user_id = user_id
        self.name = name
        self.friends = friends
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, user_id, name, friends):
        new_node = UserBST(user_id, name, friends)
        if self.root == None:
            self.root = new_node
            return
        current = self.root
        while current is not None:
            parent = current
            if user_id < current.user_id:
                current = current.left
            else:
                current = current.right
        if user_id < parent.user_id:
            parent.left = new_node
        else:
            parent.right = new_node
        
    
    def find(self, user_id):
        if self.root is None:
            return None
        current = self.root
        while current is not None:
            if current.user_id == user_id:
                return current
            if user_id < current.user_id:
                current = current.left
            else:
                current = current.right
        return current
    
    
    def inorder_traversal(self, node):
        if self.root is None:
            return []
        result = []
        if node.left is not None:
            result.extend(self.inorder_traversal(node.left))
        result.append(node.user_id)
        if node.right is not None:
            result.extend(self.inorder_traversal(node.right))
        return result
    
    
    def delete(self, user_id):
        self.root = self.delete_recursive(self.root, user_id)
        
    def delete_recursive(self, node, user_id):
        # firstly, we need to check if the tree exists
        if node is None:
            return None
        
        # secondly, find the node
        if user_id < node.user_id:
            node.left = self.delete_recursive(node.left, user_id)
            # this stage deal with the subtree, and recevie the return node
        elif user_id > node.user_id:
            node.right = self.delete_recursive(node.right, user_id)
        else:
            # if the node has no child or only one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # if the node has two children node
            # use get_max() to get the predecessor
            temp = self.get_max(node)
            node.user_id = temp.user_id
            node.name = temp.name
            node.friends = temp.friends
            
            node.left = self.delete_recursive(node.left, temp.user_id)
            
        return node
            
    def get_max(self, node):
        current = node.left
        while current.right is not None:
            current = current.right
        return current
        
        
    def suggest_friends(self, user_id, max_suggestions=5):
        target = self.find(user_id)
        if target is None:
            return []
        fof_dict = dict()
        for friend_id in target.friends:
            friend_node = self.find(friend_id)
            if friend_node is not None:
                fof_list = friend_node.friends
            for fof in fof_list:
                if fof != user_id and fof not in target.friends:
                    if fof not in fof_dict:
                        fof_dict[fof] = 1
                    else:
                        fof_dict[fof] += 1
                        
        sorted_fofs = sorted(fof_dict.items(), key=lambda x: x[1], reverse=True)
        result_ids = [item[0] for item in sorted_fofs]
    
        return result_ids[:max_suggestions]
    
    
    def get_height(self, node):
        if node is None:
            return -1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return 1 + max(left_height, right_height)
    
    
    def is_balanced(self, node):
        if node is None:
            return True
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return self.is_balanced(node.left) and self.is_balanced(node.right)
    
    
    def get_leaf_count(self, node):
        if node is None:
            return 0
        count = 0
        if node.left is None and node.right is None:
            count += 1
        
        return count + self.get_leaf_count(node.left) + self.get_leaf_count(node.right)       
        
        
        
        
        
# ==========================================
# 下面是测试代码
# ==========================================
if __name__ == "__main__":
    # 1. 初始化社交网络 BST
    network = BST()

    # 2. 插入测试数据
    print("--- 正在插入用户数据 ---")
    network.insert(50, "Alice", [20, 70])
    network.insert(20, "Bob", [50, 30, 10])
    network.insert(70, "Charlie", [50, 80])
    network.insert(30, "David", [20])
    network.insert(80, "Eve", [70])
    network.insert(10, "Frank", [20, 80, 90])
    network.insert(40, "Peter", [20])
    print("数据插入完成！")
    
    print(network.find(30).name)
    print(network.find(40).name)
    
    print(network.inorder_traversal(network.root))
    
    network.delete(50)
    print(network.root.user_id)
    
    
    
    print(network.inorder_traversal(network.root))
    print(network.suggest_friends(20))
    
    print(network.get_height(network.root))
    
    print(network.is_balanced(network.root))
    
    print(network.get_leaf_count(network.root))
    