# Note the uses of "\" to connect all lines in the if statements to make
# Make think they're on the same line. Also note the use of ";" at end of
# each individual command.
#
# Pandoc notes:
# - HTML outputs need "--standalone" to have headers inserted, so that
#   browsers can correctly encode (otherwise, single and double quotes
#   will NOT display correctly with Firefox)
# - HTML output requires "--mathjax" since Chrome refused to implement
#   mathml, BUT this requires that you CANNOT use "--self-contained", so
#   you MUST download a full local copy of reveal.js for its
#   presentations.
# - "--standalone" provides encoding headers/footers inside file directly
#   (which is needed for Firefox etc. grr)
# - "--self-contained" is ONLY used for HTML output, but does NOT WORK
#   simultaneously with MathJax. So, basically, don't use it.
#
# todo change all *.mds!

html:
	@if [ -f "bibliography.bib" ]; then \
		pandoc *.md \
			--from=markdown+yaml_metadata_block --to=html \
			--standalone --mathjax --toc \
			--filter=pandoc-citeproc --bibliography=bibliography.bib \
			--output=output-html-$(shell date +%Y%m%d).html;\
	else \
		pandoc *.md \
			--from=markdown+yaml_metadata_block --to=html \
			--standalone --mathjax --toc \
			--output=output-html-$(shell date +%Y%m%d).html; \
	fi

beamer:
	@if [ -f "bibliography.bib" ]; then \
		pandoc *.md \
			--toc \
			--from=markdown --to=beamer \
			--template=custom \
			--filter=pandoc-citeproc --bibliography=bibliography.bib \
			--output=output-beamer-$(shell date +%Y%m%d).pdf; \
	else \
		pandoc *.md \
			--toc \
			--from=markdown --to=beamer \
			--template=custom \
			--output=output-beamer-$(shell date +%Y%m%d).pdf; \
	fi

manuscript:
	@if [ -f "bibliography.bib" ]; then \
		pandoc *.md \
			--from=markdown+latex_macros --to=latex \
			--standalone \
			--template=custom \
			--filter=pandoc-citeproc --bibliography=bibliography.bib \
			--output=output-manuscript-$(shell date +%Y%m%d).pdf; \
	else \
		pandoc *.md \
			--from=markdown+latex_macros --to=latex \
			--standalone \
			--template=custom \
			--output=output-manuscript-$(shell date +%Y%m%d).pdf; \
	fi

manuscript-double:
	@if [ -f "bibliography.bib" ]; then \
		pandoc *.md \
			--from=markdown+latex_macros --to=latex \
			--standalone \
			--template=custom-double \
			--filter=pandoc-citeproc --bibliography=bibliography.bib \
			--output=output-manuscript-double-$(shell date +%Y%m%d).pdf; \
	else \
		pandoc *.md \
			--from=markdown+latex_macros --to=latex \
			--standalone \
			--template=custom-double \
			--output=output-manuscript-double-$(shell date +%Y%m%d).pdf; \
	fi

revealjs-local:
	@if [ ! -d "reveal.js" ]; then \
		echo "        For revealjs to work (without the --self-contained flag), you MUST ";\
		echo "        have a local copy downloaded of it as 'reveal.js' from";\
		echo "  --->  'github.com:hakimel/reveal.js'.";\
		echo "        Downloading this repo now...";\
		git clone git@github.com:hakimel/reveal.js;\
	fi
	@if [ -f "bibliography.bib" ]; then\
		pandoc *.md \
			--from=markdown+yaml_metadata_block --to=revealjs \
			--variable theme=white \
			--standalone --mathjax \
			--filter=pandoc-citeproc --bibliography=bibliography.bib \
			--output=output-revealjs-$(shell date +%Y%m%d).html; \
	else \
		pandoc *.md \
			--from=markdown+yaml_metadata_block --to=revealjs \
			--variable theme=white \
			--standalone --mathjax \
			--output=output-revealjs-local-$(shell date +%Y%m%d).html; \
	fi

revealjs-online:
	@if [ -f "bibliography.bib" ]; then \
		pandoc *.md \
			--from=markdown+yaml_metadata_block --to=revealjs \
			--variable theme=white \
			--standalone --mathjax \
			--variable revealjs-url=http://lab.hakim.se/reveal-js \
			--filter=pandoc-citeproc --bibliography=bibliography.bib \
			--output=output-revealjs-$(shell date +%Y%m%d).html; \
	else \
		pandoc *.md \
			--from=markdown+yaml_metadata_block --to=revealjs \
			--variable theme=white \
			--standalone --mathjax \
			--variable revealjs-url=http://lab.hakim.se/reveal-js \
			--output=output-revealjs-online-$(shell date +%Y%m%d).html; \
	fi
