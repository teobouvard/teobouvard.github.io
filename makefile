serve: install
	bundle exec jekyll serve --host 0.0.0.0

install:
	bundle install

html:
	jupyter-nbconvert --output-dir=_posts/ _jupyter/*.ipynb