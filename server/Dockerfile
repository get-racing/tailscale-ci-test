FROM python

RUN mkdir /server
COPY requirements.txt /server/requirements.txt

WORKDIR /server

RUN python -m pip install -r requirements.txt

COPY entrypoint.sh /server/entrypoint.sh
COPY server.py /server/server.py

ENTRYPOINT [ "/server/entrypoint.sh" ]
