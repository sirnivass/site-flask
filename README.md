# Como rodar (passo a passo mínimo)
1. Entrar na pasta do projeto:

```cd Projeto```

2. Criar e ativar ambiente virtual (recomendado):

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar Flask:

```pip install Flask```

4. Rodar diretamente com Python (este projeto chama ```app.run()``` em ```main.py```):

```python main.py```

4. Alternativa usando ```flask run```:

```
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```