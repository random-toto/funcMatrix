#!/usr/bin/python3
#-*- coding: utf-8 -*-

def absMat(matrice):
    '''Renvoie la matrice avec la valeur absolue de tous ses coefficients. Renvoie False si échec.
    - matrice
    - complexe
    '''
    if type(matrice) is not list:
        raise Exception("absMat : Pas une matrice.")
        #~ return False
    if not len(matrice):
        raise Exception("absMat : La matrice est une liste vide.")
        #~ return False
    M = []
    for i in matrice:
        L = []
        if type(i) is not list:
            raise Exception("absMat : Les éléments de la liste ne sont pas des listes.")
            #~ return False
        for j in i:
            try:
                e = abs(j)
            except:
                raise Exception("absMat : Impossible de calculer la valeur absolue.")
                #~ return False
            L.append(e)
        M.append(L)
    return M 


def det2Mat(matrice):
    '''Renvoie le déterminant d'une matrice 2*2. False en cas d'échec
    - matrice
    - complexe
    - 2*2
    '''
    try:
        a = matrice[0][0]
        b = matrice[0][1]
        c = matrice[1][0]
        d = matrice[1][1]
        e = a*d - b*c
        return e
    except:
        raise Exception("det2Mat : le calcul du déterminant a échoué")
        #~ return False

def isMatrice(matrice):
    '''renvoie True s'il s'agit d'une matrice
    '''
    if type(matrice) is not list:
        raise Exception("isMatrice : Pas une liste.")
        #~ return False
    for i in matrice:
        if type(i) is not list:
            raise Exception("isMatrice : Pas une liste de liste")
            #~ return False
    return True


def newMatrix(matrice):
    '''renvoie une copie de la liste de liste envoyée
    False en cas d'échec
    '''
    if not isMatrice(matrice):
        raise Exception("newMatrice : Pas une matrice")
        #~ return False
    return [i[:] for i in matrice]


def isListCpx(vecteur):
    '''
    '''
    for i in vecteur:
        try:
            abs(i)
        except:
            raise Exception("isListCpx : élément non complexe.")
            #~ return False
    return True

def pdVect(v1, v2):
    '''
    '''
    if type(v1) is not list or type(v2) is not list:
        raise Exception("pdVect : pas un vecteur/list")
        #~ return False
    if len(v1) != len(v2):
        raise Exception("pdVect : Les vecteurs n'ont pas la même taille")
        #~ return False
    if not isListCpx(v1) or not isListCpx(v2):
        raise Exception("pdVect : Un élément n'est pas un vecteur/list")
        #~ return False
    s = 0
    for i in v1:
        for j in v2:
            s += i*j
    return s
    

def det3Mat(matrice):
    '''Renvoie le déterminant d'une matrice 3*3. False en cas d'échec
    - matrice
    - complexe
    - 3*3
    '''
    try:
        a = matrice[0][0]
        b = matrice[0][1]
        c = matrice[0][2]
        d = matrice[1][0]
        e = matrice[1][1]
        f = matrice[1][2]
        g = matrice[2][0]
        h = matrice[2][1]
        i = matrice[2][2]
        r = a*e*i + d*h*c + g*b*f - (g*e*c + a*h*f + d*b*i)
        return r
    except:
        raise Exception("det3Mat : Le calcul du déterminant a échoué.")
        #~ return False

    
def transposeMat2d(matrice):
    '''renvoie la matrice transposée. False en cas d'échec
    - matrice
    - rectangulaire ?
    '''
    if isMatrice(matrice):
        return [list(i) for i in zip(*matrice)]
    else:
        raise Exception("transposeMat2d : Pas une matrice.")
        #~ return False
    
def isMatRect(matrice):
    '''renvoie True si la matrice est rectangulaire
    - matrice
    '''
    if not isMatrice(matrice):
        raise Exception("isMatRect : Pas une matrice.")
        #~ return False
    l = len(matrice[0])
    for i in matrice:
        if len(i) != l:
            return False
    return True


def isMatCarree(matrice):
    '''renvoie True si la matrice est carrée
    - matrice
    '''
    if not isMatrice(matrice):
        raise Exception("isMatCarree : Pas une matrice")
        #~ return False
    l = len(matrice[0])
    for i in matrice:
        if len(i) != l:
            return False
    return l == len(matrice)
            
    
def isMatReel(matrice):
    '''renvoie True si tous les éléments lde la matrice sont réels
    - matrice
    '''
    if not isMatrice(matrice):
        return False
    for i in matrice:
        for j in i:
            try:
                float(j)
            except:
                return False
    return True

def isMatComplexe(matrice):
    '''renvoie True si tous les éléments de la matrice sont complexes
    - matrice
    '''
    if not isMatrice(matrice):
        return False
    for i in matrice:
        for j in i:
            try:
                abs(j)
            except:
                return False
    return True

def hilbertMat(matrice):
    '''renvoie la transposée conjuguée d'une matrice
    - matrice
    - complexe
    - rectangulaire
    '''
    if not isMatrice(matrice):
        return False
    if not isMatComplexe(matrice):
        return False
    if not isMatRect(matrice):
        return False
    M = []
    for i in matrice:
        L = []
        for j in i:
            if type(j) is complex:
                #~ L.append(complex(j.real, -j.imag))
                L.append(j.conjugate())
            else:
                L.append(j)
        M.append(L)
    R = transposeMat2d(M)
    return R


def sumMat(matrice):
    '''renvoie la somme des termes de la matrice
    - matrice
    - complexe
    '''
    if not isMatComplexe(matrice):
        return False
    s = 0
    for i in matrice:
        for j in i:
            s += j
    return s

def isInMat(e, matrice):
    ''' retourne True si l'élément est dans la matrice
    - matrice
    '''
    r = False
    if not isMatrice(matrice):
        return False
    for i in matrice:
        for j in i:
            if j == e:
                return True
    return False



def tailleMat(matrice):
    ''' retourne la taille de la matrice
    - matrice
    - rectangulaire
    '''
    if not isMatRect(matrice):
        return False
    i = len(matrice) # nombre de lignes
    p = len(matrice[0]) # nombre de colonnes
    return (i, p)


def isMatSym(matrice):
    ''' True si la matrice est symétrique
    - matrice
    - carrée
    '''
    if not isMatCarree(matrice):
        return False
    return matrice == transposeMat2d(matrice)

def nbFoisMat(e, matrice):
    '''retourne le nombre d'occurences de 'e'.
    - matrice
    '''
    if not isMatrice(matrice):
        return False
    n = 0
    for i in matrice:
        for j in i:
            if j == e:
                n+=1
    return n


def nbEleMat(matrice):
    '''renvoie le nombre d'éléments
    - matrice
    '''
    if not isMatrice(matrice):
        n = 0
    for i in matrice:
        for j in i:
            n += 1
    return n


def traceMatrix(matrice):
    '''
    '''
    if not isMatCarree(matrice):
        return False
    n, p = tailleMat(matrice)
    s = 0
    for i in range(n):
        s += matrice[i][i]
    return s


def sizeOfPdMat(mat1, mat2):
    '''
    '''
    if not isMatRect(mat1) or not isMatRect(mat2):
        return False
    a, b = tailleMat(mat1)
    c, d = tailleMat(mat2)
    return (a, d)


def subMatrix(matrice, ligne, colonne):
    ''' 
    ligne et colonne : 0 .. (n-1)
    '''
    try:
        ligne = int(ligne)
        colonne = int(colonne)
    except:
        return 1
    if not isMatRect(matrice):
        return matrice
    i, j = tailleMat(matrice)
    if ligne >= i or colonne >= j:
        return 3
    M = []
    #~ X = []
    #~ for i in matrice:
        #~ X.append(i[:])
    X = newMatrix(matrice)
    for i, line in enumerate(X):
        if i != ligne:
            line.pop(colonne)
            M.append(line)
    return M


def detMat(matrice):
    '''renvoie le déterinant de la matrice
    - matrice
    - rectangulaire
    - complexe
    '''
    if not isMatCarree(matrice):
        return False
    n, p = tailleMat(matrice)
    del p
    if n == 2:
        return det2Mat(matrice)
    elif n == 3:
        return det3Mat(matrice)
    else:
        s = 0
        for i, line in enumerate(matrice):
            #~ print(s)
            s += line[i]*((-1)**i)*detMat(subMatrix(matrice, 0, i))
    return s


def isInversible(matrice):
    '''
    '''
    if detMat(matrice):
        return True
    else:
        return False


def coFacteur(matrice, ligne, colonne):
    '''
    '''
    return ((-1)**(ligne+colonne))*detMat(subMatrix(matrice, ligne, colonne))


def coMatrice(matrice):
    '''
    '''
    if not isMatCarree(matrice):
        return False
    M = []
    for i, line in enumerate(matrice):
        L = []
        for j, column in enumerate(line):
            L.append(coFacteur(matrice, i, j))
        M.append(L)
    return M


def pdMat(mat1, mat2):
    '''
    '''
    if not sizeOfPdMat(mat1, mat2):
        return False
    M1 = newMatrix(mat1)
    M2 = newMatrix(mat2)
    M2 = transposeMat2d(M2)
    M = []
    for i in M1:
        L = []
        for j in M2:
            L.append(pdVect(i, j))
        M.append(L)
    return M
    



a = [
    [complex(1, 1), 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

b = [
    [1, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0], 
    [0, 0, 1, 0, 0], 
    [4, 0, 0, 1, 0], 
    [0, 0, 0, 0, 1]
    ]

c = [
    [1, 0, 0, 0], 
    [0, 1, 0, 0], 
    [0, 0, 1, 0], 
    [0, 0, 0, 1]
    ] 

#~ print(detMat(b))
#~ d = coMatrice(b)
#~ print(d)

print(pdMat(b, b))
