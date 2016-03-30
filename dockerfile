FROM ubuntu:14.04
MAINTAINER Weiheng Su <ws2ta@virginia.edu>
RUN apt-get -yqq update
RUN apt-get -yqq install python-pip python-dev
RUN apt-get -yqq install nodejs npm
RUN ln -s /usr/bin/nodejs /usr/bin/node

#COPY requirements.txt /autograder/
#RUN pip install -r /autograder/requirements.txt
ADD autograder /opt/autograder
WORKDIR /opt/autograder
RUN npm install
RUN npm run build
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","./app.py"]
