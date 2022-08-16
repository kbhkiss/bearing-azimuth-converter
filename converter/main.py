from distutils.log import error


def setAzimuthBaseValue(strikeDir, strikeValue):
    baseValue = 0
    
    if (strikeDir == 'W'):
        baseValue = 360 - strikeValue
        
    elif (strikeDir == 'E'):
        baseValue = 360 - strikeValue
        
    else:
        error('Wrong strikeDir (Cuidado com o Cadu!)')
    
    return baseValue
        
def setAzimuthValue1(baseValue, dipCoord1):
    value = 0
    
    if (dipCoord1 == 'S'):
        value = baseValue - 90
        
    elif (dipCoord1 == 'N'):
        value = baseValue + 90
        
        if(value > 360):
            value = value - 360
            
    else:
        error('Wrong dipCoord1 (Cuidado com o Cadu!)')
    
    return value
        
        

def main():
    bearingValue = input('What is your measurement? (e.g. N30W/60SW)\n') 

    strikeValue = int(bearingValue[1] + bearingValue[2])
    strikeDir = bearingValue[3].upper()
    dipValue = int(bearingValue[5] + bearingValue[6])
    dipCoord1 = bearingValue[7].upper()
    
    azimuthBaseValue = setAzimuthBaseValue(strikeDir, strikeValue)
    azimuthValue1 = setAzimuthValue1(azimuthBaseValue, dipCoord1)
    azimuthValue2 = dipValue
    
    print(f'\nResult:\n{azimuthValue1}/{azimuthValue2}\n\n\n')
    
while True:
    main()
