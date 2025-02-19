all: cover_letter_romain_caneill.pdf cv_romain_caneill.pdf

cover_letter_romain_caneill.pdf: cv.pdf
	qpdf cv.pdf --pages . 1 -- $@

cv_romain_caneill.pdf: cv.pdf
	qpdf cv.pdf --pages . 2-z -- $@

cv.pdf: container-latex.sif cv.tex
	./container-latex.sif --no-home

container-latex.sif: container/apptainer.def
	apptainer build container-latex.sif container/apptainer.def
