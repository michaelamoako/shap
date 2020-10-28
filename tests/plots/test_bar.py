''' This file contains tests for the bar plot.
'''
import matplotlib.pyplot as plt
import pytest
import shap

from .utils import explainer  # pytest fixture: do not remove


@pytest.mark.mpl_image_compare
def test_simple_bar(explainer):
    shap_values = explainer(explainer.data)
    fig = plt.figure()
    shap.plots.bar(shap_values, show=False)
    plt.tight_layout()
    return fig
