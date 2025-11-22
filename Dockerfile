FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install xgboost==2.1.4 scikit-learn==1.5.1 pandas numpy flask gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
