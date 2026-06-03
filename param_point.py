import math

# 抛物线 y = -x^2 + 2x + 3
# 与 x 轴交于 A(-1,0), B(3,0)；与 y 轴交于 C(0,3)
def f(x):
    return -x*x + 2*x + 3

A = (-1.0, 0.0)
B = (3.0, 0.0)
C = (0.0, 3.0)

# 直线 BC: y = -x + 3
def line_bc(x):
    return -x + 3.0

# 设点 P(t, f(t))，铅垂高 h(t)=f(t)-line_bc(t) = -t^2+3t，t=1.5 取最大
t = 1.5
P = (t, f(t))
Pfoot = (t, line_bc(t))   # P 正下方落在直线 BC 上的点

width, height = 740, 580
margin = 60
plot_w = width - 2 * margin
plot_h = height - 2 * margin

x_min, x_max = -2.0, 4.0
y_min, y_max = -1.0, 5.0

def to_px(x, y):
    px = margin + (x - x_min) / (x_max - x_min) * plot_w
    py = margin + (y_max - y) / (y_max - y_min) * plot_h
    return px, py

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="16" font-family="serif">
    设点法：P(t, -t&#178;+2t+3)，铅垂高求 &#9651;PBC 最大面积
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

xv = math.ceil(x_min)
while xv <= x_max:
    if xv != 0:
        px, py = to_px(xv, 0)
        svg += f'  <text x="{px:.1f}" y="{py+15:.1f}" text-anchor="middle" font-size="10">{xv}</text>\n'
    xv += 1

# 抛物线
pts = []
n = 300
for i in range(n + 1):
    x = x_min + (x_max - x_min) * i / n
    y = f(x)
    if y_min - 1 <= y <= y_max + 1:
        px, py = to_px(x, y)
        pts.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#9C27B0" stroke-width="2.5" points="{" ".join(pts)}"/>\n'

# 三角形 PBC 填充
bpx, bpy = to_px(*B)
cpx, cpy = to_px(*C)
ppx, ppy = to_px(*P)
svg += f'  <polygon points="{ppx:.1f},{ppy:.1f} {bpx:.1f},{bpy:.1f} {cpx:.1f},{cpy:.1f}" fill="#2196F3" fill-opacity="0.18" stroke="#2196F3" stroke-width="1.5"/>\n'

# 直线 BC（延伸一点）
lx1, ly1 = to_px(-0.5, line_bc(-0.5))
lx2, ly2 = to_px(3.5, line_bc(3.5))
svg += f'  <line x1="{lx1:.1f}" y1="{ly1:.1f}" x2="{lx2:.1f}" y2="{ly2:.1f}" stroke="#2196F3" stroke-width="2"/>\n'

# 铅垂高 P->Pfoot（橙色）
fpx, fpy = to_px(*Pfoot)
svg += f'  <line x1="{ppx:.1f}" y1="{ppy:.1f}" x2="{fpx:.1f}" y2="{fpy:.1f}" stroke="#FF9800" stroke-width="2.5" stroke-dasharray="5 3"/>\n'
svg += f'  <text x="{ppx+6:.1f}" y="{(ppy+fpy)/2:.1f}" font-size="11" fill="#E65100">铅垂高 h=-t&#178;+3t</text>\n'

# 关键点
for (pt, name, col, dx, dy) in [
    (A, "A(-1,0)", "#555", -36, -8),
    (B, "B(3,0)", "#555", 6, 16),
    (C, "C(0,3)", "#555", -54, 0),
    (P, "P(1.5, 3.75)", "#2E7D32", 8, -6),
]:
    cx, cy = to_px(*pt)
    svg += f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.5" fill="{col}"/>\n'
    svg += f'  <text x="{cx+dx:.1f}" y="{cy+dy:.1f}" font-size="11" fill="{col}">{name}</text>\n'

# 说明框
svg += f'''
  <rect x="{margin+8}" y="{margin+8}" width="252" height="74" fill="white" stroke="#ccc" rx="4"/>
  <text x="{margin+18}" y="{margin+28}" font-size="11">设 P(t, -t&#178;+2t+3)，BC: y=-x+3</text>
  <text x="{margin+18}" y="{margin+47}" font-size="11">铅垂高 h = (-t&#178;+2t+3)-(-t+3) = -t&#178;+3t</text>
  <text x="{margin+18}" y="{margin+66}" font-size="11">面积 = (1/2)&#183;3&#183;h，t=1.5 时最大 = 27/8</text>
'''

svg += '</svg>\n'

with open('/projects/sandbox/param_point.svg', 'w') as fp:
    fp.write(svg)

print("已生成 param_point.svg")
print("抛物线 y=-x^2+2x+3, A(-1,0) B(3,0) C(0,3)")
print("设 P(t, -t^2+2t+3), 铅垂高 h=-t^2+3t")
print("t=1.5 时 h 最大 = 2.25, 三角形面积 = 0.5*3*2.25 =", 0.5*3*2.25)
