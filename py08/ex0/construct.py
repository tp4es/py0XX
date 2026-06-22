import sys
import os
import site


def detect_env() -> bool:
    return (sys.prefix != sys.base_prefix)


def ft_venv() -> None:
    print("=== SAFE TRAINING ENVIRONMENT ===")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual ENV: {os.path.basename(sys.exec_prefix)}")
    print(f"Package installation path: {site.getsitepackages()[0]}")


def ft_matrix() -> None:
    print("*¡NO Virtual Enviroment!*")
    print(f"Every changes may affect base sys: {sys.base_prefix}")


def ft_construct() -> None:
    if detect_env():
        ft_venv()
    else:
        ft_matrix()


if __name__ == "__main__":
    ft_construct()
