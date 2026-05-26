#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):

    def __init__(self):
        self._data = list()
        self._counter = 0
        self._ingested = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise ValueError("No hay datos")
        self._counter += 1
        value = self._data.pop(0)
        return (self._counter, value)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Datos no válidos")

        if isinstance(data, list):
            for x in data:
                self._data.append(str(x))
                self._ingested += 1
        else:
            self._data.append(str(data))
            self._ingested += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Datos no válidos")

        if isinstance(data, list):
            self._data.extend(data)
            self._ingested += len(data)
        else:
            self._data.append(data)
            self._ingested += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def is_valid_dict(d):
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(d) for d in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Datos no válidos")

        if isinstance(data, list):
            for d in data:
                self._data.append(str(d))
                self._ingested += 1
        else:
            self._data.append(str(data))
            self._ingested += 1


class ExportPlugin(Protocol):
    @abstractmethod
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream():
    def __init__(self):
        self._processors = []

    def registered_processors(self) -> list:
        return (self._processors)

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self._processors.append(proc)
        else:
            raise TypeError("Incorrect DataProcessor")

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(data):
                    proc.ingest(data)
                    processed = True
                    print(
                        f"DATA: {data}, ingested as {type(proc).__name__}")
                    break
            if not processed:
                print(
                    f"Has no processor avaible for {
                        (type(data).__name__).capitalize()}")

    def print_processors_stats(self) -> None:
        for processor in self._processors:
            print(
                f"{processor.__class__.__name__}: "
                f"total {processor._ingested} items processed, "
                f"remaining: {len(processor._data)}"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Cada procesador, exporta nb elements"""
        data_list = []
        for proc in self._processors:
            for _ in range(nb):
                try:
                    data_list.append(proc.output())
                except ValueError:
                    break
            if data_list:
                plugin.process_output(data_list)
                data_list.clear()


class ExportJson():

    def process_output(self, data):
        result = {}
        for t in data:
            print(type(t[1]), t[1])
        print(result)


class ExportCsv():
    def process_output(self, data):
        pass


def consume_processor(proc: DataProcessor, amount: int) -> None:
    print(f"\nConsuming from {type(proc).__name__}")
    for _ in range(amount):
        try:
            print(proc.output())
        except ValueError as e:
            print(f"Output Error: {e}")
            break


def data_pipe():
    data_list = [1.01, 2.02, [3.03, 4], "hello", 42, 21,
                 ["hello", "world"], {"dict": "value"}, (1, 2),
                 {"Warning": "SysError"}, {"SSHConnecting": "Fail"}
                 ]

    streamx = DataStream()
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    json = ExportJson()
    csv = ExportCsv()

    processors = [
        numeric,
        text,
        log,
        "test"
    ]

    print("=== Registering Processors ===")
    for proc in processors:
        try:
            streamx.register_processor(proc)
            print(f"Rgistered {proc.__class__.__name__}")
        except Exception as e:
            print(f"Error registering '{proc}': {e}")
    print("\n=== Procesing DATA ===")
    try:
        streamx.process_stream(data_list)
    except Exception as e:
        print(f"Error: {e}")
    print("\n=== STATS ===")
    streamx.print_processors_stats()
    print("\n=== Export 2 times ===")
    streamx.output_pipeline(2, json)
    streamx.print_processors_stats()


if __name__ == "__main__":
    data_pipe()
