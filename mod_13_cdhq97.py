import unittest
from unittest.mock import patch
from io import StringIO
from stock_visualizer import main

class TestStockVisualizer(unittest.TestCase):

    def validate_input(self, symbol, chart_type, time_series, start_date, end_date):
        # Implement your validation logic here
        return True

    @patch('builtins.input', side_effect=['AAPL', 'line', '2', '2022-01-01', '2022-01-31'])
    def test_main_valid_input(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main(validator=self.validate_input)
            output = mock_stdout.getvalue().strip()
            self.assertIn('AAPL Prices from 2022-01-01 to 2022-01-31', output)
            self.assertNotIn('Invalid', output)

    @patch('builtins.input', side_effect=['AAPL', 'invalid_chart_type', '2', '2022-01-01', '2022-01-31'])
    def test_main_invalid_chart_type(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main(validator=self.validate_input)
            output = mock_stdout.getvalue().strip()
            self.assertIn('Invalid chart type. Please try again.', output)

    @patch('builtins.input', side_effect=['AAPL', 'line', 'invalid_time_series', '2022-01-01', '2022-01-31'])
    def test_main_invalid_time_series(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main(validator=self.validate_input)
            output = mock_stdout.getvalue().strip()
            self.assertIn('Enter the number:', output)
            self.assertIn('Invalid chart type. Please try again.', output)

    @patch('builtins.input', side_effect=['AAPL', 'line', '2', '2022-01-31', '2022-01-01'])
    def test_main_invalid_date_range(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main(validator=self.validate_input)
            output = mock_stdout.getvalue().strip()
            self.assertIn('Invalid date range. Please try again.', output)

if __name__ == '__main__':
    unittest.main()
