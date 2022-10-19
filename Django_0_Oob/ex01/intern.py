class Intern:

    def __init__(self, name = "My name? I’m nobody, an intern, I have no name."):
        self.name = name
        self.intern = self.Coffee()

    def __str__(self) -> str:
        return self.name

    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_Coffee(self):
            return Intern.Coffee

def test():
    intern = Intern()
    mark = Intern("Mark")
    print(intern)
    print(mark)
    try:
        intern.work()
    except Exception as e:
        print(e)
    print(mark.Coffee())

if __name__ == '__main__':
    test()            