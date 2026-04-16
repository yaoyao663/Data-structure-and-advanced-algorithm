import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_terrain(width, height, roughness, depth):
    size = (1 << depth) + 1
    
    grid = np.zeros((size, size))
    
    grid[0, 0] = 0
    grid[0, size-1] = 0
    grid[size-1, 0] = 0
    grid[size-1, size-1] = 0
    step_size = size - 1
    current_roughness = roughness
    
    while step_size > 1:
        half_step = step_size // 2
    
        for y in range(0, size - 1, step_size):
            for x in range(0, size - 1, step_size):
                # 获取正方形的四个角的值
                top_left = grid[y, x]
                top_right = grid[y, x + step_size]
                bottom_left = grid[y + step_size, x]
                bottom_right = grid[y + step_size, x + step_size]
                
                # 计算平均值并加上随机偏移
                avg = (top_left + top_right + bottom_left + bottom_right) / 4.0
                offset = np.random.uniform(-1, 1) * current_roughness
                
                # 赋值给正方形的中心点
                grid[y + half_step, x + half_step] = avg + offset

        for y in range(0, size, half_step):
            x_start = half_step if (y % step_size == 0) else 0
            
            for x in range(x_start, size, step_size):
                points = []
                if y - half_step >= 0:   points.append(grid[y - half_step, x]) # 上
                if y + half_step < size: points.append(grid[y + half_step, x]) # 下
                if x - half_step >= 0:   points.append(grid[y, x - half_step]) # 左
                if x + half_step < size: points.append(grid[y, x + half_step]) # 右
                
                # 计算平均值并加上随机偏移
                avg = sum(points) / len(points)
                offset = np.random.uniform(-1, 1) * current_roughness
                
                # 赋值给边中点
                grid[y, x] = avg + offset
            
        step_size //= 2
        current_roughness *= 0.5
        
    final_width = min(width, size)
    final_height = min(height, size)
    
    return grid[:final_height, :final_width]


# ==========================================
# test
# ==========================================
if __name__ == "__main__":
    # 参数设置：深度设为 6，意味着生成 65x65 的原始网格
    W, H = 65, 65
    ROUGHNESS = 15.0
    DEPTH = 6  
    
    # 生成地形
    terrain = generate_terrain(W, H, ROUGHNESS, DEPTH)
    
    # 创建一个画布，包含两个子图 (2D 俯视图 和 3D 表面图)
    fig = plt.figure(figsize=(14, 6))
    
    # --- 绘制 2D 地形图 ---
    ax1 = fig.add_subplot(121)
    # 使用 'terrain' 颜色映射表，完美还原水域、草地、高山和雪顶
    im = ax1.imshow(terrain, cmap='terrain', origin='lower')
    ax1.set_title(f"2D Top-Down View (Depth: {DEPTH})")
    fig.colorbar(im, ax=ax1, shrink=0.7)
    
    # --- 绘制 3D 地形图 ---
    ax2 = fig.add_subplot(122, projection='3d')
    X, Y = np.meshgrid(np.arange(terrain.shape[1]), np.arange(terrain.shape[0]))
    # 渲染 3D 表面
    surf = ax2.plot_surface(X, Y, terrain, cmap='terrain', 
                            linewidth=0, antialiased=False, alpha=0.9)
    ax2.set_title("3D Isometric View")
    
    # 隐藏 3D 图的坐标轴标签，让其更美观
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.set_zticklabels([])
    
    plt.tight_layout()
    plt.show()