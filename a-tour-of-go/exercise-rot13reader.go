package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func (r rot13Reader) Read(b []byte) (n int, e error) {
	n, e = r.r.Read(b)
	
	for i, v := range b {
		if v >= 'A' && v <= 'M' || v >= 'a' && v <= 'm' {
			b[i] += 13
		} else if v >= 'N' && v <= 'Z' || v >= 'n' && v <= 'z' {
			b[i] -= 13
		}
	}
	
	return
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}

