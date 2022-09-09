FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install -r requirements1.txt

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["table_charts_with_streamlit.py"]
