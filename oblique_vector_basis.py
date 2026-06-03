import math

# 平行四边形 ABCD, 取 AB=e1, AD=e2 为(斜)基底
A = (0.0, 0.0)
e1 = (3.2, 0.0)        # AB
e2 = (1.1, 2.4)        # AD (与 AB 不垂直)
B = e1
D = e2
C = (e1[0]+e2[0], e1[1]+e2[1])
M = ((A[0]+C[0])/2, (A[1]+C[1])/2)   # 对角线交点 = 中心
N = ((B[0]+C[0])/2, (B[1]+C[1])/2)   # BC 中点

width, height = 720, 560
margin = 55
top = 70
x_min, x_max = -0.7, 5.0
y_min, y_max = -0.7, 3.0
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
s = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - s*(x_max-x_min))/2
oy = top + margin + (plot_h - s*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*s, oy + (y_max-y)*s

def comb(a, b):  # a*e1 + b*e2 的世界坐标
    return (a*e1[0]+b*e2[0], a*e1[1]+b*e2[1])

def arrow(x1, y1, x2, y2, col, w=2.4):
    ang = math.atan2(y2-y1, x2-x1); L = 11
    p1 = (x2 - L*math.cos(ang-0.4), y2 - L*math.sin(ang-0.4))
    p2 = (x2 - L*math.cos(ang+0.4), y2 - L*math.sin(ang+0.4))
    return (f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}"/>\n'
            f'  <polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>\n')

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    向量 &#8596; 斜坐标: 取 AB=e&#8321;, AD=e&#8322; 为基底
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    平行四边形在它自己的斜坐标系里就是"单位正方形"
  </text>
'''

ap=to_px(*A); bp=to_px(*B); cp=to_px(*C); dp=to_px(*D)
svg += f'  <polygon points="{ap[0]:.1f},{ap[1]:.1f} {bp[0]:.1f},{bp[1]:.1f} {cp[0]:.1f},{cp[1]:.1f} {dp[0]:.1f},{dp[1]:.1f}" fill="#90CAF9" fill-opacity="0.18" stroke="#1565C0" stroke-width="1.6"/>\n'

for t in [0.0, 0.5, 1.0]:
    s1=to_px(*comb(0, t)); s2=to_px(*comb(1, t))
    svg += f'  <line x1="{s1[0]:.1f}" y1="{s1[1]:.1f}" x2="{s2[0]:.1f}" y2="{s2[1]:.1f}" stroke="#bbb" stroke-width="0.8" stroke-dasharray="4 3"/>\n'
    s3=to_px(*comb(t, 0)); s4=to_px(*comb(t, 1))
    svg += f'  <line x1="{s3[0]:.1f}" y1="{s3[1]:.1f}" x2="{s4[0]:.1f}" y2="{s4[1]:.1f}" stroke="#bbb" stroke-width="0.8" stroke-dasharray="4 3"/>\n'

svg += arrow(ap[0], ap[1], bp[0], bp[1], "#1565C0", 2.6)
svg += arrow(ap[0], ap[1], dp[0], dp[1], "#2E7D32", 2.6)
mb=((ap[0]+bp[0])/2,(ap[1]+bp[1])/2); md=((ap[0]+dp[0])/2,(ap[1]+dp[1])/2)
svg += f'  <text x="{mb[0]-8:.1f}" y="{mb[1]+18:.1f}" font-size="12" fill="#1565C0">e&#8321;=AB</text>\n'
svg += f'  <text x="{md[0]-44:.1f}" y="{md[1]:.1f}" font-size="12" fill="#2E7D32">e&#8322;=AD</text>\n'

svg += f'  <line x1="{ap[0]:.1f}" y1="{ap[1]:.1f}" x2="{cp[0]:.1f}" y2="{cp[1]:.1f}" stroke="#9C27B0" stroke-width="1.4" stroke-dasharray="6 3"/>\n'
svg += f'  <line x1="{bp[0]:.1f}" y1="{bp[1]:.1f}" x2="{dp[0]:.1f}" y2="{dp[1]:.1f}" stroke="#E65100" stroke-width="1.4" stroke-dasharray="6 3"/>\n'

pts = [
    (A, "A(0,0)", -10, 16),
    (B, "B(1,0)", 6, 16),
    (C, "C(1,1)", 8, -6),
    (D, "D(0,1)", -52, -4),
    (M, "M(1/2,1/2)", 8, -6),
    (N, "N(1,1/2)", 8, 4),
]
for pt, lab, dx, dy in pts:
    px, py = to_px(*pt)
    col = "#7B1FA2" if lab[0] in "MN" else "#000"
    svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{col}"/>\n'
    svg += f'  <text x="{px+dx:.1f}" y="{py+dy:.1f}" font-size="11.5" fill="{col}">{lab}</text>\n'

svg += f'''
  <rect x="{width-256}" y="{top+8}" width="238" height="74" fill="white" fill-opacity="0.93" stroke="#ccc" rx="4"/>
  <text x="{width-244}" y="{top+28}" font-size="11">AC 中点 = (1/2, 1/2)</text>
  <text x="{width-244}" y="{top+46}" font-size="11">BD 中点 = (1/2, 1/2)</text>
  <text x="{width-244}" y="{top+66}" font-size="11" fill="#7B1FA2">坐标相同 -&gt; 对角线互相平分</text>
'''
svg += '</svg>\n'
with open('/projects/sandbox/oblique_vector_basis.svg','w') as f:
    f.write(svg)
print("oblique_vector_basis.svg done")
print("C =", C, " M(center) =", M, " N(mid BC) =", N)
