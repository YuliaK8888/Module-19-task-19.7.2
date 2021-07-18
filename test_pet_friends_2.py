from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_user_with_invalid_email(password=valid_password, invalid_email="yuk@gmail.ru"):
  """проверяем, что запрос api ключа возвращает статус 403 и в результате нет слова ¨key¨"""

  # отправляем запрос и сохраняем ответ статус кода в status, а текст в result
  status, result = pf.get_api_key(invalid_email, password)

  # сверяем полученные данные с ожиданиемым результатом

  assert status == 403
  assert 'key' not in result


def test_get_api_key_for_user_with_empty_email(password=valid_password, empty_email=""):
  """проверяем, что запрос api ключа возвращает статус 403 и в результате нет слова ¨key¨"""

  # отправляем запрос и сохраняем ответ статус кода в status, а текст в result
  status, result = pf.get_api_key(empty_email, password)

  # сверяем полученные данные с ожиданиемым результатом
  assert status == 403
  assert 'key' not in result


def test_get_api_key_for_user_with_invalid_password(invalid_password="0172839", email=valid_email):
  """проверяем, что запрос api ключа возвращает статус 403 и в результате нет слова ¨key¨"""

  # отправляем запрос и сохраняем ответ статус кода в status, а текст в result
  status, result = pf.get_api_key(valid_email, invalid_password)

  # сверяем полученные данные с ожиданиемым результатом

  assert status == 403
  assert 'key' not in result

def test_get_api_key_for_user_with_empty_password(email=valid_email, empty_password=""):
  """проверяем, что запрос api ключа возвращает статус 403 и в результате нет слова ¨key¨"""

  # отправляем запрос и сохраняем ответ статус кода в status, а текст в result
  status, result = pf.get_api_key(valid_email, empty_password)

  # сверяем полученные данные с ожиданиемым результатом

  assert status == 403
  assert 'key' not in result

def test_get_api_key_for_user_with_invalid_email_and_password(invalid_email="78&^%%", invalid_password="0000000"):
  """проверяем, что запрос api ключа возвращает статус 403 и в результате нет слова ¨key¨"""

  # отправляем запрос и сохраняем ответ статус кода в status, а текст в result
  status, result = pf.get_api_key(invalid_email, invalid_password)

  # сверяем полученные данные с ожиданиемым результатом

  assert status == 403
  assert 'key' not in result


def test_get_all_pets_with_invalid_filter(filter='name'):
  """проверяем, что фильтр не выдаёт список питомцев, если указан параметр не существующего функционала фильтра."""


  # получаем api ключ и сохраняем его в переменную auth_key
  _, auth_key = pf.get_api_key(valid_email, valid_password)
  status, result = pf.get_list_of_pets(auth_key, filter)

  # сверяем полученные данные с ожиданиемым результатом
  assert status == 500
  assert 'pets' not in result

def test_get_all_pets_with_valid_key(filter='my_pets'):
  """проверяем, что фильтр выдаёт список питомцев, если указан правильный auth_key и проверяем, что список не пустой.
   доступные значения параметра фильтр: '', либо 'my_pets' """

  # получаем api ключ и сохраняем его в переменную auth_key
  _, auth_key = pf.get_api_key(valid_email, valid_password)
  status, result = pf.get_list_of_pets(auth_key, filter)

  # сверяем полученные данные с ожиданиемым результатом
  assert status == 200
  assert len(result['pets'])


def test_get_all_pets_with_invalid_filter_animal_type(filter='animal_type'):
  """проверяем, что фильтр не выдаёт список питомцев, если указан параметр не существующего функционала фильтра."""


  # получаем api ключ и сохраняем его в переменную auth_key
  _, auth_key = pf.get_api_key(valid_email, valid_password)
  status, result = pf.get_list_of_pets(auth_key, filter)

  # сверяем полученные данные с ожиданиемым результатом
  assert status == 500
  assert 'pets' not in result

def test_get_all_pets_with_invalid_filter_age(filter='age'):
  """проверяем, что фильтр не выдаёт список питомцев, если указан параметр не существующего функционала фильтра."""


  # получаем api ключ и сохраняем его в переменную auth_key
  _, auth_key = pf.get_api_key(valid_email, valid_password)
  status, result = pf.get_list_of_pets(auth_key, filter)

  # сверяем полученные данные с ожиданиемым результатом
  assert status == 500
  assert 'pets' not in result

def test_get_list_of_pets_with_wrong_auth_key(filter= ''):
  """проверяем невозможность получение списка питомцев, при введении неправильного api ключа"""
  # получаем api ключ и сохраняем его в переменную auth_key

  _, auth_key = pf.get_api_key(valid_email, valid_password)

  if auth_key:
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

  else:
    assert status == 403
    raise Exception("не верный авторизационный ключ и вывести список питомцев невозможно")