import time
from multiprocessing import Pool

def  read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as long_file:
        line_ = long_file.readline()
        while line_ != '':
            all_data.append(line_)
            line_ = long_file.readline()

filenames = [f'./Module 10/file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = time.time()
for file_ in filenames:
    read_info(file_)
# или так: list(map(read_info, filenames))
end_time = time.time()
elapsed_ = round(end_time - start_time, 6)
print(elapsed_, "секунды (Линейный)")

# Мультипроцессный
if __name__ == '__main__':
    start_time = time.time()
    with Pool() as p:
        p.map(read_info, filenames)
    end_time = time.time()
    elapsed_ = round(end_time - start_time, 6)
    print(elapsed_, "секунды (Мультипроцессный)")