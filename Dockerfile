FROM python:3.7
WORKDIR /app
COPY . . 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV 'DBI_URI'='mysql+pymysql://root:password1234@35.246.109.58/walls'
ENV 'SECRET_KEY'='a-secret-key'
RUN python create.py
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]

