#!/usr/bin/env python3


def secure_archive(file, mode="r", content=None) -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(file, mode) as f:
                data = f.read()
            return (True, data)
        elif mode == "w":
            with open(file, "w") as f:
                f.write(content if content else "")
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid mode. Use 'r' or 'w'.")
    except Exception as e:
        return (False, str(e))


def ft_vault_security():
    print("=== Cyber Archives Security ===")
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("not_existing_file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("ina_file.txt"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    ok, data = secure_archive("../ancient_fragment.txt")
    print((ok, data))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("copy.txt", "w", data if ok else ""))


if __name__ == "__main__":
    ft_vault_security()
