import math

# 第2类(度量): 单位斜基底夹角 omega=65 度, 向量 v = 2 e1 + 1.5 e2
# |v|^2 = a^2 + b^2 + 2ab cos(omega) (法: 平行四边形 + 余弦定理)
omega = 65.0
e1 = (1.0, 0.0)
e2 = (math.cos(math.radians(omega)), math.sin(math.radians(omega)))
a, b = 2.0, 1.5
v = (a*e1[0]+b*e2[0], a*e1[1]+b*e2[1])
P1 = (a*e1[0], a*e1[1])   # a e1
vlen = math.hypot(*v)
formula = a*a + b*b + 2*a*b*math.cos(math.radians(omega))

width, height = 720, 520
margin = 55
top = 70
x_min, x_max = -0.5, 3.3
y_min, y_max = -0.5, 2.1
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
sc = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - sc*(x_max-x_min))/2
oy = top + margin + (plot_h - sc*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*sc, oy + (y_max-y)*sc

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
    第2类(度量): 长度/夹角/点积 必须用"点积矩阵 G"(带 cos&#969;)
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    v=2e&#8321;+1.5e&#8322;, &#969;=65&#176;;  |v|&#178;=a&#178;+b&#178;+2ab&#183;cos&#969; (余弦定理)
  </text>
'''

opx, opy = to_px(0,0)
p1p = to_px(*P1); vp = to_px(*v)
svg += f'  <polygon points="{opx:.1f},{opy:.1f} {p1p[0]:.1f},{p1p[1]:.1f} {vp[0]:.1f},{vp[1]:.1f}" fill="#FFE0B2" fill-opacity="0.5" stroke="none"/>\n'

svg += arrow(opx, opy, to_px(*e1)[0], to_px(*e1)[1], "#1565C0", 2.6)
svg += arrow(opx, opy, to_px(*e2)[0], to_px(*e2)[1], "#2E7D32", 2.6)
svg += f'  <text x="{to_px(*e1)[0]:.1f}" y="{to_px(*e1)[1]+18:.1f}" font-size="12" fill="#1565C0">e&#8321;</text>\n'
svg += f'  <text x="{to_px(*e2)[0]-18:.1f}" y="{to_px(*e2)[1]-4:.1f}" font-size="12" fill="#2E7D32">e&#8322;</text>\n'

svg += f'  <line x1="{opx:.1f}" y1="{opy:.1f}" x2="{p1p[0]:.1f}" y2="{p1p[1]:.1f}" stroke="#1565C0" stroke-width="2" stroke-dasharray="5 3"/>\n'
svg += f'  <line x1="{p1p[0]:.1f}" y1="{p1p[1]:.1f}" x2="{vp[0]:.1f}" y2="{vp[1]:.1f}" stroke="#2E7D32" stroke-width="2" stroke-dasharray="5 3"/>\n'
svg += f'  <text x="{(opx+p1p[0])/2-6:.1f}" y="{opy+18:.1f}" font-size="11" fill="#1565C0">a=2</text>\n'
svg += f'  <text x="{(p1p[0]+vp[0])/2+4:.1f}" y="{(p1p[1]+vp[1])/2:.1f}" font-size="11" fill="#2E7D32">b=1.5</text>\n'

svg += arrow(opx, opy, vp[0], vp[1], "#9C27B0", 2.8)
svg += f'  <circle cx="{vp[0]:.1f}" cy="{vp[1]:.1f}" r="5" fill="#9C27B0"/>\n'
svg += f'  <text x="{vp[0]+6:.1f}" y="{vp[1]-6:.1f}" font-size="12" fill="#7B1FA2">v  (|v|&#8776;{vlen:.2f})</text>\n'

ang_label = to_px(P1[0]-0.18, P1[1]+0.12)
svg += f'  <text x="{ang_label[0]-8:.1f}" y="{ang_label[1]:.1f}" font-size="10" fill="#E65100">180&#176;-&#969;</text>\n'

svg += f'''
  <rect x="{width-272}" y="{top+8}" width="254" height="112" fill="white" fill-opacity="0.94" stroke="#ccc" rx="4"/>
  <text x="{width-260}" y="{top+28}" font-size="11">点积矩阵 G = [ 1      cos&#969; ]</text>
  <text x="{width-260}" y="{top+44}" font-size="11">                     [ cos&#969;   1   ]</text>
  <text x="{width-260}" y="{top+66}" font-size="11">u&#183;v = ac+bd+(ad+bc)cos&#969;</text>
  <text x="{width-260}" y="{top+86}" font-size="11">|v|&#178; = 4+2.25+2(2)(1.5)cos65&#176;</text>
  <text x="{width-260}" y="{top+106}" font-size="11" fill="#7B1FA2">= {formula:.3f},  |v| = {vlen:.3f}</text>
'''
svg += '</svg>\n'
with open('/projects/sandbox/oblique_metric.svg','w') as f:
    f.write(svg)
print("oblique_metric.svg done; |v|^2=", round(formula,3), " |v|=", round(vlen,3))
