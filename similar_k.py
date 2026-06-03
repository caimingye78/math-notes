import math

# 三角形 ABC, DE // BC, D 在 AB 上, E 在 AC 上, AD:DB = 2:3
# 用设 k 法: 设 AD=2k, DB=3k => AD:AB = 2:5
A = (2.0, 5.0)
B = (0.0, 0.0)
C = (6.0, 0.0)
r = 2.0/5.0   # AD:AB
D = (A[0] + r*(B[0]-A[0]), A[1] + r*(B[1]-A[1]))   # (1.2, 3)
E = (A[0] + r*(C[0]-A[0]), A[1] + r*(C[1]-A[1]))   # (3.6, 3)

width, height = 720, 560
margin = 70
# 直接用一个简单的世界->像素映射 (x右, y上)
x_min, x_max = -1.0, 7.0
y_min, y_max = -1.0, 6.0
plot_w = width - 2*margin
plot_h = height - 2*margin

def to_px(x, y):
    px = margin + (x - x_min)/(x_max - x_min)*plot_w
    py = margin + (y_max - y)/(y_max - y_min)*plot_h
    return px, py

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="white"/>
  <text x="{width/2}" y="28" text-anchor="middle" font-size="16" font-family="serif">
    设 k 法：DE // BC, AD:DB=2:3，求 &#9651;ADE 与梯形 DBCE 面积比
  </text>
'''

# 大三角形 ABC
apx, apy = to_px(*A)
bpx, bpy = to_px(*B)
cpx, cpy = to_px(*C)
svg += f'  <polygon points="{apx:.1f},{apy:.1f} {bpx:.1f},{bpy:.1f} {cpx:.1f},{cpy:.1f}" fill="#90CAF9" fill-opacity="0.25" stroke="#1565C0" stroke-width="2"/>\n'

# 小三角形 ADE
dpx, dpy = to_px(*D)
epx, epy = to_px(*E)
svg += f'  <polygon points="{apx:.1f},{apy:.1f} {dpx:.1f},{dpy:.1f} {epx:.1f},{epy:.1f}" fill="#A5D6A7" fill-opacity="0.7" stroke="#2E7D32" stroke-width="2"/>\n'

# DE 线
svg += f'  <line x1="{dpx:.1f}" y1="{dpy:.1f}" x2="{epx:.1f}" y2="{epy:.1f}" stroke="#2E7D32" stroke-width="2"/>\n'

# 顶点标注
for (pt, name, dx, dy) in [
    (A, "A", -6, -8),
    (B, "B", -16, 6),
    (C, "C", 8, 6),
    (D, "D", -20, 4),
    (E, "E", 8, 4),
]:
    cx, cy = to_px(*pt)
    svg += f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="#333"/>\n'
    svg += f'  <text x="{cx+dx:.1f}" y="{cy+dy:.1f}" font-size="13" font-family="serif">{name}</text>\n'

# 边上比例标注
# AD 段 (A->D) 标 2k, DB 段 (D->B) 标 3k
adm = ((apx+dpx)/2, (apy+dpy)/2)
dbm = ((dpx+bpx)/2, (dpy+bpy)/2)
svg += f'  <text x="{adm[0]-28:.1f}" y="{adm[1]:.1f}" font-size="12" fill="#C62828">AD=2k</text>\n'
svg += f'  <text x="{dbm[0]-30:.1f}" y="{dbm[1]:.1f}" font-size="12" fill="#C62828">DB=3k</text>\n'

# 说明框
svg += f'''
  <rect x="{width-300}" y="{margin+10}" width="270" height="118" fill="white" stroke="#ccc" rx="4"/>
  <text x="{width-288}" y="{margin+32}" font-size="12">设 AD=2k, DB=3k，则 AB=5k</text>
  <text x="{width-288}" y="{margin+54}" font-size="12">DE//BC =&gt; &#9651;ADE &#8764; &#9651;ABC</text>
  <text x="{width-288}" y="{margin+76}" font-size="12">相似比 = AD:AB = 2:5</text>
  <text x="{width-288}" y="{margin+98}" font-size="12">面积比 = (2:5)&#178; = 4:25</text>
  <text x="{width-288}" y="{margin+120}" font-size="12">&#9651;ADE : 梯形 = 4 : (25-4) = 4:21</text>
'''
svg += '</svg>\n'

with open('/projects/sandbox/similar_k.svg', 'w') as fp:
    fp.write(svg)
print("已生成 similar_k.svg")
print("AD:AB=2:5 -> 面积比 ADE:ABC = 4:25 -> ADE:梯形 = 4:21")
