import math

S = 12.0
c = 2.0  # demo corner cut (represents x)
width, height = 620, 600
margin = 60
top = 64
x_min, x_max = -1.5, 13.0
y_min, y_max = -1.5, 13.0
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
sc = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))
ox = margin + (plot_w - sc*(x_max-x_min))/2
oy = top + margin + (plot_h - sc*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x-x_min)*sc, oy + (y_max-y)*sc

def rect(x0,y0,x1,y1,fill,stroke,sw=1.5):
    p0=to_px(x0,y1); p1=to_px(x1,y0)
    return f'  <rect x="{p0[0]:.1f}" y="{p0[1]:.1f}" width="{(p1[0]-p0[0]):.1f}" height="{(p1[1]-p0[1]):.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n'

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="15" font-family="serif">
    无盖盒子: 12&#215;12 铁皮四角剪去 x&#215;x 折成盒子
  </text>
  <text x="{width/2}" y="46" text-anchor="middle" font-size="12" fill="#666">
    底面 (12-2x)&#215;(12-2x), 高 x, 体积 V(x)=x(12-2x)&#178;
  </text>
'''
svg += rect(0,0,S,S,"#FFF8E1","#8d6e63",2)
svg += rect(c,c,S-c,S-c,"#A5D6A7","#2E7D32",1.2)
midb=to_px(S/2,S/2)
svg += f'  <text x="{midb[0]:.1f}" y="{midb[1]:.1f}" text-anchor="middle" font-size="11" fill="#2E7D32">底面 (12-2x)&#178;</text>\n'
for (x0,y0) in [(0,0),(S-c,0),(0,S-c),(S-c,S-c)]:
    svg += rect(x0,y0,x0+c,y0+c,"#FFCDD2","#C62828",1.2)
    cc=to_px(x0+c/2,y0+c/2)
    svg += f'  <text x="{cc[0]:.1f}" y="{cc[1]+4:.1f}" text-anchor="middle" font-size="10" fill="#C62828">x&#183;x</text>\n'
t1=to_px(0,S+0.5); t2=to_px(S,S+0.5)
svg += f'  <line x1="{t1[0]:.1f}" y1="{t1[1]:.1f}" x2="{t2[0]:.1f}" y2="{t2[1]:.1f}" stroke="#444" stroke-width="1"/>\n'
svg += f'  <text x="{(t1[0]+t2[0])/2:.1f}" y="{t1[1]-4:.1f}" text-anchor="middle" font-size="12">12</text>\n'
lx=to_px(-0.7,0); ly=to_px(-0.7,c)
svg += f'  <line x1="{lx[0]:.1f}" y1="{lx[1]:.1f}" x2="{ly[0]:.1f}" y2="{ly[1]:.1f}" stroke="#C62828" stroke-width="1"/>\n'
svg += f'  <text x="{lx[0]-6:.1f}" y="{(lx[1]+ly[1])/2:.1f}" text-anchor="end" font-size="12" fill="#C62828">x</text>\n'
b1=to_px(c,-0.7); b2=to_px(S-c,-0.7)
svg += f'  <line x1="{b1[0]:.1f}" y1="{b1[1]:.1f}" x2="{b2[0]:.1f}" y2="{b2[1]:.1f}" stroke="#2E7D32" stroke-width="1"/>\n'
svg += f'  <text x="{(b1[0]+b2[0])/2:.1f}" y="{b1[1]+15:.1f}" text-anchor="middle" font-size="11" fill="#2E7D32">12-2x</text>\n'
svg += '</svg>\n'
with open('/projects/sandbox/box_net.svg','w') as fp:
    fp.write(svg)
print("box_net.svg done")
