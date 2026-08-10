.PHONY: setup test run-api enroll clean

setup:
	pip install -r requirements.txt
	mkdir -p data/raw data/processed

test:
	pytest tests/ -v

api:
	uvicorn src.api:app --reload

enroll:
	@echo "Usage: make enroll NAME='John Doe' CAT='star' AUDIO='path.wav'"
	python src/enroll.py --name "$(NAME)" --category "$(CAT)" --audio "$(AUDIO)"

clean:
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
