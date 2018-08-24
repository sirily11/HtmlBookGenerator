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
                attr += '{}:"{}" '.format(key, value)
            self.attrs = attr

        except Exception as e:
            self.attrs = ""


    def add(self, element):
        try:
            if htmlelement.class_name != "HTMLElement":
                print("You need to add a html element")
                return
        except Exception as e:
            print("You need to add a html element")
            return
        self.children.append(element)

    def toString(self):
        self.parser()
        child_str = ""
        if self.children:
            for child in self.children:
                child_str += child.toString()
        return self.attrs + child_str



class Div(HTMLElement):
    def __init__(self, attrs, contents=""):
        HTMLElement.__init__(self, attrs, contents)


htmlelement = HTMLElement({"class": "col row", "id": "test id"})
htmlelement2 = Div({"class": "col row", "id": "test id"})
htmlelement.add(htmlelement2)
print(htmlelement.toString())
