def draw_sierpinski(canvas, x, y, size, depth):
    # 1. 基础情况 (Base Case)：深度为 0 时，直接画一个实心三角形
    if depth == 0:
        # 计算等边/等腰三角形的三个顶点
        # 顶点1：顶部居中
        h = (size * (3 ** 0.5)) / 2  # 等边三角形的高度
        p1_x = x + (size / 2)
        p1_y = y
        # 顶点2：左下角
        p2_x = x
        p2_y = y + h
        # 顶点3：右下角
        p3_x = x + size
        p3_y = y + h
        
        # 在 canvas 上绘制多边形（三角形）
        canvas.create_polygon(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, fill="black", outline="black")
        
    # 2. 递归步骤 (Recursive Step)：深度大于 0 时，画 3 个更小的三角形
    else:
        new_size = size / 2
        new_h = (new_size * (3 ** 0.5)) / 2
        # 递归调用 1：顶部的小三角形
        draw_sierpinski(canvas, x + (new_size / 2), y, new_size, depth - 1)
        
        # 递归调用 2：左下角的小三角形
        draw_sierpinski(canvas, x, y + new_h, new_size, depth - 1)
        
        # 递归调用 3：右下角的小三角形
        draw_sierpinski(canvas, x + new_size, y + new_h, new_size, depth - 1)
        
# 示例用法
if __name__ == "__main__":
    import tkinter as tk
    
    # 创建主窗口
    root = tk.Tk()
    root.title("Sierpinski Triangle")
    
    # 创建画布
    canvas_size = 600
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
    canvas.pack()
    
    # 绘制 Sierpinski 三角形
    initial_size = 400
    initial_depth = 5
    draw_sierpinski(canvas, (canvas_size - initial_size) / 2, (canvas_size - initial_size) / 2, initial_size, initial_depth)
    
    # 启动主循环
    root.mainloop()