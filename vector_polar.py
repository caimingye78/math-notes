import math

# 力 F = 10 N, 与 x 轴成 37 度。分解: Fx=10cos37=8, Fy=10sin37=6
F = 10.0
ang = 37.0
th = math.radians(ang)
Fx = round(F * 0.8, 3)   # 10cos37 ~ 8
Fy = round(F * 0.6, 3)   # 10sin37 ~ 6

width, height = 680, 600
margin = 55
top = 64
x_min, x_max = -1.0, 10.0
y_min, y_max = -1.0, 8.0
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
s = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - s*(x_max-x_min))/2
oy = top + margin + (plot_h - s*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*s, oy + (y_max-y)*s

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    向量(力)的极坐标形式: 大小 |F| + 方向 &#952; , 分解成分量
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    F=10N, &#952;=37&#176;  &#8594;  Fx=10cos37&#176;=8,  Fy=10sin37&#176;=6
  </text>
'''

xa1 = to_px(x_min, 0); xa2 = to_px(x_max, 0)
ya1 = to_px(0, y_min); ya2 = to_px(0, y_max)
svg += f'  <line x1="{xa1[0]:.1f}" y1="{xa1[1]:.1f}" x2="{xa2[0]:.1f}" y2="{xa2[1]:.1f}" stroke="#000" stroke-width="1"/>\n'
svg += f'  <line x1="{ya1[0]:.1f}" y1="{ya1[1]:.1f}" x2="{ya2[0]:.1f}" y2="{ya2[1]:.1f}" stroke="#000" stroke-width="1"/>\n'
svg += f'  <text x="{xa2[0]-4:.1f}" y="{xa2[1]+16:.1f}" font-size="11" font-style="italic">x</text>\n'
svg += f'  <text x="{ya2[0]+6:.1f}" y="{ya2[1]+4:.1f}" font-size="11" font-style="italic">y</text>\n'

opx, opy = to_px(0, 0)
fp = to_px(Fx, Fy)
def arrow(x1, y1, x2, y2, col, w=2.4):
    ang2 = math.atan2(y2-y1, x2-x1)
    L = 11
    p1 = (x2 - L*math.cos(ang2-0.4), y2 - L*math.sin(ang2-0.4))
    p2 = (x2 - L*math.cos(ang2+0.4), y2 - L*math.sin(ang2+0.4))
    out = f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"/>\n'
    out += f'  <polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>\n'
    return out

svg += arrow(opx, opy, fp[0], fp[1], "#9C27B0", 2.6)
mid = ((opx+fp[0])/2, (opy+fp[1])/2)
svg += f'  <text x="{mid[0]-44:.1f}" y="{mid[1]-6:.1f}" font-size="13" fill="#7B1FA2">F = 10</text>\n'

fax = to_px(Fx, 0); fay = to_px(0, Fy)
svg += arrow(opx, opy, fax[0], fax[1], "#1565C0", 2.2)
svg += arrow(opx, opy, fay[0], fay[1], "#2E7D32", 2.2)
svg += f'  <line x1="{fp[0]:.1f}" y1="{fp[1]:.1f}" x2="{fax[0]:.1f}" y2="{fax[1]:.1f}" stroke="#999" stroke-width="1" stroke-dasharray="4 3"/>\n'
svg += f'  <line x1="{fp[0]:.1f}" y1="{fp[1]:.1f}" x2="{fay[0]:.1f}" y2="{fay[1]:.1f}" stroke="#999" stroke-width="1" stroke-dasharray="4 3"/>\n'
svg += f'  <text x="{(opx+fax[0])/2-14:.1f}" y="{fax[1]+16:.1f}" font-size="12" fill="#1565C0">Fx = 8</text>\n'
svg += f'  <text x="{fay[0]-44:.1f}" y="{(opy+fay[1])/2:.1f}" font-size="12" fill="#2E7D32">Fy = 6</text>\n'

R = 40
p0 = (opx+R, opy)
p1 = (opx+R*math.cos(th), opy-R*math.sin(th))
svg += f'  <path d="M {p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 0 0 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#E65100" stroke-width="1.5"/>\n'
svg += f'  <text x="{opx+R+6:.1f}" y="{opy-12:.1f}" font-size="12" fill="#E65100">&#952;=37&#176;</text>\n'
svg += f'  <rect x="{fax[0]-12:.1f}" y="{fax[1]-12:.1f}" width="12" height="12" fill="none" stroke="#999" stroke-width="1"/>\n'
svg += f'  <circle cx="{fp[0]:.1f}" cy="{fp[1]:.1f}" r="4.5" fill="#9C27B0"/>\n'
svg += '</svg>\n'
with open('/projects/sandbox/vector_polar.svg', 'w') as f:
    f.write(svg)
print("vector_polar.svg done: Fx=", Fx, "Fy=", Fy)
