import numpy as np

def calculate(list):
    
    matrix = np.array(list)
    try:
        len(matrix) >= 9
        matrix = matrix.reshape(3,3)
        print(matrix.reshape(3,3))
        
    except:
        raise ValueError('List must contain nine numbers.')

    calculations = dict()
    meanArr = []
    meanColu = np.mean(matrix, axis = 0).tolist()
    meanRows = np.mean(matrix, axis = 1).tolist()
    meanFlat = np.mean(matrix)
    
    meanArr.append(meanColu)
    meanArr.append(meanRows)
    meanArr.append(meanFlat)
    #print(meanArr)
    
    calculations['mean'] = meanArr

    
    varArr = []
    varColu = np.var(matrix, axis = 0).tolist()
    varRows = np.var(matrix, axis = 1).tolist()
    varFlat = np.var(matrix)

    varArr.append(varColu)
    varArr.append(varRows)
    varArr.append(varFlat)
    #print(varArr)

    calculations['variance'] = varArr

    
    stdArr = []
    stdColu = np.std(matrix, axis = 0).tolist()
    stdRows = np.std(matrix, axis = 1).tolist()
    stdFlat = np.std(matrix)

    stdArr.append(stdColu)
    stdArr.append(stdRows)
    stdArr.append(stdFlat)
    #print(stdArr)

    calculations['standard deviation'] = stdArr

    
    maxArr = []
    maxColu = np.max(matrix, axis = 0).tolist()
    maxRows = np.max(matrix, axis = 1).tolist()
    maxFlat = np.max(matrix)

    maxArr.append(maxColu)
    maxArr.append(maxRows)
    maxArr.append(maxFlat)
    #print(maxArr)
    
    calculations['max'] = maxArr

    
    minArr = []
    minColu = np.min(matrix, axis = 0).tolist()
    minRows = np.min(matrix, axis = 1).tolist()
    minFlat = np.min(matrix)

    minArr.append(minColu)
    minArr.append(minRows)
    minArr.append(minFlat)
    #print(minArr)

    calculations['min'] = minArr

    
    sumArr = []
    sumColu = np.sum(matrix, axis = 0).tolist()
    sumRows = np.sum(matrix, axis = 1).tolist()
    sumFlat = np.sum(matrix)

    sumArr.append(sumColu)
    sumArr.append(sumRows)
    sumArr.append(sumFlat)
    #print(sumArr)

    calculations['sum'] = sumArr

    return calculations