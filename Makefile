test:
		@py.test -v test_isitup.py
		@py.test --pep8 test_isitup.py isitup/*.py
