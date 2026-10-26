CS=2530000; CAP=CS*20
LTTV={1:5310000,2:4730000,3:4140000,4:3700000}
BR=[(10e6,.05),(30e6,.10),(60e6,.20),(100e6,.30),(float('inf'),.35)]
OLD=[(5e6,.05),(10e6,.10),(18e6,.15),(32e6,.20),(52e6,.25),(80e6,.30),(float('inf'),.35)]
def tax(t,br=BR):
    s=0;prev=0
    for lim,r in br:
        if t>prev: s+=(min(t,lim)-prev)*r
        prev=lim
    return round(s)
def g2n(g,dep=0,reg=1,ins=None,old=False):
    ins=g if ins is None else ins
    b1=min(ins,CAP); b2=min(ins,LTTV[reg]*20)
    bhxh=b1*.08;bhyt=b1*.015;bhtn=b2*.01;bh=bhxh+bhyt+bhtn
    ded=(11e6+4.4e6*dep) if old else (15.5e6+6.2e6*dep)
    tx=max(0,g-bh-ded); t=tax(tx,OLD if old else BR)
    co=b1*.215 - b1*.01 + b2*.01  # 14+3+.5+3 on b1, 1 on b2
    return dict(g=g,bhxh=bhxh,bhyt=bhyt,bhtn=bhtn,bh=bh,ded=ded,taxable=tx,tax=t,net=g-bh-t,co=g+co,coins=co)
if __name__=='__main__':
    for g,d in [(10e6,0),(15e6,0),(20e6,0),(20e6,1),(30e6,0),(30e6,2),(50e6,0),(60e6,1)]:
        a=g2n(g,d);o=g2n(g,d,old=True)
        print(int(g),d,{k:int(v) for k,v in a.items()},'old tax',o['tax'])
