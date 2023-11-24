# docker run -d -p 3000:3000 -v $PWD:/app abi-web-img


FROM python:3.9.18
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:3000"]
