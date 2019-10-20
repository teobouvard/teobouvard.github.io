serve: install html
	bundle exec jekyll serve --host 0.0.0.0

install:
	bundle install

html:
	jupyter-nbconvert --to html --output-dir=_posts/ _jupyter/*.ipynb
	sed -i 's=<title>\(.*\)</title>=<title>x</title>=g' _posts/*.html