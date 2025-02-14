from numpy import median
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------------------------
data = sns.load_dataset("mpg")
sns.set_style("darkgrid")
sns.lineplot(x='model_year', y='horsepower', hue="origin", data=data)
# sns.axes_style()
# {'axes.facecolor': '#EAEAF2',
#  'axes.edgecolor': 'white',
#  'axes.grid': True,
#  'axes.axisbelow': True,
#  'axes.labelcolor': '.15',
#  'figure.facecolor': 'white',
#  'grid.color': 'white',
#  'grid.linestyle': '-',
#  'text.color': '.15',
#  'xtick.color': '.15',
#  'ytick.color': '.15',
#  'xtick.direction': 'out',
#  'ytick.direction': 'out',
#  'lines.solid_capstyle': 'round',
#  'patch.edgecolor': 'w',
#  'patch.force_edgecolor': True,
#  'image.cmap': 'rocket',
#  'font.family': ['sans-serif'],
#  'font.sans-serif': ['Arial',
#                      'DejaVu Sans',
#                      'Liberation Sans',
#                      'Bitstream Vera Sans',
#                      'sans-serif'],
#  'xtick.bottom': False,
#  'xtick.top': False,
#  'ytick.left': False,
#  'ytick.right': False,
#  'axes.spines.left': True,
#  'axes.spines.bottom': True,
#  'axes.spines.right': True,
#  'axes.spines.top': True}

# plt.title("Візуальне оформлення графіків")
# plt.show()
# ----------------------------------------------------------------
sns.set_style("darkgrid")
sns.set_context("talk")  # параметр з набору: paper, notebook, talk, poster.
sns.axes_style()  # це або свій словник з параметрами, або ім'я стилю із заданого набору: darkgrid, whitegrid, dark, white, ticks
sns.scatterplot(x='mpg', y='displacement', data=data)

plt.title("Візуальне оформлення графіків")
plt.show()
# ----------------------------------------------------------------
sns.palplot(sns.color_palette())
plt.show()
# ----------------------------------------------------------------

