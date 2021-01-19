FROM python:3.7
WORKDIR /app
COPY . . 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python create.py
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]

