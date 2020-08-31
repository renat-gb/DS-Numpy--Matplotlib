import pandas as pd

# Задание 1

a_dic = {'author_id': [1, 2, 3],
         'author_name': ['Тургенев', 'Чехов', 'Островский']}
authors = pd.DataFrame(a_dic)
print(authors)
print('-' * 50)

b_dic = {'author_id': [1, 1, 1, 2, 2, 3, 3],
         'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо',
                        'Толстый и тонкий', 'Дама с собачкой', 'Гроза',
                        'Таланты и поклонники'],
         'price': [450, 300, 350, 500, 450, 370, 290]}
book = pd.DataFrame(b_dic)
print(book)
print('-' * 50)

# Задание 2

authors_price = pd.merge(authors, book, on='author_id', how='inner')
print(authors_price)
print('-' * 50)

# Задание 3

top_5 = authors_price.nlargest(5, 'price')
print(top_5)
print('-' * 50)

# Задание 4

mid_res = {'author_name': ['Тургенев', 'Чехов', 'Островский'],
           'min_price': authors_price['price'].min(),
           'max_price': authors_price['price'].max(),
           'mean_price': round(authors_price['price'].mean(), 2)}

final_res = pd.DataFrame(mid_res)
print(final_res)

