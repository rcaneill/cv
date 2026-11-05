cv.pdf: container-latex.sif cv.tex publications.bib
	./container-latex.sif --no-home

container-latex.sif: container/apptainer.def
	apptainer build container-latex.sif container/apptainer.def
