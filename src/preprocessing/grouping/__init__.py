#
# src/preprocessing/grouping/__init__.py
"""
grouping/__init__.py:

Importa todas las funciones necesarias de los archivos group_by_columns.py y aggregate_functions.py.
Define la lista __all__ para especificar qué funciones se exportan cuando se importa el módulo grouping.
"""

from .group_by_columns import group_by_column, group_by_multiple_columns
from .aggregate_functions import sum_aggregation, mean_aggregation, custom_aggregation

__all__ = [
    'group_by_column',
    'group_by_multiple_columns',
    'sum_aggregation',
    'mean_aggregation',
    'custom_aggregation'
]