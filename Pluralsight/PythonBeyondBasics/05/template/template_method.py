class AbstractClass:

    def template_method(self):
        self._part1()
        self._part2()
        self._part3()


    def _part1(self):
        raise NotImplementedError("Override this method")

    def _part2(self):
        raise NotImplementedError("Override this method")

    def _part3(self):
        print("Done!")


class ConcreteClass(AbstractClass):

    def _part1(self):
        print("Perform part1")

    def _part2(self):
        print("Perform part2")

    def _part3(self):
        print("Perform part3")