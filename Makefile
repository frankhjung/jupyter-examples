#!/usr/bin/env make

# Render a LaTeX document to PDF.
# Example:
#	make python.example.pdf

.PHONY: all clean
.SUFFIXES: .ipynb .tex .pdf
.DEFAULT: all

IPYNB	:= $(wildcard *.ipynb)
TEXS	:= $(patsubst %.ipynb, %.tex, $(IPYNB))
PDFS	:= $(patsubst %.tex, %.pdf, $(TEXS))

all: $(PDFS)

.ipynb.tex:
	-jupyter nbconvert --to=latex $<

.tex.pdf:
	-latexmk -f -gg -quiet -pdf \
		-interaction=nonstopmode -shell-escape \
		-pdflatex="pdflatex %O %S" $<

clean:
	-latexmk -quiet -f -c $(TEXS)
	@$(RM) -rf $(wildcard *_files)
ifneq ("$(TEXS)", "")
	@$(RM) $(patsubst %.tex, %.*.*, $(TEXS))
	@$(RM) $(TEXS)
endif
