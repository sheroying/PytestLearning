# This config file is to prepare:
# the pre-conditions;
# shared data in different tests cases;
# tear down steps
import pytest


# --env=integration -s --capture=fd --alluredir=/Users/yiyu/repo/QA_Automation/Local/allure_report
# def pytest_configure(config):
# pytest.env = config.getoption('--env')
def pytest_addoption(parser):
    """"
    ENV:
        for AC: stage - ac_stage; qa - ac_qa; ac_integration;
        adap_ac - for integration tests,
        gap - gap
        adap production - live
    """
    parser.addoption("--env", action="store", default="integration",  choices=['dev', 'qa', 'integration', 'com'], help="command parameter, '--env' to set switch different test env ")
    # parser.addoption("--env_fed", action="store", default="qe60")
    # parser.addoption("--flaky", action="store", default="true")
    # parser.addoption("--set", action="store", default="all")
    # parser.addoption("--key", action="store", default=None)
    # parser.addoption("--browser_stack", action="store", default='false')
    # parser.addoption("--os_system", action="store", default='Windows 10')
    # parser.addoption("--browser", action="store", default='Chrome latest')
    # parser.addoption("--customize_fed", action="store", default='false')
    # parser.addoption("--customize_fed_url", action="store", default="qa.secure.cf3.io")
    # # parser.addoption("--service_tag", action="store", default="smoke")
    # parser.addoption("--jenkins_test_url", action="store", default='')
    # parser.addoption("--deployment_url", action="store", default='')
    # parser.addoption("--crp", action="store", default="false")
    # parser.addoption("--jira", action="store", default="")


@pytest.fixture(scope="session", autouse=True)
def get_env(request):
    option = request.config.getoption("--env")
    if option == "integration":
        print("current env is " + option)
    return option


def pytest_configure(config):
    pytest.env = config.getoption('--env')





# def pytest_configure(config):
#     os.environ['baseurl'] = config.getoption('baseurl')
#     os.environ['auth'] = config.getoption('auth')
#     os.environ['site'] = config.getoption('site')
#     os.environ['env'] = config.getoption('env')



# @pytest.fixture(autouse=True)
# def set_env(get_env):
#     pytest.env = get_env
#     pass
    # with open() as f:
    #     f.write(get_env)
