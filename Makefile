install:
	# install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt && \
		python -m textblob.download_corpora
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker container
	docker run -p 8080:8080 deploy-fastapi:latest
deploy:
	#deploy
all: install lint test deploy