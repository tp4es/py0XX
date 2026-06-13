import sys
import importlib


def check_deps(deps: list[str]) -> list[str]:
    ok = []
    missing = []
    for dep in deps:
        try:
            module = importlib.import_module(dep)
            ok.append(module)
            print(f"{dep.capitalize()} ({module.__version__})")
        except ImportError as e:
            print(f"{dep.capitalize()} module NOT FOUND.")
            missing.append(dep)
    if len(missing) > 0:
        print("1- Install using pip:\n  pip install -r requirements.txt")
        print("2- Install using Poetry:\n  poetry install")
    return (ok, missing)


def main() -> None:
    with open("requierements.txt", "r") as read:
        lines: list[str] = read.readlines()
    modules = list()
    for line in lines:
        modules.append(line.strip(" ").strip("\n"))
    check_deps(modules)


if __name__ == "__main__":
    main()
