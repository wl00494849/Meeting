package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"strings"
)

type ky struct {
	K string
	V int
}
type maxheap []ky

func (h maxheap) up(i int) {
	for {
		parent := (i - 1) / 2
		if parent == i || h[parent].V > h[i].V {
			break
		}
		h.swap(&h[parent], &h[i])
		i = parent
	}
}
func (h maxheap) down(i0 int) {
	i := i0
	for {
		j1 := i*2 + 1
		if j1 < 0 || j1 >= h.len() {
			break
		}
		j := j1
		if j2 := i*2 + 2; j2 < h.len() && h[j1].V < h[j2].V {
			j = j2
		}
		if h[i].V > h[j].V {
			break
		}
		h.swap(&h[i], &h[j])
		i = j
	}
}
func (h *maxheap) push(n ky) {
	*h = append(*h, n)
	h.up(h.len() - 1)
}
func (h *maxheap) pop() (string, int) {
	n := (*h)[0].K
	v := (*h)[0].V
	h.swap(&(*h)[0], &(*h)[h.len()-1])
	*h = (*h)[:h.len()-1]
	if h.len() > 1 {
		h.down(0)
	}
	return n, v
}

func (h maxheap) swap(a, b *ky) {
	*a, *b = *b, *a
}

func (h maxheap) len() int {
	return len(h)
}

func readCSV(fileStr string) [][]string {
	f, err := os.Open(fileStr)
	if err != nil {
		panic(err)
	}

	defer f.Close()

	csvRd := csv.NewReader(f)
	record, err := csvRd.ReadAll()
	if err != nil {
		panic(err)
	}

	return record
}

func main() {
	m := map[string]int{}
	h := &maxheap{}
	data := readCSV("new.csv")
	for i := 1; i < len(data); i++ {
		sli := strings.Split(data[i][2], ";")
		for _, s := range sli {
			m[s]++
		}
	}

	for k, v := range m {
		d := &ky{
			K: k,
			V: v,
		}
		h.push(*d)
	}

	for i := 0; i < len(*h); i++ {
		s, v := h.pop()
		fmt.Println("Key: ", s, ",", "Val: ", v)
	}
}
