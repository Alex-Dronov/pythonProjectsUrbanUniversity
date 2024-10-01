import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):

        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                break
        if self.current_user is None:
            print('Пользователь не найден.')

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        if self.users.__len__() > 0:
            user_not_exists = True

            for user in self.users:
                if nickname == user.nickname:
                    print(f"Пользователь {nickname} уже существует")
                    user_not_exists = False
                    break

            if user_not_exists:
                new_user = User(nickname, password, age)
                self.users.append(new_user)
                self.current_user = new_user

        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def add(self, *new_videos):
        video_not_exists = True
        for new_video in new_videos:
            for video in self.videos:
                if video.title == new_video.title:
                    video_not_exists = False
                    break
            if video_not_exists:
                self.videos.append(new_video)

    def get_videos(self, search_word):
        videos_on_demand = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                videos_on_demand.append(video.title)
        return videos_on_demand

    def watch_video(self, search_title):
        if self.current_user is not None:
            for video in self.videos:
                if video.title == search_title:
                    if video.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        while video.time_now < video.duration:
                            video.time_now += 1
                            print(video.time_now,end = ' ')
                            time.sleep(1.0)
                        print(f"\"Конец видео\"")
                        video.time_now = 0

                    break # Exit from loop "for video in self.videos:"
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')