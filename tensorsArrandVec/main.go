package main

import (
	"fmt"

	t "gorgonia.org/tensor"
)

func main() {

	// inputs :=

	inputs := t.New(t.WithBacking([]float32{1, 2, 3, 2.5}))

	rawW := []float32{
		0.2, 0.8, -0.5, 1.0,
		0.5, -0.92, 0.36, -0.5,
		-0.26, -0.27, 0.17, 0.87,
	}
	weights := t.New(t.WithBacking(rawW), t.WithShape(3, 4))

	biases := t.New(t.WithBacking([]float32{2, 3, 0.5}))

	dp, err := t.Dot(weights, inputs)
	if err != nil {
		fmt.Println(err)
	}

	out, err := t.Add(dp, biases)
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(out)

}

// l := [][][]int32{
// 	{
// 		{1, 5, 6, 2},
// 		{3, 2, 1, 3},
// 	},

// 	{
// 		{5, 2, 1, 2},
// 		{6, 4, 8, 4},
// 	},

// 	{
// 		{2, 8, 5, 3},
// 		{1, 1, 9, 4},
// 	},
// }
