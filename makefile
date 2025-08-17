.PHONY: help install run test clean
SAMPLES_DIR=samples

help:
	@echo "Available commands:"
	@echo "  make install               - Install dependencies"
	@echo "  make run <input> <output>  - Run the app with input and output files"
	@echo "  make test                  - Run tests"
	@echo "  make clean                 - Remove temporary files"

install:
	pip install -r requirements.txt


run:
	@if [ "$(words $(MAKECMDGOALS))" -lt 2 ]; then \
		echo "Usage: make run <input_filename> <output_file>"; \
		exit 1; \
	fi
	python main.py $(SAMPLES_DIR)/$(word 2,$(MAKECMDGOALS)) $(word 3,$(MAKECMDGOALS))

# Prevent make from interpreting filenames as targets
%:
	@:
# Prevent make from interpreting filenames as targets
%:
	@:

test:
	pytest -v

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache *.pyc