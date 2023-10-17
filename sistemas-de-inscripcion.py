from abc import ABC, abstractmethod


class Person:

    def __init__(self, name: str, last_name: str, email: str, password: str):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def validate_credentials(self):
        pass


class Student:
    def __init__(self):
        self.students = []


class Teacher:
    def __init__(self):
        self.teachers = []