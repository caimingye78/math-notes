import math

# z = 2(cos60 + i sin60) = 1 + (root3) i
r = 2.0
ang = 60.0
th = math.radians(ang)
a = r * math.cos(th)   # 实部 = 1
b = r * math.sin(th)   # 虚部 = root3 ~ 1.732

width, height = 620, 640
margin = 55
top = 64
x_min, x_max = -1.0, 3.0
y_min, y_max = -1.0, 3.0
plot_w = width - 2 * margin
plot_h = (height - top) - 2 * margin
s = min(plot_w / (x_max - x_min), plot_h / (y_max - y_min))
ox = margin + (plot_w - s * (x_max - x_min)) / 2
oy = top + margin + (plot_h - s * (y_max - y_min)) / 2

def to_px(x, y):
    return ox + (x - x_min) * s, oy + (y_max - y) * s

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    复数的极坐标形式: z = r(cos&#952; + i&#183;sin&#952;) = r&#183;e^(i&#952;)
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    例: z = 2(cos60&#176;+i&#183;sin60&#176;) = 1 + &#8730;3&#183;i
  </text>
'''

xa1 = to_px(x_min, 0); xa2 = to_px(x_max, 0)
ya1 = to_px(0, y_min); ya2 = to_px(0, y_max)
svg += f'  <line x1="{xa1[0]:.1f}" y1="{xa1[1]:.1f}" x2="{xa2[0]:.1f}" y2="{xa2[1]:.1f}" stroke="#000" stroke-width="1"/>\n'
svg += f'  <line x1="{ya1[0]:.1f}" y1="{ya1[1]:.1f}" x2="{ya2[0]:.1f}" y2="{ya2[1]:.1f}" stroke="#000" stroke-width="1"/>\n'
svg += f'  <text x="{xa2[0]-4:.1f}" y="{xa2[1]+16:.1f}" font-size="12" font-style="italic">实轴 (Re)</text>\n'
svg += f'  <text x="{ya2[0]+6:.1f}" y="{ya2[1]+6:.1f}" font-size="12" font-style="italic">虚轴 (Im)</text>\n'
for v in [1, 2, 3]:
    px, py = to_px(v, 0)
    svg += f'  <text x="{px:.1f}" y="{py+14:.1f}" text-anchor="middle" font-size="9">{v}</text>\n'
    px, py = to_px(0, v)
    svg += f'  <text x="{px-7:.1f}" y="{py+3:.1f}" text-anchor="end" font-size="9">{v}i</text>\n'

opx, opy = to_px(0, 0)
zpx, zpy = to_px(a, b)
svg += f'  <line x1="{opx:.1f}" y1="{opy:.1f}" x2="{zpx:.1f}" y2="{zpy:.1f}" stroke="#9C27B0" stroke-width="2.5"/>\n'
mid = ((opx + zpx) / 2, (opy + zpy) / 2)
svg += f'  <text x="{mid[0]-44:.1f}" y="{mid[1]-4:.1f}" font-size="12" fill="#7B1FA2">r = |z| = 2</text>\n'

R = 40
p0 = (opx + R, opy)
p1 = (opx + R * math.cos(th), opy - R * math.sin(th))
svg += f'  <path d="M {p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 0 0 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#E65100" stroke-width="1.5"/>\n'
lpx = opx + (R + 18) * math.cos(math.radians(ang / 2))
lpy = opy - (R + 18) * math.sin(math.radians(ang / 2))
svg += f'  <text x="{lpx-8:.1f}" y="{lpy+4:.1f}" font-size="12" fill="#E65100">&#952;=60&#176;</text>\n'

fa = to_px(a, 0); fb = to_px(0, b)
svg += f'  <line x1="{zpx:.1f}" y1="{zpy:.1f}" x2="{fa[0]:.1f}" y2="{fa[1]:.1f}" stroke="#1565C0" stroke-width="1.4" stroke-dasharray="4 3"/>\n'
svg += f'  <line x1="{zpx:.1f}" y1="{zpy:.1f}" x2="{fb[0]:.1f}" y2="{fb[1]:.1f}" stroke="#2E7D32" stroke-width="1.4" stroke-dasharray="4 3"/>\n'
svg += f'  <text x="{(opx+fa[0])/2-22:.1f}" y="{fa[1]+15:.1f}" font-size="11" fill="#1565C0">a=2cos60=1</text>\n'
svg += f'  <text x="{fb[0]+4:.1f}" y="{(opy+fb[1])/2:.1f}" font-size="11" fill="#2E7D32">b=2sin60=&#8730;3</text>\n'
svg += f'  <circle cx="{zpx:.1f}" cy="{zpy:.1f}" r="5" fill="#9C27B0"/>\n'
svg += f'  <text x="{zpx+8:.1f}" y="{zpy-4:.1f}" font-size="13" fill="#7B1FA2">z = 1 + &#8730;3 i</text>\n'
svg += '</svg>\n'

with open('/projects/sandbox/complex_polar.svg', 'w') as f:
    f.write(svg)
print("complex_polar.svg done: a=", round(a, 3), "b=", round(b, 3))
