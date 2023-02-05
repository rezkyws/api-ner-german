FROM python:3.8

COPY ./ /
RUN pip install --no-cache-dir -r ./requirements/base.txt
RUN python -m spacy download de_core_news_md
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3345", "--workers", "5"]
