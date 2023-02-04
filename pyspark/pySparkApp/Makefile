build:
	python3 setup.py sdist
	rm -r foo.egg-info

build_zip:
	mkdir -p dist/
	rsync -av foo dist/
	cd dist ; zip -r foo.zip . * ; cd ..
	#rm -fr dist/foo