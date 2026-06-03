import math

# 参数设置
width, height = 800, 500
margin = 80
plot_w = width - 2 * margin
plot_h = height - 2 * margin

x_min, x_max = -20, 20
y_min, y_max = -0.4, 1.2

def to_px(x, y):
    """将数学坐标转为SVG像素坐标"""
    px = margin + (x - x_min) / (x_max - x_min) * plot_w
    py = margin + (y_max - y) / (y_max - y_min) * plot_h
    return px, py

# 生成数据点
points = []
n = 500
for i in range(n + 1):
    x = x_min + (x_max - x_min) * i / n
    if abs(x) < 1e-10:
        y = 1.0  # lim sin(x)/x = 1
    else:
        y = math.sin(x) / x
    # 裁剪到可视范围
    y_clamped = max(y_min, min(y_max, y))
    px, py = to_px(x, y_clamped)
    points.append(f"{px:.1f},{py:.1f}")

# 构建 SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  
  <!-- 标题 -->
  <text x="{width/2}" y="30" text-anchor="middle" font-size="18" font-family="serif" font-style="italic">
    y = sin(x) / x
  </text>
'''

# 网格线
svg += '  <!-- 网格线 -->\n  <g stroke="#e0e0e0" stroke-width="0.5">\n'
# 水平网格
for yv in [-0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    _, py = to_px(0, yv)
    svg += f'    <line x1="{margin}" y1="{py:.1f}" x2="{width-margin}" y2="{py:.1f}"/>\n'
# 垂直网格
for xv in range(-15, 16, 5):
    px, _ = to_px(xv, 0)
    svg += f'    <line x1="{px:.1f}" y1="{margin}" x2="{px:.1f}" y2="{height-margin}"/>\n'
svg += '  </g>\n'

# 坐标轴
ax_x0, ax_y0 = to_px(0, 0)
svg += f'''
  <!-- 坐标轴 -->
  <line x1="{margin}" y1="{ax_y0:.1f}" x2="{width-margin}" y2="{ax_y0:.1f}" stroke="black" stroke-width="1"/>
  <line x1="{ax_x0:.1f}" y1="{margin}" x2="{ax_x0:.1f}" y2="{height-margin}" stroke="black" stroke-width="1"/>
'''

# X 轴刻度标签
svg += '  <!-- X轴刻度 -->\n'
for xv in range(-20, 21, 5):
    if xv == 0:
        continue
    px, py = to_px(xv, 0)
    svg += f'  <text x="{px:.1f}" y="{py+15:.1f}" text-anchor="middle" font-size="10">{xv}</text>\n'

# Y 轴刻度标签
svg += '  <!-- Y轴刻度 -->\n'
for yv_10 in range(-4, 13, 2):  # -0.4 到 1.2，步长 0.2
    yv = yv_10 / 10
    if yv == 0:
        continue
    px, py = to_px(0, yv)
    svg += f'  <text x="{px-8:.1f}" y="{py+4:.1f}" text-anchor="end" font-size="10">{yv:.1f}</text>\n'

# 轴标签
svg += f'  <text x="{width-margin+10}" y="{ax_y0+4:.1f}" font-size="13" font-family="serif" font-style="italic">x</text>\n'
svg += f'  <text x="{ax_x0+8:.1f}" y="{margin-5}" font-size="13" font-family="serif" font-style="italic">y</text>\n'

# 曲线
points_str = " ".join(points)
svg += f'''
  <!-- 函数曲线 -->
  <polyline fill="none" stroke="#2196F3" stroke-width="2.5" stroke-linejoin="round" 
            points="{points_str}"/>
'''

# 标注 (0, 1) 点
p0x, p0y = to_px(0, 1)
svg += f'''
  <!-- 标注极限点 -->
  <circle cx="{p0x:.1f}" cy="{p0y:.1f}" r="4" fill="#F44336"/>
  <text x="{p0x+10:.1f}" y="{p0y-8:.1f}" font-size="12" fill="#F44336">lim(x→0) = 1</text>
'''

# 图例
svg += f'''
  <!-- 图例 -->
  <rect x="{width-200}" y="45" width="130" height="28" fill="white" stroke="#ccc" rx="4"/>
  <line x1="{width-190}" y1="59" x2="{width-160}" y2="59" stroke="#2196F3" stroke-width="2.5"/>
  <text x="{width-155}" y="64" font-size="12" font-family="serif">y = sin(x)/x</text>
'''

svg += '</svg>\n'

# 写入文件
with open('/projects/sandbox/sinc_function.svg', 'w') as f:
    f.write(svg)

print("✅ 图像已生成: sinc_function.svg")
print(f"   数据点数: {len(points)}")
print(f"   x 范围: [{x_min}, {x_max}]")
print(f"   y 范围: [{y_min}, {y_max}]")
print(f"\n函数特点:")
print(f"   • x=0 时，lim sin(x)/x = 1")
print(f"   • 函数是偶函数：f(-x) = f(x)")
print(f"   • 零点位于 x = nπ (n=±1,±2,...)")
print(f"   • 随 |x| 增大，振幅逐渐衰减趋于 0")
