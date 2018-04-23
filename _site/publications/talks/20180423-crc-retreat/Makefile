beamer:
	pandoc *.md \
		--slide-level=2 --toc \
		--from=markdown --to=beamer \
		--template=custom \
		--output=beamer_slides.pdf

beamer_bib:
	pandoc *.md \
		--slide-level=2 --toc \
		--from=markdown --to=beamer \
		--template=custom \
		--filter=pandoc-citeproc --bibliography=bibliography.bib \
		--output=beamer_bib_slides.pdf

html:
	pandoc *.md \
		--from=markdown --to=revealjs \
		--slide-level=2 --self-contained --mathml \
		--css=${HOME}/.pandoc/templates/custom.css \
		--variable revealjs-url=${HOME}/.pandoc/revealjs \
		--variable theme=white \
		--output=html_slides.html

html_bib:
	pandoc *.md \
		--from=markdown --to=revealjs \
		--slide-level=2 --self-contained --mathml \
		--css=${HOME}/.pandoc/templates/custom.css \
		--variable revealjs-url=${HOME}/.pandoc/revealjs \
		--variable theme=white \
		--filter=pandoc-citeproc --bibliography=bibliography.bib \
		--output=html_bib_slides.html

manuscript:
	pandoc *.md \
		--from=markdown+latex_macros --to=latex \
		--standalone \
		--template=custom \
		--output=manuscript_$(shell date +%Y%m%d).pdf

manuscript_bib:
	pandoc *.md \
		--from=markdown+latex_macros --to=latex \
		--standalone \
		--template=custom \
		--filter=pandoc-citeproc --bibliography=bibliography.bib \
		--output=manuscript_bib_$(shell date +%Y%m%d).pdf
		
manuscript_double:
	pandoc *.md \
		--from=markdown+latex_macros --to=latex \
		--standalone \
		--template=custom-double \
		--output=manuscript_double_$(shell date +%Y%m%d).pdf

manuscript_double_bib:
	pandoc *.md \
		--from=markdown+latex_macros --to=latex \
		--standalone \
		--template=custom \
		--filter=pandoc-citeproc --bibliography=bibliography.bib \
		--output=manuscript_double_bib_$(shell date +%Y%m%d).pdf
