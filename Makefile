report: report.tex plot.pdf
	latexmk -pdf report.tex

plot.pdf: data/schools.csv data/students.csv final.py
	python3 final.py

data/schools.csv: mkdir.data
		cd data && wget https://raw.githubusercontent.com/srivankit/py-school-match-data/master/schools.csv

data/students.csv: mkdir.data
		cd data && wget https://raw.githubusercontent.com/srivankit/py-school-match-data/master/students.csv

mkdir.data:
	if [ ! -d "data" ]; then mkdir data ; fi

.PHONY: clean almost_clean

clean: almost_clean
	rm report.pdf
	rm plot.pdf

almost_clean:
	latexmk -c
