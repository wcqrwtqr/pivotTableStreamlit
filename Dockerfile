FROM python:3.9-slim

COPY . /app

WORKDIR /app
RUN pip install --upgrade pip
# RUN pip install -r requirements1.txt
RUN pip install --no-cache-dir pandas Pillow plotly streamlit openpyxl

EXPOSE 8501

# ENTRYPOINT ["streamlit","run"]

CMD ["streamlit","run","table_charts_with_streamlit.py"]
