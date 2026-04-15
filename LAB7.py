import random

def split_region(x, y, width, height, min_size):
    if width <= min_size or height <= min_size:
        return [(x, y, width, height)]
    
    mid_w = width // 2
    mid_h = height // 2
    
    quadrants = []
    quadrants.extend(split_region(x, y, mid_w, mid_h, min_size))
    quadrants.extend(split_region(x + mid_w, y, mid_w, mid_h, min_size))
    quadrants.extend(split_region(x, y + mid_h, mid_w, mid_h, min_size))
    quadrants.extend(split_region(x + mid_w, y + mid_h, mid_w, mid_h, min_size))
    
    return quadrants

def count_points_in_region(points, region):
    rx, ry, rw, rh = region
    return sum(1 for px, py in points if rx <= px < rx + rw and ry <= py < ry + rh)

def find_dense_regions(points, x, y, width, height, min_size, density_threshold):
    current_region = (x, y, width, height)
    num_points = count_points_in_region(points, current_region)
    area = width * height
    density = num_points / area if area > 0 else 0
    
    results = []
    if density > density_threshold:
        results.append({"region": current_region, "points": num_points, "density": round(density, 4)})

    if width > min_size and height > min_size:
        hw, hh = width // 2, height // 2
        sub_regions = [
            (x, y, hw, hh),
            (x + hw, y, hw, hh),
            (x, y + hh, hw, hh),
            (x + hw, y + hh, hw, hh)
        ]
        for sub in sub_regions:
            results.extend(find_dense_regions(points, *sub, min_size, density_threshold))
            
    return results

def run_test_cases():
    print("--- Test Case 1: Uniform Distribution ---")
    random.seed(42)
    pts1 = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(200)]
    results1 = find_dense_regions(pts1, 0, 0, 100, 100, 25, 0.03)
    for r in results1:
        print(f"Region: {r['region']}, Points: {r['points']}, Density: {r['density']}")

    print("\n--- Test Case 2: Highly Clustered (Top-Left) ---")
    pts2 = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(50)]
    results2 = find_dense_regions(pts2, 0, 0, 100, 100, 20, 0.1)
    for r in results2:
        print(f"Region: {r['region']}, Points: {r['points']}, Density: {r['density']}")

    print("\n--- Test Case 3: Small min_size on Empty Space ---")
    pts3 = [(50, 50)]
    results3 = find_dense_regions(pts3, 0, 0, 100, 100, 40, 0.0001)
    for r in results3:
        print(f"Region: {r['region']}, Points: {r['points']}, Density: {r['density']}")

if __name__ == "__main__":
    run_test_cases()