FROM python:3-slim
RUN apt update && apt install -y python3-dev default-libmysqlclient-dev build-essential pkg-config
RUN python -m pip install pip-tools my
WORKDIR /ticar
COPY . .
RUN pip-compile requirements.in
RUN mv requirements.txt req.txt && grep -v msgspec req.txt > requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_ENV=testing
ENV FLASK_APP=ticar.app
ENV USERNAME=ticar
CMD ["flask","run","--host=0.0.0.0"]
