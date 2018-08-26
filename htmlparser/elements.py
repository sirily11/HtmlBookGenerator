# noinspection PyCompatibility
class HTMLElement:

    def __init__(self, attrs, contents=""):
        self.attrs = attrs
        self.content = contents
        self.children = []
        self.type = self.__class__.__name__.lower()
        self.class_name = "HTMLElement"

    def parser(self):
        attr = ""
        try:
            for key, value in self.attrs.items():
                attr += '{}="{}" '.format(key, value)
            self.attrs = attr

        except Exception as e:
            self.attrs = ""

    def add(self, element):
        try:
            if element.class_name != "HTMLElement":
                print("You need to add a html element")
                return
        except Exception as e:
            print("You need to add a html element")
            return
        self.children.append(element)
        return self

    def toString(self):
        self.parser()
        child_str = ""
        if self.children:
            for child in self.children:
                child_str += child.toString()
        return '<{} {}>{}\n{}\n</{}>\n'.format(self.type, self.attrs, self.content, child_str, self.type)


class Div(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class Header(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class Main(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class Body(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class H1(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class H2(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class H5(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class A(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class I(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class Ul(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


class Li(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)
