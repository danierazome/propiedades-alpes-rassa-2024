FROM python:3.10

EXPOSE 8003

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8003", "--reload"]