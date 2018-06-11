import json
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup


def byte_conversion(index_value, index_unit, file_info_contents):
    """Convert the file size into bytes given a size value and a byte unit.

    Arguments:
    file_info_contents: A list containing the splited header of file information from github
    index_unit: The index value of the unit text at the file_info_contents
    index_value: The index value of the bytes text at the file_info_contents

    Github file pages differ in their information header.
    Therefore we use the correct index of the splited header to retrieve the size and unit.

    Returns:
    A flot number representing the file size in bytes

    """

    if (file_info_contents[index_unit] == 'GB'):
        number_of_bytes = round(float(file_info_contents[index_value]) * 1000000000, 3)
    elif (file_info_contents[index_unit] == 'MB'):
        number_of_bytes = round(float(file_info_contents[index_value]) * 1000000, 3)
    elif (file_info_contents[index_unit] == 'KB'):
        number_of_bytes = round(float(file_info_contents[index_value]) * 1000, 3)
    else:
        number_of_bytes = float(file_info_contents[index_value])

    return number_of_bytes


def retrieve_file_information(url):
    """Retrieve the file information header from a file page on github.

    Arguments:
    url: An url for a file page on github

    Returns:
    A dictionary containing the following keys and values:
    lines: An interget of the number of lines on the file
    bytes: A float of the bytes size of the file
    extenstion: The file extenstion
    file_path: The file path based on the breadcumb of the page
    file_name: The full name of the file with its extenstion
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    file_info = soup.find(class_='file-info')
    is_executable = file_info.find('span', class_='file-mode')

    if is_executable:
        is_executable.decompose()

    file_info_contents = file_info.get_text(' ', strip=True).split()

    # This is a file that do not have a number of lines or sloc such as an .enc
    if len(file_info_contents) == 2:
        number_of_bytes = byte_conversion(0, 1, file_info_contents)
        number_of_lines = 0
    # Other files that have them have a different composition of the file info header
    # If new files headers are created they should be addressed here
    else:
        number_of_lines = file_info_contents[0]
        number_of_bytes = byte_conversion(4, 5, file_info_contents)

    file_name = soup.find('strong', class_='final-path').get_text()
    file_extension = file_name.split('.')[-1:][0]
    file_path = soup.find(class_='breadcrumb').get_text().strip('\n')

    return {'lines': int(number_of_lines), 'bytes': float(number_of_bytes), 'extension': file_extension, 'file_path': file_path, 'file_name': file_name}


def iterate_over_director_tree(url):
    """Enters a link in the page project table to retrieve its information and extend a list. Uses recursive function to navigate through folder links.

    Arguments:
    url: An url for a project page on github

    Returns:
    A list of dictionaries contaning the information of each file page found on the project. The dictionaries are created by the retrieve_file_information function.
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    files = []

    file_tree_table = soup.find(class_='files')

    have_up_tree = file_tree_table.find(class_='up-tree')

    if have_up_tree:
        have_up_tree.decompose()

    files_list = file_tree_table.find_all(class_='js-navigation-item')

    # If github changes how to identify folders and files, or add a new type change it here
    for file in files_list:
        if (file.find('svg').get('class')[1] == 'octicon-file'):
            url = 'https://github.com/' + file.find('a', class_='js-navigation-open').get('href')
            files.append(retrieve_file_information(url))
        else:
            url = 'https://github.com/' + file.find('a', class_='js-navigation-open').get('href')
            files.extend(iterate_over_director_tree(url))

    return files


def create_file_details_list(files):
    """Creates an list of dictionaries sorted by its file_path key.

    Arguments:
    files: A list of dictionaries contaning the file information

    Returns:
    A list of dictionaries sorted by their file_path key. The dictionary keys and values are the following:
    file_name: Complete file name with extenstion
    lines: number of lines of the file
    bytes: number of bytes of the file
    file_path: the path inside the project that the file exists
    """

    file_details = []

    for file in files:
        file_details.append({'file_name': file['file_name'], 'lines': file['lines'], 'bytes': file['bytes'], 'file_path': file['file_path']})

    ordered_details = sorted(file_details, key=lambda x: x['file_path'])

    return ordered_details


def aggregate_file_data(files):
    """Aggregate the project files infomration in a dictionary.

    Arguments:
    files: A list of dictionaries contaning the file information

    Returns:
    A dictionary contaning the following keys and values:
    total_lines: The total lines existing in the whole project
    total_bytes: The total bytes from all files in the project.
    aggregated_data: a collection of dictionaries for each of the file extensions found in the projectself.
        Example of the nested dictionaries:
        {"file_extension": {
            "bytes":  total number of bytes from files of that extenstion
            "lines": total number of lines from files of that extention
            }
        }
    """

    bytes_and_lines = {}
    total_bytes = 0
    total_lines = 0

    for file in files:
        total_bytes += file['bytes']
        total_lines += file['lines']

        if file['extension'] not in bytes_and_lines:
            bytes_and_lines[file['extension']] = {'bytes': file['bytes'], 'lines': file['lines']}
        else:
            bytes_and_lines[file['extension']]['bytes'] += file['bytes']
            bytes_and_lines[file['extension']]['lines'] += file['lines']

    for extension in bytes_and_lines:
        bytes_and_lines[extension]['bytes_percentage'] = round(bytes_and_lines[extension]['bytes']*100/total_bytes, 2)
        bytes_and_lines[extension]['lines_percentage'] = round(bytes_and_lines[extension]['lines']*100/total_lines, 2)

    return({'total_bytes': total_bytes, 'total_lines': total_lines, 'aggregated_data': bytes_and_lines})


def report_creator(url, repository):
    """Creates a file report of the repository

    Arguments:
    url: An url of a github project
    repository: The repository name

    Returns:
    Nothing. The output is a .txt file contaning the Project Name, its file details, and aggregated_data
    """

    project = repository.split('/')[-1:][0]
    file_name = '{}.txt'.format(project)
    files = iterate_over_director_tree(url)
    aggregated_data = aggregate_file_data(files)
    directory_tree = create_file_details_list(files)

    with open(file_name, 'w+') as outfile:
        outfile.write('Project: {}\n'.format(repository))
        outfile.write('File Details\n'.format(repository))
        json.dump(directory_tree, outfile, indent=2, sort_keys=True)
        outfile.write('\nProject Data\n'.format(repository))
        json.dump(aggregated_data, outfile, indent=2, sort_keys=True)
        outfile.close()


def webscrapper():
    """Scraps multiple github projects.

    Arguments:
    None. Uses a repositories.txt file to collect the projects directories.

    Returns:
    Nothing. The output is delegated to the report_creator function
    """

    function_arguments = []
    with open('repositories.txt', 'r') as f:
        repositories = [line.strip() for line in f]

    for repository in repositories:
        url = 'https://github.com/' + repository
        function_arguments.append((url, repository))

    with Pool(5) as pool:
        pool.starmap(report_creator, function_arguments)


if __name__ == "__main__":
    webscrapper()
