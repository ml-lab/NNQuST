import torch

def cplx_SS(x, y):
	'''A function that does complex scalar multiplication.'''
	if list(x.size())[0] < 2 or list(y.size())[0] < 2:
		raise ValueError('An input is not of the right dimension.')

	z = torch.zeros(2)	
	z[0] = x[0]*y[0] - x[1]*y[1]
	z[1] = x[0]*y[1] + x[1]*y[0]

	return z

def cplx_MV(x, y):
	'''A function that returns x*y, where x is a complex tensor and y is a complex vector.''' 
	if len(list(x.size())) < 3 or len(list(y.size())) < 2:
		raise ValueError('An input is not of the right dimension.')

	z = torch.zeros(2, x.size()[0])
	z[0] = torch.mv(x[0],y[0]) - torch.mv(x[1],y[1])
	z[1] = torch.mv(x[0],y[1]) + torch.mv(x[1],y[0])

	return z

def cplx_MM(x, y):
	'''A function that returns x*y, where x and y are complex tensors.'''
	if len(list(x.size())) < 3 or len(list(y.size())) < 3:
		raise ValueError('An input is not of the right dimension.')

	z = torch.zeros(2, x.size()[1], y.size()[2])
	z[0] = torch.matmul(x[0],y[0]) - torch.matmul(x[1], y[1])
	z[1] = torch.matmul(x[0],y[1]) + torch.matmul(x[1], y[0])

	return z

def cplx_ADD(x, y):
	'''A function that adds two complex tensors or vectors, x and y.'''
	if len(list(x.size())) < 2 or len(list(y.size())) < 2:
		raise ValueError('An input is not of the right dimension.')

	z = torch.zeros_like(x)
	z[0] = x[0] + y[0]
	z[1] = x[1] + y[1]

	return z
	
def cplx_DOT(x,y):
	'''A function that returns the dot product of two complex vectors, x and y.'''	
	if len(list(x.size())) < 2 or len(list(y.size())) < 2:
		raise ValueError('An input is not of the right dimension.')
	
	z = torch.zeros(2)
	z[0] = torch.dot(x[0], y[0]) - torch.dot(x[1], y[1])
	z[1] = torch.dot(x[0], y[1]) + torch.dot(x[1], y[0])
	
	return z

def cplx_OUTER(x,y):
	'''A function that returns the outer product of two complex vectors, x and y.'''
	if len(list(x.size())) < 2 or len(list(y.size())) < 2:
		raise ValueError('An input is not of the right dimension.')

	z = torch.zeros(2, x.size()[1], y.size()[1])
	z[0] = torch.ger(x[0], y[0]) - torch.ger(x[1], y[1])
	z[1] = torch.ger(x[0], y[1]) + torch.ger(x[1], y[0])

	return z

def cplx_TRANSPOSE(x):
	'''A function that returns the complex transpose of a complex tensor or vector, x.'''
	if len(list(x.size())) < 3:
		raise ValueError('An input is not of the right dimension.')

	z = torch.zeros(2, x.size()[2], x.size()[1])
	z[0] = torch.transpose(x[0], 0, 1) 
	z[1] = -torch.transpose(x[1], 0, 1) 

	return z