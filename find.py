import torch

i = 0
poly_coef = []
print('confirm list of coefficients with \'y\'')
print('cancel list of coefficients with \'n\'')
while(True):
	inpt = input(f'input {i}th order polynomial coefficient: ')
	if inpt == 'y':
		break
	if inpt == 'n':
		i = 0
		poly_coef = []
		continue
	inpt = int(inpt)
	poly_coef.append(inpt)
	i += 1
x = torch.tensor(float(input('initial value of x: ')), requires_grad=True)

def forward(x):
	outp = torch.tensor(0.0)
	for i in range(len(poly_coef)):
		outp += poly_coef[i] * (x ** i)
	return outp

iters = int(input('number of iterations: '))
for i in range(iters):
	y = forward(x)
	y.backward()
	print(f'x = {x}, y = {y}, grad = {x.grad}')
	delta = float(y / x.grad)
	x = torch.tensor(float(x-delta), requires_grad=True)
