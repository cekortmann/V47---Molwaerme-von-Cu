all: build/v47.pdf

build/v47.pdf: v47.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v47.tex
	lualatex  --output-directory=build v47.tex
	biber build/v47.bcf
	lualatex  --output-directory=build v47.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
