import math

# 三角形 ABC: |AB|=3, |AC|=2, 角BAC=60度
# 取 AB=e1, AC=e2 为斜基底 -> A(0,0) B(1,0) C(0,1)
# E = AB 中点 (1/2,0);  F 在 AC 上 AF=(2/3)AC -> (0, 2/3)
omega = 60.0
LAB, LAC = 3.0, 2.0
A = (0.0, 0.0)
B = (LAB, 0.0)
C = (LAC*math.cos(math.radians(omega)), LAC*math.sin(math.radians(omega)))  # (1, sqrt3)
E = ((A[0]+B[0])/2, (A[1]+B[1])/2)
F = (A[0] + (2/3)*(C[0]-A[0]), A[1] + (2/3)*(C[1]-A[1]))
EF_len = math.hypot(F[0]-E[0], F[1]-E[1])

width, height = 720, 560
margin = 55
top = 70
x_min, x_max = -0.5, 3.5
y_min, y_max = -0.5, 2.2
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
sc = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - sc*(x_max-x_min))/2
oy = top + margin + (plot_h - sc*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*sc, oy + (y_max-y)*sc

def arrow(x1,y1,x2,y2,col,w=2.4):
    ang=math.atan2(y2-y1,x2-x1); L=11
    p1=(x2-L*math.cos(ang-0.4), y2-L*math.sin(ang-0.4))
    p2=(x2-L*math.cos(ang+0.4), y2-L*math.sin(ang+0.4))
    return (f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"/>\n'
            f'  <polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>\n')

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    综合例题: |AB|=3, |AC|=2, &#8736;BAC=60&#176;
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    (1)面积比 用坐标[免cos&#969;]   (2)求|EF| 用点积矩阵[带cos&#969;]
  </text>
'''

ap=to_px(*A); bp=to_px(*B); cp=to_px(*C); ep=to_px(*E); fp=to_px(*F)
svg += f'  <polygon points="{ap[0]:.1f},{ap[1]:.1f} {bp[0]:.1f},{bp[1]:.1f} {cp[0]:.1f},{cp[1]:.1f}" fill="#90CAF9" fill-opacity="0.16" stroke="#1565C0" stroke-width="2"/>\n'
svg += f'  <polygon points="{ap[0]:.1f},{ap[1]:.1f} {ep[0]:.1f},{ep[1]:.1f} {fp[0]:.1f},{fp[1]:.1f}" fill="#A5D6A7" fill-opacity="0.6" stroke="#2E7D32" stroke-width="1.6"/>\n'
svg += f'  <line x1="{ep[0]:.1f}" y1="{ep[1]:.1f}" x2="{fp[0]:.1f}" y2="{fp[1]:.1f}" stroke="#7B1FA2" stroke-width="2"/>\n'

svg += arrow(ap[0],ap[1], bp[0],bp[1], "#1565C0", 1.6)
svg += arrow(ap[0],ap[1], cp[0],cp[1], "#2E7D32", 1.6)

R=30
p0=(ap[0]+R, ap[1])
p1=(ap[0]+R*math.cos(math.radians(omega)), ap[1]-R*math.sin(math.radians(omega)))
svg += f'  <path d="M {p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 0 0 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#E65100" stroke-width="1.4"/>\n'
svg += f'  <text x="{ap[0]+R+4:.1f}" y="{ap[1]-12:.1f}" font-size="11" fill="#E65100">60&#176;</text>\n'

for pt,lab,dx,dy,col in [
    (A,"A(0,0)",-12,18,"#000"),
    (B,"B(1,0)",4,18,"#000"),
    (C,"C(0,1)",-6,-8,"#000"),
    (E,"E(1/2,0)",-6,20,"#1565C0"),
    (F,"F(0,2/3)",8,-4,"#2E7D32"),
]:
    px,py=to_px(*pt)
    svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{col}"/>\n'
    svg += f'  <text x="{px+dx:.1f}" y="{py+dy:.1f}" font-size="11.5" fill="{col}">{lab}</text>\n'

svg += f'''
  <rect x="{width-262}" y="{top+8}" width="244" height="116" fill="white" fill-opacity="0.94" stroke="#ccc" rx="4"/>
  <text x="{width-250}" y="{top+28}" font-size="11">(1) S&#9651;AEF/S&#9651;ABC = (1/2)(2/3) = 1/3</text>
  <text x="{width-250}" y="{top+48}" font-size="11">    [只用坐标, 不需 &#969;]</text>
  <text x="{width-250}" y="{top+72}" font-size="11">(2) EF = -1/2 e&#8321; + 2/3 e&#8322;</text>
  <text x="{width-250}" y="{top+90}" font-size="11">    |EF|&#178;=73/36 -&gt; |EF|=&#8730;73/6</text>
  <text x="{width-250}" y="{top+110}" font-size="11" fill="#7B1FA2">    &#8776; {EF_len:.3f}  [用 e&#8321;&#183;e&#8322;=3]</text>
'''
svg += '</svg>\n'
with open('/projects/sandbox/oblique_example.svg','w') as f:
    f.write(svg)
print("oblique_example.svg done")
print("|EF| =", round(EF_len,4), " (= sqrt73/6 =", round(math.sqrt(73)/6,4), ")")
