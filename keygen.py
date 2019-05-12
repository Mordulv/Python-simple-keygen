from random import randint

class Keygen():

    def __init__(self,bloques=8,cantidad = 6):
        
        self.bloques, self.cantidad, self.suma_total = bloques, cantidad, int(90*cantidad*0.8)

    def letra_aleatoria(self):
        
        return chr(randint(65,90))

    def bloque_letras_x(self):
        
        texto, suma_b1, cont_b1 = '', 0, 0
        
        while suma_b1 != self.suma_total:
            if suma_b1 != self.suma_total and cont_b1==self.cantidad:
                suma_b1,cont_b1,texto = 0,0,''
            else:
                letra = self.letra_aleatoria()
                suma_b1 +=  ord(letra)
                texto +=  letra
                cont_b1 +=  1
                
        return texto

    def generar_key(self):
        
        key = ''
        for i in range(self.bloques):
            key +=  self.bloque_letras_x() + '-'
            
        return key.strip('-')

    def validar_bloque(self,bloque):
        
        suma = sum([ord(i) for i in bloque])
        
        return suma == self.suma_total

    def validar_key(self,key):
        
        suma = sum([self.validar_bloque(i) for i in key.split('-')])

        return suma == self.bloques
