#!/usr/bin/env bash
set -e
python experiments/run_benchmarks.py
python experiments/run_separation.py
python experiments/run_threshold_sweep.py
python experiments/run_application_demo.py
python experiments/run_communication_application.py
python experiments/export_dynmatch.py
python artifacts/generate_artifacts.py
python artifacts/merge_external_results.py
echo "Core DMRC suite complete. External DynMatch results are added by experiments/run_dynmatch_external.py when CHSZLabLib is installed."
