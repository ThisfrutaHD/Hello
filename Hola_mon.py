def encrypt(inputValue, keys, token):
    ERROR_MSG = "No es posible encriptar la cadena. Verifique los parámetros de entrada." #Missatge d'error comú per a tota la funció encrypt
    #Validació del token. Només 1 caràcter i dins dels permesos.
    tokens_permesos = ("=", "*", "+", "#", "%", "/")
    if token not in tokens_permesos: #or len(token) != 1: en un inici vaig posar aquest codi extra, però no és correcte, ja que això ja esta cobert amb el not in tokens_permesos
        #Si el paràmetre token no és un dels permesos retorna error i para l'execució de la funció. 
        return ERROR_MSG
    
    #Validació inputValue sense tokens al str.
    for t in tokens_permesos: #Bucle comptador que recorre tots els tokens un per un.
        if t in inputValue: #Un cop té el primer token, compara que no aparegui en cap moment dins el str del paràmetre inputValue i així amb tots els tokens fins que acabi el bucle.
            return ERROR_MSG #Si apareix qualsevol token al text retorna error i para l'execució de la funció.
    
    #Validació de keys. Només poden ser lletres i no repetir-se cap cop en tot el diccionari. 
    # Les claus repetides no cal validar-les aquí: si en crear el diccionari es repeteix una clau, Python conserva només l'últim valor associat.
    # Exemple: {"a":1, "a":2} es converteix en {"a":2}
    for key in keys: #Una variable key recorre totes les claus del diccionari, per defecte s'itera sobre les keys del diccionari a Python.
        if not key.isalpha() or len(key) != 1: #isalpha() permet més lletres d'altres alfabets, però crec que seria OK, si volem més restricció la validació d'avall seria correcta.
            return ERROR_MSG #Si NO són lletres permeses per isalpha() dona True en tenir el Not davant i s'activa missatge d'error.
    #O també s'activa error si la longitud té més d'un caracter en les keys. exemple correcte: "a"   exemple incorrecte:"aa" Per fer-ho viable després quan fem l'encriptació/substitució de lletres per números
    
    #Validacio alternativa de keys + restrictiva, nomes alfabet català
    #keys_permeses = set("abcdefghijklmnopqrstuvwxyzàèéíòóúüçABCDEFGHIJKLMNOPQRSTUVWXYZÀÈÉÍÒÓÚÜÇïÏ")
    #for key in keys:
    #    if len(key) != 1 or key not in keys_permeses:
    #       return ERROR_MSG

    #Validació de values. Només números enters i no es poden repetir.
    for value in keys.values(): #Iterem amb la variable value sobre tots els valors del diccionari. 
        if type(value) is not int: #Permetem nombres negatius, si no volem negatius afegir or value < 0. Més endavant, en desencriptar tinc en compte que el nombre pot aparèixer amb un signe negatiu.
            return ERROR_MSG #Qualsevol decimal, llista amb mes nombres o tot el que no sigui un sol int dona ERROR_MSG
    #Validació de values. No values repetits
    if len(keys.values()) != len(set(keys.values())): # El set elimina duplicats, comparem longitud de la llista amb set i sense. Si es diferent es perque hi havia nombres duplicats.
        return ERROR_MSG   

    #Proces d'encriptació
    text_encriptat = [] #Creem una llista on guardarem el text encriptat.
    for i in inputValue: #Iterem sobre cada caràcter de la cadena a encriptar.
        if i in keys: #Si trobem que apareix com a clau en el diccionari.
            text_encriptat.append(f"{token}{keys[i]}{token}") #Afegim la cadena amb el token, el valor corresponent i el token final mitjançant una f-string a la llista.
        else: #Si no apareix al diccionari com a clau.
            text_encriptat.append(i) #Afegim la lletra o numero al diccionari sense modificar.
    return "".join(text_encriptat) #Unim tots els elements de la llista en una sola cadena, sense cap separador.

"""
He fet servir l'estratègia d'early return. No sé si és la manera més correcta de plantejar-ho, 
però és la solució que he considerat més adient per desenvolupar aquest projecte.
D'altra banda, he procurat no repetir els comentaris en les validacions de la funció decrypt, 
ja que són les mateixes que a la funció encrypt.

Detecto possibles errors d'execució si la funció rep paràmetres buits, valors de tipus inesperat o dades fora dels casos previstos, 
com per exemple un int a inputValue. Tot i això, considero que la implementació compleix les restriccions demanades a l'exercici. 
Per tant, la funció no pretén ser completament robusta davant de qualsevol entrada incorrecta, sinó resoldre correctament els casos contemplats per l'enunciat.
"""
result = encrypt("soc la sara", {"a":1,"b":2}, "+")
print(result)


"""
Pregunta 2
"""

def decrypt(inputValue, keys, token):
    ERROR_MSG = "No és possible desencriptar la cadena. Verifiqueu els paràmetres d'entrada" #Missatge d'error comú per a tota la funció decrypt
    #Validació del token. Només 1 caràcter i dins dels permesos.
    tokens_permesos = ("=", "*", "+", "#", "%", "/")
    if token not in tokens_permesos:
        return ERROR_MSG #És exactament la mateixa validació que a la funció encrypt.

    #Validació de keys. Només poden ser lletres i no repetir-se cap cop en tot el diccionari.
    for key in keys:
        if not key.isalpha() or len(key) != 1:
            return ERROR_MSG #De nou el mateix que a la funció anterior.
    
    #Validació de values. Només números enters i no es poden repetir.
    valors = keys.values() #Així evitem fer key.values() en el bucle for diversos cops com si hem fet en la funció encrypt. Tot i que la diferencia a cridar keys.values() a cada iteració de bucle versus així és inapreciable.
    for v in valors:
        if type(v) is not int:
            return ERROR_MSG
    if len(valors) != len(set(valors)):
        return ERROR_MSG #Mateixa validació que a la funció encrypt.



    #Proces de desencriptació
    i = 0 #comptador iniciat a 0.
    text_desencriptat = [] #Llista on guardarem text desencriptat.
    numeros = "0123456789" #Cadena amb els dígits per comprovar si un caràcter és numèric.

    while i<len(inputValue): # Recorrem el text encriptat mentre l'índex no surti de la cadena.
        #Comprovem si el str comença per token, si no és el cas vol dir que no hem de fer canvis fins que aparegui un token.
        if inputValue[i] != token: 
            text_desencriptat.append(inputValue[i]) # Si no és un token, copiem el caràcter tal com està.
            i += 1 # Incrementem l'índex per avançar caràcter a caràcter pel text encriptat.
            continue #Molt important el continue per continuar executant el if del principi mentres el bucle while avança.
        #Apareix el primer token per tant sabem que aquí hi ha valor a desencriptar. Ens quedem amb la posició de i.
        j = i + 1 #saltem el primer token. Seguim incrementat l'índex pero ara amb una nova variable j per després poder comparar on es troba el número situat i poder fer slicing.
        # i seria la posició del primer token. i+1 on comença el nombre. j on acaba el segon token. j-1 on acaba el nombre.
        if inputValue[j] == "-": # Si el nombre comença amb "-", avancem una posició per continuar llegint els dígits.
            j += 1 #Si te signe negatiu, incrementem índex per continuar avançant en el nombre sino no fa res.
        while inputValue[j] in numeros: #Avancem mentre hi hagi dígits consecutius fins que aparegui el token final.
            j +=1 #Repetim aixo mentres sigui un nombre. 
        numero = inputValue[i+1 : j] #Si ja està aquí l'execució es perque ja no hi han mes nombres i j es troba a la posició del token final. 
        #Fem slicing per trobar el nombre amb les seves posicions.
        #El slicing de la cadena agafa la posició inicial del nombre i la final, com slicing fa -1 a j ja agafa la posició d'abans del token final. 
        #i +1 agafa la posicio inicial del nombre.
        for k, v in keys.items(): #Un cop tenim el número recorrem les parelles clau-valor fins trobar quin valor correspon al número llegit.
            if numero == str(v): #Igualem tipus amb str perquè pugui comparar.
                text_desencriptat.append(k) #Afegim lletra desencriptada al text.
                break # Aturem el for perquè ja hem trobat la lletra corresponent i no cal continuar recorrent el diccionari.
        i = j+1 #i agafa de nou la posició final on ho havíem deixat j pero +1 i repetim el procés fins que s'acabi el text encriptat.
    return "".join(text_desencriptat) #Unim tots els elements de la llista en una sola cadena, sense cap separador.
   


deresult = decrypt("soc l+1+ s+1+r+1+", {"a": 1, "b":2}, "+")
print(deresult)