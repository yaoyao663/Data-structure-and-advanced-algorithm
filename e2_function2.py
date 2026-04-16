import math
import tkinter as tk

def draw_tree(canvas, x, y, length, angle, depth):
    # 1. Convert the angle from degrees to radians for math.sin and math.cos
    angle_rad = math.radians(angle)
    
    # 2. Calculate the end coordinates of the current branch
    # X coordinate uses cosine, Y coordinate uses sine.
    # Note: We subtract for Y because the canvas Y-axis points downwards.
    end_x = x + length * math.cos(angle_rad)
    end_y = y - length * math.sin(angle_rad)
    
    # Dynamically adjust line width based on current depth 
    # (The trunk is the thickest, getting thinner towards the leaves, minimum width is 1)
    line_width = max(1, depth)
    
    # 3. Base Case: Draw the final "leaf" (end of the branch) and stop recursion
    if depth == 0:
        canvas.create_line(x, y, end_x, end_y, fill="green", width=1)
        return  # Stop execution here for this branch
        
    # 4. Recursive Step
    else:
        # Draw the current branch/trunk
        canvas.create_line(x, y, end_x, end_y, fill="saddlebrown", width=line_width)
        
        # Calculate the length of the next level branches (e.g., scale down to 70%)
        new_length = length * 0.7
        
        # Recursive Call 1: Grow the left branch (angle increases by +30 degrees)
        draw_tree(canvas, end_x, end_y, new_length, angle + 30, depth - 1)
        
        # Recursive Call 2: Grow the right branch (angle decreases by -30 degrees)
        draw_tree(canvas, end_x, end_y, new_length, angle - 30, depth - 1)


# ==========================================
# Main Execution / Test Code
# ==========================================
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Fractal Tree Generator")
    
    # Create the canvas
    canvas_size = 600
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
    canvas.pack()
    
    # Set initial parameters:
    # Place the root of the tree at the bottom-center of the canvas
    start_x = canvas_size / 2
    start_y = canvas_size
    initial_length = 150   # Length of the main trunk
    initial_angle = 90     # 90 degrees represents growing straight up
    initial_depth = 8      # Recursion depth (higher = denser tree, 8-10 is recommended)
    
    # Call the function to start drawing the tree
    draw_tree(canvas, start_x, start_y, initial_length, initial_angle, initial_depth)
    
    # Start the GUI main loop
    root.mainloop()