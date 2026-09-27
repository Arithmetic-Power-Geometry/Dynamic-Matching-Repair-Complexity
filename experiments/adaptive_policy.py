"""Compare adaptive debt indexing against scan on frozen streams.
Usage: import run_policy(...) from dataset-specific replay code.
"""
import statistics
def summarize(name,alg,per):
 s=sorted(per);q=lambda p:s[min(len(s)-1,int(p*(len(s)-1)))] if s else 0
 return dict(algorithm=name,total_work=sum(per),median_work=statistics.median(per) if per else 0,
             p95_work=q(.95),p99_work=q(.99),max_work=max(per) if per else 0,
             recourse=alg.metrics.recourse,matching_size=alg.matching_size(),
             maximal=int(alg.validate_invariants() if hasattr(alg,"validate_invariants") else alg.is_maximal()))
