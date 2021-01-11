FROM crkarthik11/python-sklearn

WORKDIR /apps

ADD . .

COPY requirements.txt /apps
RUN \
    pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "server.py"]
