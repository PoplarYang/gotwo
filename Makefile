PROG_NAME = tobe
VERSION = v0.3.1

package:
	@python setup.py sdist bdist_wheel

up:
	@twine upload dist/*

clean:
	@rm -rf tobe.egg-info build dist
