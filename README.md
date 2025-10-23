# ChatBot

Este proyecto implementa un chatbot con recuperación de contexto (RAG) y conexión a un modelo LLM (OpenAI), organizado en distintos ejercicios progresivos.


## Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python ≥ 3.10
- uv
- Acceso a la API (dos opciones):
    1. en un archivo `.env`:

    ```env
    OPENAI_API_KEY = <INSERTA AQUÍ LA API KEY>
    ```

    2. o en `secrets/secret.yaml`:

    ```yaml
    openai:
      api_key: "<INSERTA AQUÍ LA API KEY>"
    ```


## Instalación
1. Clonación del repositorio

2. Instalación del entorno

    ```sh
    make install
    ```

    Este comando crea de forma automática un entorno virtual con `uv venv` e instala todas las dependencias del proyecto con `uv pip install -e .`


## Ejecución

El proyecto tiene distintos ejercicios numerados del 1 al 4 (más uno general 5 para el chatbot final).

1. Para la ejecución del ChatBot principal:
    ```sh
    make run
    ```

2. Para la ejecución de cada ejercicio:
    ```sh
    make run-ej<N>
    ```
    donde `N` sea el número de ejercicio deseado.

3. Para la ejecución de todos los ejercicios:
    ```sh
    make run-all
    ```

4. Para la ejecución de los tests:
    ```sh
    make test
    ```


## Limpieza del entorno

```sh
make clean
```