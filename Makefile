all: package clean

release: wheel upload clean

package:
	makepkg -si

build:
	python setup.py build

install:
	python setup.py install

wheel:
	python setup.py sdist bdist_wheel 

upload:	
	twine upload dist/*

clean: 
	rm -rf ./src ./pkg ./build ./dist ./*.egg-info *.tar.gz *.tar.zst
