"""Shared aggregation helpers for research reports."""
from collections import Counter


def site_value_prevalence(sites, section, key, transform=lambda value: value,
                          predicate=lambda value: True):
    """Count each retained value at most once per site.

    Report tuples contain declaration counts, but prevalence is a site-level
    metric. The counts are intentionally ignored here.
    """
    totals = Counter()
    for site in sites.values():
        values = set()
        for value, _declaration_count in site.get(section, {}).get(key, []):
            value = transform(value)
            if predicate(value):
                values.add(value)
        totals.update(values)
    return totals
