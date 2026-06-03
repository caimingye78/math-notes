def V(x):
    return x*(12-2*x)**2

xstar, Vstar = 2.0, 128.0
width, height = 720, 560
margin = 58
top = 64
x_min, x_max = -0.6, 6.6
y_min, y_max = -12.0, 150.0
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
scx = plot_w/(x_max-x_min)
scy = plot_h/(y_max-y_min)
ox = margin
oy = top + margin

def to_px(x, y):
    return ox + (x-x_min)*scx, oy + (y_max-y)*scy

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    用导数求最大体积: V(x)=x(12-2x)&#178;, 0&lt;x&lt;6
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    V'(x)=12(x-2)(x-6); x=2 时体积最大 = 128
  </text>
'''
ax0x, ax0y = to_px(0,0)
svg += f'  <line x1="{to_px(x_min,0)[0]:.1f}" y1="{ax0y:.1f}" x2="{to_px(x_max,0)[0]:.1f}" y2="{ax0y:.1f}" stroke="#999" stroke-width="1"/>\n'
svg += f'  <line x1="{ax0x:.1f}" y1="{to_px(0,y_max)[1]:.1f}" x2="{ax0x:.1f}" y2="{to_px(0,y_min)[1]:.1f}" stroke="#999" stroke-width="1"/>\n'
for v in [1,2,3,4,5,6]:
    px,py=to_px(v,0); svg += f'  <text x="{px:.1f}" y="{py+14:.1f}" text-anchor="middle" font-size="9">{v}</text>\n'
for v in [40,80,120]:
    px,py=to_px(0,v); svg += f'  <text x="{px-6:.1f}" y="{py+3:.1f}" text-anchor="end" font-size="9">{v}</text>\n'
svg += f'  <text x="{to_px(x_max,0)[0]-2:.1f}" y="{ax0y+15:.1f}" font-size="11" font-style="italic">x</text>\n'
svg += f'  <text x="{ax0x+4:.1f}" y="{to_px(0,y_max)[1]+6:.1f}" font-size="11" font-style="italic">V</text>\n'
pts=[]
for i in range(301):
    x=6*i/300; y=V(x)
    px,py=to_px(x,y); pts.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#9C27B0" stroke-width="2.6" points="{" ".join(pts)}"/>\n'
mp=to_px(xstar,Vstar)
svg += f'  <line x1="{mp[0]:.1f}" y1="{mp[1]:.1f}" x2="{to_px(xstar,0)[0]:.1f}" y2="{to_px(xstar,0)[1]:.1f}" stroke="#E65100" stroke-width="1.3" stroke-dasharray="5 3"/>\n'
svg += f'  <line x1="{mp[0]:.1f}" y1="{mp[1]:.1f}" x2="{to_px(0,Vstar)[0]:.1f}" y2="{to_px(0,Vstar)[1]:.1f}" stroke="#E65100" stroke-width="1.3" stroke-dasharray="5 3"/>\n'
svg += f'  <circle cx="{mp[0]:.1f}" cy="{mp[1]:.1f}" r="6" fill="#E65100"/>\n'
svg += f'  <text x="{mp[0]+8:.1f}" y="{mp[1]-6:.1f}" font-size="13" fill="#E65100">最大 (2, 128)</text>\n'
t1=to_px(xstar-0.8,Vstar); t2=to_px(xstar+0.8,Vstar)
svg += f'  <line x1="{t1[0]:.1f}" y1="{t1[1]:.1f}" x2="{t2[0]:.1f}" y2="{t2[1]:.1f}" stroke="#1565C0" stroke-width="2"/>\n'
svg += f'  <text x="{t2[0]+2:.1f}" y="{t2[1]+4:.1f}" font-size="10" fill="#1565C0">V&#39;=0</text>\n'
for xe in [0.0,6.0]:
    ep=to_px(xe,0)
    svg += f'  <circle cx="{ep[0]:.1f}" cy="{ep[1]:.1f}" r="3.5" fill="#777"/>\n'
svg += f'  <text x="{to_px(6,0)[0]-2:.1f}" y="{to_px(6,0)[1]-8:.1f}" font-size="10" fill="#777">V=0</text>\n'
svg += '</svg>\n'
with open('/projects/sandbox/box_volume.svg','w') as fp:
    fp.write(svg)
print("box_volume.svg done; V(1)=",V(1)," V(2)=",V(2)," V(3)=",V(3))
