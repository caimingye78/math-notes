import math

# 斜坐标系: 基底 e1, e2 夹角 60 度 (不垂直)
# 向量 OP = 3*e1 + 2*e2
omega = 60.0
e1 = (1.0, 0.0)
e2 = (math.cos(math.radians(omega)), math.sin(math.radians(omega)))
cx_, cy_ = 3.0, 2.0  # 斜坐标
P = (cx_*e1[0] + cy_*e2[0], cx_*e1[1] + cy_*e2[1])
A = (cx_*e1[0], cx_*e1[1])   # 3*e1
B = (cy_*e2[0], cy_*e2[1])   # 2*e2

width, height = 700, 520
margin = 55
top = 64
x_min, x_max = -0.6, 5.4
y_min, y_max = -0.6, 3.2
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
s = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - s*(x_max-x_min))/2
oy = top + margin + (plot_h - s*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*s, oy + (y_max-y)*s

def arrow(x1, y1, x2, y2, col, w=2.3):
    a = math.atan2(y2-y1, x2-x1); L = 11
    p1 = (x2 - L*math.cos(a-0.4), y2 - L*math.sin(a-0.4))
    p2 = (x2 - L*math.cos(a+0.4), y2 - L*math.sin(a+0.4))
    return (f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"/>\n'
            f'  <polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>\n')

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    斜坐标系 = 沿不垂直基底分解向量 (平面向量基本定理)
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    基底 e&#8321;,e&#8322; 夹角60&#176;;  OP = 3e&#8321; + 2e&#8322;;  投影是"平行于另一轴", 不是垂直
  </text>
'''

opx, opy = to_px(0,0)
ax1 = to_px(5.2, 0)
ax2e = to_px(2.6*e2[0], 2.6*e2[1])
svg += f'  <line x1="{opx:.1f}" y1="{opy:.1f}" x2="{ax1[0]:.1f}" y2="{ax1[1]:.1f}" stroke="#888" stroke-width="1.2"/>\n'
svg += f'  <line x1="{opx:.1f}" y1="{opy:.1f}" x2="{ax2e[0]:.1f}" y2="{ax2e[1]:.1f}" stroke="#888" stroke-width="1.2"/>\n'

ap = to_px(*A); bp = to_px(*B); pp = to_px(*P)
svg += f'  <line x1="{pp[0]:.1f}" y1="{pp[1]:.1f}" x2="{ap[0]:.1f}" y2="{ap[1]:.1f}" stroke="#1565C0" stroke-width="1.2" stroke-dasharray="5 3"/>\n'
svg += f'  <line x1="{pp[0]:.1f}" y1="{pp[1]:.1f}" x2="{bp[0]:.1f}" y2="{bp[1]:.1f}" stroke="#2E7D32" stroke-width="1.2" stroke-dasharray="5 3"/>\n'

e1p = to_px(*e1); e2p = to_px(*e2)
svg += arrow(opx, opy, e1p[0], e1p[1], "#1565C0", 2.6)
svg += f'  <text x="{e1p[0]:.1f}" y="{e1p[1]+18:.1f}" font-size="13" fill="#1565C0">e&#8321;</text>\n'
svg += arrow(opx, opy, e2p[0], e2p[1], "#2E7D32", 2.6)
svg += f'  <text x="{e2p[0]-18:.1f}" y="{e2p[1]-4:.1f}" font-size="13" fill="#2E7D32">e&#8322;</text>\n'

svg += f'  <circle cx="{ap[0]:.1f}" cy="{ap[1]:.1f}" r="4" fill="#1565C0"/>\n'
svg += f'  <text x="{ap[0]-14:.1f}" y="{ap[1]+18:.1f}" font-size="12" fill="#1565C0">3e&#8321;</text>\n'
svg += f'  <circle cx="{bp[0]:.1f}" cy="{bp[1]:.1f}" r="4" fill="#2E7D32"/>\n'
svg += f'  <text x="{bp[0]-30:.1f}" y="{bp[1]:.1f}" font-size="12" fill="#2E7D32">2e&#8322;</text>\n'

svg += arrow(opx, opy, pp[0], pp[1], "#9C27B0", 2.6)
svg += f'  <circle cx="{pp[0]:.1f}" cy="{pp[1]:.1f}" r="5" fill="#9C27B0"/>\n'
svg += f'  <text x="{pp[0]+8:.1f}" y="{pp[1]-6:.1f}" font-size="13" fill="#7B1FA2">P (斜坐标 3, 2)</text>\n'

R = 34
p0 = (opx+R, opy)
p1 = (opx+R*math.cos(math.radians(omega)), opy-R*math.sin(math.radians(omega)))
svg += f'  <path d="M {p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 0 0 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#E65100" stroke-width="1.4"/>\n'
svg += f'  <text x="{opx+R+4:.1f}" y="{opy-14:.1f}" font-size="11" fill="#E65100">&#969;=60&#176;</text>\n'
svg += f'  <circle cx="{opx:.1f}" cy="{opy:.1f}" r="3.5" fill="#000"/>\n'
svg += f'  <text x="{opx-16:.1f}" y="{opy+16:.1f}" font-size="12">O</text>\n'
svg += '</svg>\n'
with open('/projects/sandbox/oblique_basis.svg','w') as f:
    f.write(svg)
print("oblique_basis.svg done, P=", (round(P[0],3), round(P[1],3)))
