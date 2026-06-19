import os


def load_env():
    pass


def main():
    try:
        from dotenv import load_dotenv  # type: ignore
    except Exception:
        print("Error: 'python-dotenv' package is missing.")
        print("Install: pip install python-dotenv")
        SystemExit
    print("Continue")


if __name__ == "__main__":
    main()
