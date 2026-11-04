"""Unit tests for human-readable report helpers."""

import unittest

from annabell_beast.reporting import figure_block, format_count, latex_text


class ReportingTests(unittest.TestCase):
    def test_format_count_avoids_unneeded_decimal_places(self):
        self.assertEqual(format_count(12.0), "12")
        self.assertEqual(format_count(12.34), "12.3")

    def test_latex_text_escapes_underscores_in_algorithm_names(self):
        self.assertEqual(latex_text("bubble_early_exit"), r"bubble\_early\_exit")

    def test_figure_block_uses_fallback_for_missing_plot(self):
        latex = figure_block("out", "chart.png", "Example chart")

        self.assertIn("\\IfFileExists{out/chart.png}", latex)
        self.assertIn("(plot missing)", latex)
        self.assertIn("\\caption{Example chart}", latex)
