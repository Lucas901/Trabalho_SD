# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import rpyc

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    class MyService(rpyc.Service):
        def on_connect(self, conn):

            # código que é executado quando uma conexão é iniciada, caso seja necessário
            pass

    def on_disconnect(self, conn):

        # código que é executado quando uma conexão é finalizada,caso seja necessário
        pass

    def exposed_get_answer(self):  # este é um método exposto
        return 42

    exposed_the_real_answer_though = 43  # este é um atributo exposto

    def get_question(self):  # este método não é exposto
        return "Qual é a cor do cavalo branco de Napoleão?"

    # Para iniciar o servidor
    if __name__ == "__main__":
        from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
