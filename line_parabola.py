import math

# ===== 示例参数（一般式 y = a x^2 + b x + c） =====
a, b, c = 1.0, -2.0, -3.0   # 抛物线 y = x^2 - 2x - 3
# 两个交点横坐标
x1, x2 = -2.0, 3.0

# 由公式：斜率 k = a(x1+x2)+b，截距 m = c - a*x1*x2
k = a * (x1 + x2) + b
m = c - a * x1 * x2

# 交点纵坐标（用抛物线算）
y1 = a * x1 * x1 + b * x1 + c
y2 = a * x2 * x2 + b * x2 + c

# ===== 画布设置 =====
width, height = 760, 560
margin = 60
plot_w = width - 2 * margin
plot_h = height - 2 * margin

x_min, x_max = -3.5, 4.5
y_min, y_max = -5.0, 6.0

def to_px(x, y):
    px = margin + (x - x_min) / (x_max - x_min) * plot_w
    py = margin + (y_max - y) / (y_max - y_min) * plot_h
    return px, py

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="28" text-anchor="middle" font-size="18" font-family="serif">
    直线与抛物线 y = a x&#178; + b x + c 交于两点
  </text>
'''

# 网格
svg += '  <g stroke="#e8e8e8" stroke-width="0.5">\n'
xv = math.ceil(x_min)
while xv <= x_max:
    px, _ = to_px(xv, 0)
    svg += f'    <line x1="{px:.1f}" y1="{margin}" x2="{px:.1f}" y2="{height-margin}"/>\n'
    xv += 1
yv = math.ceil(y_min)
while yv <= y_max:
    _, py = to_px(0, yv)
    svg += f'    <line x1="{margin}" y1="{py:.1f}" x2="{width-margin}" y2="{py:.1f}"/>\n'
    yv += 1
svg += '  </g>\n'

# 坐标轴
ax0x, ax0y = to_px(0, 0)
svg += f'  <line x1="{margin}" y1="{ax0y:.1f}" x2="{width-margin}" y2="{ax0y:.1f}" stroke="black" stroke-width="1"/>\n'
svg += f'  <line x1="{ax0x:.1f}" y1="{margin}" x2="{ax0x:.1f}" y2="{height-margin}" stroke="black" stroke-width="1"/>\n'
svg += f'  <text x="{width-margin+8}" y="{ax0y+4:.1f}" font-size="13" font-style="italic">x</text>\n'
svg += f'  <text x="{ax0x+6:.1f}" y="{margin-4}" font-size="13" font-style="italic">y</text>\n'

# 刻度
xv = math.ceil(x_min)
while xv <= x_max:
    if xv != 0:
        px, py = to_px(xv, 0)
        svg += f'  <text x="{px:.1f}" y="{py+15:.1f}" text-anchor="middle" font-size="10">{xv}</text>\n'
    xv += 1
yv = math.ceil(y_min)
while yv <= y_max:
    if yv != 0:
        px, py = to_px(0, yv)
        svg += f'  <text x="{px-8:.1f}" y="{py+4:.1f}" text-anchor="end" font-size="10">{yv}</text>\n'
    yv += 1

# 抛物线 y = a x^2 + b x + c
pts = []
n = 300
for i in range(n + 1):
    x = x_min + (x_max - x_min) * i / n
    y = a * x * x + b * x + c
    if y_min - 1 <= y <= y_max + 1:
        px, py = to_px(x, y)
        pts.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#9C27B0" stroke-width="2.5" points="{" ".join(pts)}"/>\n'

# 直线 y = kx + m （画在可视范围内）
lx1, ly1 = to_px(x_min, k * x_min + m)
lx2, ly2 = to_px(x_max, k * x_max + m)
svg += f'  <line x1="{lx1:.1f}" y1="{ly1:.1f}" x2="{lx2:.1f}" y2="{ly2:.1f}" stroke="#2196F3" stroke-width="2.5"/>\n'

# 交点
for (xi, yi, name) in [(x1, y1, "A (x\u2081)"), (x2, y2, "B (x\u2082)")]:
    cx, cy = to_px(xi, yi)
    svg += f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="#F44336"/>\n'
    svg += f'  <text x="{cx+8:.1f}" y="{cy-8:.1f}" font-size="12" fill="#F44336">{name}=({xi:.0f},{yi:.0f})</text>\n'
    # 虚线投影到 x 轴
    _, axy = to_px(xi, 0)
    svg += f'  <line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx:.1f}" y2="{axy:.1f}" stroke="#F44336" stroke-width="1" stroke-dasharray="4 3"/>\n'

# 图例
svg += f'''
  <rect x="{margin+10}" y="{margin+10}" width="230" height="56" fill="white" stroke="#ccc" rx="4"/>
  <line x1="{margin+22}" y1="{margin+30}" x2="{margin+52}" y2="{margin+30}" stroke="#9C27B0" stroke-width="2.5"/>
  <text x="{margin+58}" y="{margin+34}" font-size="12">抛物线  y = x&#178; - 2x - 3</text>
  <line x1="{margin+22}" y1="{margin+50}" x2="{margin+52}" y2="{margin+50}" stroke="#2196F3" stroke-width="2.5"/>
  <text x="{margin+58}" y="{margin+54}" font-size="12">直线  y = {k:.0f}x + {m:.0f}</text>
'''

svg += '</svg>\n'

with open('/projects/sandbox/line_parabola.svg', 'w') as f:
    f.write(svg)

print("已生成 line_parabola.svg")
print(f"抛物线: y = x^2 - 2x - 3  (a={a:.0f}, b={b:.0f}, c={c:.0f})")
print(f"交点横坐标 x1={x1:.0f}, x2={x2:.0f}")
print(f"斜率 k = a(x1+x2)+b = {k:.0f}")
print(f"截距 m = c - a*x1*x2 = {m:.0f}")
print(f"直线: y = {k:.0f}x + {m:.0f}")
print(f"验证: A=({x1:.0f},{y1:.0f}), B=({x2:.0f},{y2:.0f})")
