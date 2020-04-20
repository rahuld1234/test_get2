FROM python

COPY . /app/rahul2
WORKDIR /app/rahul2

RUN pip install requests && pip install pytest

CMD pytest -v test_get2.py
