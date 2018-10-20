
#---Clase de los Nodos que guardarán los elementos en la lista
class Nodo(object):
    #---Constructor del Nodo, define a @e como su elemento, el Nodo no tiene siguientes ni anteriores cuando es recién creado
    def __init__(self,e):
        self.elem = e
        self.prev = None
        self.next = None
    #---Método que regresa el elemento que está dentro del Nodo
    def get_elem(self):
        return self.elem
    #---Método que establece el elemento del Nodo si esté no se estableció antes
    def set_elem(self,e):
        self.elem = e
    #---Método que establece al Nodo anterior de éste Nodo
    def set_prev(self,prev):
        self.prev = prev
    #---Método que establece el Nodo siguiente de éste Nodo
    def set_next(self,next):
        self.next = next
    #---Método que regresa el Nodo anterior a éste Nodo
    def get_prev(self):
        return self.prev
    #---Método que regresa el Nodo siguiente a éste Nodo
    def get_next(self):
        return self.next
