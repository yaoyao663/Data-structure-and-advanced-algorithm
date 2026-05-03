class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_username = False
        self.user_id = None

class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0
        self.total_nodes = 1

    def insert(self, username, user_id):
        node = self.root
        for char in username:
            if char not in node.children:
                node.children[char] = TrieNode()
                self.total_nodes += 1
            node = node.children[char]
        if not node.is_end_of_username:
            node.is_end_of_username = True
            node.user_id = user_id
            self.word_count += 1

    def search(self, username):
        node = self.root
        for char in username:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.user_id if node.is_end_of_username else None

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix, max_results=10):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        def dfs(curr_node, curr_path):
            if len(results) >= max_results:
                return
            if curr_node.is_end_of_username:
                results.append((curr_path, curr_node.user_id))
            for char in sorted(curr_node.children.keys()):
                dfs(curr_node.children[char], curr_path + char)
        
        dfs(node, prefix)
        return results

    def count_words(self):
        return self.word_count

    def get_height(self):
        def _get_height(node):
            if not node.children:
                return 0
            return 1 + max(_get_height(child) for child in node.children.values())
        return _get_height(self.root)

    def get_total_nodes(self):
        return self.total_nodes

    def delete(self, username):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_username:
                    return False
                node.is_end_of_username = False
                node.user_id = None
                self.word_count -= 1
                return len(node.children) == 0
            
            char = word[depth]
            if char not in node.children:
                return False
            
            should_delete_child = _delete(node.children[char], word, depth + 1)
            if should_delete_child:
                del node.children[char]
                self.total_nodes -= 1
                return not node.is_end_of_username and len(node.children) == 0
            return False
            
        _delete(self.root, username, 0)

class ActivitySegmentTree:
    def __init__(self, activity_array):
        self.n = len(activity_array)
        self.tree_sum = [0] * (4 * self.n)
        self.tree_max = [-float('inf')] * (4 * self.n)
        self.tree_min = [float('inf')] * (4 * self.n)
        self.build(activity_array)

    def build(self, activity_array):
        def _build(node, start, end):
            if start == end:
                val = activity_array[start]
                self.tree_sum[node] = val
                self.tree_max[node] = val
                self.tree_min[node] = val
                return
            mid = (start + end) // 2
            _build(2 * node, start, mid)
            _build(2 * node + 1, mid + 1, end)
            self.tree_sum[node] = self.tree_sum[2 * node] + self.tree_sum[2 * node + 1]
            self.tree_max[node] = max(self.tree_max[2 * node], self.tree_max[2 * node + 1])
            self.tree_min[node] = min(self.tree_min[2 * node], self.tree_min[2 * node + 1])

        if self.n > 0:
            _build(1, 0, self.n - 1)

    def query(self, l, r):
        def _query(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return self.tree_sum[node]
            mid = (start + end) // 2
            return _query(2 * node, start, mid, l, r) + _query(2 * node + 1, mid + 1, end, l, r)
        return _query(1, 0, self.n - 1, l, r)

    def get_range_max(self, l, r):
        def _query(node, start, end, l, r):
            if r < start or end < l:
                return -float('inf')
            if l <= start and end <= r:
                return self.tree_max[node]
            mid = (start + end) // 2
            return max(_query(2 * node, start, mid, l, r), _query(2 * node + 1, mid + 1, end, l, r))
        return _query(1, 0, self.n - 1, l, r)

    def get_range_min(self, l, r):
        def _query(node, start, end, l, r):
            if r < start or end < l:
                return float('inf')
            if l <= start and end <= r:
                return self.tree_min[node]
            mid = (start + end) // 2
            return min(_query(2 * node, start, mid, l, r), _query(2 * node + 1, mid + 1, end, l, r))
        return _query(1, 0, self.n - 1, l, r)

    def get_tree_size(self):
        return len(self.tree_sum)

    def get_height(self):
        import math
        return math.ceil(math.log2(self.n)) + 1 if self.n > 0 else 0

    def get_leaf_values(self):
        leaves = []
        def _get_leaves(node, start, end):
            if start == end:
                leaves.append(self.tree_sum[node])
                return
            mid = (start + end) // 2
            _get_leaves(2 * node, start, mid)
            _get_leaves(2 * node + 1, mid + 1, end)
        if self.n > 0:
            _get_leaves(1, 0, self.n - 1)
        return leaves