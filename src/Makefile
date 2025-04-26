## @file Makefile
#  @brief Build and management script for the calculator project
#  @author Šimon Urban
#  
#  This Makefile provides commands to run, test, document, lint, clean, 
#  and package the calculator project, as well as manage dependencies.

PYTHON       = python3
VENV         = venv
ZIP_NAME     = xcechvj00_xivanad00_xmezeim00_xurbans00.zip
FILES        = calculator_GUI.py math_lib.py math_lib_test.py profiling.cpp requirements.txt Doxyfile Makefile logo.png
DOXYFILE     = Doxyfile

## Detect operating system
OS := $(shell uname)

EXE_NAME = calculator
VENV_PYTHON = $(VENV)/bin/python

## Remove file/directory
RM = rm -f
RMDIR = rm -rf

EXE_PATH     = dist/$(EXE_NAME)

.PHONY: all deps run test lint upd_req doc pack clean stddev help rebuild build_exe remove_exe

## Default target: create venv and install dependencies once
all: $(VENV) deps
	@echo "Environment ready: venv created and dependencies installed."
	@echo -e "\033[1;36m\033[3mPlease run 'source venv/bin/activate' to activate the virtual environment.\033[0m"
	
## Create virtual environment directory (only if missing)
$(VENV):
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV) --upgrade-deps

## Install Python package dependencies (only when needed)
deps: $(VENV)
	@echo "Installing dependencies into virtual environment..."
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PYTHON) -m pip install -r requirements.txt

## Run the GUI using the venv Python
run: $(VENV)
	@echo "Running program..."
	$(VENV_PYTHON) calculator_GUI.py

## Run tests with pytest inside venv
test: $(VENV)
	@echo "Running tests..."
	$(VENV_PYTHON) -m pytest math_lib_test.py

## Lint code with flake8 inside venv
lint: $(VENV)
	@echo "Running lint..."
	$(VENV_PYTHON) -m flake8 .

## Update requirements.txt from venv
upd_req: $(VENV)
	@echo "Updating requirements.txt..."
	$(VENV_PYTHON) -m pip freeze > requirements.txt

## Generate documentation
doc:
	@echo "Generating documentation..."
	doxygen $(DOXYFILE)

## Create zip archive of project files, ensuring venv folder exists
pack: $(VENV)
	@echo "Creating zip archive..."
	zip $(ZIP_NAME) $(FILES)

## Clean project directory, preserving venv
clean:
	@echo "Cleaning up files (Linux/Unix)..."
	@# Build find exclude arguments
	@exclude_files=""
	$(foreach file,$(FILES),$(eval exclude_files += ! -name '$(file)' ))
	find . -maxdepth 1 -type f $(exclude_files) -delete
	find . -maxdepth 1 -type d \( ! -name '.' ! -name '$(VENV)' \) -exec rm -rf {} +
	$(RMDIR) $(VENV)

## Placeholder for standard deviation profiling setup (no reinstall)
stddev: $(VENV)
	@echo "Preparing for stddev profiling..."

## Rebuild venv and deps from scratch
rebuild:
	$(RMDIR) $(VENV)
	$(MAKE) all

## Install: create executable, rebuild only if sources changed
$(EXE_PATH): calculator_GUI.py math_lib.py | $(VENV)
	@echo "Building executable..."
	$(VENV_PYTHON) -m pip install --upgrade pyinstaller
	$(VENV_PYTHON) -m PyInstaller --onefile --name $(basename $(EXE_NAME)) --add-data "logo.png:." calculator_GUI.py

install: $(EXE_PATH)
	@echo "Executable created at $(EXE_PATH)"

## Uninstall: delete the executable and build files
uninstall:
	@echo "Removing executable..."
	$(RM) $(EXE_PATH)
	$(RMDIR) build/ $(basename $(EXE_NAME)).spec

## Help message 
help:
	@echo "Makefile Help:"
	@echo "  all       - Create venv and install dependencies"  
	@echo "  deps      - Install dependencies into venv"  
	@echo "  run       - Run the main script inside venv"  
	@echo "  test      - Run tests inside venv"  
	@echo "  lint      - Lint code inside venv"  
	@echo "  upd_req   - Regenerate requirements.txt from venv"  
	@echo "  doc       - Generate documentation with Doxygen"  
	@echo "  pack      - Zip up project files"  
	@echo "  clean     - Clean artifacts (venv preserved)"  
	@echo "  stddev    - Stddev profiling setup (placeholder)"  
	@echo "  rebuild   - Delete and recreate venv and deps"  
	@echo "  help      - Show this message"
