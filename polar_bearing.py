import math

# 例：O 处观测，P 在 O 的"北偏东 30 度"方向、距离 r=100 处
# 这就是极坐标 (r, theta)。转成"东/北"分量 = 直角坐标
r = 100.0
theta_deg = 30.0          # 与正北方向的夹角
th = math.radians(theta_deg)
east = r * math.sin(th)   # 东向分量 = r sin30 = 50
north = r * math.cos(th)  # 北向分量 = r cos30 = 50 sqrt3 ~ 86.60
P = (east, north)

width, height = 660, 720
margin = 60
top = 64
x_min, x_max = -25.0, 115.0
y_min, y_max = -25.0, 115.0
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin

def to_px(x, y):
    px = margin + (x - x_min)/(x_max - x_min)*plot_w
    py = top + margin + (y_max - y)/(y_max - y_min)*plot_h
    return px, py

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="16" font-family="serif">
    极坐标的"影子"：方位角问题 (r=100, 北偏东30&#176;)
  </text>
  <text x="{width/2}" y="48" text-anchor="middle" font-size="12" fill="#666">
    用(距离, 角度)定位一点 -&gt; 解直角三角形求东/北分量
  </text>
'''

Ox, Oy = to_px(0, 0)
ntop = to_px(0, 110)
svg += f'  <line x1="{Ox:.1f}" y1="{Oy:.1f}" x2="{ntop[0]:.1f}" y2="{ntop[1]:.1f}" stroke="#888" stroke-width="1.2" stroke-dasharray="5 4"/>\n'
svg += f'  <text x="{ntop[0]-6:.1f}" y="{ntop[1]-6:.1f}" font-size="13" fill="#444">北 N</text>\n'
eend = to_px(110, 0)
svg += f'  <line x1="{Ox:.1f}" y1="{Oy:.1f}" x2="{eend[0]:.1f}" y2="{eend[1]:.1f}" stroke="#888" stroke-width="1.2" stroke-dasharray="5 4"/>\n'
svg += f'  <text x="{eend[0]+4:.1f}" y="{eend[1]+4:.1f}" font-size="13" fill="#444">东 E</text>\n'

svg += f'  <circle cx="{Ox:.1f}" cy="{Oy:.1f}" r="4.5" fill="#000"/>\n'
svg += f'  <text x="{Ox-22:.1f}" y="{Oy+16:.1f}" font-size="13">O</text>\n'

ppx, ppy = to_px(*P)
svg += f'  <line x1="{Ox:.1f}" y1="{Oy:.1f}" x2="{ppx:.1f}" y2="{ppy:.1f}" stroke="#9C27B0" stroke-width="2.5"/>\n'
mid = ((Ox+ppx)/2, (Oy+ppy)/2)
svg += f'  <text x="{mid[0]-44:.1f}" y="{mid[1]:.1f}" font-size="12" fill="#7B1FA2">r = 100</text>\n'

arcR = 46
def pt_on_arc(deg_from_north):
    a = math.radians(deg_from_north)
    x = arcR * math.sin(a)
    y = arcR * math.cos(a)
    return (Ox + x, Oy - y)
p_start = pt_on_arc(0)
p_end = pt_on_arc(theta_deg)
svg += f'  <path d="M {p_start[0]:.1f} {p_start[1]:.1f} A {arcR} {arcR} 0 0 1 {p_end[0]:.1f} {p_end[1]:.1f}" fill="none" stroke="#E65100" stroke-width="1.6"/>\n'
lbl = pt_on_arc(theta_deg/2)
svg += f'  <text x="{lbl[0]+2:.1f}" y="{lbl[1]-2:.1f}" font-size="12" fill="#E65100">30&#176;</text>\n'

footN = to_px(0, north)
footE = to_px(east, 0)
svg += f'  <line x1="{ppx:.1f}" y1="{ppy:.1f}" x2="{footN[0]:.1f}" y2="{footN[1]:.1f}" stroke="#1565C0" stroke-width="1.6" stroke-dasharray="4 3"/>\n'
svg += f'  <line x1="{ppx:.1f}" y1="{ppy:.1f}" x2="{footE[0]:.1f}" y2="{footE[1]:.1f}" stroke="#2E7D32" stroke-width="1.6" stroke-dasharray="4 3"/>\n'

svg += f'  <circle cx="{ppx:.1f}" cy="{ppy:.1f}" r="5" fill="#9C27B0"/>\n'
svg += f'  <text x="{ppx+8:.1f}" y="{ppy:.1f}" font-size="12" fill="#7B1FA2">P</text>\n'

svg += f'  <text x="{(ppx+footN[0])/2-30:.1f}" y="{ppy-6:.1f}" font-size="11" fill="#1565C0">东向=100sin30=50</text>\n'
svg += f'  <text x="{footE[0]+6:.1f}" y="{(ppy+footE[1])/2:.1f}" font-size="11" fill="#2E7D32">北向=100cos30=50&#8730;3&#8776;86.6</text>\n'

svg += f'''
  <rect x="{margin+4}" y="{top+margin+4}" width="252" height="92" fill="white" fill-opacity="0.92" stroke="#ccc" rx="4"/>
  <text x="{margin+16}" y="{top+margin+26}" font-size="11">极坐标记法: P = (r, &#952;) = (100, 北偏东30&#176;)</text>
  <text x="{margin+16}" y="{top+margin+46}" font-size="11">直角坐标: 东 x = r&#183;sin&#952;,  北 y = r&#183;cos&#952;</text>
  <text x="{margin+16}" y="{top+margin+66}" font-size="11">=&gt; P 在 O 正东 50, 正北 50&#8730;3 处</text>
  <text x="{margin+16}" y="{top+margin+86}" font-size="11">本质就是初中"解直角三角形"</text>
'''
svg += '</svg>\n'

with open('/projects/sandbox/polar_bearing.svg', 'w') as fp:
    fp.write(svg)

print("已生成 polar_bearing.svg")
print(f"东向分量 = 100*sin30 = {east:.2f}")
print(f"北向分量 = 100*cos30 = {north:.4f}  (=50*sqrt3)")
