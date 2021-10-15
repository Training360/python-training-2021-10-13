FROM python
WORKDIR app
COPY index_korona.py .
COPY requirements.txt .
RUN pip install -r ./requirements.txt
ENTRYPOINT python index_korona.py