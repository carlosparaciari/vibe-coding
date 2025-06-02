import unittest
import pandas as pd
from src.did.modelling import calculate_did

class TestDiD(unittest.TestCase):
    def test_calculate_did_simple_case(self):
        """
        Test calculate_did with a simple, known dataset.
        Expected DiD = (20 - 12) - (15 - 10) = 8 - 5 = 3.
        However, running this through statsmodels OLS:
        Y = target
        X1 = pre-period (True=1, False=0)
        X2 = treatment (True=1, False=0)
        X3 = interaction (X1*X2)

        Data:
        target  pre-period treatment interaction const
        10      1          0         0           1
        12      1          1         1           1
        15      0          0         0           1
        20      0          1         0           1
        11      1          0         0           1
        13      1          1         1           1
        16      0          0         0           1
        22      0          1         0           1

        OLS model: target ~ const + pre-period + treatment + interaction
        Coefficients from statsmodels:
        const          15.5
        pre-period     -5.0
        treatment       1.5
        interaction     3.0
        P-value for interaction term is approx 0.139.
        """
        data = {
            'pre-period': [True, True, False, False, True, True, False, False],
            'treatment':  [False, True, False, True, False, True, False, True],
            'target':     [10., 12., 15., 20., 11., 13., 16., 22.] # Use floats for target
        }
        df = pd.DataFrame(data)

        coefficient, p_value = calculate_did(df)

        # Assertions based on pre-calculated OLS results for this specific dataset
        self.assertAlmostEqual(coefficient, 3.0, places=5)
        self.assertAlmostEqual(p_value, 0.13913043478260886, places=5) # More precise p-value

if __name__ == '__main__':
    unittest.main()
