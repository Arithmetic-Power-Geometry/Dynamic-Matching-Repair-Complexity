"""Run established DynMatch algorithms through CHSZLabLib on DMRC update streams.

Install the frontend according to https://github.com/CHSZLab/CHSZLabLib.
This script intentionally fails with a clear message if the external dependency is absent.
"""
import argparse,csv,time,os

ALGOS=["naive","static_blossom","neiman_solomon","baswana_gupta_sen","random_walk","blossom"]

def read_stream(path):
    ops=[];n=0
    with open(path) as f:
        for line in f:
            if not line.strip(): continue
            if line.startswith("#"):
                parts=line.split();n=int(parts[1]);continue
            op,u,v=map(int,line.split());ops.append((op,u,v))
    return n,ops

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("stream")
    ap.add_argument("--algorithms",nargs="+",default=ALGOS)
    ap.add_argument("--out",default="results/dynmatch_external.csv")
    args=ap.parse_args()
    try:
        from chszlablib import DynamicProblems
    except Exception as e:
        raise SystemExit("CHSZLabLib/DynMatch Python frontend is not installed. Follow DYNMATCH_COMPARISON.md. Original error: "+str(e))
    n,ops=read_stream(args.stream);rows=[]
    for name in args.algorithms:
        solver=DynamicProblems.matching(n,algorithm=name)
        t=time.perf_counter()
        for op,u,v in ops:
            (solver.insert_edge if op==1 else solver.delete_edge)(u,v)
        elapsed=time.perf_counter()-t
        res=solver.get_current_solution()
        rows.append(dict(stream=os.path.basename(args.stream),algorithm="dynmatch_"+name,
                         vertices=n,operations=len(ops),time_s=elapsed,matching_size=res.matching_size))
    os.makedirs(os.path.dirname(args.out) or ".",exist_ok=True)
    exists=os.path.exists(args.out)
    with open(args.out,"a",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys())
        if not exists:w.writeheader()
        w.writerows(rows)
    print(*rows,sep="\n")
if __name__=="__main__":main()
