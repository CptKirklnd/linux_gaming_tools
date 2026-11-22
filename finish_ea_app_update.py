# performs the second half of updating the EA app on linux
# did this take longer to write than it would have been to just do it myself? very much.
# inspired by: https://forums.lutris.net/t/update-process-for-ea-app/20335/4

import re, shutil

from pathlib import Path

EA_DESKTOP_DIR = "/home/cam/Games/ea-app/drive_c/Program Files/Electronic Arts/EA Desktop/"
SEMVER_PATTERN = re.compile(r"^(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)$")

def is_semver(input: str) -> bool:
    return bool(SEMVER_PATTERN.fullmatch(input))

def parse_version(v: str) -> tuple[int, ...]:
    return tuple(int(part) for part in v.split("."))

def main():
    ea_app_directory = Path(EA_DESKTOP_DIR)
    dirs: list[str] = [item.name for item in ea_app_directory.iterdir() if item.is_dir() and is_semver(item.name)]

    latest_version: str = sorted(dirs, key=parse_version)[-1]
    eadt_folder = Path(EA_DESKTOP_DIR + latest_version)

    shutil.copytree(
        eadt_folder,
        ea_app_directory,
        dirs_exist_ok=True
    )
    shutil.rmtree(str(ea_app_directory)+"/EA Desktop?")


if __name__ == "__main__":
    main()