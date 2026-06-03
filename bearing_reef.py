import math

# 船由西向东沿一条直线航行。
# 在 A 处测得小岛 P 在 北偏东 60 度；继续航行 AB=10 海里 到 B，
# 在 B 处测得 P 在 北偏东 30 度。P 周围 8 海里内有暗礁，问继续东行是否触礁。
#
# 解：角PAB = 90-60 = 30；B处朝东方向与BP夹角 = 90-30 = 60，故 角PBA=120，
# 三角形内角和 -> 角APB = 30，等腰 BP = AB = 10。
# 作 PD 垂直航线于 D，PD = BP sin60 = 10*(根3/2) = 5根3 约 8.66 > 8，安全。

A = (0.0, 0.0)
B = (10.0, 0.0)
PD = 10.0 * math.sin(math.radians(60))   # 5*sqrt3
BD = 10.0 * math.cos(math.radians(60))    # = 5
D = (B[0] + BD, 0.0)
P = (D[0], PD)
reef = 8.0

width, height = 760, 600
margin = 55
top = 70
x_min, x_max = -4.0, 22.0
y_min, y_max = -4.0, 14.0
plot_w = width - 2*margin
plot_h = (height - top) - 2*margin
s = min(plot_w/(x_max-x_min), plot_h/(y_max-y_min))   # 等比例, 保证圆是圆
ox = margin + (plot_w - s*(x_max-x_min))/2
oy = top + margin + (plot_h - s*(y_max-y_min))/2

def to_px(x, y):
    return ox + (x - x_min)*s, oy + (y_max - y)*s

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="26" text-anchor="middle" font-size="16" font-family="serif">
    方位角应用题：船由西向东航行，会触礁吗？
  </text>
  <text x="{width/2}" y="48" text-anchor="middle" font-size="12" fill="#666">
    A处测P北偏东60&#176;，行 AB=10 海里到 B 测P北偏东30&#176;，暗礁半径 8 海里
  </text>
'''

l1 = to_px(x_min+0.5, 0); l2 = to_px(x_max-0.5, 0)
svg += f'  <line x1="{l1[0]:.1f}" y1="{l1[1]:.1f}" x2="{l2[0]:.1f}" y2="{l2[1]:.1f}" stroke="#333" stroke-width="1.5"/>\n'
svg += f'  <polygon points="{l2[0]:.1f},{l2[1]:.1f} {l2[0]-10:.1f},{l2[1]-5:.1f} {l2[0]-10:.1f},{l2[1]+5:.1f}" fill="#333"/>\n'
svg += f'  <text x="{l2[0]-4:.1f}" y="{l2[1]+18:.1f}" font-size="12" fill="#333">向东航行</text>\n'

cp = []
for i in range(361):
    a = math.radians(i)
    cx, cy = to_px(P[0]+reef*math.cos(a), P[1]+reef*math.sin(a))
    cp.append(f"{cx:.1f},{cy:.1f}")
svg += f'  <polyline fill="#F44336" fill-opacity="0.06" stroke="#E53935" stroke-width="1.4" stroke-dasharray="4 3" points="{" ".join(cp)}"/>\n'
tx = to_px(P[0]-7.6, P[1])
svg += f'  <text x="{tx[0]:.1f}" y="{tx[1]:.1f}" font-size="11" fill="#E53935">暗礁区(半径8)</text>\n'

for pt, nm in [(A,"A"), (B,"B")]:
    bx, by = to_px(*pt)
    nt = to_px(pt[0], pt[1]+6.5)
    svg += f'  <line x1="{bx:.1f}" y1="{by:.1f}" x2="{nt[0]:.1f}" y2="{nt[1]:.1f}" stroke="#888" stroke-width="1" stroke-dasharray="4 3"/>\n'
    svg += f'  <text x="{nt[0]-4:.1f}" y="{nt[1]-4:.1f}" font-size="11" fill="#666">北</text>\n'
    svg += f'  <circle cx="{bx:.1f}" cy="{by:.1f}" r="4.5" fill="#000"/>\n'
    svg += f'  <text x="{bx-4:.1f}" y="{by+18:.1f}" font-size="13">{nm}</text>\n'

apx, apy = to_px(*A); ppx, ppy = to_px(*P); bpx, bpy = to_px(*B)
svg += f'  <line x1="{apx:.1f}" y1="{apy:.1f}" x2="{ppx:.1f}" y2="{ppy:.1f}" stroke="#1565C0" stroke-width="1.6"/>\n'
svg += f'  <line x1="{bpx:.1f}" y1="{bpy:.1f}" x2="{ppx:.1f}" y2="{ppy:.1f}" stroke="#2E7D32" stroke-width="1.6"/>\n'

def arc(pt, deg, R, col):
    cx, cy = to_px(*pt)
    p0 = (cx, cy - R)
    a = math.radians(deg)
    p1 = (cx + R*math.sin(a), cy - R*math.cos(a))
    path = f'  <path d="M {p0[0]:.1f} {p0[1]:.1f} A {R} {R} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="{col}" stroke-width="1.4"/>\n'
    lab = (cx + (R+10)*math.sin(math.radians(deg/2)), cy - (R+10)*math.cos(math.radians(deg/2)))
    return path, lab
a1, l1p = arc(A, 60, 34, "#1565C0")
svg += a1 + f'  <text x="{l1p[0]-6:.1f}" y="{l1p[1]:.1f}" font-size="11" fill="#1565C0">60&#176;</text>\n'
a2, l2p = arc(B, 30, 30, "#2E7D32")
svg += a2 + f'  <text x="{l2p[0]-4:.1f}" y="{l2p[1]:.1f}" font-size="11" fill="#2E7D32">30&#176;</text>\n'

svg += f'  <circle cx="{ppx:.1f}" cy="{ppy:.1f}" r="5" fill="#9C27B0"/>\n'
svg += f'  <text x="{ppx+8:.1f}" y="{ppy-4:.1f}" font-size="13" fill="#7B1FA2">P (小岛)</text>\n'

dpx, dpy = to_px(*D)
svg += f'  <line x1="{ppx:.1f}" y1="{ppy:.1f}" x2="{dpx:.1f}" y2="{dpy:.1f}" stroke="#E65100" stroke-width="2" stroke-dasharray="5 3"/>\n'
svg += f'  <rect x="{dpx-12:.1f}" y="{dpy-12:.1f}" width="12" height="12" fill="none" stroke="#E65100" stroke-width="1"/>\n'
svg += f'  <circle cx="{dpx:.1f}" cy="{dpy:.1f}" r="3.5" fill="#E65100"/>\n'
svg += f'  <text x="{dpx-2:.1f}" y="{dpy+18:.1f}" font-size="12" fill="#E65100">D</text>\n'
svg += f'  <text x="{ppx+8:.1f}" y="{(ppy+dpy)/2:.1f}" font-size="12" fill="#E65100">PD=5&#8730;3&#8776;8.66</text>\n'
svg += f'  <text x="{(apx+bpx)/2-16:.1f}" y="{apy+18:.1f}" font-size="11">AB=10</text>\n'

svg += f'''
  <rect x="{width-250}" y="{top+10}" width="232" height="104" fill="white" fill-opacity="0.93" stroke="#ccc" rx="4"/>
  <text x="{width-238}" y="{top+30}" font-size="11">&#8736;PAB = 90-60 = 30&#176;</text>
  <text x="{width-238}" y="{top+48}" font-size="11">&#8736;PBA = 180-(90-30) = 120&#176;</text>
  <text x="{width-238}" y="{top+66}" font-size="11">&#8736;APB = 30&#176; -&gt; 等腰 BP=AB=10</text>
  <text x="{width-238}" y="{top+84}" font-size="11">PD = BP&#183;sin60&#176; = 5&#8730;3 &#8776; 8.66</text>
  <text x="{width-238}" y="{top+102}" font-size="11" fill="#E53935">8.66 &gt; 8，不会触礁</text>
'''
svg += '</svg>\n'

with open('/projects/sandbox/bearing_reef.svg', 'w') as fp:
    fp.write(svg)

print("PD =", round(PD,4), "= 5*sqrt3 ~ 8.66")
print("BD =", BD, " (D 在 B 东侧)")
print("8.66 > 暗礁半径 8  ->  安全, 不会触礁")
