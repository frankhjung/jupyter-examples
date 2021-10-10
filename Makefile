#!/usr/bin/env make

# Renders a Juypter Notebook to TeX.
# Then converts the LaTeX document to PDF.

.PHONY: html pdf clean
.SUFFIXES: .ipynb .tex .pdf
.DEFAULT: html

IPYNB	:= $(wildcard *.ipynb)
TEXS	:= $(patsubst %.ipynb, %.tex, $(IPYNB))
HTMLS	:= $(patsubst %.tex, %.html, $(TEXS))
PDFS	:= $(patsubst %.tex, %.pdf, $(TEXS))

.ipynb.tex:
	-jupyter nbconvert --to=latex $<

.tex.pdf:
	-latexmk -f -gg -quiet -pdf \
		-interaction=nonstopmode -shell-escape \
		-pdflatex="pdflatex %O %S" $<

html:	$(HTMLS)

pdf:	$(PDFS)

clean:
	-latexmk -quiet -f -c $(TEXS)
	@$(RM) -rf $(wildcard *_files)
ifneq ("$(TEXS)", "")
	@$(RM) $(patsubst %.tex, %.*.*, $(TEXS))
	@$(RM) $(TEXS)
endif
