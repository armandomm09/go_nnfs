package main

import "fmt"

func main() {
	inputs := []float32{1, 2, 3, 2.5}

	weights := [][]float32{
		{0.2, 0.8, -0.5, 1.0},
		{0.5, -0.91, 0.26, -0.5},
		{-0.26, -0.27, 0.17, 0.87},
	}

	biases := []float32{2, 3, 0.5}

	outputs := make([]float32, 3)

	for i := range weights {
		neuronWeights := weights[i]
		neuronB := biases[i]

		var neuronOut float32

		for j := range neuronWeights {
			neuronOut += neuronWeights[j] * inputs[j]
		}

		neuronOut += neuronB
		outputs[i] = neuronOut
	}

	fmt.Println(outputs)

}
