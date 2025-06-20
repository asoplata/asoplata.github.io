.PHONY: all serve update

all: serve

serve:
	@echo "Make sure you are in the 'rbenv shell 3.3.6' environment"
	bundle exec jekyll serve

update:
	@echo "Make sure you are in the 'rbenv shell 3.3.6' environment"
	gem update
	gem install bundler jekyll
	bundle update
