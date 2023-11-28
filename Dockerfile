FROM python:3:10
WORKDIR .
ADD ..
RUN pip install -r requirements.txt
CMD ["pytest", "--env","com","--alluredir","allure-results"]