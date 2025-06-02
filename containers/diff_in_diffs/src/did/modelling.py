import pandas as pd
import statsmodels.api as sm

def calculate_did(df: pd.DataFrame) -> tuple[float, float]:
    """
    Calculates the Difference-in-Differences (DiD) estimate.

    Args:
        df: A pandas DataFrame with columns 'pre-period' (boolean),
            'treatment' (boolean), and 'target' (float).

    Returns:
        A tuple containing the coefficient and p-value for the interaction term.
    """
    # Create interaction term
    df['interaction'] = df['pre-period'].astype(int) * df['treatment'].astype(int)

    # Define independent variables (add constant for intercept)
    X = df[['pre-period', 'treatment', 'interaction']]
    X = sm.add_constant(X)

    # Define dependent variable
    Y = df['target']

    # Run OLS regression
    model = sm.OLS(Y, X)
    results = model.fit()

    # Get coefficient and p-value for the interaction term
    coefficient = results.params['interaction']
    p_value = results.pvalues['interaction']

    return coefficient, p_value
