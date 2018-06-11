import webscrapperfiledetails


class TestSuite(object):
    def test_byte_conversion_kb(self):
        position_value = 0
        position_unit = 1
        file_info_contents = [1, 'KB']

        number_of_bytes = webscrapperfiledetails.byte_conversion(position_value, position_unit, file_info_contents)

        assert number_of_bytes == 1000

    def test_byte_conversion_mb(self):
        position_value = 0
        position_unit = 1
        file_info_contents = [1, 'MB']

        number_of_bytes = webscrapperfiledetails.byte_conversion(position_value, position_unit, file_info_contents)

        assert number_of_bytes == 1000000

    def test_byte_conversion_gb(self):
        position_value = 0
        position_unit = 1
        file_info_contents = [1, 'GB']

        number_of_bytes = webscrapperfiledetails.byte_conversion(position_value, position_unit, file_info_contents)

        assert number_of_bytes == 1000000000

    def test_byte_conversion_bytes(self):
        position_value = 0
        position_unit = 1
        file_info_contents = [1, 'Bytes']

        number_of_bytes = webscrapperfiledetails.byte_conversion(position_value, position_unit, file_info_contents)

        assert number_of_bytes == 1

    def test_get_bytes_and_lines(self):
        url = "https://github.com/EVolpert/githubscrapper/blob/master/requirements.txt"

        bytes_and_lines = webscrapperfiledetails.retrieve_file_information(url)

        assert bytes_and_lines['lines'] == 14
        assert bytes_and_lines['bytes'] == 203
        assert bytes_and_lines['extension'] == 'txt'
        assert bytes_and_lines['file_path'] == 'githubscrapper/requirements.txt'
        assert bytes_and_lines['file_name'] == 'requirements.txt'

    def test_iterate_over_director_tree(self):
        url = "https://github.com/EVolpert/githubscrapper"
        expected_result = [{'lines': 0, 'file_path': 'githubscrapper/tests/__init__.py', 'extension': 'py', 'bytes': 0.0, 'file_name': '__init__.py'}, {'lines': 155, 'file_path': 'githubscrapper/tests/test_suite.py', 'extension': 'py', 'bytes': 7790.0, 'file_name': 'test_suite.py'}, {'lines': 96, 'file_path': 'githubscrapper/.gitignore', 'extension': 'gitignore', 'bytes': 1100.0, 'file_name': '.gitignore'}, {'lines': 31, 'file_path': 'githubscrapper/README.md', 'extension': 'md', 'bytes': 1750.0, 'file_name': 'README.md'}, {'lines': 83, 'file_path': 'githubscrapper/githubscrapper.txt', 'extension': 'txt', 'bytes': 1680.0, 'file_name': 'githubscrapper.txt'}, {'lines': 14, 'file_path': 'githubscrapper/requirements.txt', 'extension': 'txt', 'bytes': 203.0, 'file_name': 'requirements.txt'}, {'lines': 214, 'file_path': 'githubscrapper/webscrapperdirectorytree.py', 'extension': 'py', 'bytes': 7900.0, 'file_name': 'webscrapperdirectorytree.py'}, {'lines': 229, 'file_path': 'githubscrapper/webscrapperfiledetails.py', 'extension': 'py', 'bytes': 8190.0, 'file_name': 'webscrapperfiledetails.py'}]

        files = webscrapperfiledetails.iterate_over_director_tree(url)

        assert expected_result == files

    def test_create_file_details_list(self):
        files = [{'lines': 0, 'file_path': 'githubscrapper/tests/__init__.py', 'extension': 'py', 'bytes': 0.0, 'file_name': '__init__.py'}, {'lines': 155, 'file_path': 'githubscrapper/tests/test_suite.py', 'extension': 'py', 'bytes': 7790.0, 'file_name': 'test_suite.py'}, {'lines': 96, 'file_path': 'githubscrapper/.gitignore', 'extension': 'gitignore', 'bytes': 1100.0, 'file_name': '.gitignore'}, {'lines': 31, 'file_path': 'githubscrapper/README.md', 'extension': 'md', 'bytes': 1750.0, 'file_name': 'README.md'}, {'lines': 83, 'file_path': 'githubscrapper/githubscrapper.txt', 'extension': 'txt', 'bytes': 1680.0, 'file_name': 'githubscrapper.txt'}, {'lines': 14, 'file_path': 'githubscrapper/requirements.txt', 'extension': 'txt', 'bytes': 203.0, 'file_name': 'requirements.txt'}, {'lines': 214, 'file_path': 'githubscrapper/webscrapperdirectorytree.py', 'extension': 'py', 'bytes': 7900.0, 'file_name': 'webscrapperdirectorytree.py'}, {'lines': 229, 'file_path': 'githubscrapper/webscrapperfiledetails.py', 'extension': 'py', 'bytes': 8190.0, 'file_name': 'webscrapperfiledetails.py'}]

        expected_result = [
          {
            "bytes": 1100.0,
            "file_name": ".gitignore",
            "file_path": "githubscrapper/.gitignore",
            "lines": 96
          },
          {
            "bytes": 1750.0,
            "file_name": "README.md",
            "file_path": "githubscrapper/README.md",
            "lines": 31
          },
          {
            "bytes": 1680.0,
            "file_name": "githubscrapper.txt",
            "file_path": "githubscrapper/githubscrapper.txt",
            "lines": 83
          },
          {
            "bytes": 203.0,
            "file_name": "requirements.txt",
            "file_path": "githubscrapper/requirements.txt",
            "lines": 14
          },
          {
            "bytes": 0.0,
            "file_name": "__init__.py",
            "file_path": "githubscrapper/tests/__init__.py",
            "lines": 0
          },
          {
            "bytes": 7790.0,
            "file_name": "test_suite.py",
            "file_path": "githubscrapper/tests/test_suite.py",
            "lines": 155
          },
          {
            "bytes": 7900.0,
            "file_name": "webscrapperdirectorytree.py",
            "file_path": "githubscrapper/webscrapperdirectorytree.py",
            "lines": 214
          },
          {
            "bytes": 8190.0,
            "file_name": "webscrapperfiledetails.py",
            "file_path": "githubscrapper/webscrapperfiledetails.py",
            "lines": 229
          }
        ]

        result = webscrapperfiledetails.create_file_details_list(files)

        assert expected_result == result

    def test_aggregated_data(self):
        files = [{'lines': 0, 'file_path': 'githubscrapper/tests/__init__.py', 'extension': 'py', 'bytes': 0.0, 'file_name': '__init__.py'}, {'lines': 155, 'file_path': 'githubscrapper/tests/test_suite.py', 'extension': 'py', 'bytes': 7790.0, 'file_name': 'test_suite.py'}, {'lines': 96, 'file_path': 'githubscrapper/.gitignore', 'extension': 'gitignore', 'bytes': 1100.0, 'file_name': '.gitignore'}, {'lines': 31, 'file_path': 'githubscrapper/README.md', 'extension': 'md', 'bytes': 1750.0, 'file_name': 'README.md'}, {'lines': 83, 'file_path': 'githubscrapper/githubscrapper.txt', 'extension': 'txt', 'bytes': 1680.0, 'file_name': 'githubscrapper.txt'}, {'lines': 14, 'file_path': 'githubscrapper/requirements.txt', 'extension': 'txt', 'bytes': 203.0, 'file_name': 'requirements.txt'}, {'lines': 214, 'file_path': 'githubscrapper/webscrapperdirectorytree.py', 'extension': 'py', 'bytes': 7900.0, 'file_name': 'webscrapperdirectorytree.py'}, {'lines': 229, 'file_path': 'githubscrapper/webscrapperfiledetails.py', 'extension': 'py', 'bytes': 8190.0, 'file_name': 'webscrapperfiledetails.py'}]

        expected_result = {
          "aggregated_data": {
            "gitignore": {
              "bytes": 1100.0,
              "bytes_percentage": 3.84,
              "lines": 96,
              "lines_percentage": 11.68
            },
            "md": {
              "bytes": 1750.0,
              "bytes_percentage": 6.12,
              "lines": 31,
              "lines_percentage": 3.77
            },
            "py": {
              "bytes": 23880.0,
              "bytes_percentage": 83.46,
              "lines": 598,
              "lines_percentage": 72.75
            },
            "txt": {
              "bytes": 1883.0,
              "bytes_percentage": 6.58,
              "lines": 97,
              "lines_percentage": 11.8
            }
          },
          "total_bytes": 28613.0,
          "total_lines": 822
        }

        result = webscrapperfiledetails.aggregate_file_data(files)

        assert expected_result == result
