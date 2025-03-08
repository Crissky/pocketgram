###############################################################################
# Tests                                                                       #
###############################################################################

# Code Style
pep8: ## Checks code style (PEP8)
	@flake8

unit-test: ## Do unit tests using pytest
	@python -m pytest -s tests

tests: pep8 unit-test