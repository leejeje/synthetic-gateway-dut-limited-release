#!/usr/bin/env python3
"""Offline validation for manuscript-consistent aggregate CSVs.

This test uses only the Python standard library. It never contacts a DUT,
opens a network socket, or reads experiment.db/log files. It does not generate,
impute, simulate, bootstrap, or recompute scientific results; the constants
below are packaging-validation expectations derived from the accepted manuscript.
"""
from pathlib import Path
import csv

POLICIES = {
    "MAB+PPO", "Expert Chain", "MAB-Only", "PPO-Only",
    "DQN", "Round-Robin", "Random",
}
SEEDS = {42, 123, 456, 789, 2024, 7, 11, 19, 27, 31, 37, 41,
         43, 47, 53, 59, 61, 67, 71, 73}

def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def main():
    repo = Path(__file__).resolve().parents[1]
    data = repo / "data" / "manuscript_consistent"
    table = rows(data / "table_vii_primary_results.csv")
    require({r["Policy"] for r in table} == POLICIES, "Table VII policy set mismatch")
    require(len(table) == 7, "Table VII must have 7 policy rows")

    s1 = rows(data / "supplementary_s1_manuscript.csv")
    require({r["Policy"] for r in s1} == POLICIES, "Supplementary S1 policy set mismatch")
    require(len(s1) == 7, "Supplementary S1 must have 7 policy rows")

    s2 = rows(data / "supplementary_s2_manuscript.csv")
    require({r["Policy"] for r in s2} == POLICIES, "Supplementary S2 policy set mismatch")
    require(len(s2) == 7, "Supplementary S2 must have 7 policy rows")
    for r in s2:
        total = int(r["Total_Executable_Attempts"])
        successful = int(r["Successful_Attempts"])
        asr = float(r["ASR_pct"])
        require(total == 2000, f"S2 denominator is not 2000 for {r['Policy']}")
        require(0 <= successful <= total, f"S2 attempt bounds fail for {r['Policy']}")
        require(round(100 * successful / total, 1) == round(asr, 1),
                f"S2 ASR arithmetic mismatch for {r['Policy']}")

    appendix = rows(data / "appendix_seed_metrics_transcribed.csv")
    require(len(appendix) == 140, "Appendix must contain 140 data rows")
    require({r["Policy"] for r in appendix} == POLICIES, "Appendix policy set mismatch")
    for policy in POLICIES:
        subset = [r for r in appendix if r["Policy"] == policy]
        require(len(subset) == 20, f"Appendix row count is not 20 for {policy}")
        require({int(r["Seed"]) for r in subset} == SEEDS,
                f"Appendix seed set mismatch for {policy}")

    print("offline_smoke_test: PASS")
    print("checked: Table VII=7 rows; S1=7 rows; S2=7 rows/2000 aggregate denominator; Appendix=140 rows/20 seeds x 7 policies")
    print("network: not used; raw DB/log: not read")

if __name__ == "__main__":
    main()
