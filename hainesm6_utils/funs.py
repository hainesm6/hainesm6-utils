"""This module contains utility functions"""

from pingouin import power_anova


def experimental_power(n_treatments: int, practical_diff: float, variance: float, replicates: int) -> float:
    """Estimates statistical power for an experiment determining the effect of a single treatment.

    Replicates that yield a power > 0.8 | 0.9 are considered sufficient.
    Refer to Design and Analysis of Experiments with R (Lawson, 2015).

    Args:
        n_treatment: Number of levels of the treatment.
        practical_diff: The difference in the effect that the experimenter wishes to detect.
        variance: Experimentally measured variance of the reference treatment.
        replicates: Number of replicates.

    Returns:
        Experimental power.

    """
    css = practical_diff ** 2 / 2
    non_central_param = replicates / variance * css
    eta_squared = non_central_param / (n_treatments * replicates + non_central_param)
    return power_anova(eta_squared=eta_squared, k=n_treatments, n=replicates)
