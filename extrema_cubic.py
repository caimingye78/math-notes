import math

# 用导数求单调性与极值: f(x)=x^3-3x, f'(x)=3x^2-3=3(x^2-1)
def f(x):
    return x**3 - 3*x

width, height = 700, 600
margin = 55
top = 64
x_min, x_max = -2.4, 2.4
y_min, y_max = -4.6, 4.6
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
    导数的应用: f(x)=x&#179;-3x 的单调性与极值
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    f'(x)=3x&#178;-3=3(x&#178;-1); f'&gt;0 增(绿), f'&lt;0 减(红), f'=0 在 x=&#177;1 取极值
  </text>
'''

ax0x, ax0y = to_px(0,0)
svg += f'  <line x1="{to_px(x_min,0)[0]:.1f}" y1="{ax0y:.1f}" x2="{to_px(x_max,0)[0]:.1f}" y2="{ax0y:.1f}" stroke="#999" stroke-width="1"/>\n'
svg += f'  <line x1="{ax0x:.1f}" y1="{to_px(0,y_max)[1]:.1f}" x2="{ax0x:.1f}" y2="{to_px(0,y_min)[1]:.1f}" stroke="#999" stroke-width="1"/>\n'
for v in [-2,-1,1,2]:
    px,py=to_px(v,0); svg += f'  <text x="{px:.1f}" y="{py+14:.1f}" text-anchor="middle" font-size="9">{v}</text>\n'
for v in [-4,-2,2,4]:
    px,py=to_px(0,v); svg += f'  <text x="{px-7:.1f}" y="{py+3:.1f}" text-anchor="end" font-size="9">{v}</text>\n'

def seg(a,b,col):
    pts=[]
    N=120
    for i in range(N+1):
        x=a+(b-a)*i/N; y=f(x)
        px,py=to_px(x,y); pts.append(f"{px:.1f},{py:.1f}")
    return f'  <polyline fill="none" stroke="{col}" stroke-width="2.6" points="{" ".join(pts)}"/>\n'
svg += seg(x_min,-1,"#2E7D32")
svg += seg(-1,1,"#E53935")
svg += seg(1,x_max,"#2E7D32")

for (x,y,lab,dx,dy) in [(-1,2,"极大 (-1, 2)",8,-8),(1,-2,"极小 (1, -2)",8,18)]:
    px,py=to_px(x,y)
    t1=to_px(x-0.6,y); t2=to_px(x+0.6,y)
    svg += f'  <line x1="{t1[0]:.1f}" y1="{t1[1]:.1f}" x2="{t2[0]:.1f}" y2="{t2[1]:.1f}" stroke="#E65100" stroke-width="2" stroke-dasharray="5 3"/>\n'
    svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="#1565C0"/>\n'
    svg += f'  <text x="{px+dx:.1f}" y="{py+dy:.1f}" font-size="12" fill="#1565C0">{lab}</text>\n'
    svg += f'  <text x="{px+dx:.1f}" y="{py+dy+15:.1f}" font-size="10" fill="#E65100">切线斜率=0</text>\n'

svg += f'''
  <rect x="{margin+6}" y="{top+8}" width="152" height="78" fill="white" fill-opacity="0.93" stroke="#ccc" rx="4"/>
  <text x="{margin+16}" y="{top+28}" font-size="11" fill="#2E7D32">x&lt;-1: f'&gt;0 递增</text>
  <text x="{margin+16}" y="{top+46}" font-size="11" fill="#E53935">-1&lt;x&lt;1: f'&lt;0 递减</text>
  <text x="{margin+16}" y="{top+64}" font-size="11" fill="#2E7D32">x&gt;1: f'&gt;0 递增</text>
  <text x="{margin+16}" y="{top+82}" font-size="11" fill="#E65100">x=&#177;1: f'=0 极值</text>
'''
svg += '</svg>\n'
with open('/projects/sandbox/extrema_cubic.svg','w') as fp:
    fp.write(svg)
print("extrema_cubic.svg done; 极大(-1,2) 极小(1,-2)")
