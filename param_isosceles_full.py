import math

# 抛物线 y = -x^2 + 2x + 3, B(3,0), C(0,3), Q 在对称轴 x=1 上, 设 Q(1,m)
def f(x):
    return -x*x + 2*x + 3

B = (3.0, 0.0)
C = (0.0, 3.0)
axis_x = 1.0
BC = math.sqrt((3-0)**2 + (0-3)**2)   # = 3*sqrt2
R = BC

# 三种情况解出的 m
m_eq = 1.0                                    # QB = QC
m_b1, m_b2 = math.sqrt(14), -math.sqrt(14)    # QB = BC
m_c1, m_c2 = 3 + math.sqrt(17), 3 - math.sqrt(17)  # QC = BC

Qs = [
    (1.0, m_eq, "#1565C0"),
    (1.0, m_b1, "#C62828"),
    (1.0, m_b2, "#C62828"),
    (1.0, m_c1, "#2E7D32"),
    (1.0, m_c2, "#2E7D32"),
]

width, height = 680, 700
margin = 50
x_min, x_max = -5.0, 8.0
y_min, y_max = -5.0, 8.0
plot_w = width - 2*margin
plot_h = (height - 70) - 2*margin
top = 60

def to_px(x, y):
    px = margin + (x - x_min)/(x_max - x_min)*plot_w
    py = top + margin + (y_max - y)/(y_max - y_min)*plot_h
    return px, py

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="16" font-family="serif">
    完整压轴题：对称轴上 Q(1,m) 使 &#9651;QBC 为等腰，共 5 个点
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    BC=3&#8730;2；红圈=以B为心半径BC，绿圈=以C为心半径BC，蓝虚线=BC中垂线 y=x
  </text>
'''

# 网格
svg += '  <g stroke="#eee" stroke-width="0.5">\n'
xv = math.ceil(x_min)
while xv <= x_max:
    px, _ = to_px(xv, 0)
    svg += f'    <line x1="{px:.1f}" y1="{to_px(0,y_max)[1]:.1f}" x2="{px:.1f}" y2="{to_px(0,y_min)[1]:.1f}"/>\n'
    xv += 1
yv = math.ceil(y_min)
while yv <= y_max:
    _, py = to_px(0, yv)
    svg += f'    <line x1="{to_px(x_min,0)[0]:.1f}" y1="{py:.1f}" x2="{to_px(x_max,0)[0]:.1f}" y2="{py:.1f}"/>\n'
    yv += 1
svg += '  </g>\n'

# 坐标轴
ax0x, ax0y = to_px(0, 0)
svg += f'  <line x1="{to_px(x_min,0)[0]:.1f}" y1="{ax0y:.1f}" x2="{to_px(x_max,0)[0]:.1f}" y2="{ax0y:.1f}" stroke="black" stroke-width="1"/>\n'
svg += f'  <line x1="{ax0x:.1f}" y1="{to_px(0,y_max)[1]:.1f}" x2="{ax0x:.1f}" y2="{to_px(0,y_min)[1]:.1f}" stroke="black" stroke-width="1"/>\n'
for xv in range(int(x_min)+1, int(x_max)+1):
    if xv != 0:
        px, py = to_px(xv, 0)
        svg += f'  <text x="{px:.1f}" y="{py+13:.1f}" text-anchor="middle" font-size="9">{xv}</text>\n'
for yv in range(int(y_min)+1, int(y_max)+1):
    if yv != 0:
        px, py = to_px(0, yv)
        svg += f'  <text x="{px-7:.1f}" y="{py+3:.1f}" text-anchor="end" font-size="9">{yv}</text>\n'

# 对称轴
axpx, _ = to_px(axis_x, 0)
svg += f'  <line x1="{axpx:.1f}" y1="{to_px(0,y_max)[1]:.1f}" x2="{axpx:.1f}" y2="{to_px(0,y_min)[1]:.1f}" stroke="#FF9800" stroke-width="1.5" stroke-dasharray="5 4"/>\n'
svg += f'  <text x="{axpx+4:.1f}" y="{to_px(0,y_max)[1]+14:.1f}" font-size="10" fill="#FF9800">x=1</text>\n'

# 抛物线
pts = []
for i in range(401):
    x = x_min + (x_max - x_min)*i/400
    y = f(x)
    if y_min-2 <= y <= y_max+2:
        px, py = to_px(x, y)
        pts.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#9C27B0" stroke-width="2.5" points="{" ".join(pts)}"/>\n'

def circle_pts(cx, cy, R):
    p = []
    for i in range(361):
        ang = 2*math.pi*i/360
        x = cx + R*math.cos(ang)
        y = cy + R*math.sin(ang)
        px, py = to_px(x, y)
        p.append(f"{px:.1f},{py:.1f}")
    return " ".join(p)

svg += f'  <polyline fill="none" stroke="#C62828" stroke-width="1.2" stroke-dasharray="3 3" points="{circle_pts(*B, R)}"/>\n'
svg += f'  <polyline fill="none" stroke="#2E7D32" stroke-width="1.2" stroke-dasharray="3 3" points="{circle_pts(*C, R)}"/>\n'

# BC 中垂线 y = x
l1 = to_px(-5, -5); l2 = to_px(8, 8)
svg += f'  <line x1="{l1[0]:.1f}" y1="{l1[1]:.1f}" x2="{l2[0]:.1f}" y2="{l2[1]:.1f}" stroke="#1565C0" stroke-width="1.2" stroke-dasharray="6 4"/>\n'

# BC 线段与端点
bpx, bpy = to_px(*B)
cpx, cpy = to_px(*C)
svg += f'  <line x1="{bpx:.1f}" y1="{bpy:.1f}" x2="{cpx:.1f}" y2="{cpy:.1f}" stroke="#000" stroke-width="2"/>\n'
svg += f'  <circle cx="{bpx:.1f}" cy="{bpy:.1f}" r="4.5" fill="#000"/>\n'
svg += f'  <text x="{bpx+6:.1f}" y="{bpy+16:.1f}" font-size="12">B(3,0)</text>\n'
svg += f'  <circle cx="{cpx:.1f}" cy="{cpy:.1f}" r="4.5" fill="#000"/>\n'
svg += f'  <text x="{cpx-50:.1f}" y="{cpy:.1f}" font-size="12">C(0,3)</text>\n'

labels = [
    "Q1(1, 1)",
    "Q2(1, \u221a14\u22483.74)",
    "Q3(1, -\u221a14\u2248-3.74)",
    "Q4(1, 3+\u221a17\u22487.12)",
    "Q5(1, 3-\u221a17\u2248-1.12)",
]
for (x, m, col), lab in zip(Qs, labels):
    cx, cy = to_px(1.0, m)
    svg += f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="{col}"/>\n'
    svg += f'  <text x="{cx+8:.1f}" y="{cy+4:.1f}" font-size="10.5" fill="{col}">{lab}</text>\n'

svg += '</svg>\n'
with open('/projects/sandbox/param_isosceles.svg', 'w') as fp:
    fp.write(svg)

print("BC =", round(BC,4), "= 3*sqrt2")
print("QB=QC -> m=1")
print("QB=BC -> m=+/-sqrt14 =", round(m_b1,3), round(m_b2,3))
print("QC=BC -> m=3+/-sqrt17 =", round(m_c1,3), round(m_c2,3))
print("共 5 个点, 图已更新 param_isosceles.svg")
