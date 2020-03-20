PROG_NAME = gto
VERSION = v0.1.0

package:
	@python setup.py sdist bdist_wheel

up:
	@twine upload dist/*

clean:
	@rm -rf gto.egg-info build dist
