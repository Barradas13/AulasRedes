FROM python

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install


EXPOSE 8550

ENTRYPOINT ["poetry", "run", "python3", "/app/__init__.py"]