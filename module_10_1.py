import time, threading

def write_words(word_count, file_name):
    start_time = time.time()
    with (open(file_name, 'w', encoding='utf-8') as file):
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i} \n")
            time.sleep(0.1)
            i += 1
        end_time = time.time()
        elapsed = round(end_time - start_time, 6)
        print(f"Завершилась запись в файл {file_name}")
        print(f"Функция write_words работала с файлом {file_name} - {elapsed} секунд(ы)")

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

thread1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=write_words, args=(100, "example8.txt"))

print(f"Старт работы потока № 1: {time.strftime('%H:%M:%S',time.localtime(time.time()))}")
thread1.start()
thread1.join()
print(f"Окончание работы потока № 1: {time.strftime('%H:%M:%S',time.localtime(time.time()))}")
print(f"Старт работы потока № 2: {time.strftime('%H:%M:%S',time.localtime(time.time()))}")
thread2.start()
thread2.join()
print(f"Окончание работы потока № 2: {time.strftime('%H:%M:%S',time.localtime(time.time()))}")
print(f"Старт работы потока № 3: {time.strftime('%H:%M:%S',time.localtime(time.time()))}")
thread3.start()
thread3.join()
print(f"Окончание работы потока № 3: {time.strftime('%H:%M:%S',time.localtime(time.time()))}")
print(f"Старт работы потока № 4: {time.strftime('%H:%M:%S',time.localtime(time.time()))}")
thread4.start()
thread4.join()
print(f"Окончание работы потока № 4: {time.strftime('%H:%M:%S',time.localtime(time.time()))}")