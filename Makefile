report: report.tex plot.jpg pie.jpg
	latexmk  -pdf report.tex

plot.jpg: data/schools.csv data/students.csv final.py
	python3 final.py
data/schools.csv: mkdir.data
	cd data && wget -N https://raw.githubusercontent.com/srivankit/py-school-match-data/master/schools.csv

data/students.csv: mkdir.data
	cd data && wget -N https://raw.githubusercontent.com/srivankit/py-school-match-data/master/students.csv
mkdir.data:
	if [ ! -d "data" ]; then mkdir data ; fi

.PHONY: clean almost_clean

clean:
	latexmk -C
	rm *.jpg

almost_clean:
	latexmk -c
	rm *.jpg