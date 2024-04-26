# Dockerized Python Developing and Running  

## Usage

### Run the application
```bash
docker compose run python
```
Modify the script and retry the above command to have a new outcome.

## Development

Firstly,

### Run Python container in bash mode in order to run commands interactively
```bash
docker compose run --entrypoint '/bin/bash' python
```

then run commands, for example:


### Run the application
`python3 ./src/script.py`

### Linting
`flake8`


### Formatting automatically
`find -type f -name '*.py' ! -exec autopep8 --in-place --aggressive --aggressive '{}' \;`
