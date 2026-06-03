import math

# 同一条抛物线 y = -x^2 + 2x + 3
def f(x):
    return -x*x + 2*x + 3

A = (-1.0, 0.0)
B = (3.0, 0.0)
C = (0.0, 3.0)
axis_x = 1.0          # 对称轴 x = -b/(2a) = 1
Q = (1.0, 1.0)        # 设 Q(1,m)，由 QB=QC 解得 m=1

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
    设点法(二)：对称轴上设 Q(1, m)，求使 &#9651;QBC 为等腰(QB=QC)
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

ax0x, ax0y = to_px(0, 0)
svg += f'  <line x1="{margin}" y1="{ax0y:.1f}" x2="{width-margin}" y2="{ax0y:.1f}" stroke="black" stroke-width="1"/>\n'
svg += f'  <line x1="{ax0x:.1f}" y1="{margin}" x2="{ax0x:.1f}" y2="{height-margin}" stroke="black" stroke-width="1"/>\n'

xv = math.ceil(x_min)
while xv <= x_max:
    if xv != 0:
        px, py = to_px(xv, 0)
        svg += f'  <text x="{px:.1f}" y="{py+15:.1f}" text-anchor="middle" font-size="10">{xv}</text>\n'
    xv += 1

# 对称轴
axpx, _ = to_px(axis_x, 0)
svg += f'  <line x1="{axpx:.1f}" y1="{margin}" x2="{axpx:.1f}" y2="{height-margin}" stroke="#FF9800" stroke-width="1.5" stroke-dasharray="5 4"/>\n'
svg += f'  <text x="{axpx+5:.1f}" y="{margin+14:.1f}" font-size="11" fill="#FF9800">对称轴 x=1</text>\n'

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

# 三角形 QBC
qpx, qpy = to_px(*Q)
bpx, bpy = to_px(*B)
cpx, cpy = to_px(*C)
svg += f'  <polygon points="{qpx:.1f},{qpy:.1f} {bpx:.1f},{bpy:.1f} {cpx:.1f},{cpy:.1f}" fill="#4CAF50" fill-opacity="0.15" stroke="#4CAF50" stroke-width="1.5"/>\n'

# 标 QB, QC 等长
midqb = ((qpx+bpx)/2, (qpy+bpy)/2)
midqc = ((qpx+cpx)/2, (qpy+cpy)/2)
svg += f'  <text x="{midqb[0]+4:.1f}" y="{midqb[1]:.1f}" font-size="11" fill="#2E7D32">QB=&#8730;5</text>\n'
svg += f'  <text x="{midqc[0]-46:.1f}" y="{midqc[1]:.1f}" font-size="11" fill="#2E7D32">QC=&#8730;5</text>\n'

for (pt, name, col, dx, dy) in [
    (B, "B(3,0)", "#555", 6, 16),
    (C, "C(0,3)", "#555", -52, 0),
    (Q, "Q(1,1)", "#2E7D32", 8, -6),
]:
    cx, cy = to_px(*pt)
    svg += f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.5" fill="{col}"/>\n'
    svg += f'  <text x="{cx+dx:.1f}" y="{cy+dy:.1f}" font-size="11" fill="{col}">{name}</text>\n'

svg += f'''
  <rect x="{margin+8}" y="{margin+8}" width="262" height="74" fill="white" stroke="#ccc" rx="4"/>
  <text x="{margin+18}" y="{margin+28}" font-size="11">设 Q(1, m)。 QB&#178;=(1-3)&#178;+m&#178;=4+m&#178;</text>
  <text x="{margin+18}" y="{margin+47}" font-size="11">QC&#178;=(1-0)&#178;+(m-3)&#178;=m&#178;-6m+10</text>
  <text x="{margin+18}" y="{margin+66}" font-size="11">令两者相等 -> m=1，故 Q(1,1)</text>
'''
svg += '</svg>\n'

with open('/projects/sandbox/param_isosceles.svg', 'w') as fp:
    fp.write(svg)
print("已生成 param_isosceles.svg, Q(1,1), QB=QC=sqrt5")
