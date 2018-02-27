import os
import shutil

class CyWECLI():
    

    def __init__(self):
        super().__init__()
        self._arg_dict = {}
    
    def start(self):
        print('\n This CLI helps your rapidly create your own game. \n')
        self.get_input('name', 'Your cyberwar folder name:\n')
        self.get_input('cywe_path', 'Your local CyWE path: (Don\'t use "~")\n')
        self.get_input('pypy_path', 'Your local pypy path: (Don\'t use "~")\n')
        self.get_input('cc', 'Your C&C folder name: (leave blank for not creating C&C)\n')


    def processing(self):
        os.mkdir(self._arg_dict['name'])
        os.system('cp {}/python/game/samples/simple_player_object_types.ini {}'.format(self._arg_dict['cywe_path'], self._arg_dict['name']))
        os.system('cp {}python/game/src/cyberwar/braininterface/translations.py {}'.format(self._arg_dict['cywe_path'], self._arg_dict['name']))
        os.system('cp {}/python/game/samples/simple_player_object_types.ini {}'.format(self._arg_dict['cywe_path'], self._arg_dict['name']))
        os.system('cp {}/python/game/samples/simple_player_object_types.ini {}'.format(self._arg_dict['cywe_path'], self._arg_dict['name']))
    
    def get_input(self, key, prompt):
        tmp = ''
        while True:
            tmp = input(prompt).strip()
            if key == 'name':
                if len(tmp) > 0:
                    break
                else:
                    prompt = 'Please specify your folder name:\n'
            elif key == 'cywe_path' or key == 'pypy_path':
                if os.path.exists(tmp):
                    break
                else:
                    prompt = 'Path does not exist, input again:\n'
            else:
                break
        self._arg_dict[key] = tmp

def main():
    cli = CyWECLI()
    cli.start()
    print(cli._arg_dict)

if __name__ == '__main__':
    main()