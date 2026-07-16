package main

import "fmt"

func main() {
	str := "hello main this is me"

	mapping := map[string]int{}

	for _, ch := range str {
		if ch == ' ' {
			continue
		}
		mapping[string(ch)]++
	}
	fmt.Println(mapping)
}