import importlib
from typing import Any


def check_deps(deps: list[str]) -> tuple[list[dict[Any, Any]], list[str]]:
    ok = []
    missing = []
    dependencie: dict = {}
    for dep in deps:
        try:
            if dep != "matplotlib":
                module = importlib.import_module(dep)
                dependencie = {module.__name__: module}
                ok.append(dependencie)
            else:
                pyplot = importlib.import_module("matplotlib.pyplot")
                dependencie = {"matplotlib": pyplot}
                ok.append(dependencie)
            print(f"[OK] {dep.capitalize()} ({module.__version__})")
        except ImportError:
            print(f"{dep.capitalize()} module NOT FOUND.")
            missing.append(dep)
    if len(missing) > 0:
        print("1- Install using pip:\n  pip install -r requirements.txt")
        print("2- Install using Poetry:\n  poetry install")
    return (ok, missing)


def matrix_gen(module: importlib):  # type: ignore
    print("Generating DATA for Matrix!")
    samples = module.arange(1000)  # type: ignore
    signal = (
        50
        + 10 * module.sin(samples / 50)  # type: ignore
        + module.random.normal(0, 2, 1000)  # type: ignore
    )
    return (samples, signal)


def matrix_graf(
            module: importlib, samples, signal) -> Any:  # type: ignore
    print("Analizing DATA in Matrix!")
    graf = module.DataFrame({  # type: ignore
        "sample": samples,
        "signal": signal
    })
    return (graf)


def matrix_map(module: importlib, graf) -> None:  # type: ignore
    print("Generating Visualization!")
    module.plot(graf["sample"], graf["signal"])  # type: ignore
    module.savefig("matrix_analysis.png")  # type: ignore


def main() -> None:
    try:
        with open("requirements.txt", "r") as read:
            lines: list[str] = read.readlines()
        requirement = list()
        for line in lines:
            requirement.append(line.strip(" ").strip("\n"))
        try:
            modules: tuple = check_deps(requirement)
            if modules:
                charged: int = 0
                for module in modules[0]:
                    if module.get("numpy"):
                        numpy: importlib = module.get("numpy")  # type: ignore
                        charged += 1
                    if module.get("pandas"):
                        pandas: importlib = (  # type: ignore
                            module.get("pandas")
                        )
                        charged += 1
                    if module.get("matplotlib"):
                        matplotlib: importlib = (  # type: ignore
                            module.get("matplotlib")
                        )
                        charged += 1
                if charged >= 3:
                    print("Requierements: Ok")
                    samples, signal = matrix_gen(numpy)
                    frame = matrix_graf(pandas, samples, signal)
                    matrix_map(matplotlib, frame)
        except Exception as e:
            print(f"Error caught: {e}")
    except Exception as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()
