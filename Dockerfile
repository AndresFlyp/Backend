FROM python:3.12.0rc2-bookworm
WORKDIR /backend
COPY requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt
COPY . /backend
EXPOSE 8000