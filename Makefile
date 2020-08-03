report: report.tex plot.pdf
	latexmk -pdf

plot.pdf: data/schools.csv data/students.csv final.py
	python3 final.py

data/schools.csv:
		cd data && wget https://raw.githubusercontent.com/srivankit/py-school-match-data/master/schools.csv

data/students.csv:
		cd data && wget https://raw.githubusercontent.com/srivankit/py-school-match-data/master/students.csv

.PHONY: clean almost_clean

clean: almost_clean
	rm report.pdf
	rm plot.pdf

almost_clean:
	latexmk -c
