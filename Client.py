from __future__ import print_function
import logging
import grpc
import re
from protos import directorselection_pb2
from protos import directorselection_pb2_grpc

def client_work() -> None:
    while True:
        string_input_path = input('\nВведите путь к директории для получения информации или "Exit" для завершения работы: ')
        re_pattern_path = re.compile(r'([A-Za-z]:\\)((?:.*\\)?)')
        if string_input_path == 'Exit':
            print('Завершение работы клиента. До свидания.')
            return 0
        elif re_pattern_path.match(string_input_path):
            print("Попытка запроса к серверу")
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = directorselection_pb2_grpc.GetInformationAboutDirectoryStub(channel)
                response = stub.DirectoryCall(directorselection_pb2.Request(string_directory_path = string_input_path))
                string_responce = response.message
                if string_responce != 'Данная директория не существует. Повторите запрос, изменив входные данные.':
                    list_output = string_responce.split('|')
                    print('Запрос успешно выполнен.\nПолучен ответ от сервера.')
                    print('Сведения о файлах и поддиректориях:\n Общий размер директории: {}'.format(list_output[0]))
                    for element in list_output[1:]:
                        print(' {}'.format(element))
                else: print(string_responce)
        else: print('Процесс выполнения запроса завершился ошибкой.\nВходные данные некорректны. Повторите попытку ввода.\n')

if __name__ == "__main__":
    logging.basicConfig()
    client_work()