PROG_NAME = gotwo

package:
	@python setup.py sdist bdist_wheel

up:
	@twine upload --verbose dist/*

clean:
	@rm -rf gotwo.egg-info build dist
