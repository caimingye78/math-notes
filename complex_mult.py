import math

# z1 = root3 + i  = 2(cos30 + i sin30)      模2, 幅角30
# z2 = 1 + i      = root2(cos45 + i sin45)   模root2, 幅角45
# z1*z2 = 模 2*root2, 幅角 75
z1 = (math.sqrt(3), 1.0)
z2 = (1.0, 1.0)
prod = (z1[0]*z2[0] - z1[1]*z2[1], z1[0]*z2[1] + z1[1]*z2[0])  # 复数乘法

def poldeg(z):
    return math.hypot(*z), math.degrees(math.atan2(z[1], z[0]))

width, height = 660, 660
margin = 55
top = 70
x_min, x_max = -1.0, 3.2
y_min, y_max = -0.6, 3.4
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
    复数相乘 = 模相乘, 幅角相加 (= 旋转 + 伸缩)
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    z&#8321;=2&#8736;30&#176;,  z&#8322;=&#8730;2&#8736;45&#176;  &#8594;  z&#8321;z&#8322;=2&#8730;2&#8736;75&#176;
  </text>
'''

xa1 = to_px(x_min, 0); xa2 = to_px(x_max, 0)
ya1 = to_px(0, y_min); ya2 = to_px(0, y_max)
svg += f'  <line x1="{xa1[0]:.1f}" y1="{xa1[1]:.1f}" x2="{xa2[0]:.1f}" y2="{xa2[1]:.1f}" stroke="#000" stroke-width="1"/>\n'
svg += f'  <line x1="{ya1[0]:.1f}" y1="{ya1[1]:.1f}" x2="{ya2[0]:.1f}" y2="{ya2[1]:.1f}" stroke="#000" stroke-width="1"/>\n'
svg += f'  <text x="{xa2[0]-4:.1f}" y="{xa2[1]+16:.1f}" font-size="11" font-style="italic">Re</text>\n'
svg += f'  <text x="{ya2[0]+6:.1f}" y="{ya2[1]+6:.1f}" font-size="11" font-style="italic">Im</text>\n'
for v in [1, 2, 3]:
    px, py = to_px(v, 0)
    svg += f'  <text x="{px:.1f}" y="{py+14:.1f}" text-anchor="middle" font-size="9">{v}</text>\n'
for v in [1, 2, 3]:
    px, py = to_px(0, v)
    svg += f'  <text x="{px-7:.1f}" y="{py+3:.1f}" text-anchor="end" font-size="9">{v}i</text>\n'

opx, opy = to_px(0, 0)
def arrow(z, col, lab, lab_dx=8, lab_dy=-4):
    zp = to_px(*z)
    out = f'  <line x1="{opx:.1f}" y1="{opy:.1f}" x2="{zp[0]:.1f}" y2="{zp[1]:.1f}" stroke="{col}" stroke-width="2.3"/>\n'
    out += f'  <circle cx="{zp[0]:.1f}" cy="{zp[1]:.1f}" r="5" fill="{col}"/>\n'
    out += f'  <text x="{zp[0]+lab_dx:.1f}" y="{zp[1]+lab_dy:.1f}" font-size="12" fill="{col}">{lab}</text>\n'
    return out

svg += arrow(z1, "#1565C0", "z&#8321; (模2, 30&#176;)", 8, 16)
svg += arrow(z2, "#2E7D32", "z&#8322; (模&#8730;2, 45&#176;)", 8, -6)
svg += arrow(prod, "#9C27B0", "z&#8321;z&#8322; (模2&#8730;2, 75&#176;)", 8, -6)

def arc(deg, R, col):
    p0 = (opx + R, opy)
    p1 = (opx + R * math.cos(math.radians(deg)), opy - R * math.sin(math.radians(deg)))
    return f'  <path d="M {p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 0 0 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="{col}" stroke-width="1.3"/>\n'
svg += arc(30, 34, "#1565C0")
svg += arc(45, 48, "#2E7D32")
svg += arc(75, 62, "#9C27B0")

r3, a3 = poldeg(prod)
svg += f'''
  <rect x="{width-250}" y="{top+8}" width="232" height="86" fill="white" fill-opacity="0.93" stroke="#ccc" rx="4"/>
  <text x="{width-238}" y="{top+28}" font-size="11">模: 2 &#215; &#8730;2 = 2&#8730;2 &#8776; {r3:.2f}</text>
  <text x="{width-238}" y="{top+48}" font-size="11">幅角: 30&#176; + 45&#176; = 75&#176;</text>
  <text x="{width-238}" y="{top+68}" font-size="11">乘 z&#8322; = 把 z&#8321; 逆时针转45&#176;</text>
  <text x="{width-238}" y="{top+86}" font-size="11">再放大 &#8730;2 倍</text>
'''
svg += '</svg>\n'

with open('/projects/sandbox/complex_mult.svg', 'w') as f:
    f.write(svg)
print("complex_mult.svg done")
print("z1*z2 =", round(prod[0], 3), "+", round(prod[1], 3), "i")
print("模 =", round(r3, 4), " 幅角 =", round(a3, 2), "度")
