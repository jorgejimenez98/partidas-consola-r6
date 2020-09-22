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
        """
        METODO PARA ANNADIR LOS NOMBRES DE LOS OPERADORES O RECLUTAS A UN ARRAY DESDE UN TXT
        """
        array = []
        for i in [e.strip() for e in open(fileUrl, 'r').readlines()]:
            auxArray = i.split(";")
            if type == "ATACANTE" or type == "DEFENSOR":
                array.append({
                    'Nombre': auxArray[0],
                    "Arma Principal": auxArray[1].split(","),
                    "Arma Secundaria": auxArray[2].split(","),
                    "Dispositivo Secundario": auxArray[3].split(",")
                })
            else:
                array.append({
                    'Nombre': auxArray[0],
                    "Arma Principal": auxArray[1].split(","),
                    "Arma Secundaria": auxArray[2].split(","),
                    "Dispositivo Principal": auxArray[3].split(","),
                    "Dispositivo Secundario": auxArray[4].split(",")
                })
        if type == "ATACANTE":
            self.attackersPlayers = array
        elif type == "DEFENSOR":
            self.defenderPlayers = array
        elif type == "RECLUTA_DEFENSOR":
            self.defenderOperators = array
        else:
            self.attackerOperators = array

    def loadMapsFromTXT(self):
        """
            METODO PARA CARGAR TODOS LOS MAPAS DE UN TXT Y ALMACENARLOS EN UN ARRAY
            """
        array = []
        for i in [e.strip() for e in open('archivos/pistas.txt', 'r').readlines()]:
            auxArray = i.split(";")
            array.append({
                "Nombre": auxArray[0],
                "Asegurar Zona": [auxArray[1].split(","), auxArray[2].split(",")],
                "Rehen": [auxArray[1].split(","), auxArray[3].split(",")],
                "Bombas": [auxArray[1].split(","), auxArray[4].split(",")]
            })
        self.maps = array

    # METODOS GETTER Y SETTERS DE LA CLASE GAME
    @property
    def defenderOperators(self):
        return self.__defenderRecruits

    @defenderOperators.setter
    def defenderOperators(self, value):
        self.__defenderRecruits = value

    @property
    def attackerOperators(self):
        return self.__attackerRecruits

    @attackerOperators.setter
    def attackerOperators(self, value):
        self.__attackerRecruits = value

    @property
    def defenderPlayers(self):
        return self.__defenderPlayers

    @defenderPlayers.setter
    def defenderPlayers(self, value):
        self.__defenderPlayers = value

    @property
    def attackersPlayers(self):
        return self.__attackerPlayers

    @attackersPlayers.setter
    def attackersPlayers(self, value):
        self.__attackerPlayers = value

    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self, value):
        self.__map = value

    @property
    def orangeTeamPlayerNames(self):
        return self.__orangeTeam

    @orangeTeamPlayerNames.setter
    def orangeTeamPlayerNames(self, value):
        self.__orangeTeam = value

    @property
    def blueTeamPlayerNames(self):
        return self.__blueTeam

    @blueTeamPlayerNames.setter
    def blueTeamPlayerNames(self, value):
        self.__blueTeam = value

    @property
    def roundsWonByOrangeTeam(self):
        return self.__roundsWonByOrangeTeam

    @roundsWonByOrangeTeam.setter
    def roundsWonByOrangeTeam(self, value):
        self.__roundsWonByOrangeTeam = value

    @property
    def roundsWonByBlueTeam(self):
        return self.__roundsWonByBlueTeam

    @roundsWonByBlueTeam.setter
    def roundsWonByBlueTeam(self, value):
        self.__roundsWonByBlueTeam = value

    @property
    def rondsCount(self):
        return self.__roundsCount

    @rondsCount.setter
    def rondsCount(self, value):
        self.__roundsCount = value

    @property
    def auxCount(self):
        return self.__auxCount

    @auxCount.setter
    def auxCount(self, value):
        self.__auxCount = value

    @property
    def maps(self):
        return self.__maps

    @maps.setter
    def maps(self, value):
        self.__maps = value

    @property
    def typeOfGame(self):
        return self.__gameType

    @typeOfGame.setter
    def typeOfGame(self, value):
        self.__gameType = value
