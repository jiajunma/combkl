#!/usr/bin/env python3
"""Independent finite sanity checks, not a verification of the sheaf proof.

KLV input: Abdallah--Hultman, arXiv:1612.07133, Proposition 2.7
and equation (2). Only (SL(2n), Sp(2n)), trivial local systems.
Polynomial tuples store coefficients in increasing powers of q.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from functools import lru_cache
import json
from pathlib import Path

Poly = tuple[int, ...]
ZERO: Poly = ()
ONE: Poly = (1,)

def trim(a) -> Poly:
    a=list(a)
    while a and a[-1]==0: a.pop()
    return tuple(a)
def add(a: Poly, b: Poly) -> Poly:
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a: Poly) -> Poly: return tuple(-x for x in a)
def shift(a: Poly, n: int = 1) -> Poly: return (0,)*n+a if a else ZERO
def mul(a: Poly, b: Poly) -> Poly:
    if not a or not b: return ZERO
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return trim(r)
def polystr(a):
    return ' + '.join(str(c) if i==0 else f'{c}*q^{i}' for i,c in enumerate(a) if c) or '0'

def check_dihedral(max_m: int = 18, infinite_cutoff: int = 18) -> dict:
    cases=0
    for m in list(range(2,max_m+1))+[None]:
        vertices=list(range(-m+1,m+1)) if m else list(range(-infinite_cutoff,infinite_cutoff+1))
        def le(a,b): return a==b or abs(a)<abs(b)
        def edge(a,b): return abs(a)<abs(b) and (a-b)%2==1
        def key(a,b):
            v=a+b
            return v%(2*m) if m else (0 if v>0 else 1,v)
        for x in vertices:
            for c in vertices:
                if not le(x,c): continue
                iv=[a for a in vertices if le(x,a) and le(a,c)]
                for y in iv:
                    if not edge(x,y): continue
                    k=(abs(y)-abs(x)-1)//2
                    for reverse in (False,True):
                        later=lambda a,b: key(a,b)<key(x,y) if reverse else key(a,b)>key(x,y)
                        hx=sum(edge(x,z) and later(x,z) for z in iv)
                        hy=sum(edge(y,z) and later(y,z) for z in iv)
                        assert hx-hy==k,(m,x,y,c,reverse,hx,hy,k)
                        cases+=1
    return {'finite_dihedral_m':[2,max_m], 'infinite_dihedral_absolute_length_bound':infinite_cutoff,'edge_top_order_cases':cases,'failures':0}

def compose(a,b): return tuple(a[i] for i in b)
def fpf_involutions(n):
    def match(rest,p):
        if not rest:
            yield tuple(p);return
        a=rest[0]
        for b in rest[1:]:
            p[a]=b;p[b]=a
            yield from match([i for i in rest if i!=a and i!=b],p)
    return list(match(list(range(n)),list(range(n))))
def inversions(w): return sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))

class SymplecticKLV:
    def __init__(self, n: int):
        if n<2 or n%2: raise ValueError('n must be positive even, at least 2')
        self.n=n; self.w0=tuple(reversed(range(n)))
        self.vertices=sorted((compose(self.w0,p) for p in fpf_involutions(n)),key=lambda w:(inversions(w),w))
        self.rank={w:inversions(w)//2 for w in self.vertices}
        self.set=set(self.vertices)
        self.prefix={w:[tuple(sorted(w[:k])) for k in range(1,n+1)] for w in self.vertices}
        self.lower={w:[u for u in self.vertices if self.le(u,w)] for w in self.vertices}
    @lru_cache(None)
    def le(self,u,w):
        if u==w:return True
        if self.rank[u]>=self.rank[w]:return False
        return all(all(a<=b for a,b in zip(x,y)) for x,y in zip(self.prefix[u],self.prefix[w]))
    def star(self,w,i):
        # w * s_i = theta(s_i) w s_i; zero-based i and values.
        a=list(w);a[i],a[i+1]=a[i+1],a[i]
        j=self.n-2-i
        return tuple(j+1 if v==j else j if v==j+1 else v for v in a)
    @lru_cache(None)
    def Q(self,u,w):
        if not self.le(u,w): return ZERO
        if u==w:return ONE
        i=next(i for i in range(self.n-1) if w[i]>w[i+1])
        us,ws=self.star(u,i),self.star(w,i)
        assert us in self.set and ws in self.set
        assert self.rank[ws]==self.rank[w]-1
        if self.rank[us]<self.rank[u]:return self.Q(us,ws)
        if us==u:return shift(self.Q(u,ws))
        assert self.rank[us]==self.rank[u]+1
        return add(shift(self.Q(us,ws)),mul((-1,1),self.Q(u,ws)))
    @lru_cache(None)
    def P(self,u,w):
        if not self.le(u,w):return ZERO
        if u==w:return ONE
        d=self.rank[w]-self.rank[u]
        rhs=ZERO
        for z in self.lower[w]:
            if z!=u and self.le(u,z):rhs=add(rhs,mul(self.Q(u,z),self.P(z,w)))
        p=trim([-rhs[k] if k<len(rhs) else 0 for k in range((d+1)//2)])
        reciprocal=[0]*(d+1)
        for k,c in enumerate(p):reciprocal[d-k]=c
        assert add(trim(reciprocal),neg(p))==rhs,('reciprocity',u,w,rhs,p)
        assert all(c>=0 for c in p),('positivity',u,w,p)
        return p
    def validate_Q_all_descents(self):
        cases=0
        for w in self.vertices:
            for u in self.lower[w]:
                if u==w:continue
                for i in range(self.n-1):
                    if w[i]<w[i+1]:continue
                    us,ws=self.star(u,i),self.star(w,i)
                    if self.rank[us]<self.rank[u]:ans=self.Q(us,ws)
                    elif us==u:ans=shift(self.Q(u,ws))
                    else:ans=add(shift(self.Q(us,ws)),mul((-1,1),self.Q(u,ws)))
                    assert ans==self.Q(u,w),('descent',u,w,i)
                    cases+=1
        return cases
    def scan_intervals(self):
        import networkx as nx
        classes=defaultdict(list)
        count=0; iso_tests=0; counterexamples=[];nontrivial=0
        for w in self.vertices:
            for u in self.lower[w]:
                iv=[z for z in self.lower[w] if self.le(u,z)]
                d=self.rank[w]-self.rank[u]
                p=self.P(u,w);nontrivial+=int(len(p)>1)
                ranks=defaultdict(list)
                for z in iv:ranks[self.rank[z]-self.rank[u]].append(z)
                # These twisted-identity intervals are graded by rank=length/2.
                edges=[(a,b) for k in range(d) for a in ranks[k] for b in ranks[k+1] if self.le(a,b)]
                g=nx.DiGraph();g.add_nodes_from(range(len(iv)))
                idx={z:i for i,z in enumerate(iv)}
                g.add_edges_from((idx[a],idx[b]) for a,b in edges)
                for z in iv:g.nodes[idx[z]]['rank']=self.rank[z]-self.rank[u]
                key=(d,tuple(len(ranks[k]) for k in range(d+1)),
                     tuple(sorted((g.nodes[v]['rank'],g.in_degree(v),g.out_degree(v)) for v in g)))
                matched=False
                for old in classes[key]:
                    iso_tests+=1
                    if nx.is_isomorphic(g,old['graph'],node_match=lambda a,b:a['rank']==b['rank']):
                        matched=True
                        if p!=old['p']:
                            counterexamples.append({'pair1':[list(old['u']),list(old['w'])], 'pair2':[list(u),list(w)],'p1':old['p'],'p2':p,'rank':d})
                        break
                if not matched:classes[key].append({'graph':g,'p':p,'u':u,'w':w})
                count+=1
        return {'degree_n':self.n,'number_of_parameters':len(self.vertices),'intervals_including_singletons':count,'nonconstant_polynomial_intervals':nontrivial,'poset_isomorphism_classes':sum(map(len,classes.values())),'exact_isomorphism_tests':iso_tests,'counterexamples':counterexamples}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-even-degree',type=int,default=8);ap.add_argument('--output',type=Path,default=Path('results/checks.json'));args=ap.parse_args()
    if args.max_even_degree < 4 or args.max_even_degree % 2:
        ap.error('--max-even-degree must be an even integer at least 4')
    if not __debug__:
        ap.error('Do not run with -O: the checks use assertions')
    out={'warning':'Finite sanity checks only; no full BMP/sheaf proof verification and no general KLV theorem.','dihedral_later_edge_check':check_dihedral(),'symplectic_klv':[]}
    for n in range(4,args.max_even_degree+1,2):
        m=SymplecticKLV(n);r=m.scan_intervals();r['all_descent_checks']=m.validate_Q_all_descents();out['symplectic_klv'].append(r)
        print(json.dumps(r),flush=True)
        if n==4:
            u,v,w=m.vertices
            out['SL4_Sp4_three_element_chain']={'twisted_identity_parameters_one_based':[[x+1 for x in z] for z in m.vertices], 'ranks':[m.rank[z] for z in m.vertices],'Q_bottom_middle':m.Q(u,v),'Q_middle_top':m.Q(v,w),'Q_bottom_top':m.Q(u,w),'P_bottom_top':m.P(u,w)}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
    print('Wrote',args.output)
if __name__=='__main__':main()
