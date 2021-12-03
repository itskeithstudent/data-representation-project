FROM python:3

# copy all the files to the container server folder
COPY ./Server /Server
# copy requiremetns.txt to server folder in container, for install required packages
COPY requirements.txt /Server

# set a directory for the app
WORKDIR /Server

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# start container with python
ENTRYPOINT ["python"]
# then run app.py
CMD ["app.py"]