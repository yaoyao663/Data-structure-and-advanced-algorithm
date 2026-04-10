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
    
    def dfs_recursive(self, user_id):
        visited = [user_id]
        def dfs_helper(current_user):
            for friend in self.graph[current_user]:
                if friend not in visited:
                    visited.append(friend)
                    dfs_helper(friend)
            
        dfs_helper(user_id)
        return visited
    
    def dfs_iterative(self, user_id):
        visited = []
        stack = [user_id]
        while stack:
            current_user = stack.pop()
            if current_user not in visited:
                visited.append(current_user)
                for friend in self.graph[current_user]:
                    if friend not in visited:
                        stack.append(friend)
        
        return visited
    
    def find_connected_components(self):
        visited = []
        components = []
        for user_id in self.graph:
            if user_id not in visited:
                component = self.dfs_recurive(user_id)
                components.append(component)
                visited.extend(component)
        
        return components
    
    def is_connected(self):
        if not self.graph:
            return True
        visited = self.dfs_recurive(next(iter(self.graph)))
        return len(visited) == len(self.graph)
    
    def have_path(self, user_id1, user_id2):
        if user_id1 in self.graph and user_id2 in self.graph:
            visited = self.dfs_recurive(user_id1)
            return user_id2 in visited
        
        else:
            return False
        
    def find_path(self, user_id1, user_id2):
        if user_id1 in self.graph and user_id2 in self.graph:
            visited = set()
            path = []
            def dfs(current_user):
                visited.add(current_user)
                path.append(current_user)
                if current_user == user_id2:
                    return True
                for friend in self.graph[current_user]:
                    if friend not in visited:
                        if dfs(friend):
                            return True
                path.pop()
                return False
            
            dfs(user_id1)
            return path
        
        else:
            return None
        
    def get_connected_size(self):
        visited = []
        sizes = []
        for user_id in self.graph:
            if user_id not in visited:
                component = self.dfs_recurive(user_id)
                visited.extend(component)
                sizes.append(len(component))
        return sizes

    def find_largest_component(self):
        visited = []
        largest_component = []
        for user_id in self.graph:
            if user_id not in visited:
                component = self.dfs_recurive(user_id)
                visited.extend(component)
                if len(component) > len(largest_component):
                    largest_component = component
        return largest_component
    
    def find_isolated_users(self):
        isolated_users = []
        for user_id, friends in self.graph.items():
            if not friends:
                isolated_users.append(user_id)
        return isolated_users
    


# Example usage
if __name__ == "__main__":
    graph = SocialGraph()
    graph.add_user(1)
    graph.add_user(2)
    graph.add_user(3)
    graph.add_user(4)
    graph.add_friendship(1, 2)
    graph.add_friendship(2, 3)
    graph.show_graph()
    print("Is complete:", graph.is_complete())
    print("Graph density:", graph.graph_density())
    print("Degree distribution:", graph.degree_distribution())
    print("DFS Recursive from user 1:", graph.dfs_recursive(1))
    print("DFS Iterative from user 1:", graph.dfs_iterative(1))
    print("Connected components:", graph.find_connected_components())
    print("Is connected:", graph.is_connected())
    print("Path between user 1 and 3:", graph.find_path(1, 3))
    print("Connected component sizes:", graph.get_connected_size())
    print("Largest component:", graph.find_largest_component())
    print("Isolated users:", graph.find_isolated_users())