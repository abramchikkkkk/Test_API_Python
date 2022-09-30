FROM python
WORKDIR /test_project/
COPY . .
RUN pip3 install -r requirements.txt
