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

    def makeRounds(self):
        """REALIZAR TODAS LAS RONDAS DE LA PARTIDA HASTA QUE HALLA UN GANADOR"""
        self.insertPlayerNamesFromConsole()
        self.selectARandomMap()
        while self.roundsWonByBlueTeam != 4 and self.roundsWonByOrangeTeam != 4:
            self.makeOneRound()
        blueTeamPlayerNames = " - ".join(i for i in self.blueTeamPlayerNames)
        OrangeTeamPlayerNames = " - ".join(i for i in self.orangeTeamPlayerNames)
        self.printTeamDetails("AZUL", blueTeamPlayerNames)
        self.printTeamDetails("NARANJA", OrangeTeamPlayerNames)
        winnerTeam = blueTeamPlayerNames
        if self.roundsWonByOrangeTeam > self.roundsWonByBlueTeam:
            winnerTeam = OrangeTeamPlayerNames
        print("\n\tEquipo ganador: {}\tFIN DE LA PARTIDA".format(winnerTeam))

    def makeOneRound(self):
        """METODO PARA REALIZAR UNA SIMPLE RONDA DE LA PARTIDA"""
        self.rondsCount += 1
        print("\n{}\n\t\tInicio de la ronda {}".format("-" * 80, self.rondsCount))
        print("Opciones de ronda:\n1- Jugar con reclutas\n2- Jugar con operadores")
        option = input("Selecciones una de las opciones anteriores (1/2): ")
        if option == "1":
            self.makeOneRoundWith("reclutas")
        elif option == "2":
            self.makeOneRoundWith("operadores")
        else:
            print("Solo debe seleccionar (1) 0 (2)")
            self.rondsCount -= 1
            self.makeOneRound()

    def makeOneRoundWith(self, operator):
        """
        REALIZAR UNA RONDA CON UN TIPO DE JUGADOR
        :param operator: 'reclutas' o 'operadores'
        """
        print("\n*-**-**-* Opciones de ronda con {}:\n1- Banear {}\n2- Jugar con todos los {} disponibles".format(operator, operator, operator))
        option = input("Selecciones una opcion para empezar (1/2): ")
        if option == "1":
            self.continueMakeOneRoundWithKindOfPlayer(True, operator)
        elif option == "2":
            self.continueMakeOneRoundWithKindOfPlayer(False, operator)
        else:
            print("\nError. Solo debe seleccionar (1) 0 (2)")
            self.makeOneRoundWith(operator)

    def continueMakeOneRoundWithKindOfPlayer(self, isBanned, operator):
        """
        METODO QUE REALIZA UNA RONDA CON UN TIPO DE JUGADOR (RECLUTAS O OPERADORES) Y CONTROLA LOS JUGADORES QUE EL
        USUARIO HA ELEGIDO BANEAR
        """
        print("\n*-**-**-* Reclutas disponibles: ")
        attackerOperatorNames = [e["Nombre"] for e in self.attackerOperators]
        defenderOperatorNames = [e["Nombre"] for e in self.defenderOperators]
        if operator == "operadores":
            attackerOperatorNames = [e["Nombre"] for e in self.attackersPlayers]
            defenderOperatorNames = [e["Nombre"] for e in self.defenderPlayers]
        print("\t{} atacantes: {}".format(operator.title(), " *-* ".join(i for i in attackerOperatorNames)))
        print("\t{} defensores: {}".format(operator.title(), " *-* ".join(i for i in defenderOperatorNames)))
        if isBanned:
            string1 = "\nIngrse los nombres de los {} atacantes que desea banear separados por un (;): ".format(operator)
            string2 = "Ingrse los nombres de los {} defensores que desea banear separados por un (;): ".format(operator)
            bannedAttackerOperators = input(string1).split(";")
            bannedDefenderOperators = input(string2).split(";")
            if len(bannedAttackerOperators) >= len(attackerOperatorNames) or len(bannedDefenderOperators) >= len(defenderOperatorNames):
                print("\nSolo se deben banear como maximo 4 {} ya sea atacante o defensor".format(operator))
                self.makeOneRoundWith(operator)
            else:
                self.continueRoundWithBannedOperators(bannedAttackerOperators, bannedDefenderOperators, operator, isBanned)
        else:
            self.continueRoundWithBannedOperators([], [], operator, isBanned)

    def continueRoundWithBannedOperators(self, attackerBannedOperators, defenderBannedOperators, operator, isBanned):
        """
        METODO PARA CONTINUAR LA RONDA CUANDO EL USUARIO BANEA O NO A LOS OPERADORES DESEADOS
        :param attackerBannedOperators: NOMBRE DE LOS OPERADORES ATACANTES BANEADOS
        :param defenderBannedOperators: NOMBRE DE LOS OPERADORES DEFENSORES BANEADOS
        :param operator: ES EL TIPO DE OPERADOR (RECLUTA O OPERADOR)
        :param isBanned: BOOLEANO PARA SABER SI EL USUARIO ELIGIO BANEAR JUGADORES O NO
        :finalmente: IMPRIME LOS RESULTADOS DE LA RONDA MOSTRADON EL EQUIPO GANADOR
        """
        position1, position2 = "", ""
        birthAttackerPlacesArray, birthDefenderPlacesArray = [], []
        if self.auxCount % 2 == 0:
            self.attackerOperators = self.getOperatorArrayFromTXT("archivos/{}_atacantes.txt".format(operator), operator)
            self.defenderOperators = self.getOperatorArrayFromTXT("archivos/{}_defensores.txt".format(operator), operator)
            self.auxCount += 1
            birthAttackerPlacesArray = self.getMap()[self.typeOfGame][0]
            birthDefenderPlacesArray = self.getMap()[self.typeOfGame][1]
            position1 = "ATACANTES"
            position2 = "DEFENSORES"
        elif self.auxCount % 2 != 0:
            self.attackerOperators = self.getOperatorArrayFromTXT("archivos/{}_defensores.txt".format(operator), operator)
            self.defenderOperators = self.getOperatorArrayFromTXT("archivos/{}_atacantes.txt".format(operator), operator)
            birthAttackerPlacesArray = self.getMap()[self.typeOfGame][1]
            birthDefenderPlacesArray = self.getMap()[self.typeOfGame][0]
            self.auxCount += 1
            position1 = "DEFENSORES"
            position2 = "ATACANTES"

        attackersOperatorsArray = self.getOperatorArrayWithEmptyValues(self.blueTeamPlayerNames, operator)
        defendersOperatorsArray = self.getOperatorArrayWithEmptyValues(self.orangeTeamPlayerNames, operator)
        attackerIndexes = self.generateRandomIndexes(self.attackerOperators, len(attackersOperatorsArray), attackerBannedOperators, defenderBannedOperators, isBanned)
        defenderIndexes = self.generateRandomIndexes(self.defenderOperators, len(defendersOperatorsArray), attackerBannedOperators, defenderBannedOperators, isBanned)
        self.getFullOperatorsArray(attackersOperatorsArray, attackerIndexes, self.attackerOperators, operator)
        self.getFullOperatorsArray(defendersOperatorsArray, defenderIndexes, self.defenderOperators, operator)

        self.printRecruits(attackersOperatorsArray, position1, operator)
        self.printBirthPlace(birthAttackerPlacesArray)
        self.printRecruits(defendersOperatorsArray, position2, operator)
        self.printBirthPlace(birthDefenderPlacesArray)

        blueTeamPlayerNames = " - ".join(i for i in self.blueTeamPlayerNames)
        orangeTeamPlayerNames = " - ".join(i for i in self.orangeTeamPlayerNames)
        while True:
            print("\n*--**--* Resultados de la ronda\n1- Equipo Azul: {}\n2- Equipo naranja: {}".format(blueTeamPlayerNames, orangeTeamPlayerNames))
            option = input("Seleccione una de las siguientes opciones (1/2): ")
            if option == "1":
                self.roundsWonByBlueTeam += 1
                print("\nRonda ganada por el equipo azul ({}) -- {}".format(self.roundsWonByBlueTeam, blueTeamPlayerNames))
                break
            elif option == "2":
                self.roundsWonByOrangeTeam += 1
                print("\nRonda ganada por el equipo naranja ({}) -- {}".format(self.roundsWonByOrangeTeam, orangeTeamPlayerNames))
                break
            else:
                print("\nError. Seleccione el ganador de la ronda. (1/2)")

    def getOperatorArrayFromTXT(self, url, type):
        """
        METODO PARA OBTENER UNA LISTA DE OPERADORES DE UN TXT
        """
        array = []
        for i in [e.strip() for e in open(url, 'r').readlines()]:
            auxArray = i.split(";")
            if type == "operadores":
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
        return array

    def getMap(self):
        """
        METODO PARA DEVOLVER UNA PISTA SEGUN LA PISTA SELECCIONADA PARA LA PARTIDA
        """
        for i in self.maps:
            if i["Nombre"] == self.map:
                return i
        return None

    def getOperatorArrayWithEmptyValues(self, operatorNamesArray, operator):
        """
        METODO QUE DEVUELVE UN ARRAY CON TODOS LOS NOMBRES DE LOS JUGADORES PASADOS POR PARAMETRO PERO CADA JUGADOR
        SE DEVUELVE CON SUS CARACTERISTICAS PERSONALES CON UN VALOR VACIO.
        """
        array = []
        for i in operatorNamesArray:
            if operator == "reclutas":
                dicc = {
                    "Nombre Jugador": i,
                    "Nombre": "",
                    "Arma Principal": "",
                    "Arma Secundaria": "",
                    "Dispositivo Principal": "",
                    "Dispositivo Secundario": ""
                }
            else:
                dicc = {
                    "Nombre Jugador": i,
                    "Nombre": "",
                    "Arma Principal": "",
                    "Arma Secundaria": "",
                    "Dispositivo Secundario": "",
                }
            array.append(dicc)
        return array

    def generateRandomIndexes(self, recruitsArray, length, bannedAttackerPlayers, defenderBannedPlayers, isBanned):
        """
        METODO QUE GENERA LOS INDECES ALEATORIOS PARA LUEGO PODER ESCOGER LOS OPERADORES ALEATORIAMENTE A PARTIR DE
        ESTOS INDICES
        """
        indexesArray = []
        while len(indexesArray) != length:
            ind = randint(0, len(recruitsArray) - 1)
            if isBanned:
                if (recruitsArray[ind]["Nombre"] not in bannedAttackerPlayers and recruitsArray[ind]["Nombre"] not in defenderBannedPlayers) and ind not in indexesArray:
                    indexesArray.append(ind)
            elif ind not in indexesArray:
                indexesArray.append(ind)
        return indexesArray

    def getFullOperatorsArray(self, operatorsArray, recruitsIndexes, recruitsArray, operator):
        """
        METODO QUE SE ENCARGA DE LLENAR EL ARRAY operatorsArray CON LOS NOMBRES ALEATORIOS DE LOS ATACANTES Y DEFENSORES
        Y CADA UNO CON UN ARMAMENTO ALEATORIO
        """
        for i in range(len(operatorsArray)):
            operatorsArray[i]["Nombre"] = recruitsArray[recruitsIndexes[i]]["Nombre"]
            operatorsArray[i]["Arma Principal"] = self.getRandomEquipement(recruitsArray[recruitsIndexes[i]]["Arma Principal"])
            operatorsArray[i]["Arma Secundaria"] = self.getRandomEquipement(recruitsArray[recruitsIndexes[i]]["Arma Secundaria"])
            operatorsArray[i]["Dispositivo Secundario"] = self.getRandomEquipement(recruitsArray[recruitsIndexes[i]]["Dispositivo Secundario"])
            if operator == "reclutas":
                operatorsArray[i]["Dispositivo Principal"] = self.getRandomEquipement(recruitsArray[recruitsIndexes[i]]["Dispositivo Principal"])

    def getRandomEquipement(self, weaponsArray):
        pass

    def printRecruits(self, recruitsArray, playersPosition, operator):
        """
        METODO PARA IMPRIMIR TODOS LOS OPERADORES O RECLUTAS CON SUS CARACTERISTICAS Y ASIGNADO A UN JUGADOR YA SEA
        DE UN JUGADOR DEL EQUIPO BLANCO O AZUL
        """
        print("\n*--**--**--**--* Jugadores {}".format(playersPosition))
        for i in recruitsArray:
            if operator == "reclutas":
                string = "NJ: {}  -- NR: {} -- AP: {}  -- AS: {}  -- DP: {}  -- DS: {}"
                print(string.format(i["Nombre Jugador"], i["Nombre"], i["Arma Principal"], i["Arma Secundaria"], i["Dispositivo Principal"], i["Dispositivo Secundario"]))
            else:
                string = "NJ: {}  -- NR: {} -- AP: {}  -- AS: {}  -- DS: {}"
                print(string.format(i["Nombre Jugador"], i["Nombre"], i["Arma Principal"], i["Arma Secundaria"], i["Dispositivo Secundario"]))

    def printBirthPlace(self, array):
        """
        METODO PARA IMPRIMIR EL NOMBRE DEL LUGAR DE NACIMIENTO PARA LOS JUGADORES, YA SEA ATACANTE O DEFENSOR
        """
        print("\nLugar de nacimiento: {}".format(array[randint(0, len(array) - 1)]))

    def insertPlayerNamesFromConsole(self):
        """
        METODO PARA INSERTAR POR CONSOLA LOS NOMBRES DE LOS JUGADORES DEL EQUIPO AZUL Y NARANJA A PARTIR DE LA CANTIDAD
        DE JUGADORES ESCOGIDAS POR EL USUARIO
        """
        print("\n\t\t\tInicio de la partida Rainbow Six Siege")
        bluePlayersCount = int(input("Entre la cantidad de jugadores del equipo azul: "))
        orangePlayersCount = int(input("Entre la cantidad de jugadores del equipo naranja: "))
        print("\n\t\t\tEquipo Azul")
        for i in range(bluePlayersCount):
            self.blueTeamPlayerNames.append(input("Entre el nombre del jugador {} del equipo azul: ".format(i + 1)))
        print("\n\t\t\tEquipo naranja")
        for i in range(orangePlayersCount):
            self.orangeTeamPlayerNames.append(
                input("Entre el nombre del jugador {} del equipo naranja: ".format(i + 1)))

    def selectARandomMap(self):
        """
        METODO PARA SELECCIONAR UNA PISTA ALEATORIA SELECCIONANDOLAS DESDE UN TXT
        """
        mapsArray = [i.strip().split(";")[0] for i in open('archivos/pistas.txt', 'r').readlines()]
        self.map = mapsArray[randint(0, len(mapsArray) - 1)]
        self.typeOfGame = str("Asegurar Zona;Rehen;Bombas".split(";")[randint(0, 2)])
        print("\nLa pista aleatoria en la que se va a realizar la partida es: \t\t{} - {}".format(self.map, self.typeOfGame))


    def printTeamDetails(self, team, names):
        """
        METODO PARA IMPRIMIR LAS RONDAS GANADAS Y LOS NOBMBRES DE CADA EQUIPO
        """
        if team == "AZUL":
            print("Rondas ganadas por el equipo azul: {} RONDAS\t {} ".format(self.roundsWonByBlueTeam, names))
        else:
            print("Rondas ganadas por el equipo naranja: {} RONDAS\t {} ".format(self.roundsWonByOrangeTeam, names))

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
