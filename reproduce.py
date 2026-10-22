#!/usr/bin/env python3
"""Reproduce every published finite check offline, using Python 3.10+ only.

Run from any directory: python path/to/reproduce.py
Writes results/verification.json and results/denominator_comparison.json.
Failures are recorded when possible and produce a nonzero exit status.
Finite computations do not replace the general proof or establish novelty.
"""

from datetime import datetime, timezone
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
from time import perf_counter
import traceback


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=None,
                        help="result directory (default: results/ beside this script)")
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        print("Python 3.10 or later is required.", file=sys.stderr)
        return 1
    root = Path(__file__).resolve().parent
    code_path = root / "code" / "finite_checks.py"
    spec = importlib.util.spec_from_file_location("plethysm_finite_checks", code_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    results = args.output_dir.resolve() if args.output_dir is not None else root / "results"
    results.mkdir(parents=True, exist_ok=True)
    started = perf_counter()
    report = {
        "schema_version": 1,
        "command": ("python reproduce.py --output-dir <chosen directory>"
                    if args.output_dir is not None else "python reproduce.py"),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "dependencies": "Python standard library only; no network access",
        "code_sha256": {
            relative: hashlib.sha256((root / relative).read_bytes()).hexdigest()
            for relative in ("reproduce.py", "code/finite_checks.py")
        },
        "limitations": [
            "Finite checks do not prove the infinite theorem.",
            "Passing these checks does not establish novelty or priority.",
            "The general positive combinatorial plethysm problem remains open.",
            "Denominator, recurrence-order and quasiperiod values are upper bounds.",
            "Elapsed time below is reproduction metadata, not a performance comparison.",
        ],
        "checks": {},
    }
    tasks = [
        ("hook_divisibility", module.hook_divisibility),
        ("half_difference", module.half_difference),
        ("ssyt_coefficients", module.ssyt_coefficients),
        ("odd_mu3_example", module.odd_mu3_example),
        ("denominator_comparison", module.denominator_comparison),
        ("ssyt_series_cross_checks", module.ssyt_series_cross_checks),
        ("denominator_specializations", module.denominator_specializations),
    ]
    for name, check_function in tasks:
        try:
            report["checks"][name] = check_function()
            status = "passed" if report["checks"][name]["passed"] else "FAILED"
            print(f"{name}: {status}", flush=True)
        except Exception as error:
            report["checks"][name] = {
                "passed": False, "error_type": type(error).__name__,
                "error": str(error),
            }
            print(f"{name}: FAILED ({type(error).__name__}: {error})", file=sys.stderr)
            traceback.print_exc()

    expected_counts = [
        ("hook_divisibility", "partitions_checked", 680),
        ("hook_divisibility", "partition_divisor_pairs_checked", 6542),
        ("half_difference", "identities_checked", 98),
        ("ssyt_coefficients", "partitions_checked", 41),
        ("ssyt_coefficients", "specializations", 246),
        ("ssyt_coefficients", "coefficient_comparisons", 3771),
        ("ssyt_coefficients", "tableau_instances", 33707),
        ("denominator_comparison", "comparisons_checked", 4),
        ("ssyt_series_cross_checks", "comparisons", 174),
    ]
    count_checks = []
    for name, key, expected in expected_counts:
        actual = report["checks"][name].get(key)
        count_checks.append({"check": name, "field": key, "expected": expected,
                             "actual": actual, "passed": actual == expected})
    specialization_counts = report["checks"]["denominator_specializations"].get("counts", {})
    for mode, expected in (("exact_integer_specialization", 382),
                           ("modular_screening", 504)):
        actual = specialization_counts.get(mode)
        count_checks.append({"check": "denominator_specializations", "field": mode,
                             "expected": expected, "actual": actual,
                             "passed": actual == expected})
    report["expected_count_checks"] = count_checks
    report["all_passed"] = (all(check["passed"] for check in report["checks"].values())
                            and all(check["passed"] for check in count_checks))
    report["elapsed_seconds"] = round(perf_counter() - started, 3)
    comparison = report["checks"]["denominator_comparison"]
    (results / "denominator_comparison.json").write_text(
        json.dumps(comparison, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (results / "verification.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"all_passed": report["all_passed"],
                      "elapsed_seconds": report["elapsed_seconds"],
                      "result_file": "verification.json"}, indent=2))
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
