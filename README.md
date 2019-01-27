# Jupyter Notebooks

Some examples in Python and R.

## Notebooks

* [Python 3 - example 1](./python3-example-1.ipynb)
* [Python 3 - example 2](./python3-example-2.ipynb)
* [Python Widgets](./widgets-example.ipynb)
* [R - example 1](./r-example-1.ipynb)
* [R - example 2](./r-example-2.ipynb)

Compare this to R Markdown:

* [R - example 1](r-example-1.Rmd)

## Render Jupyter Notebook as PDF

The method used here is to render a PDF from LaTeX. The [Makefile](./Makefile)
describes how this is done. Call [make](https://www.gnu.org/software/make/)
with:

```bash
make python3-example-1.pdf
make python3-example-2.pdf
```

## Google Colaboratory

[Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb) is a
free online Jupyter notebook environment. It runs entirely in the cloud, so is a
good external test for your notebooks. It also integrates with documents on
Google Drive. See [here](https://github.com/burnash/gspread) for an example on
how to read from a spreadsheet.

## Examples

Find many interesting examples of notebooks from
[this](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#pandas-for-data-analysis)
page.

## References

* [Jupyter Notebook](http://jupyter.org/)
* [matplotlib](https://matplotlib.org/)
* [pandas](https://pandas.pydata.org/)
* [scikit-learn](http://scikit-learn.org/)
