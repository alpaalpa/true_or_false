SRC=true_or_false/*.py
TEST_SRC=tests/*.py

test: $(SRC) $(TEST_SRC)
	poetry run pytest tests

build: $(SRC) pyproject.toml README.md
	poetry build

publish: build
	poetry publish