# - Notes:
#   - Must used '--self-contained' for truly self-contained html/js
#   presentations, since '--standalone' will NOT do it
#   - options:
# 		--bibliography=bibliography.bib \

CONTENT=$(basename $(wildcard *.md))
 
presentation:
	$(foreach INDIV,$(CONTENT),$(call create_presentation,$(INDIV)))

define create_presentation
	pandoc \
		metadata.yaml $1.md \
		--to=revealjs \
		--slide-level=2 \
		--filter pandoc-crossref \
		--variable revealjs-url=${HOME}/.pandoc/reveal.js \
		--variable theme=white \
		--self-contained \
		--output=$1.html

endef
