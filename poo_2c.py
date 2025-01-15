class Personaje:
    #Atributos de la clase
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    def _init_(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    #¿Qué es self? Es una referencia al mismo objeto
    #¿Qué es el método init? Constructor que inicializa
    #atributos de un objeto
    #¿Por qué se usa doble guión bajo? Dunder. Porque es
    #método mágico.
    #¿Cuándo se ejecuta el método init? Autom. al crear
    #una nueva instancia
    
    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza:",self.__fuerza)
        print("-Inteligencia:",self.inteligencia)
        print("-Defensa:",self.__defensa)
        print("-Vida:",self.__vida)
    
    def subir_nivel(self,fuerza, inteligencia, defensa):
        self._fuerza = self._fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self._defensa = self._defensa + defensa
    
    def esta_vivo(self):        
        return self.__vida > 0
        
    def morir(self):
        self.__vida = 0
        print(self.__nombre,"ha muerto")
        
    def dañar(self, enemigo):
        return self._fuerza - enemigo._defensa
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        if daño < 0 :
            daño = 0
        if enemigo.__vida - daño < 0:
            enemigo.__vida
        else:
            enemigo._vida = enemigo._vida - daño
        print(self._nombre,"ha realizado",daño,"puntos de daño a", enemigo._nombre)
        print("Vida de",enemigo._nombre,"es",enemigo._vida)
    
    def get_vida(self):
        return self.__vida
    
    def set_vida(self, vida):
        self.__vida = vida  
        if self.__vida <= 0 :
            self.morir()
            
        
        
           
#Variable del constructor 
mi_personaje = Personaje("EsteBandido", 100, 50, 45, 100)
mi_enemigo = Personaje("Ángel",70,100,70,100)
print(mi_personaje.get_vida())
mi_personaje.set_vida(-5)
print(mi_personaje.get_vida())
mi_personaje.Personaje_vida = -50
mi_personaje.imprimir_atributos()


#mi_personaje.imprimir_atributos()
#mi_personaje.atacar(mi_enemigo)
# mi_personaje.morir()
#print(mi_personaje.esta_vivo())
# mi_personaje.subir_nivel(15,5,10)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()

#Modificando valores de los atributos
# mi_personaje.__nombre = "EstebanDido"
# mi_personaje.__fuerza = 300
# mi_personaje.inteligencia = -2
# mi_personaje.__defensa = 30
# mi_personaje.__vida = 2

# print("El nombre de mi personaje es: ",mi_personaje.__nombre)
# print("El fuerza de mi personaje es: ",mi_personaje.__fuerza)
# print("El inteligencia de mi personaje es: ",mi_personaje.inteligencia)
# print("El defensa de mi personaje es: ",mi_personaje.__defensa)
# print("El vida de mi personaje es: ",mi_personaje.__vida)