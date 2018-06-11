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
        expected_result = [{'file_path': 'githubscrapper/tests/__init__.py', 'extension': 'py', 'bytes': 0.0, 'file_name': '__init__.py', 'lines': 0}, {'file_path': 'githubscrapper/tests/test_suite.py', 'extension': 'py', 'bytes': 5990.0, 'file_name': 'test_suite.py', 'lines': 135}, {'file_path': 'githubscrapper/.gitignore', 'extension': 'gitignore', 'bytes': 1100.0, 'file_name': '.gitignore', 'lines': 96}, {'file_path': 'githubscrapper/README.md', 'extension': 'md', 'bytes': 1910.0, 'file_name': 'README.md', 'lines': 39}, {'file_path': 'githubscrapper/__init__.py', 'extension': 'py', 'bytes': 0.0, 'file_name': '__init__.py', 'lines': 0}, {'file_path': 'githubscrapper/requirements.txt', 'extension': 'txt', 'bytes': 203.0, 'file_name': 'requirements.txt', 'lines': 14}, {'file_path': 'githubscrapper/webscrapperdirectorytree.py', 'extension': 'py', 'bytes': 7900.0, 'file_name': 'webscrapperdirectorytree.py', 'lines': 214}, {'file_path': 'githubscrapper/webscrapperfiledetails.py', 'extension': 'py', 'bytes': 8190.0, 'file_name': 'webscrapperfiledetails.py', 'lines': 229}]

        files = webscrapperfiledetails.iterate_over_director_tree(url)

        assert expected_result == files

    def test_create_file_details_list(self):
        files = [{'file_path': 'githubscrapper/tests/__init__.py', 'extension': 'py', 'bytes': 0.0, 'file_name': '__init__.py', 'lines': 0}, {'file_path': 'githubscrapper/tests/test_suite.py', 'extension': 'py', 'bytes': 5990.0, 'file_name': 'test_suite.py', 'lines': 135}, {'file_path': 'githubscrapper/.gitignore', 'extension': 'gitignore', 'bytes': 1100.0, 'file_name': '.gitignore', 'lines': 96}, {'file_path': 'githubscrapper/README.md', 'extension': 'md', 'bytes': 1910.0, 'file_name': 'README.md', 'lines': 39}, {'file_path': 'githubscrapper/__init__.py', 'extension': 'py', 'bytes': 0.0, 'file_name': '__init__.py', 'lines': 0}, {'file_path': 'githubscrapper/requirements.txt', 'extension': 'txt', 'bytes': 203.0, 'file_name': 'requirements.txt', 'lines': 14}, {'file_path': 'githubscrapper/webscrapperdirectorytree.py', 'extension': 'py', 'bytes': 7900.0, 'file_name': 'webscrapperdirectorytree.py', 'lines': 214}, {'file_path': 'githubscrapper/webscrapperfiledetails.py', 'extension': 'py', 'bytes': 8190.0, 'file_name': 'webscrapperfiledetails.py', 'lines': 229}]

        expected_result = [
          {
            "bytes": 1100.0,
            "file_name": ".gitignore",
            "file_path": "githubscrapper/.gitignore",
            "lines": 96
          },
          {
            "bytes": 1910.0,
            "file_name": "README.md",
            "file_path": "githubscrapper/README.md",
            "lines": 39
          },
          {
            "bytes": 0.0,
            "file_name": "__init__.py",
            "file_path": "githubscrapper/__init__.py",
            "lines": 0
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
            "bytes": 5990.0,
            "file_name": "test_suite.py",
            "file_path": "githubscrapper/tests/test_suite.py",
            "lines": 135
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
        files = [{'file_path': 'githubscrapper/tests/__init__.py', 'extension': 'py', 'bytes': 0.0, 'file_name': '__init__.py', 'lines': 0}, {'file_path': 'githubscrapper/tests/test_suite.py', 'extension': 'py', 'bytes': 5990.0, 'file_name': 'test_suite.py', 'lines': 135}, {'file_path': 'githubscrapper/.gitignore', 'extension': 'gitignore', 'bytes': 1100.0, 'file_name': '.gitignore', 'lines': 96}, {'file_path': 'githubscrapper/README.md', 'extension': 'md', 'bytes': 1910.0, 'file_name': 'README.md', 'lines': 39}, {'file_path': 'githubscrapper/__init__.py', 'extension': 'py', 'bytes': 0.0, 'file_name': '__init__.py', 'lines': 0}, {'file_path': 'githubscrapper/requirements.txt', 'extension': 'txt', 'bytes': 203.0, 'file_name': 'requirements.txt', 'lines': 14}, {'file_path': 'githubscrapper/webscrapperdirectorytree.py', 'extension': 'py', 'bytes': 7900.0, 'file_name': 'webscrapperdirectorytree.py', 'lines': 214}, {'file_path': 'githubscrapper/webscrapperfiledetails.py', 'extension': 'py', 'bytes': 8190.0, 'file_name': 'webscrapperfiledetails.py', 'lines': 229}]

        expected_result = {
          "aggregated_data": {
            "gitignore": {
              "bytes": 1100.0,
              "bytes_percentage": 4.35,
              "lines": 96,
              "lines_percentage": 13.2
            },
            "md": {
              "bytes": 1910.0,
              "bytes_percentage": 7.55,
              "lines": 39,
              "lines_percentage": 5.36
            },
            "py": {
              "bytes": 22080.0,
              "bytes_percentage": 87.3,
              "lines": 578,
              "lines_percentage": 79.5
            },
            "txt": {
              "bytes": 203.0,
              "bytes_percentage": 0.8,
              "lines": 14,
              "lines_percentage": 1.93
            }
          },
          "total_bytes": 25293.0,
          "total_lines": 727
        }

        result = webscrapperfiledetails.aggregate_file_data(files)

        assert expected_result == result
