import os

root_path = 'templates'
static_files = []
html_files = []
for root, dirs, files in os.walk(root_path):
    for name in files:
        file_path = os.path.join(root, name)
        if '.html' in file_path:
            html_files.append(file_path)
        else:
            static_files.append(file_path[len(root_path) + 1:])
print(static_files, html_files, sep='\n')

for file_name in html_files:
    with open(file_name, 'r') as f:
        old_data = f.read()

    new_data = "{% load static %}\n" + old_data
    for static_file_name in static_files:
        new_data = new_data.replace(static_file_name, "{% static '" + static_file_name + "' %}")
    for html_file_name in html_files:
        new_data = new_data.replace(html_file_name[len(root_path) + 1:], "{% url '" + html_file_name[len(root_path) + 1: -5] + "' %}")

    with open(file_name, 'w') as f:
        f.write(new_data)
