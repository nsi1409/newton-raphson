import torch

i = 0
poly_coef = []
print('confirm list of coefficients with \'y\'')
print('cancel list of coefficients with \'n\'')
while(True):
	inpt = input(f'input {i}th order polynomial term: ')
	if inpt == 'y':
		break
	if inpt == 'n':
		i = 0
		poly_coef = []
		continue
	inpt = torch.Tensor([int(inpt)])
	poly_coef.append(inpt)
	i += 1

print(poly_coef)
