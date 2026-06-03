import math

# 圆周上的点 P, 极坐标基: e_r(径向, 沿OP向外), e_theta(切向, 逆时针)
R = 2.5
phi = 55.0
ph = math.radians(phi)
P = (R*math.cos(ph), R*math.sin(ph))
er = (math.cos(ph), math.sin(ph))          # 径向单位向量
et = (-math.sin(ph), math.cos(ph))         # 切向单位向量(逆时针)

width, height = 660, 660
margin = 55
top = 66
x_min, x_max = -3.4, 3.4
y_min, y_max = -3.4, 3.4
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
s = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - s*(x_max-x_min))/2
oy = top + margin + (plot_h - s*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*s, oy + (y_max-y)*s

def arrow(x1, y1, x2, y2, col, w=2.2):
    a = math.atan2(y2-y1, x2-x1); L = 10
    p1 = (x2 - L*math.cos(a-0.4), y2 - L*math.sin(a-0.4))
    p2 = (x2 - L*math.cos(a+0.4), y2 - L*math.sin(a+0.4))
    return (f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"/>\n'
            f'  <polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>\n')

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    极坐标基底向量: 径向 e_r 与 切向 e_&#952; (圆周运动)
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    位置沿 e_r, 速度沿 e_&#952;, 向心加速度沿 -e_r
  </text>
'''

xa1 = to_px(x_min, 0); xa2 = to_px(x_max, 0)
ya1 = to_px(0, y_min); ya2 = to_px(0, y_max)
svg += f'  <line x1="{xa1[0]:.1f}" y1="{xa1[1]:.1f}" x2="{xa2[0]:.1f}" y2="{xa2[1]:.1f}" stroke="#bbb" stroke-width="1"/>\n'
svg += f'  <line x1="{ya1[0]:.1f}" y1="{ya1[1]:.1f}" x2="{ya2[0]:.1f}" y2="{ya2[1]:.1f}" stroke="#bbb" stroke-width="1"/>\n'

cp = []
for i in range(361):
    a = math.radians(i)
    px, py = to_px(R*math.cos(a), R*math.sin(a))
    cp.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#9C27B0" stroke-width="2" points="{" ".join(cp)}"/>\n'

opx, opy = to_px(0,0)
ppx, ppy = to_px(*P)
svg += arrow(opx, opy, ppx, ppy, "#7B1FA2", 2.2)
mid = ((opx+ppx)/2,(opy+ppy)/2)
svg += f'  <text x="{mid[0]-34:.1f}" y="{mid[1]-6:.1f}" font-size="12" fill="#7B1FA2">位置向量 r</text>\n'
svg += f'  <circle cx="{opx:.1f}" cy="{opy:.1f}" r="3.5" fill="#000"/>\n'
svg += f'  <text x="{opx-16:.1f}" y="{opy+16:.1f}" font-size="12">O</text>\n'

L = 1.05
er_end = to_px(P[0]+L*er[0], P[1]+L*er[1])
et_end = to_px(P[0]+L*et[0], P[1]+L*et[1])
svg += arrow(ppx, ppy, er_end[0], er_end[1], "#1565C0", 2.4)
svg += f'  <text x="{er_end[0]+4:.1f}" y="{er_end[1]+2:.1f}" font-size="13" fill="#1565C0">e_r</text>\n'
svg += arrow(ppx, ppy, et_end[0], et_end[1], "#2E7D32", 2.4)
svg += f'  <text x="{et_end[0]-30:.1f}" y="{et_end[1]-4:.1f}" font-size="13" fill="#2E7D32">e_&#952;</text>\n'

Lv = 1.7
v_end = to_px(P[0]+Lv*et[0], P[1]+Lv*et[1])
svg += arrow(ppx, ppy, v_end[0], v_end[1], "#2E7D32", 1.4)
svg += f'  <text x="{v_end[0]-44:.1f}" y="{v_end[1]+14:.1f}" font-size="11" fill="#2E7D32">速度 v</text>\n'
La = 1.2
a_end = to_px(P[0]-La*er[0], P[1]-La*er[1])
svg += arrow(ppx, ppy, a_end[0], a_end[1], "#E53935", 1.4)
svg += f'  <text x="{a_end[0]+4:.1f}" y="{a_end[1]:.1f}" font-size="11" fill="#E53935">向心加速度 a</text>\n'

svg += f'  <circle cx="{ppx:.1f}" cy="{ppy:.1f}" r="5" fill="#9C27B0"/>\n'
svg += f'  <text x="{ppx+8:.1f}" y="{ppy-8:.1f}" font-size="13" fill="#7B1FA2">P</text>\n'
svg += '</svg>\n'
with open('/projects/sandbox/polar_unit_vectors.svg', 'w') as f:
    f.write(svg)
print("polar_unit_vectors.svg done")
