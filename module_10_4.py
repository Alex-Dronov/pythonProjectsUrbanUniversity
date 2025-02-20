import threading, queue, time, random

class Table:
    def __init__(self, number, guest=None):
        self.number = int(number)
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.name = str(name)

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables_):
        self.tables = tables_
        self.queue = queue.Queue()

    def guest_arrival(self, *guests_):
        for gst in guests_:
            for tbl in self.tables:
                if tbl.guest is None:
                    tbl.guest = gst
                    gst.start()
                    print(f"{gst.name} сел(-а) за стол номер {tbl.number}")
                    break
            if not gst.is_alive():
                self.queue.put(gst)

    def discuss_guests(self):
        there_are_occupied_tables = True
        while not self.queue.empty() or there_are_occupied_tables:
            there_are_occupied_tables = False
            for tbl in self.tables:
                if tbl.guest is not None:
                    if tbl.guest.is_alive():
                        there_are_occupied_tables = True
                    else:
                        print(F"{tbl.guest.name} покушал(-а) и ушёл(ушла) \nСтол номер {tbl.number} свободен")
                        tbl.guest = None
                if tbl.guest is None and not self.queue.empty():
                    tbl.guest = self.queue.get()
                    print(f"{tbl.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {tbl.number}")
                    there_are_occupied_tables = True
                    tbl.guest.start()

        print("\nГостей больше нет. Кафе закрыто.")

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
