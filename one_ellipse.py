import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The Axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
    
    # Calculate ellipse radii
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Scaling and translation based on the data
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

# Example use case for plotting raw data
def plot_data_with_ellipse(data):
    """
    Plot a scatter plot of raw data and a confidence ellipse.
    
    Parameters
    ----------
    data : numpy.ndarray, shape (n_samples, 2)
        Raw data with two columns for x and y values.
    """
    if data.shape[1] != 2:
        raise ValueError("Data must have exactly two columns (x and y).")
    
    x, y = data[:, 0], data[:, 1]
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Scatter plot of the raw data
    ax.scatter(x, y, s=1, alpha=0.5)

    # Add confidence ellipse
    confidence_ellipse(x, y, ax, edgecolor='red')

    # Add reference lines
    ax.axvline(c='grey', lw=1)
    ax.axhline(c='grey', lw=1)

    plt.show()

# Example raw data
np.random.seed(1)
raw_data = np.random.multivariate_normal([6 * np.random.rand() - 3, 6 * np.random.rand() - 3], [[6 * np.random.rand() - 3, 6 * np.random.rand() - 3], [6 * np.random.rand() - 3, 6 * np.random.rand() - 3]], size=1000)

plot_data_with_ellipse(raw_data)
