.PHONY: install run test clean

install:
	uv venv
	uv pip install -e .

# Para ejecutar el programa al completo
run-all:
	uv run python main.py

# Para ejecutar ejercicios específicos
run-ej1:
	uv run python main.py 1

run-ej2:
	uv run python main.py 2

run-ej3:
	uv run python main.py 3

run-ej4:
	uv run python main.py 4

# Para ejecutar el programa principal del chatbot
run:
	uv run python main.py 5

# Para ejecutar los tests
test:
	PYTHONPATH=. uv run pytest -q

clean:
	rm -rf .venv
	rm -rf __pycache__ */__pycache__ */*/__pycache__
	rm -rf .pytest_cache
	rm -rf dist build *.egg-info src/*.egg-info
	@echo "Limpieza completada."