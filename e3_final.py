from collections import deque

class SocialGraph:
    def __init__(self, num_users):
        self.num_users = num_users
        self.num_edges = 0
        
        self.adj_list = {i: set() for i in range(1, num_users+1)}

    def add_user(self):
        self.num_users += 1
        self.adj_list[self.num_users] = set()
        return self.num_users

    def add_friendship(self, u, v):
        if 1 <= u <= self.num_users and 1 <= v <= self.num_users:
            if u != v and v not in self.adj_list[u]:
                self.adj_list[u].add(v)
                self.adj_list[v].add(u)
                
                self.num_edges += 1
                return True
        return False

    def get_friends(self, u):
        return self.adj_list.get(u, set())
    
    
    # Part 1 : Implement BFS traversals
    
    # Part A - Basic BFS using queue
    def bfs(self, start_user):
        result = []
        queue = deque([start_user])
        visited = {start_user} 
        while len(queue) > 0 :
            current = queue.popleft()
            result.append(current)
            for i in self.adj_list[current]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return result
        
    # Part B - BFS with distance tracking
    def bfs_with_distances(self, start_user):
        distance = {start_user:0}
        queue = deque([start_user])
        while len(queue) > 0 :
            current = queue.popleft()
            
            for i in self.adj_list[current]:
                if i not in distance: 
                    queue.append(i)
                    distance[i] = distance[current] + 1
        return distance
    
    # Part C - Find shortest path between users
    def shortest_path(self, start_user, target_user):
        if start_user == target_user: # 判断特殊情况
            return [start_user]
        
        parent_dict = {start_user:None}
        queue = deque([start_user])
        
        while len(queue) > 0 :
            current = queue.popleft()
            
            for i in self.adj_list[current]:
                if i not in parent_dict: 
                    parent_dict[i] = current
                    if i == target_user:
                        path = []
                        temp = target_user
                        while temp is not None:
                            path.append(temp)
                            temp = parent_dict[temp]
                        return path[::-1] 
                        
                    queue.append(i)
        return None
    
    # Part D - Find degrees of separation
    def degrees_of_separation(self, start_user, target_user):
        if start_user == target_user:
            return 0
        distance = {start_user:0}
        queue = deque([start_user])
        
        while len(queue) > 0 :
            current = queue.popleft()
            
            for i in self.adj_list[current]:
                if i not in distance: 
                    queue.append(i)
                    distance[i] = distance[current] + 1
                    if i == target_user:
                        return distance[i]
        return -1
    
    # Part E - Find all users within k hops
    def friends_with_k_hops(self, start_user, k):
        k_hops_friends = set() # a = set()才是创建集合， a = {}是创建字典
        distance = {start_user:0}
        queue = deque([start_user])
        
        while len(queue) > 0 :
            current = queue.popleft()
            if distance[current] == k: # 注意检查k的条件应该在循环开始时进行，这样才能正确地收集所有距离为k的用户
                return k_hops_friends
                    
            for i in self.adj_list[current]:
                if i not in distance: # 直接检查 distance 字典来判断是否访问过，避免了额外的 visited 集合
                    queue.append(i)
                    distance[i] = distance[current] + 1
                    k_hops_friends.add(i)
                    
        return k_hops_friends
    
    
    
    # Part 2 : Implement traversal-based analytics
    def compute_average_degrees_of_separation(self):
        total_distance = 0
        total_pairs = 0
        for user in self.adj_list:
            distances = self.bfs_with_distances(user)
            
            for dist in distances.values():
                total_distance += dist
            total_pairs += len(distances) - 1 # 减去自己的距离
        return total_distance / total_pairs if total_pairs > 0 else 0 # 避免除以零的情况
    # 把全部加起来再求平均，不然每次求平均会有问题，因为每个用户的朋友数量不同，平均值会被稀释掉

    def get_distance_distribution(self, start_user):
        user_distance = self.bfs_with_distances(start_user)
        distribution = {}
        for dist in user_distance.values():
            if dist in distribution:
                distribution[dist] +=1
            else:
                distribution[dist] = 1
        return distribution
            
    def recommend_friends(self, start_user, max_recommendations = 5):
        recommendations = set()
        for friend in self.adj_list[start_user]:
            for fof in self.adj_list[friend]:
                if fof not in self.adj_list[start_user] and fof not in recommendations and fof != start_user:
                    recommendations.add(fof)
                    
                    if len(recommendations) == max_recommendations:
                        return recommendations
        return recommendations
            
    
# test
def create_test_graph(num_users, friendships, isolated_users=None):
    graph = SocialGraph(num_users)
    for u, v in friendships:
        graph.add_friendship(u, v)
        
    if isolated_users:
        for _ in range(isolated_users):
            graph.add_user()
            
    return graph




def test_social_network():
    print("==================================================")
    print("      SocialGraph Integration Test Suite          ")
    print("==================================================")
    
    print("\n[1] Setup & Initialization")
    # Define edges and initialize the graph
    edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (2, 5), (4, 5), (5, 6)]
    
    # Note: Assuming create_test_graph handles 1-indexed nodes properly based on our previous setup.
    my_social_network = create_test_graph(6, edges) 
    
    print("All initialized nodes:", list(my_social_network.adj_list.keys()))
    print("Friends of Node 1:", my_social_network.adj_list.get(1, set()))
    print("Friends of Node 2:", my_social_network.adj_list.get(2, set()))
    print("Friends of Node 3:", my_social_network.adj_list.get(3, set()))
    print("Friends of Node 4:", my_social_network.adj_list.get(4, set()))
    print("Friends of Node 5:", my_social_network.adj_list.get(5, set()))
    print("Friends of Node 6:", my_social_network.adj_list.get(6, set()))

    print("\n[2] Part A: Basic BFS using queue")
    print("BFS Traversal from Node 1:", my_social_network.bfs(1))
    print("BFS Traversal from Node 4:", my_social_network.bfs(4))

    print("\n[3] Part B: BFS with distance tracking")
    print("Distance dictionary from Node 1:", my_social_network.bfs_with_distances(1))
    print("Distance dictionary from Node 4:", my_social_network.bfs_with_distances(4))

    print("\n[4] Part C: Find shortest path between users")
    print("Shortest path from Node 1 to Node 6:", my_social_network.shortest_path(1, 6))

    print("\n[5] Part D: Find degrees of separation")
    print("Degrees of separation between 1 and 6:", my_social_network.degrees_of_separation(1, 6))

    print("\n[6] Part E: Find all users within k hops")
    print("Users within 1 hops from Node 1:", my_social_network.friends_with_k_hops(1, 1))
    print("Users within 2 hops from Node 1:", my_social_network.friends_with_k_hops(1, 2))
    print("Users within 3 hops from Node 1:", my_social_network.friends_with_k_hops(1, 3))

    print("\n[7] Analytics: Average degrees of separation")
    avg_distance = my_social_network.compute_average_degrees_of_separation()
    print(f"Global average distance: {avg_distance:.4f}")

    print("\n[8] Analytics: Distance distribution")
    print("Distance distribution for Node 1:", my_social_network.get_distance_distribution(1))

    print("\n[9] Analytics: Friend recommendations")
    print("Friend recommendations for Node 1:", my_social_network.recommend_friends(1))
    print("Friend recommendations for Node 4:", my_social_network.recommend_friends(4))
    
    print("\n==================================================")
    print("               All Tests Completed                ")
    print("==================================================")

def test_edge_cases():
    print("==================================================")
    print("           Edge Cases Test Suite                  ")
    print("==================================================")
    
    # Setup the Extreme Graph
    # 1,2,3 are fully connected. 4 is isolated. 5,6 are an isolated pair.
    edges = [(1, 2), (2, 3), (1, 3), (5, 6)]
    
    # Assuming create_test_graph handles up to node 6
    edge_graph = create_test_graph(6, edges) 
    
    print("\n[Edge Case 1] Same Start and Target Node")
    # Should handle immediately without entering the queue loop
    print("Shortest path (1 to 1):", edge_graph.shortest_path(1, 1))
    print("Degrees of sep (1 to 1):", edge_graph.degrees_of_separation(1, 1))

    print("\n[Edge Case 2] Unreachable Target (Disconnected Components)")
    # Trying to find a path across the "void" between disconnected networks
    print("Shortest path (1 to 5):", edge_graph.shortest_path(1, 5))
    print("Degrees of sep (1 to 5):", edge_graph.degrees_of_separation(1, 5))

    print("\n[Edge Case 3] Isolated Node Behavior")
    # How does an isolated user behave when searching for friends or paths?
    print("BFS from isolated Node 4:", edge_graph.bfs(4))
    print("Distance dict for Node 4:", edge_graph.bfs_with_distances(4))

    print("\n[Edge Case 4] K-Hops with k = 0")
    # k=0 means "friends within 0 distance", which should technically just be empty or self
    print("Users within 0 hops from Node 1:", edge_graph.friends_with_k_hops(1, 0))

    print("\n[Edge Case 5] K-Hops on Isolated Node")
    # Even with a large k, an isolated node should return an empty set
    print("Users within 10 hops from Node 4:", edge_graph.friends_with_k_hops(4, 10))

    print("\n[Edge Case 6] Friend Recommendations for Fully Connected User")
    # Node 1 is already friends with 2 and 3. There are no "friends of friends" left to recommend.
    # It should return an empty set without crashing.
    print("Recommendations for Node 1:", edge_graph.recommend_friends(1))

    print("\n[Edge Case 7] Friend Recommendations for Isolated Node")
    # Node 4 has no friends, so it cannot have "friends of friends".
    print("Recommendations for Node 4:", edge_graph.recommend_friends(4))

    print("\n==================================================")
    print("           Edge Case Tests Completed              ")
    print("==================================================")

# Execute the test suite
if __name__ == "__main__":
    test_social_network()
    test_edge_cases()