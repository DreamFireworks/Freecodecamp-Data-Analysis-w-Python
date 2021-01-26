import numpy as np

def calculate(x):
  if len(x) == 9:
    x=np.array(x).reshape(3,3)
    calculations={
      'mean':[np.mean(x,axis=0).tolist(),np.mean(x,axis=1).tolist(),np.mean(x).tolist()],
      'variance':[np.var(x,axis=0).tolist(),np.var(x,axis=1).tolist(),np.var(x).tolist()],
      'standard deviation':[np.std(x,axis=0).tolist(),np.std(x,axis=1).tolist(),np.std(x).tolist()],
      'max':[np.max(x,axis=0).tolist(),np.max(x,axis=1).tolist(),np.max(x).tolist()],
      'min':[np.min(x,axis=0).tolist(),np.min(x,axis=1).tolist(),np.min(x).tolist()],
      'sum':[np.sum(x,axis=0).tolist(),np.sum(x,axis=1).tolist(),np.sum(x).tolist()]}
    return calculations  
  else:
    raise ValueError("List must contain nine numbers.") 
