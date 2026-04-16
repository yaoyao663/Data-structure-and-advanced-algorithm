import numpy as np

def detect_artifacts(terrain_grid, threshold):
    grid = np.asarray(terrain_grid)
    rows, cols = grid.shape
    artifacts = []
    
    for r in range(rows):
        for c in range(cols):
            neighbors = []
            
            if r > 0:
                neighbors.append(grid[r-1, c])
            if r < rows - 1:
                neighbors.append(grid[r+1, c])
            if c > 0:
                neighbors.append(grid[r, c-1])
            if c < cols - 1:
                neighbors.append(grid[r, c+1])
                
            if any(abs(grid[r, c] - n) > threshold for n in neighbors):
                artifacts.append((r, c))
                
    return artifacts