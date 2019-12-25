/*
https://codeforces.com/contest/1278/problem/A
https://codeforces.com/contest/1278/submission/67583453
https://github.com/miloszlakomy/competitive/tree/master/codeforces/1278A
*/

package main

import (
	"fmt"
)

func main() {
	var (
		t        uint
		channels []chan bool
	)

	for fmt.Scanln(&t); t > 0; t-- {
		// Declaration inside the for block necessary to avoid races.
		var p, h string

		fmt.Scanln(&p)
		fmt.Scanln(&h)

		ch := make(chan bool)
		channels = append(channels, ch)
		go func() {
			ch <- solve(p, h)
		}()
	}

	for _, ch := range channels {
		if <-ch {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
	}
}

func solve(p, h string) bool {
	if len(h) < len(p) {
		return false
	}

	var pms, hms ['z' - 'a' + 1]uint
	for _, c := range p {
		pms[c-'a']++
	}
	for _, c := range h[:len(p)] {
		hms[c-'a']++
	}

	if pms == hms {
		return true
	}

	for i := 0; i < len(h)-len(p); i++ {
		hms[h[i]-'a']--
		hms[h[i+len(p)]-'a']++

		if pms == hms {
			return true
		}
	}

	return false
}
