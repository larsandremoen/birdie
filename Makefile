.PHONY: install
install:
	PIPENV_VENV_IN_PROJECT=1 pipenv install

.PHONY: run
run:
	.venv/bin/uvicorn main:app --reload
