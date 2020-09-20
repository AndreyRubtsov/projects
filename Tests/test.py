FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']


def show_count_friends(count_friends):
    text= 'У тебя ' + str(count_friends) + ' друзей'
    return text

def process_query(query):
    if query == 'Сколько у меня друзей?':
        count = len(FRIENDS)
        return show_count_friends(count)



# Внимание! Это те самые вызовы, которые не надо трогать
print(process_query('Сколько у меня друзей?'))
