"""Exact axis-aligned rectangular-cell surface exporter; no CAD engine required.
Default dimensions mirror slide-tray.scad. For changed SCAD parameters export
using OpenSCAD instead; these exports are only the documented default design.
"""
from pathlib import Path
from collections import Counter
import json
R=Path(__file__).resolve().parent

def make(name,xs,ys,zs,inside):
    occupied=set()
    for i in range(len(xs)-1):
        for j in range(len(ys)-1):
            for k in range(len(zs)-1):
                if inside((xs[i]+xs[i+1])/2,(ys[j]+ys[j+1])/2,(zs[k]+zs[k+1])/2):occupied.add((i,j,k))
    tris=[]
    for i,j,k in occupied:
        a,b=xs[i:i+2];c,d=ys[j:j+2];e,f=zs[k:k+2]
        faces=[((-1,0,0),[(a,c,e),(a,c,f),(a,d,f),(a,d,e)]),((1,0,0),[(b,c,e),(b,d,e),(b,d,f),(b,c,f)]),((0,-1,0),[(a,c,e),(b,c,e),(b,c,f),(a,c,f)]),((0,1,0),[(a,d,e),(a,d,f),(b,d,f),(b,d,e)]),((0,0,-1),[(a,c,e),(a,d,e),(b,d,e),(b,c,e)]),((0,0,1),[(a,c,f),(b,c,f),(b,d,f),(a,d,f)])]
        for (di,dj,dk),v in faces:
            if (i+di,j+dj,k+dk) not in occupied:
                tris.extend([(v[0],v[1],v[2]),(v[0],v[2],v[3])])
    edges=Counter();directed=Counter();volume=0;lines=[f'solid {name}']
    for p,q,r in tris:
        u=[q[n]-p[n] for n in range(3)];v=[r[n]-p[n] for n in range(3)]
        n=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]
        mag=sum(t*t for t in n)**.5;assert mag>0
        normal=[t/mag for t in n]
        volume+=sum(p[t]*[q[1]*r[2]-q[2]*r[1],q[2]*r[0]-q[0]*r[2],q[0]*r[1]-q[1]*r[0]][t] for t in range(3))/6
        lines+=['facet normal '+' '.join(map(str,normal)),'outer loop']+['vertex '+' '.join(map(str,a)) for a in (p,q,r)]+['endloop','endfacet']
        for a,b in [(p,q),(q,r),(r,p)]:edges[tuple(sorted([a,b]))]+=1;directed[(a,b)]+=1
    assert all(v==2 for v in edges.values()),'Nonmanifold edges'
    assert all(directed[(b,a)]==v for (a,b),v in directed.items()),'Inconsistent normals'
    expected=sum((xs[i+1]-xs[i])*(ys[j+1]-ys[j])*(zs[k+1]-zs[k]) for i,j,k in occupied)
    assert abs(volume-expected)<1e-6
    lines.append(f'endsolid {name}');(R/f'{name}.stl').write_text('\n'.join(lines)+'\n')
    return dict(triangles=len(tris),closed_two_faces_per_edge=True,consistent_winding=True,volume_mm3=round(volume,6),bounds_mm=[[min(xs),min(ys),min(zs)],[max(xs),max(ys),max(zs)]])

def main():
    results={}
    results['tray']=make('tray',[-45,-37.7,-10,10,37.7,45],[-19,-12.7,-10,10,12.7,19],[0,2,4],lambda x,y,z:not(abs(x)<10 and abs(y)<10) and not(z>2 and abs(x)<37.7 and abs(y)<12.7))
    results['spacer']=make('spacer',[0,8],[0,8],[0,8],lambda x,y,z:True)
    results['mask']=make('mask',[0,5,25,30],[0,5,25,30],[0,1],lambda x,y,z:not(5<x<25 and 5<y<25))
    results['status']='geometry checked. still needs slicing, printing, and a real fit check.'
    (R/'validation.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
if __name__=='__main__':main()
