# BPai

## Installation

    conda install --name bapi --file requirement.txt

### Activate the environment

    conda activate bpai

### Run TDD

    echo 'export PYTHONPATH=~/Projects/BPai:$PYTHONPATH' >> ~/.bash_profile
    pytest -s

### Run APIs

    uvicorn api:server --reload

