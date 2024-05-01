all: build/v203.pdf

build/v203.pdf: v203.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v206.tex
	lualatex  --output-directory=build v206.tex
	biber build/v206.bcf
	lualatex  --output-directory=build v206.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
