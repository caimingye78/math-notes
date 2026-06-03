import math

# 三角形 ABC, 取 AB=e1, AC=e2 为斜基底 -> A(0,0) B(1,0) C(0,1)
# 重心 G(1/3,1/3) 把三角形分成三个等面积小三角形, 用行列式(斜坐标)直接算面积比
A = (0.0, 0.0)
e1 = (3.4, 0.0)
e2 = (1.0, 2.6)
B = e1
C = e2
G = ((A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3)
Mbc = ((B[0]+C[0])/2, (B[1]+C[1])/2)
Mac = ((A[0]+C[0])/2, (A[1]+C[1])/2)
Mab = ((A[0]+B[0])/2, (A[1]+B[1])/2)

width, height = 720, 560
margin = 55
top = 70
x_min, x_max = -0.6, 4.0
y_min, y_max = -0.6, 3.0
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
sc = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - sc*(x_max-x_min))/2
oy = top + margin + (plot_h - sc*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*sc, oy + (y_max-y)*sc

def poly(pts, fill, stroke):
    sp = " ".join(f"{to_px(*p)[0]:.1f},{to_px(*p)[1]:.1f}" for p in pts)
    return f'  <polygon points="{sp}" fill="{fill}" fill-opacity="0.45" stroke="{stroke}" stroke-width="1"/>\n'

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    第1类(仿射): 面积比/共线 用斜坐标"行列式"直接算, 不需要&#969;
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    A(0,0) B(1,0) C(0,1), 重心 G(1/3,1/3) 把三角形三等分
  </text>
'''

svg += poly([G, B, C], "#90CAF9", "#1565C0")
svg += poly([G, C, A], "#A5D6A7", "#2E7D32")
svg += poly([G, A, B], "#FFCC80", "#E65100")

for s_, e_ in [(A, Mbc), (B, Mac), (C, Mab)]:
    p1 = to_px(*s_); p2 = to_px(*e_)
    svg += f'  <line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" stroke="#999" stroke-width="1" stroke-dasharray="5 3"/>\n'

ap=to_px(*A); bp=to_px(*B); cp=to_px(*C)
svg += f'  <polygon points="{ap[0]:.1f},{ap[1]:.1f} {bp[0]:.1f},{bp[1]:.1f} {cp[0]:.1f},{cp[1]:.1f}" fill="none" stroke="#333" stroke-width="2"/>\n'

for pt, lab, dx, dy, col in [
    (A, "A(0,0)", -12, 16, "#000"),
    (B, "B(1,0)", 6, 16, "#000"),
    (C, "C(0,1)", -10, -8, "#000"),
    (G, "G(1/3,1/3)", 8, -6, "#7B1FA2"),
]:
    px, py = to_px(*pt)
    svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{col}"/>\n'
    svg += f'  <text x="{px+dx:.1f}" y="{py+dy:.1f}" font-size="12" fill="{col}">{lab}</text>\n'

for tri in [[G,B,C],[G,C,A],[G,A,B]]:
    cxp = sum(to_px(*p)[0] for p in tri)/3
    cyp = sum(to_px(*p)[1] for p in tri)/3
    svg += f'  <text x="{cxp-10:.1f}" y="{cyp+4:.1f}" font-size="12" fill="#333">S/3</text>\n'

svg += f'''
  <rect x="{width-264}" y="{top+8}" width="246" height="92" fill="white" fill-opacity="0.93" stroke="#ccc" rx="4"/>
  <text x="{width-252}" y="{top+28}" font-size="11">面积 = |行列式| &#215; S&#8320;  (S&#8320;=|e&#8321;&#215;e&#8322;|)</text>
  <text x="{width-252}" y="{top+48}" font-size="11">比值里 S&#8320; 抵消 -&gt; 只看行列式</text>
  <text x="{width-252}" y="{top+68}" font-size="11">S(GBC)/S(ABC) = (1/6)/(1/2) = 1/3</text>
  <text x="{width-252}" y="{top+88}" font-size="11" fill="#7B1FA2">三块各占 1/3, 与 &#969; 无关</text>
'''
svg += '</svg>\n'
with open('/projects/sandbox/oblique_area.svg','w') as f:
    f.write(svg)
print("oblique_area.svg done; G=", (round(G[0],3),round(G[1],3)))
