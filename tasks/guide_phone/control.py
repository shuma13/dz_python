from random import choice
from unittest import mock
import view, model

def start():
    choice = 1
    while choice != 9:
        choice = view.show_menu()
        match(choice):
            case 0:
                phone_book = model.get_phone_book()
                view.show_phone_book(phone_book)
            case 1:
                path =view.input_path()
                model.open_file(path)
            case 2:
                path =view.input_path_record()
                model.record_file(path)
            case 3:
                contackt = view.input_contackt()
                model.new_contack(contackt)
            case 4:
                contackt = view.input_change()
                model.chage_contackt(*contackt)
            case 5:
                id = view.input_delete()
                model.delete_contackt(id)
            case 6:
                my_search = view.input_search()
                model.search_contackt(*my_search)
                search_phone_book = model.get_search_phone_book()
                view.show_Search_phone_book(search_phone_book)

