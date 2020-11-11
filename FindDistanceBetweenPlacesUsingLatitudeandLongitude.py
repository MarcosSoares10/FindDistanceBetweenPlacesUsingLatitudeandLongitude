import math



def calculateDistanceMiles_KM(lat1,long1,lat2,long2):
    GRAU_RAD = 0.0174532925
    LATITUDE1 = lat1
    LONGITUDE1 = long1
    LATITUDE2 = lat2
    LONGITUDE2 = long2

    LATITUDE1_RAD  = LATITUDE1 * GRAU_RAD
    LONGITUDE1_RAD  = LONGITUDE1 * GRAU_RAD
    LATITUDE2_RAD  = LATITUDE2 * GRAU_RAD
    LONGITUDE2_RAD  = LONGITUDE2 * GRAU_RAD
    DIST_LATITUDE = LATITUDE2_RAD - LATITUDE1_RAD
    DIST_LONGITUDE = LONGITUDE2_RAD - LONGITUDE1_RAD
    COEFF_A = math.pow(math.sin(DIST_LATITUDE/2),2)+math.cos(LATITUDE1_RAD)*math.cos(LATITUDE2_RAD)*math.pow(math.sin(DIST_LONGITUDE/2),2)
    DISTANCE = 3963.192456*(2*math.atan2(math.sqrt(COEFF_A), math.sqrt(1 - COEFF_A))) 
    return round(DISTANCE,3),round(DISTANCE*1.6,3)
    

print("Distance Miles: ",calculateDistanceMiles_KM(34.1008453,-117.8861533,29.9560042,-90.0836929)[0])
print("Distance KM: ",calculateDistanceMiles_KM(34.1008453,-117.8861533,29.9560042,-90.0836929)[1])