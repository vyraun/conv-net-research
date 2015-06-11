import numpy as np
import ELLA
import convnet
import load


if __name__ == "__main__":
	print("\nLoading Data...")
	load_activations = convnet.ConvolutionalNeuralNetwork().load_data
	num_chunks = 20
	trAs = [load_activations("saved/trA{0:02d}.txt".format(i), (60000/num_chunks, 625)) for i in range(num_chunks)]
	trA = np.concatenate(trAs)
	print("trA.shape: {0}".format(trA.shape))
	teA = load_activations("saved/teA.txt", (10000, 625))
	print("teA.shape: {0}".format(teA.shape))
	trX, teX, trY, teY = load.mnist(onehot = True)
	trC = np.argmax(trY, axis = 1)
	print("trC.shape: {0}".format(trC.shape))
	teC = np.argmax(teY, axis = 1)
	print("teC.shape: {0}".format(teC.shape))
	print("Done.")

	print("\nCreating ELLA Model...")
	pass
	print("Done.")

	print("\nAnalyzing Training Data...")
	pass
	print("Done.")

	print("\nAnalyzing Testing Data...")
	pass
	print("Done.")

	print("\nExecution complete.\nProgram terminated successfully.\n")
