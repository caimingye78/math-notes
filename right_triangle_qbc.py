import math

# 抛物线 y=-x^2+2x+3, B(3,0), C(0,3), Q 在对称轴 x=1 上 Q(1,m)
# 使 三角形QBC 为直角三角形, 分三种情况(直角在Q/B/C)
def f(x):
    return -x*x + 2*x + 3
B = (3.0, 0.0)
C = (0.0, 3.0)
# 直角在Q: QB.QC=0 -> m^2-3m-2=0 -> m=(3±sqrt17)/2
mq1 = (3+math.sqrt(17))/2
mq2 = (3-math.sqrt(17))/2
# 直角在B: m=-2 ; 直角在C: m=4
center = (1.5, 1.5)          # BC 中点(Thales圆心)
rad = math.dist(B, C)/2      # 3*sqrt2/2

Q = [
    (1.0, mq1, "#E53935", "&#8736;Q=90&#176;"),
    (1.0, mq2, "#E53935", "&#8736;Q=90&#176;"),
    (1.0, -2.0, "#1565C0", "&#8736;B=90&#176;"),
    (1.0, 4.0,  "#2E7D32", "&#8736;C=90&#176;"),
]

width, height = 660, 700
margin = 50
top = 64
x_min, x_max = -1.3, 4.3
y_min, y_max = -2.9, 4.9
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
sc = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - sc*(x_max-x_min))/2
oy = top + margin + (plot_h - sc*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*sc, oy + (y_max-y)*sc

def rt_square(V, P1, P2, col, s=0.32):
    import math as m
    def u(a,b):
        dx,dy=b[0]-a[0],b[1]-a[1]; L=m.hypot(dx,dy); return (dx/L,dy/L)
    u1=u(V,P1); u2=u(V,P2)
    c0=V; c1=(V[0]+s*u1[0],V[1]+s*u1[1]); c2=(V[0]+s*(u1[0]+u2[0]),V[1]+s*(u1[1]+u2[1])); c3=(V[0]+s*u2[0],V[1]+s*u2[1])
    pts=" ".join(f"{to_px(*p)[0]:.1f},{to_px(*p)[1]:.1f}" for p in [c0,c1,c2,c3])
    return f'  <polygon points="{pts}" fill="none" stroke="{col}" stroke-width="1.2"/>\n'

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="24" text-anchor="middle" font-size="15" font-family="serif">
    升级: 对称轴上 Q(1,m) 使 &#9651;QBC 为直角三角形 (4 个解)
  </text>
  <text x="{width/2}" y="44" text-anchor="middle" font-size="12" fill="#666">
    直角在Q(红,落在以BC为直径的圆上) / 在B(蓝) / 在C(绿)
  </text>
'''

# 网格+轴
ax0x, ax0y = to_px(0,0)
svg += f'  <line x1="{to_px(x_min,0)[0]:.1f}" y1="{ax0y:.1f}" x2="{to_px(x_max,0)[0]:.1f}" y2="{ax0y:.1f}" stroke="#ccc" stroke-width="1"/>\n'
svg += f'  <line x1="{ax0x:.1f}" y1="{to_px(0,y_max)[1]:.1f}" x2="{ax0x:.1f}" y2="{to_px(0,y_min)[1]:.1f}" stroke="#ccc" stroke-width="1"/>\n'

# 对称轴
axpx,_=to_px(1,0)
svg += f'  <line x1="{axpx:.1f}" y1="{to_px(0,y_max)[1]:.1f}" x2="{axpx:.1f}" y2="{to_px(0,y_min)[1]:.1f}" stroke="#FF9800" stroke-width="1.3" stroke-dasharray="5 4"/>\n'
svg += f'  <text x="{axpx+4:.1f}" y="{to_px(0,y_max)[1]+12:.1f}" font-size="10" fill="#FF9800">x=1</text>\n'

# Thales 圆
cp=[]
for i in range(361):
    a=math.radians(i)
    px,py=to_px(center[0]+rad*math.cos(a), center[1]+rad*math.sin(a))
    cp.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#E53935" stroke-width="1.1" stroke-dasharray="4 3" points="{" ".join(cp)}"/>\n'

# 抛物线
pts=[]
for i in range(301):
    x=x_min+(x_max-x_min)*i/300
    y=f(x)
    if y_min-1<=y<=y_max+1:
        px,py=to_px(x,y); pts.append(f"{px:.1f},{py:.1f}")
svg += f'  <polyline fill="none" stroke="#9C27B0" stroke-width="2.2" points="{" ".join(pts)}"/>\n'

# BC
bpx,bpy=to_px(*B); cpx,cpy=to_px(*C)
svg += f'  <line x1="{bpx:.1f}" y1="{bpy:.1f}" x2="{cpx:.1f}" y2="{cpy:.1f}" stroke="#000" stroke-width="2"/>\n'
svg += f'  <circle cx="{bpx:.1f}" cy="{bpy:.1f}" r="4.5" fill="#000"/><text x="{bpx+6:.1f}" y="{bpy+16:.1f}" font-size="12">B(3,0)</text>\n'
svg += f'  <circle cx="{cpx:.1f}" cy="{cpy:.1f}" r="4.5" fill="#000"/><text x="{cpx-50:.1f}" y="{cpy:.1f}" font-size="12">C(0,3)</text>\n'

# 直角标记
svg += rt_square((1.0,mq1), B, C, "#E53935")
svg += rt_square((1.0,mq2), B, C, "#E53935")
svg += rt_square(B, (1.0,-2.0), C, "#1565C0")
svg += rt_square(C, (1.0,4.0), B, "#2E7D32")
# 蓝/绿 直角的腿
qb=to_px(1.0,-2.0)
svg += f'  <line x1="{qb[0]:.1f}" y1="{qb[1]:.1f}" x2="{bpx:.1f}" y2="{bpy:.1f}" stroke="#1565C0" stroke-width="1.2"/>\n'
qg=to_px(1.0,4.0)
svg += f'  <line x1="{qg[0]:.1f}" y1="{qg[1]:.1f}" x2="{cpx:.1f}" y2="{cpy:.1f}" stroke="#2E7D32" stroke-width="1.2"/>\n'

labels_done=set()
for (x,m,col,lab) in Q:
    px,py=to_px(x,m)
    svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{col}"/>\n'
    svg += f'  <text x="{px+8:.1f}" y="{py+4:.1f}" font-size="10.5" fill="{col}">Q(1,{m:.2f}) {lab}</text>\n'
svg += '</svg>\n'
with open('/projects/sandbox/right_triangle_qbc.svg','w') as f:
    f.write(svg)
print("right_triangle_qbc.svg done")
print("直角在Q: m=(3±sqrt17)/2 =", round(mq1,3), round(mq2,3))
print("直角在B: m=-2 ; 直角在C: m=4")
