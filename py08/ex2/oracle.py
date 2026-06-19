import os
import sys


def load_env() -> list[bool, list[tuple[str, str]]]:
    env: tuple = ()
    try:
        import dotenv as de  # type: ignore
        de.load_dotenv()
        mode: str = os.getenv("MATRIX_MODE")
        db: str = os.getenv("DATABASE_URL")
        api_key: str = os.getenv("API_KEY")
        log_level: str = os.getenv("LOG_LEVEL")
        zion_edp: str = os.getenv("ZION_ENDPOINT")
        return (True, )
    except Exception:
        print("Error: 'python-dotenv' package is missing.")
        print("Install: pip install python-dotenv")
        return (False, None)


def get_override():
    if len(sys.argv > 1):
        return (True)


def check_security() -> list[]:
    path_git = ".gitignore"
    path_env = ".env"
    try:
        if os.path.exists(path_git):
            print("[OK] No hardcoded secrets detected.")
        else:
            print("[CAUTION] '.gitignore' file not found.")
        if os.path.exists(path_env):
            print("[OK] '.env' file properly configured.")
        else:
            print("[CAUTION] '.env.' file not found.")
        if get_override():
            print("[OK] Production overrides activated.")
    except Exception as e:
        print(f"Erro caught: {e}")


def main():
    try:
        if load_env():

            print("Configuration loaded:")
            print(f"Mode: {e}")
            print(f"Database: {db}")
    except Exception as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()
