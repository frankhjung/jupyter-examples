#!/usr/bin/env make

# Renders a Juypter Notebook to TeX.
# Then converts the LaTeX document to PDF.

.DEFAULT:	html
.PHONY:		html pdf clean
.SUFFIXES:	.ipynb .tex .pdf .html

IPYNB	:= $(wildcard *.ipynb)
TEXS	:= $(patsubst %.ipynb, %.tex, $(IPYNB))
HTMLS	:= $(patsubst %.tex, %.html, $(TEXS))
PDFS	:= $(patsubst %.tex, %.pdf, $(TEXS))

.ipynb.tex:
	-jupyter nbconvert --to=latex $<

.ipynb.html:
	-jupyter nbconvert --to=html $<

.tex.pdf:
	-latexmk -f -gg -quiet -pdf \
		-interaction=nonstopmode -shell-escape \
		-pdflatex="pdflatex %O %S" $<

html:	$(HTMLS)

pdf:	$(PDFS)

clean:
	latexmk -quiet -f -C $(TEXS)
	@$(RM) -f $(wildcard *_files)
	@$(RM) -f $(HTMLS)
ifneq ("$(TEXS)", "")
	@$(RM) -f $(patsubst %.tex, %.*.*, $(TEXS))
	@$(RM) -f $(TEXS)
endif
