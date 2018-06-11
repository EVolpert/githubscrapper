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

        assert bytes_and_lines['lines'] == 7
        assert bytes_and_lines['bytes'] == 97
        assert bytes_and_lines['extension'] == 'txt'
        assert bytes_and_lines['file_path'] == 'githubscrapper/requirements.txt'
        assert bytes_and_lines['file_name'] == 'requirements.txt'

    def test_iterate_over_director_tree(self):
        url = "https://github.com/EVolpert/githubscrapper"
        expected_result = [{'file_name': '.gitignore', 'bytes': 1100, 'lines': 96, 'extension': 'gitignore', 'file_path': 'githubscrapper/.gitignore'}, {'file_name': 'README.md', 'bytes': 1100, 'lines': 30, 'extension': 'md', 'file_path': 'githubscrapper/README.md'}, {'file_name': 'requirements.txt', 'bytes': 97, 'lines': 7, 'extension': 'txt', 'file_path': 'githubscrapper/requirements.txt'}, {'file_name': 'webscrapperfiledetails.py', 'bytes': 5660, 'lines': 144, 'extension': 'py', 'file_path': 'githubscrapper/webscrapperfiledetails.py'}, {'file_name': 'webscrapperB.py', 'bytes': 5390, 'lines': 139, 'extension': 'py', 'file_path': 'githubscrapper/webscrapperB.py'}]

        files = webscrapperfiledetails.iterate_over_director_tree(url)

        assert expected_result == files

    def test_create_file_details_list(self):
        files = [{'file_name': '.gitignore', 'bytes': 1100, 'lines': 96, 'extension': 'gitignore', 'file_path': 'githubscrapper/.gitignore'}, {'file_name': 'README.md', 'bytes': 1100, 'lines': 30, 'extension': 'md', 'file_path': 'githubscrapper/README.md'}, {'file_name': 'requirements.txt', 'bytes': 97, 'lines': 7, 'extension': 'txt', 'file_path': 'githubscrapper/requirements.txt'}, {'file_name': 'webscrapperfiledetails.py', 'bytes': 5660, 'lines': 144, 'extension': 'py', 'file_path': 'githubscrapper/webscrapperfiledetails.py'}, {'file_name': 'webscrapperB.py', 'bytes': 5390, 'lines': 139, 'extension': 'py', 'file_path': 'githubscrapper/webscrapperB.py'}]

        expected_result = [{
            "bytes": 1100,
            "file_name": ".gitignore",
            "file_path": "githubscrapper/.gitignore",
            "lines": 96
          },
          {
            "bytes": 1100,
            "file_name": "README.md",
            "file_path": "githubscrapper/README.md",
            "lines": 30
          },
          {
            "bytes": 97,
            "file_name": "requirements.txt",
            "file_path": "githubscrapper/requirements.txt",
            "lines": 7
          },
          {
            "bytes": 5660,
            "file_name": "webscrapperfiledetails.py",
            "file_path": "githubscrapper/webscrapperfiledetails.py",
            "lines": 144
          },
          {
            "bytes": 5390,
            "file_name": "webscrapperB.py",
            "file_path": "githubscrapper/webscrapperB.py",
            "lines": 139
          }]

        result = webscrapperfiledetails.create_file_details_list(files)

        assert expected_result == result

    def test_aggregated_data(self):
        files = [{'file_name': '.gitignore', 'bytes': 1100, 'lines': 96, 'extension': 'gitignore', 'file_path': 'githubscrapper/.gitignore'}, {'file_name': 'README.md', 'bytes': 1100, 'lines': 30, 'extension': 'md', 'file_path': 'githubscrapper/README.md'}, {'file_name': 'requirements.txt', 'bytes': 97, 'lines': 7, 'extension': 'txt', 'file_path': 'githubscrapper/requirements.txt'}, {'file_name': 'webscrapperfiledetails.py', 'bytes': 5660, 'lines': 144, 'extension': 'py', 'file_path': 'githubscrapper/webscrapperfiledetails.py'}, {'file_name': 'webscrapperB.py', 'bytes': 5390, 'lines': 139, 'extension': 'py', 'file_path': 'githubscrapper/webscrapperB.py'}]

        expected_result = {
          "aggregated_data": {
            "gitignore": {
              "bytes": 1100,
              "bytes_percentage": 8.24,
              "lines": 96,
              "lines_percentage": 23.08
            },
            "md": {
              "bytes": 1100,
              "bytes_percentage": 8.24,
              "lines": 30,
              "lines_percentage": 7.21
            },
            "py": {
              "bytes": 11050,
              "bytes_percentage": 82.79,
              "lines": 283,
              "lines_percentage": 68.03
            },
            "txt": {
              "bytes": 97,
              "bytes_percentage": 0.73,
              "lines": 7,
              "lines_percentage": 1.68
            }
          },
          "total_bytes": 13347,
          "total_lines": 416
        }

        result = webscrapperfiledetails.aggregate_file_data(files)

        assert expected_result == result
