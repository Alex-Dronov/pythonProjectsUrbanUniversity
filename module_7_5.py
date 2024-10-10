import os, time

directory = r"C:\Users\1\PycharmProjects\pythonProjectsUrbanUniversity"

for root, dirs, files in os.walk(directory):
  for file in files:
      if file.find('module_') > -1:
          filepath = os.path.join(root, file)
          filetime = os.path.getmtime(filepath)
          formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
          filesize = os.path.getsize(filepath)
          parent_dir = os.path.dirname(filepath)
          print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
