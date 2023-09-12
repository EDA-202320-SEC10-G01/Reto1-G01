def crear_lista_cumpleanios_amor_de_mi_vida():
    cami_te_amo = []
    
    while True:
        nombre = input("Ingrese el nombre de la persona (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            return cami_te_amo
        
        patos_o_no_patos = input("¿Le gustaría que la persona esté invitada? (bien/mas o menos/mal): ")
        
        if patos_o_no_patos == 'bien':
            invitado = True
        else:
            invitado = False
        
        cami_te_amo.append((nombre, invitado))
        


if __name__ == "__main__":
    lista_cumpleanios = crear_lista_cumpleanios_amor_de_mi_vida()
    
    print("Lista de invitados:")
    for nombre, invitado in lista_cumpleanios:
        estado = "Invitado" if invitado else "No invitado"
        print(f"{nombre}: {estado}")      