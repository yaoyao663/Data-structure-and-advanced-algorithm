import numpy as np
import matplotlib.pyplot as plt
import random

def split_region(x, y, w, h, min_size, regions):
    if w <= min_size or h <= min_size:
        return
    regions.append((x, y, w, h))
    hw, hh = w / 2, h / 2
    split_region(x, y, hw, hh, min_size, regions)
    split_region(x + hw, y, hw, hh, min_size, regions)
    split_region(x, y + hh, hw, hh, min_size, regions)
    split_region(x + hw, y + hh, hw, hh, min_size, regions)

def count_points_in_region(points, x, y, w, h):
    count = 0
    for px, py in points:
        if x <= px < x + w and y <= py < y + h:
            count += 1
    return count

def draw_tree(canvas, x, y, length, angle, depth):
    if depth == 0:
        x_end = x + length * np.cos(np.radians(angle))
        y_end = y + length * np.sin(np.radians(angle))
        canvas.plot([x, x_end], [y, y_end], color='green', lw=1)
        return
    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))
    canvas.plot([x, x_end], [y, y_end], color='brown', lw=depth)
    draw_tree(canvas, x_end, y_end, length * 0.7, angle - 30, depth - 1)
    draw_tree(canvas, x_end, y_end, length * 0.7, angle + 30, depth - 1)

def midpoint_displacement(h1, h2, roughness, depth):
    if depth == 0:
        return []
    mid = (h1 + h2) / 2 + random.uniform(-roughness, roughness)
    return midpoint_displacement(h1, mid, roughness / 2, depth - 1) + [mid] + midpoint_displacement(mid, h2, roughness / 2, depth - 1)

def generate_terrain_1d(width, roughness, depth):
    h1, h2 = 0, 0
    points = [h1] + midpoint_displacement(h1, h2, roughness, depth) + [h2]
    return points

def measure_fractal_dimension(points, box_sizes):
    counts = []
    for s in box_sizes:
        count = 0
        for i in range(0, len(points), s):
            count += 1
        counts.append(count)
    coeffs = np.polyfit(np.log(1/np.array(box_sizes)), np.log(counts), 1)
    return coeffs[0]

def detect_artifacts(terrain, threshold):
    artifacts = []
    for i in range(1, len(terrain)):
        if abs(terrain[i] - terrain[i-1]) > threshold:
            artifacts.append(i)
    return artifacts

def run_integration():
    depth = 8
    terrain = generate_terrain_1d(512, 100, depth)
    
    box_sizes = [2**i for i in range(1, 5)]
    d_dim = measure_fractal_dimension(terrain, box_sizes)
    print(f"Fractal Dimension D: {d_dim:.2f}")
    
    if d_dim < 1.8 or d_dim > 2.5:
        print("Warning: Unnatural Fractal Dimension!")
        
    artifacts = detect_artifacts(terrain, 50)
    
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    ax[0].plot(terrain)
    for idx in artifacts:
        ax[0].plot(idx, terrain[idx], 'ro')
    ax[0].set_title("Terrain with Artifacts")
    
    regions = []
    split_region(0, 0, 512, 512, 64, regions)
    for r in regions:
        rect = plt.Rectangle((r[0], r[1]), r[2], r[3], fill=False, edgecolor='blue', alpha=0.3)
        ax[1].add_patch(rect)
    ax[1].set_xlim(0, 512)
    ax[1].set_ylim(0, 512)
    ax[1].set_title("Quadtree Split View")
    plt.show()

if __name__ == "__main__":
    run_integration()