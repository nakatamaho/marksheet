LATEX=platex
DVI2PDF=dvipdfmx
DVI2PS=dvips
TEXFILE=kaitouyoushi

.SUFFIXES:	.tex .dvi .ps .pdf
.tex.dvi:	
	${LATEX} $< $@
	${LATEX} $< $@

.dvi.ps:	
	${DVI2PS} $< > $@

.dvi.pdf:	
	${DVI2PDF} $<

all: ${TEXFILE}.pdf

clean:
	rm -f ${TEXFILE}.dvi ${TEXFILE}.pdf ${TEXFILE}.log ${TEXFILE}.out ${TEXFILE}.aux texput.log *~
