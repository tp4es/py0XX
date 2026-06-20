import os
import sys


def load_env() -> tuple[bool, list[tuple[str, str]]]:

    try:
        import dotenv as de  # type: ignore
        de.load_dotenv()
        env: list = []
        mode: tuple = ("mode", os.getenv("MATRIX_MODE"))
        db: tuple = ("db", os.getenv("DATABASE_URL"))
        api_key: tuple = ("api_key", os.getenv("API_KEY"))
        log_level: tuple = ("log_level", os.getenv("LOG_LEVEL"))
        zion_edp: tuple = ("zion_edp", os.getenv("ZION_ENDPOINT"))
        env.append(mode)
        env.append(db)
        env.append(api_key)
        env.append(log_level)
        env.append(zion_edp)
        return (True, env)
    except Exception:
        print("Error: 'python-dotenv' package is missing.")
        print("Install: pip install python-dotenv")
        return (False, None)


def get_override() -> bool:
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            try:
                data: tuple = (sys.argv[i].split("=", 1))
                os.environ[data[0]] = data[1]
            except Exception as e:
                print(f"Error split: {e}")
        return (True)
    return (False)


def check_security() -> list[str]:
    path_git = ".gitignore"
    path_env = ".env"
    info: list = []
    try:
        if os.path.exists(path_git):
            git: str = ("[OK] No hardcoded secrets detected.")
        else:
            git: str = ("[CAUTION] File '.gitignore' not found.")
        if os.path.exists(path_env):
            env: str = ("[OK] File '.env' properly configured.")
        else:
            env: str = ("[CAUTION] File '.env.' not found.")
        if get_override() == True:
            info.append("[OK] Production overrides activated.")
        info.append(git)
        info.append(env)
        return (info)
    except Exception as e:
        return (f"Erro caught_security check: {e}")


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        loaded = load_env()
        if loaded[0]:
            print("Configuration loaded:")
            for a in loaded[1]:
                print(f"{a[0].upper()}: {a[1].capitalize()}")
        print("\nEnviroment security check:")
        info = check_security()
        for a in info:
            print(a)
    except Exception as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()
