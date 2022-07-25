"""This module contains utility dataclasses."""

from dataclasses import dataclass


@dataclass
class AnalyteEU:
    """dataclass for describing an experimental unit when investigating the effect of an analyte on a process.

    Args:
        analyte: Name of the analyte.
        concentration: Concentration of analyte.
        unit: Unit of concentration.
        id: Identify for experimental unit. Typically a well of a microtitre plate.

    """

    analyte: str
    concentration: float
    unit: str = "M"
    id: str = ""
