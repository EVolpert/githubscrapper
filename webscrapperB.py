import requests
from bs4 import BeautifulSoup
import json


# This function receives the information header from a file page and the position of the byte size and Unit
# We need the position due to github having different headers for specific file types such as .enc
def byte_conversion(position_value, position_unit, file_info_contents):
    if (file_info_contents[position_unit] == 'GB'):
        number_of_bytes = round(float(file_info_contents[position_value]) * 1000000000, 3)
    elif (file_info_contents[position_unit] == 'MB'):
        number_of_bytes = round(float(file_info_contents[position_value]) * 1000000, 3)
    elif (file_info_contents[position_unit] == 'KB'):
        number_of_bytes = round(float(file_info_contents[position_value]) * 1000, 3)
    else:
        number_of_bytes = float(file_info_contents[position_value])

    return number_of_bytes


# This functions extracts from a file page its relevant informations and returns it as a dictionary
def get_lines_and_bytes(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    file_info = soup.find(class_='file-info')
    is_executable = file_info.find('span', class_='file-mode')

    if is_executable:
        is_executable.decompose()

    file_info_contents = file_info.get_text(' ', strip=True).split()

    if len(file_info_contents) == 2:
        number_of_bytes = byte_conversion(0, 1, file_info_contents)
        number_of_lines = 0
    else:
        number_of_lines = file_info_contents[0]
        number_of_bytes = byte_conversion(4, 5, file_info_contents)

    file_name = soup.find('strong', class_='final-path').get_text()
    file_extension = file_name.split('.')[-1:][0]

    return {'lines': int(number_of_lines), 'bytes': int(number_of_bytes), 'extension': file_extension, 'file_name': file_name}


# This functions iterates over the file tree on github
# If it's a file link it passes the url to the get_lines_and_bytes function and apppend that result to a list
# If i'ts a folder link it recursive call's itself to initiate a new crapping for the files on that folder
def iterate_over_director_tree(url, file_name, level=1):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    files = []

    file_tree_table = soup.find(class_='files')

    have_up_tree = file_tree_table.find(class_='up-tree')

    if have_up_tree:
        have_up_tree.decompose()

    files_list = file_tree_table.find_all(class_='js-navigation-item')

    for file in files_list:
        if (file.find('svg').get('class')[1] == 'octicon-file'):
            url = 'https://github.com/' + file.find('a', class_='js-navigation-open').get('href')
            file_info = get_lines_and_bytes(url)
            files.append(file_info)
            with open(file_name, 'a') as outfile:
                outfile.write('|_'*level + file_info['file_name'] + '(' + str(file_info['lines']) + ' lines)\n')
                outfile.close()
        else:
            url = 'https://github.com/' + file.find('a', class_='js-navigation-open').get('href')
            folder_name = url.split('/')
            with open(file_name, 'a') as outfile:
                outfile.write('|_'*level + '[' + folder_name[-1] + ']\n')
                outfile.close()
            files.extend(iterate_over_director_tree(url, file_name, level+1))

    return files


# This functions aggregate the file size and lines for a given extension as well as the total bytes and lines of the project
def aggregate_file_data(files):
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
    project = repository.split('/')[-1:][0]
    file_name = '{}.txt'.format(project)

    report_file = open(file_name, 'w+')
    report_file.write('Project: {}\n\nDirectory Tee:\n[{}]\n'.format(repository, project))
    report_file.close()

    files = iterate_over_director_tree(url, file_name)
    aggregated_data = aggregate_file_data(files)

    with open(file_name, 'a') as outfile:
        outfile.write('\nProject Data:\n'.format(repository))
        json.dump(aggregated_data, outfile, indent=2, sort_keys=True)
        outfile.close()


def webscrapper():
    with open('repositories.txt', 'r') as f:
        repositories = [line.strip() for line in f]

    for repository in repositories:
        url = 'https://github.com/' + repository
        report_creator(url, repository)


webscrapper()
