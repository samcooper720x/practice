package main

import (
	"golang.org/x/tour/pic"
)

func Pic(dx, dy int) [][]uint8 {
	pic := make([][]uint8, dy)

	for i := 0; i < dy; i++ {
		pic[i] = make([]uint8, dx)
	}

	for i := range pic {
		for j := range pic {
			switch {
			case i%2 == 0:
				switch {
				case j%2 == 0:
					pic[i][j] = 0
				default:
					pic[i][j] = 240
				}
			default:
				switch {
				case j%2 == 0:
					pic[i][j] = 240
				default:
					pic[i][j] = 0
				}
			}
		}
	}

	return pic
}

func main() {
	pic.Show(Pic)
}

