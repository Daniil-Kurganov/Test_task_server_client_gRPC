from concurrent import futures
import logging
import grpc
import os
from protos import directorselection_pb2
from protos import directorselection_pb2_grpc

class GetInformationAboutDirectory(directorselection_pb2_grpc.GetInformationAboutDirectoryServicer):
    def get_size_format(self, int_bits: int, int_format=1024, string_suffix='B') -> str:
        '''Вычисление единиц измерения размера'''
        for string_prefix in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
            if type(int_bits) == list: int_bits = int_bits[0]
            if int_bits < int_format: return f'{int_bits:.2f}{string_prefix}{string_suffix}'
            int_bits /= int_format
        return f'{int_bits:.2f}Y{string_suffix}'

    def get_directory_size(self, string_path: str) -> list:
        '''Вычисление общего размера директории и создания пар вида "файл/поддиректория - размер"'''
        list_output_informtion = [0]
        int_curren_direction_size, int_currnt_file_size = 0, 0
        try:
            for element in os.scandir(string_path):
                if element.is_file():
                    int_current_file_size = element.stat().st_size
                    list_output_informtion[0] += int_current_file_size
                    list_output_informtion.append(element.name + ' ' + self.get_size_format(int_curren_direction_size))
                elif element.is_dir():
                    int_curren_direction_size = self.get_directory_size(element.path)
                    list_output_informtion[0] += int_curren_direction_size[0]
                    list_output_informtion.append(element.name + ' ' + self.get_size_format(int_curren_direction_size[0]))
        except NotADirectoryError: return element.path.getsize(string_path)
        except PermissionError: return 0
       # list_output_informtion[0] = str(list_output_informtion[0])
        return list_output_informtion
    def DirectoryCall(self, request, context):
        string_directory_path = request.string_directory_path
        if os.path.isdir(string_directory_path):
            print('\nНачало обработки запроса: {}'.format(string_directory_path))
            list_message = self.get_directory_size(string_directory_path)
            list_message[0] = self.get_size_format(list_message[0])
            print('Запрос успешно обработан. Отправка ответа клиенту.')
            return directorselection_pb2.Reply(message = '|'.join(list_message))
        else:
            print('\nОбработка запроса "{}" завершилась ошибкой. Отправка отчёта клиенту.'.format(string_directory_path))
            return directorselection_pb2.Reply(message = 'Данная директория не существует. Повторите запрос, изменив входные данные.')

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    directorselection_pb2_grpc.add_GetInformationAboutDirectoryServicer_to_server(GetInformationAboutDirectory(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Сервер запущен. Прослушивается порт: " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()