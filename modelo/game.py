from random import randint


class Game:
    """CONSTRUCTOR Y ATRIBUTOS DE LA CLASE PARTIDA"""

    def __init__(self):
        """ARRAYS DONDE SE ALMACENA LOS NOMBRES DE LOS JUGADORES (HUMANOS) DE LOS EQUIPOS AZUL Y NARANJA"""
        self.__blueTeam = []
        self.__orangeTeam = []
        """ARRAY DONDE SE ALMACENAN LAS PISTAS DEL JUEGO"""
        self.__maps = []
        """ARRAYS DONDE SE ALMACENAN LOS NOMBRES DE LOS JUGADORES (OPERADORES Y RECLUTAS) ATACANTES Y DEFENSORES"""
        self.__attackerPlayers = []
        self.__defenderPlayers = []
        self.__attackerRecruits = []
        self.__defenderRecruits = []
        """CONTADORES DONDE SE ALMACENAN LAS RONDAS GANADAS POR CADA EQUIPO"""
        self.__roundsWonByBlueTeam = 0
        self.__roundsWonByOrangeTeam = 0
        """CONTADORES DONDE SE ALMACENAN LA CANTIDAD DE RONDAS DE LA PARTIDA Y UN CONTADOR AUXILIAR"""
        self.__roundsCount = 0
        self.__auxCount = 0
        """VARIABLE DONDE SE ALMACENA EL NOMBRE DE LA PISTA SELECCIONADA ALEATORIAMENTE"""
        self.__map = ""
        """VARIABLE DONDE SE ALMACENA EL NOMBRE DEL TIPO DE PARTIDA SELECCIONADO ALEATORIAMENTE"""
        self.__gameType = ""

        """ANNADIR LOS JUGADORES Y LAS PISTAS AL SISTEMA CARGANDOLOS DE UN TXT"""
        self.addPlayersFromTXT("ATACANTE", 'archivos/operadores_atacantes.txt')
        self.addPlayersFromTXT("DEFENSOR", 'archivos/operadores_defensores.txt')
        self.addPlayersFromTXT("RECLUTA_DEFENSOR", 'archivos/reclutas_defensores.txt')
        self.addPlayersFromTXT("RECLUTA_ATACANTE", 'archivos/reclutas_atacantes.txt')
        self.loadMapsFromTXT()

    def addPlayersFromTXT(self, type, fileUrl):
        pass

    def loadMapsFromTXT(self):
        pass
