all: build/v47.pdf

build/v47.pdf: v47.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v47.tex
	lualatex  --output-directory=build v47.tex
	biber build/v47.bcf
	lualatex  --output-directory=build v47.tex

build/cv.pdf: cv.txt cv.py | build
	python cv.py

build/cv170.pdf: cv.txt cv170.py | build
	python cv170.py

build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
