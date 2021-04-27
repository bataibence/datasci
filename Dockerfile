FROM python
COPY . .

EXPOSE 8000

RUN pip3 install -r requirements.txt

CMD streamlit run app.py --server.port=8000
