from time import sleep

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

    def __str__(self):
        return self.title

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def add(self, *args):
        for video in args:
            if self.videos == []:
                self.videos.append(video)
            else:
                for v in self.videos:
                   if video.title != v.title:
                        self.videos.append(video)

    def get_videos(self, text):
        search_string = []
        for video in self.videos:
            if text.lower() in video.title.lower():
                search_string.append(video.title)
        return search_string

    def watch_video(self, film_title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        video = []
        for v in self.videos:
            if v.title == film_title:
                video = v
                break
        if video == []:
            print('Видео не найдено')
            return
        if self.current_user.age < 18 and video.adult_mode:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return
        for time_see in range(video.time_now + 1, video.duration + 1):
            print(time_see)
            sleep(1)
        video.time_now = 0
        print('Конец видео')

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

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')