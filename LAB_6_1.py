class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user_id):
        if user_id not in  self.graph:
            self.graph[user_id] = []

    def add_friendship(self, user_id1, user_id2):
        if user_id1 in self.graph and user_id2 in self.graph:
            self.graph[user_id1].append(user_id2)
            self.graph[user_id2].append(user_id1)
        
        else:
            print("One or both users not found in the graph.")

    def remove_friendship(self, user_id1, user_id2):
        if user_id1 in self.graph and user_id2 in self.graph:
            if user_id2 in self.graph[user_id1]:
                self.graph[user_id1].remove(user_id2)
            if user_id1 in self.graph[user_id2]:
                self.graph[user_id2].remove(user_id1)

        else:
            print("One or both users not found in the graph.")

    def are_friends(self, user_id1, user_id2):
        if user_id1 in self.graph and user_id2 in self.graph:
            return user_id2 in self.graph[user_id1] and user_id1 in self.graph[user_id2]
        
        else:
            return False
        
    def get_friends(self, user_id):
        if user_id in self.graph:
            return self.graph[user_id]
        
        else:
            return None
        
    def get_degree(self, user_id):
        if user_id  in self.graph:
            return len(self.graph[user_id])
        
        else:
            return None
        
    def get_num_users(self):
        return len(self.graph)
    
    def get_num_edges(self):
        return sum(len(friends) for friends in self.graph.values()) // 2

    def show_graph(self):
        for user_id, friends in self.graph.items():
            print(f"User {user_id} has friends: {', '.join(map(str, friends))}")

    def is_complete(self):
        for friends in self.graph.values():
            if len(friends) != len(self.graph) - 1:
                return False
        
        return True
    
    def graph_density(self):
        E = self.get_num_edges()
        V = self.get_num_users()
        if V == 1:
            return 0
        D = 2*abs(E)/(abs(V)*(abs(V)-1))
        return D
    
    def degree_distribution(self):
        distribution = {}
        for number in range(len(self.graph)):
            distribution[number] = 0
        for friends in self.graph.values():
            degree = len(friends)
            distribution[degree] += 1
        
        return distribution
    




# Example usage
SocialGraph = SocialGraph()
SocialGraph.add_user(1)
SocialGraph.add_user(2)
SocialGraph.add_user(3)
SocialGraph.add_user(4)
SocialGraph.add_friendship(1, 2)
SocialGraph.show_graph()
print(SocialGraph.are_friends(1, 2))
SocialGraph.add_friendship(1, 3) 
print(SocialGraph.get_friends(1))
print(SocialGraph.get_degree(1))
print(SocialGraph.get_num_users())
print(SocialGraph.get_num_edges())
SocialGraph.remove_friendship(1, 2)
SocialGraph.show_graph()
print(SocialGraph.is_complete())
print(SocialGraph.graph_density())
print(SocialGraph.degree_distribution())


import numpy as np
from collections import Counter

class SocialGraph:
    def __init__(self, users=None):
        self.users = users if users else []
        self.num_users = len(self.users)
        self.user_to_idx = {user: i for i, user in enumerate(self.users)}
        self.idx_to_user = {i: user for i, user in enumerate(self.users)}
        
        self.adj_list = {user: [] for user in self.users}
        
        self.adj_matrix = np.zeros((self.num_users, self.num_users), dtype=int)

    def add_friendship(self, u, v):
        if u in self.user_to_idx and v in self.user_to_idx:
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)
            
            idx_u, idx_v = self.user_to_idx[u], self.user_to_idx[v]
            self.adj_matrix[idx_u, idx_v] = 1
            self.adj_matrix[idx_v, idx_u] = 1

    def remove_friendship(self, u, v):
        if u in self.user_to_idx and v in self.user_to_idx:
            if v in self.adj_list[u]: self.adj_list[u].remove(v)
            if u in self.adj_list[v]: self.adj_list[v].remove(u)
            
            idx_u, idx_v = self.user_to_idx[u], self.user_to_idx[v]
            self.adj_matrix[idx_u, idx_v] = 0
            self.adj_matrix[idx_v, idx_u] = 0

    def are_friends(self, u, v):
        idx_u, idx_v = self.user_to_idx[u], self.user_to_idx[v]
        return self.adj_matrix[idx_u, idx_v] == 1

    def get_friends(self, u):
        return self.adj_list[u]

    def get_degree(self, u):
        return len(self.adj_list[u])

    def get_num_users(self):
        return self.num_users

    def get_num_edges(self):
        return np.count_nonzero(self.adj_matrix) // 2

    def is_complete_graph(self):
        V = self.num_users
        expected_edges = V * (V - 1) // 2
        return self.get_num_edges() == expected_edges

    def graph_density(self):
        V = self.num_users
        E = self.get_num_edges()
        if V < 2: 
            return 0.0
        return (2 * E) / (V * (V - 1))

    def degree_distribution(self):
        degrees = [len(friends) for friends in self.adj_list.values()]
        return dict(Counter(degrees))


    def matrix_to_list(self):
        new_list = {user: [] for user in self.users}
        for i in range(self.num_users):
            for j in range(i + 1, self.num_users):
                if self.adj_matrix[i, j] == 1:
                    u, v = self.idx_to_user[i], self.idx_to_user[j]
                    new_list[u].append(v)
                    new_list[v].append(u)
        self.adj_list = new_list
        return self.adj_list

    def list_to_matrix(self):
        new_matrix = np.zeros((self.num_users, self.num_users), dtype=int)
        for u, neighbors in self.adj_list.items():
            for v in neighbors:
                idx_u, idx_v = self.user_to_idx[u], self.user_to_idx[v]
                new_matrix[idx_u, idx_v] = 1
        self.adj_matrix = new_matrix
        return self.adj_matrix

