from modelo.game import Game

""" 
PROGRAMA PARA PODER REALIZAR TODAS LAS PARTIDAS QUE DESEE EL USUARIO DE RAINBOW SIX SIEGE CON LOS OPERADORES DEL 
JUEGO ESCOGIDO DE MANERA ALEATORIA, CREANDO PARA CADA PARTIDA UNA INSTANCIA DE LA CLASE GAME Y LLAMANDO AL METODO
(makeRounds), EL CUAL SE ENCARGA A REALIZAR LA PARTIDA AYUDANDOSE DE OTROS METODOS CREADOS DENTRO DE LA CLASE.
"""
if __name__ == '__main__':
    while True:
        print("\n{}\n\n\tMenu Principal.\n1- Iniciar una partida\n2- Salir del programa".format("*--*" * 30))
        option = input("Seleccione una opcion(1/2): ")
        if option == '1':
            p = Game()
            p.makeRounds()
        elif option == '2':
            print("\n\t\t\tMuchas gracias. Fin del programa")
            break
        else:
            print("Error. Seleccione una opcion correcta")
