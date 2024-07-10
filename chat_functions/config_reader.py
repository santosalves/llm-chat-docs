from json import load
from sys import _getframe as getfile


class ConfigReader:
    def __init__(self, file_path):
        self._config = None
        self._file_name = getfile(1).f_code.co_filename

        file = str(self._file_name).split('/')[-1]
        try:
            with open(file_path, 'r') as config_file:
                self._config = load(config_file)
        except FileNotFoundError:
            if file == 'chat.py':
                print(ConfigReader.msg('app_config.json'))

            elif file == 'ram_rag.py':
                print(ConfigReader.msg('rag_config.json'))
    

    def msg(text):
        msg = f'''
        \033[93mArquivo de configuração não encontrado. Crie um arquivo chamado 
        \033[91m{text} \033[93mna pasta 'conf' do projeto com as configurações.\033[0m
        '''

        return msg


    def get_config(self):
        return self._config
