FROM python:3.10

EXPOSE 5001

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "./src/api", "--debug", "run", "--host=0.0.0.0", "--port=5001"]