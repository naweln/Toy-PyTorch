from linear import Linear
from torch import Tensor
from network import Network
from MSE import MSE


if __name__ == '__main__':

	x = Tensor([1, 2, 3])
	y = Tensor([7, 10])
	print(x.shape, y.shape)

	linear = Linear(x.shape[0], y.shape[0], weight_init='ones')
	net = Network([linear])

	pred = net.forward(x)


	
	#loss.backward()
	print("Pred is ")
	print(pred)
	#print(x.grad)

	linear1 = Linear(x.shape[0], x.shape[0], weight_init='ones')
	linear2 = Linear(x.shape[0], y.shape[0], weight_init='ones')
	
	net_2layer = Network([linear1, linear2])

	pred_2layer = net_2layer.forward(x)

	#loss.backward()
	print("pred_2layer is ")
	print(pred_2layer)
	
	mse = MSE()
	loss = mse.forward(pred_2layer, y)
	print("loss for 2 layer net is ")
	print(loss)

	# Should be 2*(18-7) = 22
	loss_grad = mse.backward()
	print("loss_grad for 2layer net is ")
	print(loss_grad)

	net_2layer.backward(loss_grad)


	
