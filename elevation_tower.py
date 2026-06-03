import math

# 测塔高: 地面 A 处测塔顶仰角 30, 前进 AB=20 到 B 测仰角 60, 求塔高 h
# tan30 = h/AD, tan60 = h/BD, AD-BD=20 -> h=10*sqrt3
h = 10*math.sqrt(3)          # ~17.32
AD = h/math.tan(math.radians(30))   # 30
BD = h/math.tan(math.radians(60))   # 10
D = (0.0, 0.0)               # 塔脚
T = (0.0, h)                 # 塔顶
A = (-AD, 0.0)
B = (-BD, 0.0)

width, height = 740, 470
margin = 50
top = 60
x_min, x_max = -34.0, 5.0
y_min, y_max = -3.0, 21.0
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
    解直角三角形: 两次仰角测塔高
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    A 测仰角30&#176;, 前进 AB=20 到 B 测仰角60&#176; &#8594; 塔高 h = 10&#8730;3 &#8776; 17.32
  </text>
'''

g1=to_px(x_min+1,0); g2=to_px(x_max-1,0)
svg += f'  <line x1="{g1[0]:.1f}" y1="{g1[1]:.1f}" x2="{g2[0]:.1f}" y2="{g2[1]:.1f}" stroke="#8d6e63" stroke-width="2"/>\n'

dp=to_px(*D); tp=to_px(*T)
svg += f'  <line x1="{dp[0]:.1f}" y1="{dp[1]:.1f}" x2="{tp[0]:.1f}" y2="{tp[1]:.1f}" stroke="#444" stroke-width="4"/>\n'
svg += f'  <text x="{tp[0]+6:.1f}" y="{tp[1]-4:.1f}" font-size="12" fill="#444">塔顶 T</text>\n'
svg += f'  <rect x="{dp[0]:.1f}" y="{dp[1]-12:.1f}" width="12" height="12" fill="none" stroke="#444" stroke-width="1"/>\n'
svg += f'  <text x="{dp[0]+4:.1f}" y="{dp[1]+16:.1f}" font-size="12" fill="#444">D</text>\n'
midh=to_px(0, h/2)
svg += f'  <text x="{midh[0]+6:.1f}" y="{midh[1]:.1f}" font-size="12" fill="#C62828">h=10&#8730;3</text>\n'

ap=to_px(*A); bp=to_px(*B)
svg += f'  <line x1="{ap[0]:.1f}" y1="{ap[1]:.1f}" x2="{tp[0]:.1f}" y2="{tp[1]:.1f}" stroke="#1565C0" stroke-width="1.6"/>\n'
svg += f'  <line x1="{bp[0]:.1f}" y1="{bp[1]:.1f}" x2="{tp[0]:.1f}" y2="{tp[1]:.1f}" stroke="#2E7D32" stroke-width="1.6"/>\n'

for pt,nm,dx in [(A,"A",-4),(B,"B",-4)]:
    px,py=to_px(*pt)
    svg += f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="#000"/>\n'
    svg += f'  <text x="{px+dx:.1f}" y="{py+18:.1f}" font-size="12">{nm}</text>\n'

def arc_at(pt, deg, R, col):
    px,py=to_px(*pt)
    p0=(px+R,py)
    p1=(px+R*math.cos(math.radians(deg)), py-R*math.sin(math.radians(deg)))
    return f'  <path d="M {p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 0 0 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="{col}" stroke-width="1.4"/>\n'
svg += arc_at(A,30,34,"#1565C0")
svg += f'  <text x="{ap[0]+36:.1f}" y="{ap[1]-8:.1f}" font-size="11" fill="#1565C0">30&#176;</text>\n'
svg += arc_at(B,60,30,"#2E7D32")
svg += f'  <text x="{bp[0]+30:.1f}" y="{bp[1]-10:.1f}" font-size="11" fill="#2E7D32">60&#176;</text>\n'
mab=to_px((A[0]+B[0])/2,0)
svg += f'  <text x="{mab[0]-14:.1f}" y="{mab[1]+18:.1f}" font-size="11">AB=20</text>\n'

svg += f'''
  <rect x="{width-250}" y="{top+6}" width="234" height="92" fill="white" fill-opacity="0.93" stroke="#ccc" rx="4"/>
  <text x="{width-238}" y="{top+26}" font-size="11">tan30&#176; = h/AD -&gt; AD = h&#8730;3</text>
  <text x="{width-238}" y="{top+44}" font-size="11">tan60&#176; = h/BD -&gt; BD = h/&#8730;3</text>
  <text x="{width-238}" y="{top+62}" font-size="11">AD - BD = AB = 20</text>
  <text x="{width-238}" y="{top+84}" font-size="11" fill="#C62828">h(2/&#8730;3)=20 -&gt; h=10&#8730;3&#8776;17.32</text>
'''
svg += '</svg>\n'
with open('/projects/sandbox/elevation_tower.svg','w') as f:
    f.write(svg)
print("elevation_tower.svg done: h =", round(h,3), "AD=",round(AD,2),"BD=",round(BD,2))
