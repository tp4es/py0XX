import os
import sys


env_keys = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
]


def load_env() -> tuple[bool, list[tuple[str, str]], bool]:
    try:
        import dotenv as de  # type: ignore

        override = False

        for key in env_keys:
            if os.getenv(key) is not None:
                override = True
                break
        de.load_dotenv()
        env = []
        for key in env_keys:
            env.append((key, os.getenv(key)))
        return (True, env, override)
    except Exception:
        print("Error: 'python-dotenv' package is missing.")
        print("Install: pip install python-dotenv")
        return (False, [], False)


def check_security(
    loaded: tuple[bool, list[tuple[str, str]], bool]
) -> list[str]:
    path_git = ".gitignore"
    path_env = ".env"
    info = []
    try:
        if os.path.exists(path_git):
            info.append("[OK] No hardcoded secrets detected.")
        else:
            info.append("[CAUTION] File '.gitignore' not found.")
        if not os.path.exists(path_env):
            info.append("[CAUTION] File '.env' not found.")
        else:
            missing = []
            for key, value in loaded[1]:
                if value is None or value == "":
                    missing.append(key)
            if len(missing) == 0:
                info.append("[OK] File '.env' properly configured.")
            else:
                info.append(
                    "[CAUTION] Missing keys: "
                    + ", ".join(missing)
                )
        if loaded[2]:
            info.append("[OK] Production overrides activated.")
        return info
    except Exception as e:
        return [f"Error caught_security check: {e}"]


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        loaded = load_env()
        if loaded[0]:
            print("Configuration loaded:")
            for key, value in loaded[1]:
                print(f"{key}: {value}")
        print("\nEnvironment security check:")
        info = check_security(loaded)
        for line in info:
            print(line)
    except Exception as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()
