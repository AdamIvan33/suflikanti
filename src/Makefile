## @file Makefile
#  @brief Build and management script for the calculator project
#  @author Šimon Urban
#  
#  This Makefile provides commands to run, test, document, lint, clean, 
#  and package the calculator project, as well as manage dependencies.


PYTHON = python3
ZIP_NAME = xcechvj00_xivanad00_xmezeim00_xurbans00.zip
FILES = calculator_GUI.py math_lib_test.py requirements.txt Doxyfile Makefile
DOXYFILE = Doxyfile

.PHONY: all run test clean pack lint stddev upd_req deps help

	
all: deps
	@echo "All dependencies installed. You can now run your application or tests."

run:
	@echo "Running program ..."
	python3 calculator_GUI.py
	
test:
	@echo "Testing ..."
	pytest math_lib_test.py

doc:
	@echo "Generating code documentation ..."
	doxygen -g Doxyfile
	doxygen $(DOXYFILE)

clean:
	@echo "Cleaning up files..."
	find . -maxdepth 1 -type f $(foreach file, $(FILES), ! -name '$(file)') -delete
	find . -maxdepth 1 -type d ! -name '.' -exec rm -rf {} +
	

pack:
	@echo "Zipping up files ..."
	zip $(ZIP_NAME) $(FILES)

lint:
	@echo "Searching for semantic and stylistic problems  ..."
	flake8 .

stddev: deps
	@echo "Dependencies installed for stddev target. Add your stddev commands here."

upd_req:
	@echo "Updating requirements ..."
	pip freeze > requirements.txt

deps:
	$(PYTHON) -m pip install -r requirements.txt

help:
	@echo "Makefile Help:"
	@echo "  all       - Install dependencies and prepare the environment"
	@echo "  run       - Run the main Python script"
	@echo "  test      - Run tests using pytest"
	@echo "  doc       - Generate code documentation with Doxygen"
	@echo "  clean     - Remove all files and directories except those listed in FILES"
	@echo "  pack      - Create a zip archive of project files"
	@echo "  lint      - Check code for semantic and stylistic problems using flake8"
	@echo "  stddev    - Install dependencies (TODO modify to add stddev commands)"
	@echo "  upd_req   - Update requirements.txt with current installed packages"
	@echo "  deps      - Install required Python packages"
	@echo "  help      - Show this help message"

#TODO modify to add stddev commands
#TODO Zistiť čo všetko má byť v ZIP file, upraviť pack a clean via upavovania FILES