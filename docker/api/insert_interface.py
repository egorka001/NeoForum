import sys
sys.path.append('../database/')
import base_insert


def insert_new_thread(db_name, post_text, theme):
    base_insert.insert_new_thread(db_name, post_text, theme)


def insert_new_post(db_name, thread_id, post_text):
    out = base_insert.insert_new_post(db_name, thread_id, post_text)

if __name__ == "__main__":
    insert_new_thread('../api/base.db', 'Первый тред о спорте', 'Спорт')
    insert_new_thread('../api/base.db', 'Первый тред о животных', 'Животные')

    insert_new_thread('../api/base.db', 'Первый тред о программировании', 
                        'Программирование')
    insert_new_thread('../api/base.db', 'Первый тред о велосипедах', 
                                        'Велосипеды')
    insert_new_thread('../api/base.db', 'Первый тред о музыке', 
                                        'Музыка')
    insert_new_thread('../api/base.db', 'Первый тред о фильмах', 
                                        'Фильмы')
    insert_new_thread('../api/base.db', 'Первый тред о книгах', 
                                        'Книги')
    insert_new_thread('../api/base.db', 'Первый тред о электронике', 
                                        'Электроника')
    insert_new_thread('../api/base.db', 'Первый тред оффтопа', 
                                        'Оффтоп')
