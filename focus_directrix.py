import math

# 抛物线 x^2 = 4y  即 y = x^2/4 (a=1/4)
# 标准型 x^2 = 4py, 这里 p=1 -> 焦点(0,1), 准线 y=-1
a = 0.25
focus = (0.0, 1.0)
directrix_y = -1.0

# 取抛物线上一点 P 演示等距性质
xp = 3.0
yp = a * xp * xp   # = 2.25
P = (xp, yp)

width, height = 740, 560
margin = 60
plot_w = width - 2 * margin
plot_h = height - 2 * margin

x_min, x_max = -5.0, 5.0
y_min, y_max = -2.0, 6.0

def to_px(x, y):
    px = margin + (x - x_min) / (x_max - x_min) * plot_w
    py = margin + (y_max - y) / (y_max - y_min) * plot_h
    return px, py

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="17" font-family="serif">
    抛物线的焦点与准线 (x&#178; = 4y)：到焦点 = 到准线
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
    yv += 1
svg += '  </g>\n'

# 坐标轴
ax0x, ax0y = to_px(0, 0)
svg += f'  <line x1="{margin}" y1="{ax0y:.1f}" x2="{width-margin}" y2="{ax0y:.1f}" stroke="black" stroke-width="1"/>\n'
svg += f'  <line x1="{ax0x:.1f}" y1="{margin}" x2="{ax0x:.1f}" y2="{height-margin}" stroke="black" stroke-width="1"/>\n'

# x刻度
xv = math.ceil(x_min)
while xv <= x_max:
    if xv != 0:
        px, py = to_px(xv, 0)
        svg += f'  <text x="{px:.1f}" y="{py+15:.1f}" text-anchor="middle" font-size="10">{xv}</text>\n'
    xv += 1

# 准线（红色水平虚线）
_, dpy = to_px(0, directrix_y)
svg += f'  <line x1="{margin}" y1="{dpy:.1f}" x2="{width-margin}" y2="{dpy:.1f}" stroke="#E53935" stroke-width="2" stroke-dasharray="6 4"/>\n'
svg += f'  <text x="{width-margin-130}" y="{dpy-6:.1f}" font-size="12" fill="#E53935">准线 y = -1</text>\n'

# 抛物线
pts = []
n = 300
for i in range(n + 1):
    x = x_min + (x_max - x_min) * i / n
    y = a * x * x
    if y_min - 1 <= y <= y_max + 1:
        px, py = to_px(x, y)
        pts.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#9C27B0" stroke-width="2.5" points="{" ".join(pts)}"/>\n'

# 焦点
fpx, fpy = to_px(*focus)
svg += f'  <circle cx="{fpx:.1f}" cy="{fpy:.1f}" r="5" fill="#1565C0"/>\n'
svg += f'  <text x="{fpx+8:.1f}" y="{fpy-6:.1f}" font-size="12" fill="#1565C0">焦点 F(0,1)</text>\n'

# 点 P
ppx, ppy = to_px(*P)
svg += f'  <circle cx="{ppx:.1f}" cy="{ppy:.1f}" r="5" fill="#2E7D32"/>\n'
svg += f'  <text x="{ppx+8:.1f}" y="{ppy-6:.1f}" font-size="12" fill="#2E7D32">P({xp:.0f}, {yp:.2f})</text>\n'

# PF 线段（蓝）
svg += f'  <line x1="{ppx:.1f}" y1="{ppy:.1f}" x2="{fpx:.1f}" y2="{fpy:.1f}" stroke="#1565C0" stroke-width="2"/>\n'
# P 到准线垂线（红）
_, footy = to_px(xp, directrix_y)
svg += f'  <line x1="{ppx:.1f}" y1="{ppy:.1f}" x2="{ppx:.1f}" y2="{footy:.1f}" stroke="#E53935" stroke-width="2"/>\n'

# 距离标注
dist = math.hypot(xp - focus[0], yp - focus[1])
dist2 = yp - directrix_y
svg += f'''
  <rect x="{margin+8}" y="{margin+8}" width="250" height="56" fill="white" stroke="#ccc" rx="4"/>
  <text x="{margin+20}" y="{margin+30}" font-size="12" fill="#1565C0">PF = {dist:.2f}  (P到焦点)</text>
  <text x="{margin+20}" y="{margin+50}" font-size="12" fill="#E53935">P到准线 = {dist2:.2f}  (相等!)</text>
'''

svg += '</svg>\n'

with open('/projects/sandbox/focus_directrix.svg', 'w') as f:
    f.write(svg)

print("已生成 focus_directrix.svg")
print(f"抛物线 x^2=4y, 焦点 F(0,1), 准线 y=-1")
print(f"P=({xp:.0f},{yp:.2f}): PF={dist:.3f}, 到准线={dist2:.3f} (相等)")
