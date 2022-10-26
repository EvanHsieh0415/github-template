from os import listdir
from json import load, dump

# SEARCH `.code-workspace`
def FIND_WORKSPACE_SETTING(find_dir: str=None, base_dir='../') -> dict:
    find_dir = find_dir or listdir('../')
    for filename in find_dir:
        if filename.endswith('.code-workspace'):
            with open(f'{base_dir}{filename}', encoding='utf8') as file:
                return load(file)
    raise FileNotFoundError('Can\'t find workspace configuration file, the file name should be "*.code-workspace"')

# GENERATE `.vscode/config`
def GENERATE_SEPARATE_CONFIG(workspace_config: dict=FIND_WORKSPACE_SETTING()) -> None:
    for filename, data in workspace_config.items():
        with open(f'{filename}.json', 'w', encoding='utf8') as file:
            dump(data, file, indent=2, ensure_ascii=False, sort_keys=True)

GENERATE_SEPARATE_CONFIG()