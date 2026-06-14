import sys
import importlib


def check_deps(deps: list[str]) -> list[dict[str, str], str]:
    ok = []
    missing = []
    for dep in deps:
        try:
            module = importlib.import_module(dep)
            dependencie: dict = {module.__name__: module}
            ok.append(dependencie)
            print(f"[OK] {dep.capitalize()} ({module.__version__})")
        except ImportError:
            print(f"{dep.capitalize()} module NOT FOUND.")
            missing.append(dep)
    if len(missing) > 0:
        print("1- Install using pip:\n  pip install -r requirements.txt")
        print("2- Install using Poetry:\n  poetry install")
    return (ok, missing)


def matrix_gen(module: importlib):
    print("Generating DATA for Matrix!")
    samples = module.arange(1000)

    signal = (
        50
        + 10 * module.sin(samples / 50)
        + module.random.normal(0, 2, 1000)
    )
    return (samples, signal)


def matrix_graf(module: importlib, samples, signal) -> None:
    print("Analizing DATA in Matrix!")
    graf = module.DataFrame({
        "sample": samples,
        "signal": signal
    })
    return (graf)


def matrix_map(module: importlib, graf):
    print("Generating Visual.")
    """
    module.pyplot.plot(df["sample"], df["signal"])
    module.pyplot.savefig("matrix_analysis.png")"""


def main() -> None:
    try:
        with open("requirements.txt", "r") as read:
            lines: list[str] = read.readlines()
        requirement = list()
        for line in lines:
            requirement.append(line.strip(" ").strip("\n"))
        try:
            modules: list = check_deps(requirement)
            if modules:
                charged: int = 0
                for module in modules[0]:
                    if module.get("numpy"):
                        numpy: importlib = module.get("numpy")
                        charged += 1
                    if module.get("pandas"):
                        pandas: importlib = module.get("pandas")
                        charged += 1
                    if module.get("matplotlib"):
                        matplotlib: importlib = module.get("matplotlib")
                        charged += 1
                if charged >= 3:
                    samples, signal = matrix_gen(numpy)
                    frame = matrix_graf(pandas, samples, signal)
                    matrix_map(matplotlib, frame)
        except Exception as e:
            print(f"Error caught: {e}")
    except Exception as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()
