
import os
from pathlib import Path

# to log the project name
import logging

logging.basicConfig(
    level=logging.INFO, 
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
    
)
# to input the project name as required by user
while True:
    project_name=input("Enter the project name: ")
    if project_name!="":
        break
    
logging.info("Createing project by name: {project_name} ")

#list of files
list_of_files = [
    ".github/workflows/.gitkeep",   #for github action, gitkeep is a dummy file can be replaced later by actual
    f"src/{project_name}/__init__.py", #source file to create a project which contain all scripts
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f'tests/integration/__init__.py',
    "init_setup.sh", #create repo for basic conda env setup
    "requirements.txt",
    "requirements_dev.txt",  #for test files
    "setup.py",
    "pyproject.toml",  #pyproject.toml tells “frontend” build tools like pip and build what “backend” 
                       #tool to use to create distribution packages (A versioned archive file that contains 
                       # Python packages, modules, and other resource files that are used to distribute a 
                       # Release. The archive file is what an end-user will download from the internet and 
                       # install.) for your project.
    "setup.cfg",
    "tox.ini"  # used to be tested on a various environments

]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename= os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath,"w") as f:           #to insert a new file if that does not exist
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"File is already present at: {filepath}")
