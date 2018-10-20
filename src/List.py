#---Importa la clase "Nodo" que se usará para guardar los elementos en una lista
from Node import Nodo
#---Declara la clase Lista (List), object es la clase de la cual hereda List
class List(object):
    #---Crea una lista vacía
    def __init__(self):
        #self es la lista (o el objeto en donde está el elemento)
        self.head = None #Nodo cabeza de la lista, al inicio es None (no existe)
        self.tail = None #Nodo final de la lista (Nodo cola), al inicio es None (no existe)
        self.longitud = 0 #Longitud de una lista (cantidad de Nodos)
    #---Devuelve el Nodo cabeza de una lista
    def get_head(self):
        return self.head
    #---Define la cabeza de la lista
    def set_head(self,head):
        #---@head es el elemento al que igualaremos @self.head para que la cabeza de la lista (@self.head) sea igual a @head 
        self.head = head
    #---Devuelve el último Nodo de la lista (@self.tail)
    def get_tail(self):
        return self.tail
    #---Define la cola de una lista con el elemento que le pasas
    def set_tail(self,tail):
        #---@tail es el elemento que quieres que sea la cola, @self.tail es la cola de la lista
        self.tail = tail #actualiza la cola de la lista
    #---Devuelve la longitud de la lista
    def get_length(self):
        return self.longitud
    #---Checa si la lista es vacía, devuelve @True si lo es, @False en otro caso
    def is_empty(self):
        return self.get_length() == 0
    #---Revisa si un elemento está en la lista, @e es el elemento que quieres checar si está, regresa @True si sí está, @False en caso contrario
    def contains(self,e):
        i = self.head # @i es la variable temporal, empezaremos a recorrer la lista por la cabeza 
        while i.get_next() != None: # Termina el ciclo @while si @i es la cola
            if i.get_elem() == e:
                return True
            else:
                i = i.get_next()
        return False
    #---Método para agregar elementos a la lista, @e es el elemento que se va a instalar
    def add(self,e):
        n = Nodo(e) # @n es el Nodo en donde estará el elemento
        if self.head == None: # si la cabeza está vacía, establece @n como la cabeza
            self.head = n
        else:
            temp = self.head # @temp variable temporal que guarda a la cabeza
            while temp.get_next() != None: # Ciclo que para sólo si @temp es la cola
                temp = temp.get_next() # Va moviendo a temp con su siguiente
            temp.set_next(n) # Cuando llegaste a la cola, establece a @n como el siguiente de la cola
            n.set_prev(temp) # Conecta a @n con su Nodo anterior
            if n.get_next() == None: 
                self.tail = n # Actualiza la cola para que sea el nuevo Nodo que quieres insertar 
        self.longitud += 1 # Incrementa la longitud
    #---Método que elimina un elemento de la lista
    def remove(self,e):
        if not self.contains(e): # Checa que el elemento está en la lista, si no está, lanza un erro @ValueError 
            raise ValueError("Not in the list")
        else:
            temp = self.get_node(e) # El nodo de la lista que contiene a @e
            if temp.get_elem() == self.head.get_elem(): # Checa si el elemento que pedimos borrar es el primer elemento
                self.head = temp.get_next() # Actualiza la cabeza a su siguiente
                temp = None # Borra el Nodo
            else:
                temp.get_prev().set_next(temp.get_next()) # Conecta el Nodo anterior a @temp con su siguiente
                temp.get_next().set_prev(temp.get_prev()) # Conecta el Nodo siguiente a @temp a su anterior
                temp = None # Borra @temp
            self.longitud = self.longitud - 1 # Disminuye la longitud
    #---Método para buscar un elemento en la lista
    def get_node(self,e):
        temp = self.head # El primer Nodo en el que empezaremos a buscar
        while temp.get_elem() != e: # Un siclo que termina sólo si ya encontró el elemento, de lo contrario va moviendoce hacia el Nodo siguiente
            temp = temp.get_next()  
        return temp # Regresa el Nodo que contiene al elemento
    #---Método que checa si un Nodo es la cabeza
    def is_head(self,n):
        return n == self.head
    #---Método que checa si un Nodo es la cola
    def is_tail(self,n):
        return n == self.tail
    #---Método que convierte a la lista en una cadena para que sea visible
    def to_string(self):
        s = "["
        temp = self.head
        while temp != None:
            if temp == self.tail:
                s += str(temp.get_elem())
            else:
                s +=str(temp.get_elem()) + ","
            temp = temp.get_next()
        s += "]"
        return s

