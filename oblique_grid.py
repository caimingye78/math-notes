import math

# 斜坐标"网格"(斜格点), 基底夹角 70 度
omega = 70.0
e1 = (1.0, 0.0)
e2 = (math.cos(math.radians(omega)), math.sin(math.radians(omega)))

width, height = 700, 560
margin = 55
top = 70
x_min, x_max = -0.8, 5.2
y_min, y_max = -0.8, 4.0
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
s = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - s*(x_max-x_min))/2
oy = top + margin + (plot_h - s*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*s, oy + (y_max-y)*s

def lattice(m, n):
    return (m*e1[0] + n*e2[0], m*e1[1] + n*e2[1])

def arrow(x1, y1, x2, y2, col, w=2.4):
    a = math.atan2(y2-y1, x2-x1); L = 11
    p1 = (x2 - L*math.cos(a-0.4), y2 - L*math.sin(a-0.4))
    p2 = (x2 - L*math.cos(a+0.4), y2 - L*math.sin(a+0.4))
    return (f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"/>\n'
            f'  <polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>\n')

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    斜坐标网格: 线性运算照旧, 但长度/夹角公式要变
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    |v|&#178; = a&#178; + b&#178; + 2ab&#183;cos&#969;  (直角系 &#969;=90&#176;, 交叉项消失 -> a&#178;+b&#178;)
  </text>
'''

for n in range(0, 5):
    p_s = to_px(*lattice(0, n)); p_e = to_px(*lattice(5, n))
    svg += f'  <line x1="{p_s[0]:.1f}" y1="{p_s[1]:.1f}" x2="{p_e[0]:.1f}" y2="{p_e[1]:.1f}" stroke="#ddd" stroke-width="1"/>\n'
for m in range(0, 6):
    p_s = to_px(*lattice(m, 0)); p_e = to_px(*lattice(m, 4))
    svg += f'  <line x1="{p_s[0]:.1f}" y1="{p_s[1]:.1f}" x2="{p_e[0]:.1f}" y2="{p_e[1]:.1f}" stroke="#ddd" stroke-width="1"/>\n'

for m in range(0, 6):
    for n in range(0, 5):
        px, py = to_px(*lattice(m, n))
        svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="2" fill="#bbb"/>\n'

opx, opy = to_px(0,0)
e1p = to_px(*e1); e2p = to_px(*e2)
svg += arrow(opx, opy, e1p[0], e1p[1], "#1565C0", 2.6)
svg += f'  <text x="{e1p[0]-4:.1f}" y="{e1p[1]+18:.1f}" font-size="13" fill="#1565C0">e&#8321;</text>\n'
svg += arrow(opx, opy, e2p[0], e2p[1], "#2E7D32", 2.6)
svg += f'  <text x="{e2p[0]-18:.1f}" y="{e2p[1]-2:.1f}" font-size="13" fill="#2E7D32">e&#8322;</text>\n'

v = lattice(3, 2)
vp = to_px(*v)
svg += arrow(opx, opy, vp[0], vp[1], "#9C27B0", 2.6)
svg += f'  <circle cx="{vp[0]:.1f}" cy="{vp[1]:.1f}" r="5" fill="#9C27B0"/>\n'
svg += f'  <text x="{vp[0]+8:.1f}" y="{vp[1]-6:.1f}" font-size="13" fill="#7B1FA2">v = 3e&#8321; + 2e&#8322;</text>\n'
svg += f'  <circle cx="{opx:.1f}" cy="{opy:.1f}" r="3.5" fill="#000"/>\n'
svg += f'  <text x="{opx-16:.1f}" y="{opy+16:.1f}" font-size="12">O</text>\n'
svg += '</svg>\n'
with open('/projects/sandbox/oblique_grid.svg','w') as f:
    f.write(svg)
print("oblique_grid.svg done")
