FROM python:3:10


#WORKDIR .
#ADD ..
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
CMD ["pytest", "--env","com","--alluredir","allure-results"]