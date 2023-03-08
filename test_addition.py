import pytest
from io import StringIO
import sys
from program import somme_deux_nombres

class TestSommeDeuxNombres(unittest.TestCase):

    def test_somme_deux_nombres(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        somme_deux_nombres(5, 7)
        expected_output = "La somme de 5 et 7 est 12\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output = StringIO()
        sys.stdout = captured_output

        somme_deux_nombres(-3, 8)
        expected_output = "La somme de -3 et 8 est 5\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output = StringIO()
        sys.stdout = captured_output

        somme_deux_nombres(0, 0)
        expected_output = "La somme de 0 et 0 est 0\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
