"""
Печать содержимого файла на бумаге через принтер
"""


class GetPaperError(Exception):
    def __init__(self, text):
        self.__text = text


class PaperTray:

    def __init__(self, count):
        self.__count_paper = count

    def get_count_paper(self):
        return self.__count_paper

    def remove(self, count):
        self.__count_paper -= count


class Printer:

    @staticmethod
    def __draw_text(text):
        print(f"Содержимое страницы {text}")

    def print(self, paper: PaperTray, text: str):
        if paper.get_count_paper() > 0:
            self.__draw_text(text)
            paper.remove(1)
        else:
            raise GetPaperError("Бумага конец")


class PrinterFacade:

    def __init__(self, paper_count: int):
        self.__paper = PaperTray(paper_count)
        self.__printer = Printer()

    def print(self, text):
        self.__printer.print(self.__paper, text)
