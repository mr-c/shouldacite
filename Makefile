html:
	cp shoudacite_base.png shoudacite_comic.png app/static/
	cd app && python freeze.py

publish: html
	git fetch --all
	ghp-import -b gh-pages app/build
	git push origin gh-pages

serve:
	cd app && python app.py
