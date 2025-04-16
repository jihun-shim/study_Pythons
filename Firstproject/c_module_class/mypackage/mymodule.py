from random import choice
def get_weather():
    today = ['맑음','비','눈','폭우','돌풍','따뜻']
    return choice(today)
print(get_weather())