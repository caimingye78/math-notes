import math

# 差函数 g(x) = (抛物线) - (直线) = x^2 - x - 6
# 即 a=1, B=-1, C=-6，根就是交点横坐标 x1=-2, x2=3
a, B, C = 1.0, -1.0, -6.0
x1, x2 = -2.0, 3.0
axis = (x1 + x2) / 2.0   # 对称轴 = 两根平均 = -B/(2a)

width, height = 760, 560
margin = 60
plot_w = width - 2 * margin
plot_h = height - 2 * margin

x_min, x_max = -4.0, 5.0
y_min, y_max = -8.0, 8.0

def to_px(x, y):
    px = margin + (x - x_min) / (x_max - x_min) * plot_w
    py = margin + (y_max - y) / (y_max - y_min) * plot_h
    return px, py

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="17" font-family="serif">
    韦达定理：g(x)=x&#178;-x-6 的两根之和与积
  </text>
'''

# 网格
svg += '  <g stroke="#ececec" stroke-width="0.5">\n'
xv = math.ceil(x_min)
while xv <= x_max:
    px, _ = to_px(xv, 0)
    svg += f'    <line x1="{px:.1f}" y1="{margin}" x2="{px:.1f}" y2="{height-margin}"/>\n'
    xv += 1
yv = math.ceil(y_min)
while yv <= y_max:
    _, py = to_px(0, yv)
    svg += f'    <line x1="{margin}" y1="{py:.1f}" x2="{width-margin}" y2="{py:.1f}"/>\n'
    yv += 2
svg += '  </g>\n'

# 坐标轴
ax0x, ax0y = to_px(0, 0)
svg += f'  <line x1="{margin}" y1="{ax0y:.1f}" x2="{width-margin}" y2="{ax0y:.1f}" stroke="black" stroke-width="1"/>\n'
svg += f'  <line x1="{ax0x:.1f}" y1="{margin}" x2="{ax0x:.1f}" y2="{height-margin}" stroke="black" stroke-width="1"/>\n'
svg += f'  <text x="{width-margin+8}" y="{ax0y+4:.1f}" font-size="13" font-style="italic">x</text>\n'
svg += f'  <text x="{ax0x+6:.1f}" y="{margin-4}" font-size="13" font-style="italic">y</text>\n'

# x刻度
xv = math.ceil(x_min)
while xv <= x_max:
    if xv != 0:
        px, py = to_px(xv, 0)
        svg += f'  <text x="{px:.1f}" y="{py+15:.1f}" text-anchor="middle" font-size="10">{xv}</text>\n'
    xv += 1

# 对称轴（竖虚线）
axpx, _ = to_px(axis, 0)
svg += f'  <line x1="{axpx:.1f}" y1="{margin}" x2="{axpx:.1f}" y2="{height-margin}" stroke="#FF9800" stroke-width="1.5" stroke-dasharray="5 4"/>\n'
svg += f'  <text x="{axpx+5:.1f}" y="{margin+14:.1f}" font-size="11" fill="#FF9800">对称轴 x={axis:.1f}</text>\n'

# 抛物线 g(x)
pts = []
n = 300
for i in range(n + 1):
    x = x_min + (x_max - x_min) * i / n
    y = a * x * x + B * x + C
    if y_min - 1 <= y <= y_max + 1:
        px, py = to_px(x, y)
        pts.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#9C27B0" stroke-width="2.5" points="{" ".join(pts)}"/>\n'

# 两个根（与x轴交点）
for (xi, name) in [(x1, "x\u2081=-2"), (x2, "x\u2082=3")]:
    cx, cy = to_px(xi, 0)
    svg += f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="#F44336"/>\n'
    svg += f'  <text x="{cx-4:.1f}" y="{cy-10:.1f}" font-size="12" fill="#F44336">{name}</text>\n'

# 顶点
vy = a * axis * axis + B * axis + C
vpx, vpy = to_px(axis, vy)
svg += f'  <circle cx="{vpx:.1f}" cy="{vpy:.1f}" r="4" fill="#FF9800"/>\n'

# 文字说明框
bx, by = margin + 8, margin + 8
svg += f'''
  <rect x="{bx}" y="{by}" width="250" height="74" fill="white" stroke="#ccc" rx="4"/>
  <text x="{bx+12}" y="{by+22}" font-size="12">两根之和  x&#8321;+x&#8322; = -B/a = 1</text>
  <text x="{bx+12}" y="{by+42}" font-size="12">两根之积  x&#8321;&#183;x&#8322; = C/a = -6</text>
  <text x="{bx+12}" y="{by+62}" font-size="12">对称轴在两根正中间 (1/2)</text>
'''

svg += '</svg>\n'

with open('/projects/sandbox/vieta.svg', 'w') as f:
    f.write(svg)

print("已生成 vieta.svg")
print(f"g(x) = x^2 - x - 6, 两根 x1={x1:.0f}, x2={x2:.0f}")
print(f"两根之和 = {x1+x2:.0f} = -B/a = {-B/a:.0f}")
print(f"两根之积 = {x1*x2:.0f} = C/a = {C/a:.0f}")
print(f"对称轴 x = {axis:.1f}")
