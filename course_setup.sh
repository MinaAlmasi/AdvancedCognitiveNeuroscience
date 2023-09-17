#!/bin/bash

# env 
python3 -m venv env
source ./env/bin/activate

# setup 
echo -e "[INFO:] Installing necessary python packages ..." 
python3 -m pip install -r requirements.txt

echo -e "[INFO:] Attaching env to ipykernel ..." 
python3 -m ipykernel install --user --name=env

deactivate