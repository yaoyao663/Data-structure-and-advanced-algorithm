import numpy as np
import matplotlib.pyplot as plt

def fractal_dimension(fractal_image, box_sizes):
    counts = [] # List to store the number of boxes containing the fractal for each box size
    
    # 1. Count the valid boxes for each specified box size
    for size in box_sizes:
        count = 0
        
        # Iterate over the entire image matrix with a step equal to the current box 'size'
        for y in range(0, fractal_image.shape[0], size):
            for x in range(0, fractal_image.shape[1], size):
                
                # Slice the numpy array to extract the current box region
                box = fractal_image[y:y+size, x:x+size]
                
                # If this box contains any part of the fractal (any pixel value > 0), count it
                if np.any(box > 0):
                    count += 1
                    
        counts.append(count)
        
    # 2. Calculate log(count) and log(1/size)
    log_counts = np.log(counts)
    log_inv_sizes = np.log([1.0 / s for s in box_sizes])
    
    # 3. Use linear regression (least squares method) to calculate the slope
    coefficients = np.polyfit(log_inv_sizes, log_counts, 1)
    slope = coefficients[0]     # This slope (m) is our fractal dimension
    intercept = coefficients[1] # The y-intercept (c)
    
    # 4. Plot the results on a log-log graph (log(count) vs log(1/size))
    plt.figure(figsize=(8, 6))
    
    # Plot the actual data points from our box counting
    plt.plot(log_inv_sizes, log_counts, 'bo-', label='Box counts') 
    
    # Plot the best-fit line based on the calculated slope and intercept
    fitted_line = slope * log_inv_sizes + intercept
    plt.plot(log_inv_sizes, fitted_line, 'r--', label=f'Linear fit (Slope D = {slope:.3f})')
    
    # Add labels and styling to the chart
    plt.xlabel('log(1/size)')
    plt.ylabel('log(count)')
    plt.title('Fractal Dimension via Box-Counting')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return slope

# ==========================================
# Main Execution / Test Code
# ==========================================
if __name__ == "__main__":
    # Create a 512x512 matrix filled with zeros (representing a blank canvas)
    test_image = np.zeros((512, 512))
    
    # Simulate a straight diagonal line across the image
    # Note: The theoretical fractal dimension of a simple straight line is exactly 1.0
    for i in range(512):
        test_image[i, i] = 1
        
    # Define the box sizes to test 
    # (Using decreasing powers of 2 is standard practice for clean grid division)
    sizes_to_test = [128, 64, 32, 16, 8, 4, 2]
    
    # Run the function and print the result
    estimated_dim = fractal_dimension(test_image, sizes_to_test)
    print(f"Estimated Fractal Dimension: {estimated_dim:.4f}")