import numpy as np
import matplotlib.pyplot as plt

def midpoint_displacement(x1, y1, x2, y2, roughness, depth):
    if depth == 0:
        return []
    point_list = []
    midpoint = [(x1 + x2)/2, (y1 + y2)/2]
    midpoint[1] += roughness*np.random.uniform(-1, 1)
    
    new_roughness = roughness * 0.6
    point_list.extend(midpoint_displacement(x1, y1, midpoint[0], midpoint[1], new_roughness, depth-1))
    point_list.append(midpoint)
    point_list.extend(midpoint_displacement(midpoint[0], midpoint[1], x2, y2, new_roughness, depth-1))
    
    return point_list


# ==========================================
# test
# ==========================================
def test_generation():
    start_x, start_y = 0, 0
    end_x, end_y = 100, 0
    initial_roughness = 20  
    recursion_depth = 20    
    
    generated_points = midpoint_displacement(
        start_x, start_y, end_x, end_y, initial_roughness, recursion_depth
    )
    
    all_points = [[start_x, start_y]] + generated_points + [[end_x, end_y]]
    
    x_coords = [point[0] for point in all_points]
    y_coords = [point[1] for point in all_points]
    
    plt.figure(figsize=(10, 4))
    plt.plot(x_coords, y_coords, color='forestgreen', linewidth=1.5)
    
    plt.fill_between(x_coords, y_coords, min(y_coords)-10, color='saddlebrown', alpha=0.6)
    
    plt.title(f"1D Procedural Terrain (Depth: {recursion_depth})")
    plt.xlabel("X")
    plt.ylabel("Height (Y)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

if __name__ == "__main__":
    test_generation()