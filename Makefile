cv.pdf: container-latex.sif cv.tex
	./container-latex.sif --no-home

container-latex.sif: container/apptainer.def
	apptainer build container-latex.sif container/apptainer.def
