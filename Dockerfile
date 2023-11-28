FROM python:3:10
WORKDIR .
ADD ..
RUN pip3 install -r requirements.txt
CMD ["pytest", "--env","com","--alluredir","allure-results"]