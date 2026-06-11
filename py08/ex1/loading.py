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
    return (ok, missing)


def main() -> None:
    with open("requirements.txt", "r") as read:
        modules: list[str] = read.readline().splitlines()
    check_deps(modules)


if __name__ == "__main__":
    main()
