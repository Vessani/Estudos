#Em dicionário podemos adicionar outros dicionarios dentro dele, chamando assim de dicioinário aninhado

gameDict = {
    'Residente Evil 4': {
        'yearsLaunch': 2023,
        'classification': 9.8,
        'genre': ['Ação', 'Aventura']
    },
    'Mario Odyssey': {
        'yearsLaunch': 2017,
        'classification': 10.0,
        'genre': ['3D', 'Aventura']
    },
    'Donkey Kong Country': {
        'yearsLaunch': 1995,
        'classification': 9.5,
        'genre': ['Plataforma', 'Aventura']
    }
}

#Buscar informação dentro de um dicionário aninhado

print(gameDict['Mario Odyssey']['genre'])

#Adicionar novo item
gameDict['Mario Odyssey']['Players'] = 1
print(gameDict['Mario Odyssey'])

#Exlcuir um item

del gameDict['Residente Evil 4']
print(gameDict)