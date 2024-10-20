from pathlib import Path

import tests


def get_path(file_name: str):
    return str(Path(tests.__file__).parent.parent.joinpath(f'resources/{file_name}'))
