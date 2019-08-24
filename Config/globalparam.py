import os
from Utils.readConfig import ReadConfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
readConfig = ReadConfig(os.path.join(config_file_path, 'config.ini'))
# locator_config_path = os.path.join(config_file_path, 'locators')
# option_config_path = os.path.join(config_file_path, 'options')
# 项目参数设置
prj_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# prj_path = readConfig.getValue('projectConfig', 'project_path')
# 日志路径
log_path = os.path.join(prj_path, 'Report', 'log')
# print(log_path)
# 测试报告路径
report_path = os.path.join(prj_path, 'Report', 'report')
# Mock构参服务文件地址
mock_path = os.path.join(prj_path, 'MockServices')
# 下载文件地址
download_path = os.path.join(prj_path,'Validator','DownloadFile')
# 上传文件地址
upload_path = os.path.join(prj_path,'MockServices','UploadData')
# 登陆数据
url = readConfig.getValue('Site Info', 'url')
# 机构后台登录地址
admin_url = readConfig.getValue('Site Info','admin_url')
# 接口服务文件地址
interface_path = os.path.join(prj_path, 'InterfaceServices')
# 配置文件地址
config_path = os.path.join(prj_path, 'Config')
# 接口构参json文件地址
mockJson_path = os.path.join(prj_path, 'Config','mock.json')


loginUser = readConfig.getValue('Login Info', 'username')
loginPwd = readConfig.getValue('Login Info', 'password')

# 配置文件中配置的校区ID
schoolid = readConfig.getValue('School Info', 'schoolid')

# 数据库连接信息
host_name = readConfig.getValue('Database Info', 'host_name')
port = readConfig.getValue('Database Info', 'port')
username = readConfig.getValue('Database Info', 'username')
password = readConfig.getValue('Database Info', 'password')
default_schema = readConfig.getValue('Database Info', 'default_schema')

#运行环境依赖包
# environment_model = ['selenium', 'pytest', 'pytest-html', 'PyMySQL', 'requests', 'tornado']

# 是否开启数据库校验信息
# is_database_check = readConfig.getValue('check', 'is_database_check')
