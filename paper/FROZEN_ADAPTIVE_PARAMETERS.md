# Frozen adaptive parameters

Selected **only** on repeated synthetic hub-repair training:
- build_factor alpha = 0.5
- retire_factor rho = 1.0

Selection criterion: minimum aggregate charged work across k={32,64,128,256}, 50 delete/reinsert rounds each. Retirement factors 1,2,4 tied at alpha=0.5 on this workload; rho=1 was frozen as the conservative earliest-retirement choice.

Training comparison:
- plain Scan aggregate work: 96,400
- Adaptive(alpha=.5,rho=1) aggregate work: 1,964
- ratio: 49.08x lower Adaptive cumulative work on this deliberately repeated hub workload.

This is training evidence only, not an external performance claim. Parameters must not be changed after observing Simple Wiki, CAIDA, or NL-Wiki results.
