PROG_NAME = tobe
VERSION = v0.2.0

package:
	@python setup.py sdist bdist_wheel

up:
	@twine upload dist/*

clean:
	@
	@rm -rf tobe.egg-info build dist
