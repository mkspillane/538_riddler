import numpy as np

def compare(x1,x2):
    temp = np.sign(x1-x2)
    return np.sign(np.sum(temp*(np.arange(10)+1)))
    
def convert(x1):
    temp = np.zeros((10,x1.shape[1]),'int')
    for i in range(10):
        temp[i,:] = np.sum(x1==i,axis = 0)
    return temp
    
def convert2(x1):
    temp = np.zeros((10,1),'int')
    for i in range(10):
        temp[i,:] = np.sum(x1==i,axis = 0)
    return temp

def new_models(mdls,top):
    results = np.zeros((models.shape[1],models.shape[1]),'int')
    for i in range(models.shape[1]):
        for j in range(models.shape[1]):
            results[i,j] = compare(models[:,i],models[:,j])
    g1 = np.sum(results+1,axis=1)/np.sum(results+1)

    temp = np.zeros(mdls.shape,'int')
    
    for i in range(mdls.shape[1]//2):
        j0 = np.random.choice(models.shape[1],p = g1)
        temp[:,i] = np.maximum(mdls[:,j0]+convert2(np.random.choice(10,size=10,p=mdls[:,j0]/100)).reshape((10,))-np.ones((10,)),2)
        if temp[:,i].sum()!=100:
            temp[np.argmax(temp[:,i]),i] += 100-temp[:,i].sum()
        else:
            pass
    temp[:,mdls.shape[1]//2:] = top
    
    tp = mdls[:,np.argpartition(np.sum(results,axis=1), -mdls.shape[1]//20)[-mdls.shape[1]//20:]]
    
    return temp, tp
    
    
N = 1600
l = np.random.randint(0,10,(100,N))



models = convert(l)
    
models2 = convert(l)

results = np.zeros((models.shape[1],models.shape[1]),'int')

for i in range(models.shape[1]):
    for j in range(models.shape[1]):
        results[i,j] = compare(models[:,i],models[:,j])

top = models[:,np.argpartition(np.sum(results,axis=1), -N//2)[-N//2:]]

for i in range(15):
    print(i)
    models,tp  = new_models(models,top)
    if i%10==9:
        top[:,9*N//20:] = tp
    else:
        top[:,(i%10)*N//20:((i+1)%10)*N//20] = tp


comb = np.append(models,models2,axis = 1)

results = np.zeros((comb.shape[1],comb.shape[1]),'int')

for i in range(comb.shape[1]):
    for j in range(comb.shape[1]):
        results[i,j] = compare(comb[:,i],comb[:,j])
