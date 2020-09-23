    	*******************************************************************************
    	*                 VISION DEL PRODUCTO                                         *
    	*******************************************************************************


	*-*  Con este software se pretende hacer más dinámica la jugabilidad del Tom Clancy´s Rainbow Six: Siege
	con el fin de darle un ambiente aún más competitivo de una forma sencilla. Las hablidades de los jugadores se ponen a prueba de 
	cara a la suerte, algo no implementado en el juego. Con un estilo de ruleta rusa este programa realiza algoritmos 
	de selección aleatorios para que el jugador sea dotado de características completamente ajenas a su decisión, igualando
	aún más las posibilidades de los contrincantes.

    	*******************************************************************************
    	*            USUARIOS PARA EL QUE ESTA DEDICADO EL SISTEMA                    *
    	*******************************************************************************


	*-* Esperamos llegar al público fanático de la saga con una novedad que les sea llamativa y a su vez fácil de usar, con una interfaz 
	muy sencilla, enriqueciendo aún más el juego. Cualquier jugador con un mínimo de experiencia no tendrá dificultad alguna
	para usar este producto. 


	*******************************************************************************
	*		COMO USAR LA APLICACION                                               *
	*******************************************************************************


	*-* Supone una odisea usar este software en solitario, ya que quedarías completamente a manos de la suerte, una situación muy 
	ventajosa para los adversarios pero a la vez llamativa para aquellos que le gustan los retos. Los jugadores en solitario tienen varias
	opciones para llevar a cabo su fin, como lo son:
	- Operador Random
	- Armamento Random
	- Recluta Random
        - Pista Random
	
	*-* En equipo el entretenimiento sería mayor, ya que además de las antes mencionadas los juadores tendrían la posibilidad de cambiar 
	la completa temática del juego, hay varias opciones para esto, como lo son:
	-Ruleta de equipo
	-Pista Aleatoria

	*-*	A continuación una guía de como utiizar esta herramienta:
	- Se incicia el programa al correr  el archivo main.py desde un editor de texto como el PyCharm, Sublime Text, Visual Studio Code, etc  y aparece un menú con 
	las siguientes opciones:
		1- Iniciar una partida
		2- Salir del programa
	- Al selecionar la opción número 1(Iniciar una partida) se adentra en la herramienta y esta le pide que seleccione la cantidad de jugadores por equipo, primer
	dato imprescindible para su correcto funcionamiento.
	- Cuando el software conoce la cantidad de jugadores procede a pedir el nombre de cada uno de ellos, un detalle para personalizar 
	la experiencia.
	- Luego necesita ingresar las características de juego para la ronda actual que no es más que especificar si va a usar avatares reclutas (1) u operadores (2):
		* Si escoge la alternativa (1) se procede a preguntar si desea banear (excluir) algún recluta, de ser así se introducen los nombres de los reclutas
		baneados y se prosigue a recibir los  reclutas con todo su armamento y el lugar de nacimiento (respawn) para el equipo. Si no se excogiera la 
		opción baneo de reclutas el flujo del programa sigue con normalidad hasta la repartición de reclutas y lugar de nacimiento.
	
		* Al seleccionar la opción (2) se procede a preguntar si desea banear (excluir) algún operador, si es así se introducen los nombres de los operadores 
		baneados y se prosigue a recibir los  operadores con todo su armamento y el lugar de nacimiento (respawn) para el equipo. Si no se excogiera la 
		opción baneo de operadores el flujo del programa sigue con normalidad hasta la repartición de operadores y lugar de nacimiento.

		* Cuando la ronda en el juego termine se debe ingresar el resultado para que el programa almacene los datos que necesita, con estos dterminará al 
		vencedor.

		NOTA: Tenga en cuenta que todos los datos como Armamento, Pista donde se va a realizar la partida, Nombre del Operador o Recluta y tipo de juego el 
		software los va a seleccionar de una manera aleatoria, para poder lograr igualdad entre los equipos.

	- El ciclo se repite hasta que el programa determine un ganador tras haber ganado 4 rondas.
	-Tras haber concluido la partida y haberse determinado un ganador el programa despliega el menú de inicio nuevamente donde puede escoger jugar otra partida si lo desea
	o salir del programa.




