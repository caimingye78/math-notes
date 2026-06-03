import math

# z^5 = 1 的五个单位根: z_k = cos(72k) + i sin(72k), k=0..4
n = 5
width, height = 600, 640
margin = 55
top = 70
x_min, x_max = -1.45, 1.45
y_min, y_max = -1.45, 1.45
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
sc = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - sc*(x_max-x_min))/2
oy = top + margin + (plot_h - sc*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*sc, oy + (y_max-y)*sc

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    z&#8309; = 1 的五个根: 单位圆上均匀分布 (正五边形)
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    z&#8342; = cos(72&#176;k) + i&#183;sin(72&#176;k),  k=0,1,2,3,4
  </text>
'''

# 轴
svg += f'  <line x1="{to_px(x_min,0)[0]:.1f}" y1="{to_px(0,0)[1]:.1f}" x2="{to_px(x_max,0)[0]:.1f}" y2="{to_px(0,0)[1]:.1f}" stroke="#000" stroke-width="1"/>\n'
svg += f'  <line x1="{to_px(0,0)[0]:.1f}" y1="{to_px(0,y_max)[1]:.1f}" x2="{to_px(0,0)[0]:.1f}" y2="{to_px(0,y_min)[1]:.1f}" stroke="#000" stroke-width="1"/>\n'
svg += f'  <text x="{to_px(x_max,0)[0]-8:.1f}" y="{to_px(0,0)[1]+16:.1f}" font-size="11" font-style="italic">Re</text>\n'
svg += f'  <text x="{to_px(0,0)[0]+6:.1f}" y="{to_px(0,y_max)[1]+8:.1f}" font-size="11" font-style="italic">Im</text>\n'

# 单位圆
cp=[]
for i in range(361):
    a=math.radians(i)
    px,py=to_px(math.cos(a), math.sin(a))
    cp.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#bbb" stroke-width="1.2" points="{" ".join(cp)}"/>\n'

# 五边形
poly=[]
for k in range(n):
    a=2*math.pi*k/n
    poly.append(to_px(math.cos(a), math.sin(a)))
ps=" ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in poly)
svg += f'  <polygon points="{ps}" fill="#90CAF9" fill-opacity="0.18" stroke="#1565C0" stroke-width="1.6"/>\n'

ocx,ocy=to_px(0,0)
svg += f'  <circle cx="{ocx:.1f}" cy="{ocy:.1f}" r="3" fill="#000"/>\n'

for k in range(n):
    a=2*math.pi*k/n
    x,y=math.cos(a),math.sin(a)
    px,py=to_px(x,y)
    svg += f'  <line x1="{ocx:.1f}" y1="{ocy:.1f}" x2="{px:.1f}" y2="{py:.1f}" stroke="#9C27B0" stroke-width="1" stroke-dasharray="3 2"/>\n'
    svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="5.5" fill="#9C27B0"/>\n'
    deg=72*k
    lx = px + 16*math.cos(a) - 8
    ly = py - 14*math.sin(a) + 4
    svg += f'  <text x="{lx:.1f}" y="{ly:.1f}" font-size="11" fill="#7B1FA2">z{k} ({deg}&#176;)</text>\n'

svg += f'''
  <rect x="{margin}" y="{top+6}" width="150" height="56" fill="white" fill-opacity="0.9" stroke="#ccc" rx="4"/>
  <text x="{margin+12}" y="{top+26}" font-size="11">5 根间隔 360&#176;/5</text>
  <text x="{margin+12}" y="{top+44}" font-size="11">= 72&#176;, 模都为 1</text>
'''
svg += '</svg>\n'
with open('/projects/sandbox/roots_unity5.svg','w') as f:
    f.write(svg)
print("roots_unity5.svg done; 五根角度:", [72*k for k in range(5)])
