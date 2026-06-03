import math

# 导数的定义: 割线斜率的极限 = 切线斜率。以 y=x^2 在 P(1,1) 处为例。
def f(x):
    return x*x

P = (1.0, 1.0)
Qx = [2.5, 2.0, 1.5, 1.25]
slopes = [(f(q)-f(P[0]))/(q-P[0]) for q in Qx]

width, height = 720, 560
margin = 55
top = 64
x_min, x_max = -1.5, 3.0
y_min, y_max = -1.2, 7.0
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
sc = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - sc*(x_max-x_min))/2
oy = top + margin + (plot_h - sc*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*sc, oy + (y_max-y)*sc

def line_through(x0, y0, k, xa, xb):
    return (to_px(xa, y0+k*(xa-x0)), to_px(xb, y0+k*(xb-x0)))

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    导数的定义: 割线斜率的极限 = 切线斜率 (y=x&#178; 在 P(1,1))
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    Q 越靠近 P, 割线斜率 -&gt; 2, 这个极限就是 f'(1)=2
  </text>
'''

ax0x, ax0y = to_px(0,0)
svg += f'  <line x1="{to_px(x_min,0)[0]:.1f}" y1="{ax0y:.1f}" x2="{to_px(x_max,0)[0]:.1f}" y2="{ax0y:.1f}" stroke="#999" stroke-width="1"/>\n'
svg += f'  <line x1="{ax0x:.1f}" y1="{to_px(0,y_max)[1]:.1f}" x2="{ax0x:.1f}" y2="{to_px(0,y_min)[1]:.1f}" stroke="#999" stroke-width="1"/>\n'
for v in [1,2]:
    px,py=to_px(v,0); svg += f'  <text x="{px:.1f}" y="{py+14:.1f}" text-anchor="middle" font-size="9">{v}</text>\n'

cols = ["#bbbbbb","#90a4d4","#5c7fd6","#3f6ed4"]
for q,k,col in zip(Qx, slopes, cols):
    a,b = line_through(P[0],P[1],k,-1.3, 2.8)
    svg += f'  <line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{col}" stroke-width="1.2"/>\n'
    qp=to_px(q,f(q))
    svg += f'  <circle cx="{qp[0]:.1f}" cy="{qp[1]:.1f}" r="3.5" fill="{col}"/>\n'

a,b = line_through(P[0],P[1],2.0,-1.3,2.8)
svg += f'  <line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#E65100" stroke-width="2.6"/>\n'
tl=to_px(2.4,2*2.4-1)
svg += f'  <text x="{tl[0]+4:.1f}" y="{tl[1]:.1f}" font-size="11" fill="#E65100">切线 y=2x-1</text>\n'

pts=[]
for i in range(301):
    x=x_min+(x_max-x_min)*i/300; y=f(x)
    if y<=y_max+0.5:
        px,py=to_px(x,y); pts.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#9C27B0" stroke-width="2.4" points="{" ".join(pts)}"/>\n'

pp=to_px(*P)
svg += f'  <circle cx="{pp[0]:.1f}" cy="{pp[1]:.1f}" r="5" fill="#E65100"/>\n'
svg += f'  <text x="{pp[0]-36:.1f}" y="{pp[1]+18:.1f}" font-size="12" fill="#E65100">P(1,1)</text>\n'

svg += f'''
  <rect x="{margin+6}" y="{top+8}" width="186" height="118" fill="white" fill-opacity="0.93" stroke="#ccc" rx="4"/>
  <text x="{margin+18}" y="{top+28}" font-size="11">割线斜率 (P 到 Q):</text>
  <text x="{margin+18}" y="{top+46}" font-size="11">Q=2.5  -&gt; 3.5</text>
  <text x="{margin+18}" y="{top+62}" font-size="11">Q=2.0  -&gt; 3.0</text>
  <text x="{margin+18}" y="{top+78}" font-size="11">Q=1.5  -&gt; 2.5</text>
  <text x="{margin+18}" y="{top+94}" font-size="11">Q=1.25 -&gt; 2.25</text>
  <text x="{margin+18}" y="{top+114}" font-size="11" fill="#E65100">极限 -&gt; 2 = f'(1)</text>
'''
svg += '</svg>\n'
with open('/projects/sandbox/secant_tangent.svg','w') as fp:
    fp.write(svg)
print("secant_tangent.svg done; slopes=", [round(s,3) for s in slopes], "-> 2")
