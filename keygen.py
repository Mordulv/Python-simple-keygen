from random import randint

class Keygen():

    def __init__(self,bloques=8,cantidad = 6):
        self.bloques = bloques
        self.cantidad = cantidad
        
    def letra_aleatoria(self):
        return chr(randint(65,90))

    def bloque_letras_x(self):
        texto = ''
        suma_b1 = 0
        cont_b1 = 0
        suma_total = int(90*self.cantidad*0.8)
        
        while suma_b1 != suma_total:
            if suma_b1 != suma_total and cont_b1==self.cantidad:
                suma_b1,cont_b1,texto = 0,0,''
            else:
                letra = self.letra_aleatoria()
                suma_b1 = suma_b1 + ord(letra)
                texto = texto + letra
                cont_b1 = cont_b1 + 1
        return texto

    def generar_key(self):
        key = ''
        for i in range(self.bloques):
            key = key + self.bloque_letras_x() + '-'
        return key.strip('-')

    def validar_bloque(self,bloque):
        suma_total = int(90*self.cantidad*0.8)
        suma = 0
        for i in bloque:
            suma = suma + ord(i)
        return suma == suma_total

    def validar_key(self,key):
        suma = 0
        for i in key.split('-'):
            suma = suma + self.validar_bloque(i)

        return suma == self.bloques
