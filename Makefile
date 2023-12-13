install:
	python -m pip install --upgrade pip
	pip install tkinter

all : 
	python3 Mymain.py 
	

clean : 
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	# Remove all pycache
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

