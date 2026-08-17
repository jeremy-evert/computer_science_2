"""Transparent repeated-run helpers for reasoning about stability.

This module deliberately stops at descriptive summaries. It preserves the raw
per-seed experiment receipts so courses can teach their own interpretation.
"""

from dataclasses import replace
from statistics import mean

from .experiment import run_experiment


SEED_BUNDLES = {
    # The integers have no statistical magic. The bundle name is the stable
    # classroom contract. Changing these seeds later requires a new bundle name.
    "classroom_v1": (17, 101, 6262, 2026, 4000),
    "quick_v1": (17, 6262, 2026),
}


def get_seed_bundle(name):
    try:
        return SEED_BUNDLES[name]
    except KeyError as exc:
        known = ", ".join(sorted(SEED_BUNDLES))
        raise ValueError(f"unknown seed bundle {name!r}; choose from {known}") from exc


def run_seed_bundle(config, bundle_name="classroom_v1"):
    """Run the same experiment configuration across a named seed bundle."""
    return [
        run_experiment(replace(config, seed=seed))
        for seed in get_seed_bundle(bundle_name)
    ]


def summarize_metric(results, metric="win_rate_difference_pp"):
    """Return an auditable descriptive summary for one numeric result field."""
    if not results:
        raise ValueError("results must not be empty")

    values = []
    for result in results:
        value = getattr(result, metric, None)
        if not isinstance(value, (int, float)):
            raise ValueError(f"metric {metric!r} is not a numeric ExperimentResult field")
        values.append(float(value))

    minimum = min(values)
    maximum = max(values)
    return {
        "metric": metric,
        "count": len(values),
        "mean": mean(values),
        "min": minimum,
        "max": maximum,
        "range": maximum - minimum,
        "values": values,
    }
