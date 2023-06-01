from abc import ABC, abstractmethod


class ThemePage(ABC):

    @abstractmethod
    def get_color(self):
        raise NotImplementedError


class DarkTheme(ThemePage):
    __color = "Dark theme"

    def get_color(self):
        return self.__color


class OfficeTheme(ThemePage):
    __color = "Light gray"

    def get_color(self):
        return self.__color


class WebPage(ABC):

    @abstractmethod
    def get_content(self):
        raise NotImplementedError


class HomePage(WebPage):

    def __init__(self, theme: ThemePage):
        self.__theme = theme

    @property
    def theme(self):
        return self.__theme

    def get_content(self):
        print("Содержимое домашней страницы")


class AboutPage(WebPage):

    def __init__(self, page_theme: ThemePage):
        self.__theme = page_theme

    def get_content(self):
        print("Содержимое страницы о нас")


if __name__ == "__main__":
    theme = DarkTheme()
    page = HomePage(theme)
    print(page.theme.get_color())
