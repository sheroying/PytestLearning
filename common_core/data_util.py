import csv
import logging
import xml.etree.ElementTree as ET
import os
# import pandas

class XmlUtil:
    def __int__(self, xml_file_path):
        # self.xml_content = FileUtil.read_file_content(xml_file_path)
        self.tree = ET.parse(xml_file_path)  # 打开xml文档

    def parse_xml_by_parameter_name(self, parameter_name):
        try:
            tree = ET.parse("country.xml")  # 打开xml文档
            # root = ET.fromstring(country_string) #从字符串传递xml
            root = tree.getroot()  # 获得root节点
        except Exception as e:
            print
            "Error:cannot parse file:country.xml."

        print
        root.tag, "---", root.attrib
        for child in root:
            print
            child.tag, "---", child.attrib

        # for item in doc.iterfind('products/product'):
        #     id = item.findtext('id')
        #     uuid = item.get('uuid')
        #     print('uuid={}, id={}, name={}, price={}'.format(uuid, id, name, price), end=
        #
        # for country in root.findall('country'):  # 找到root节点下的所有country节点
        #     rank = country.find('rank').text  # 子节点下节点rank的值
        #     name = country.get('name')  # 子节点下属性name的值
        #     print
        #     name, rank
        #
        #     # 修改xml文件
        # for country in root.findall('country'):
        #     rank = int(country.find('rank').text)
        #     if rank > 50:
        #         root.remove(country)
        #
        # tree.write('output.xml')


class QuoteRowUtil:

    def __init__(self, csv_file_path):
        self.file_path = csv_file_path
        self.rows = CsvUtil.get_rows(self.file_path)

    # @staticmethod
    def get_row_from_csv_file(self, column_name, column_value):
        column_and_index = CsvUtil.get_column_and_index_from_csv_file(self.file_path, column_name)
        row_index = column_and_index[column_value]
        if row_index:
            return self.rows[row_index]
        else:
            logging.info("Didn't find out the row data in " + self.file_path)


class CsvUtil:
    @staticmethod
    def get_rows(csv_file_path):
        if FileUtil.check_file_exist(csv_file_path):
            with open(csv_file_path, mode = 'r') as csv_file:
                reader = csv.reader(csv_file)
                print(reader)
                return list(reader)  # read the csv content as the rows
        else:
            logging.info(csv_file_path + 'file path not exist')
            return

    @staticmethod
    def get_column_and_index_from_csv_file(csv_file_path, column_name):
        logging.info('Start read csv file..')
        column_value_and_row_index = {}  ## {"column value1":1, "column value2":2, "column value3":3 }
        try:
            with open(csv_file_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                    line_count = line_count + 1
                    column_value_and_row_index[column_name] = line_count
                    print(111 + column_name)
                    print(111 + line_count)

            logging.info('End read csv file column and save the row index for file ' + csv_file_path)
        except IOError as error:
            print(error)
            logging.error('Read from file {0} error {1}'.format(csv_file_path, error))
        print(column_value_and_row_index)
        return column_value_and_row_index

    @staticmethod
    # def read_url_from_csv_file(csv_file_path):
    #     logging.info('Start read csv file..')
    #     try:
    #         with open(csv_file_path, mode='r') as csv_file:
    #             csv_reader = csv.DictReader(csv_file)
    #             line_count = 0
    #             data_url = []
    #             for row in csv_reader:
    #                 data_url.append(row['url'])
    #                 line_count = line_count + 1
    #         logging.info('End read csv file ' + csv_file_path)
    #     except IOError as error:
    #         print
    #         'Read from file {0} error {1}'.format(csv_file_path, error)
    #     return data_url

    @staticmethod
    def read_csv_file_content(csv_file_path):
        logging.info('Start read csv file..')
        try:
            with open(csv_file_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                data_row = []
                for row in csv_reader:
                    data_row.append(row)
                    line_count = line_count + 1
            logging.info('End read csv file ' + csv_file_path)
        except IOError as error:
            print
            'Read from file {0} error {1}'.format(csv_file_path, error)
        return data_row

    @staticmethod
    def get_csv_header(csv_file_path):
        logging.info('Start get csv file header..')
        try:
            with open(csv_file_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                header = []
                for row in csv_reader:
                    header.append(row)
            logging.info('End get header, header is ' + header)
        except IOError as error:
            print
            'Read from file {0} error {1}'.format(csv_file_path, error)
        return header

    @staticmethod
    def write_csv_file_default_header(self, csv_file_path, list_source):

        logging.info('Start write csv file ' + csv_file_path)
        list_header = self.get_header_from_ds_list(list_source)
        list_header.sort()
        try:
            with open(csv_file_path, mode='w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=list_header)
                writer.writeheader()
                for row in list_source:
                    dict_row = {}
                    for header in list_header:
                        if header in row:
                            dict_row[header] = row[header]
                        else:
                            dict_row[header] = ''
                    writer.writerow(dict_row)
            logging.info('End write csv file ' + csv_file_path)
        except IOError as error:
            print
            'Write into file {0} error {1}'.format(csv_file_path, error)

    @staticmethod
    def write_csv_file(csv_file_path, list_source, list_header):
        logging.info('Start write csv file ' + csv_file_path)
        try:
            with open(csv_file_path, mode='w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=list_header)
                writer.writeheader()
                for row in list_source:
                    dict_row = {}
                    for header in list_header:
                        if header in row:
                            dict_row[header] = row[header]
                        else:
                            dict_row[header] = ''
                    writer.writerow(dict_row)
            logging.info('End write csv file ' + csv_file_path)
        except IOError as error:
            print
            'Write into file {0} error {1}'.format(csv_file_path, error)

    @staticmethod
    def save_url_into_csv_file(csv_file_path, url_list_source):
        logging.info('Start write csv file ' + csv_file_path)
        try:
            with open(csv_file_path, mode='w') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=['url'])
                writer.writeheader()
                for url in url_list_source:
                    dict_row = dict()
                    dict_row['url'] = url
                    writer.writerow(dict_row)
            logging.info('End write csv file ' + csv_file_path)
        except IOError as error:
            print
            'Write into file {0} error {1}'.format(csv_file_path, error)


def get_header_from_ds_list(dict_list):
    header_all = set()
    for row in dict_list:
        keys = list(row)
        s = set(keys)
        header_all = header_all | s
    return list(header_all)


class FileUtil:

    def __int__(self, file_path):
        self.file_path = file_path

    @staticmethod
    def check_file_exist(filePath):
        # todo
        return True

    @staticmethod
    def read_file_content(self, filePath):
        if not filePath:
            with open(filePath) as file_object:
                content = file_object.read()
                return content
        elif not self.file_path:
            with open(self.file_path) as file_object:
                content = file_object.read()
                return content

    @staticmethod
    def read_file(file_path):
        logging.info('Start read file..')
        try:
            with open(file_path, mode='r') as file:
                content = file.readlines()
            logging.info('End read file ' + file_path)
        except IOError as error:
            print
            'Read from file {0} error {1}'.format(file_path, error)
        return ''.join(content)

    @staticmethod
    def read_file_splitlines(file_path):
        logging.info('Start read file..')
        try:
            with open(file_path, mode='r') as file:
                content_lines = file.read().splitlines()
            logging.info('End read file ' + file_path)
        except IOError as error:
            print
            'Read from file {0} error {1}'.format(file_path, error)
        return content_lines

    @staticmethod
    def write_file(file_path, content):
        logging.info('Start write file at %s' % file_path)
        try:
            with open(file_path, mode='w') as file:
                file.write(content)
            logging.info('End write file..')
        except IOError as error:
            print
            'Write into file {0} error {1}'.format(file_path, error)


def file_exists(data_file):
    return os.path.exists(data_file)

def get_headers_in_csv(data_file):
    with open(data_file, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
    return headers

