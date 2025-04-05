import unittest
from visualizations.custom.custom_viz import CustomViz
from visualizations.charts.chart_definitions import ChartDefinitions

class TestVisualizations(unittest.TestCase):

    def setUp(self):
        self.custom_viz = CustomViz()
        self.chart_definitions = ChartDefinitions()

    def test_custom_viz_initialization(self):
        self.assertIsInstance(self.custom_viz, CustomViz)

    def test_chart_definitions_loading(self):
        self.assertIsNotNone(self.chart_definitions.load_definitions())

    def test_custom_viz_rendering(self):
        result = self.custom_viz.render(data={"key": "value"})
        self.assertIn("rendered_output", result)

    def test_chart_definition_structure(self):
        definitions = self.chart_definitions.load_definitions()
        for definition in definitions:
            self.assertIn("type", definition)
            self.assertIn("data", definition)

if __name__ == '__main__':
    unittest.main()