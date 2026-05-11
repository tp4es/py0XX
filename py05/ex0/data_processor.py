#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self):
        self._data = list()
        self._counter = 0

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
        else:
            self._data.append(str(data))


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
        else:
            self._data.append(data)


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
        else:
            self._data.append(str(data))


def function_test(obj: DataProcessor, list: list) -> None:
    print(f"\nStart Testing {type(obj).__name__}")
    for data in list:
        try:
            print(f"Trying to ingest Data: {
                data}, Valide DATA: {obj.validate(data)}")
            obj.ingest(data)
        except Exception as e:
            print(f"Error: {e}")
        print(f"Currently ingested: {obj._data}")
    print("\n===Output DATA ===")
    while len(obj._data) > 0:
        print(obj.output())


def data_processor():
    data_list = [1.01, 2.02, [3.03, 4], "hello",
                 ["hello", "world"], {"dict": "value"}]
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    function_test(numeric, data_list)
    function_test(text, data_list)
    function_test(log, data_list)


if __name__ == "__main__":
    data_processor()
