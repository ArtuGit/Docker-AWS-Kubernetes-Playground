# Dockerized Python Developing and Running  

## Usage

### Run the application
```bash
docker compose run python
```
Modify the script and retry the above command to have a new outcome.

## Development

### Linting
```bash
flake8
```

### Formatting automatically
```bash
find -type f -name '*.py' ! -exec autopep8 --in-place --aggressive --aggressive '{}' \;
```
