package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	for i := 0; i < n; i++ {
		line, _ := reader.ReadString('\n')
		s := strings.TrimSpace(line)

		score := 0
		for j := 0; j < len(s); j++ {
			if s[j] == ' ' {
				continue
			} else {
				for k := 0; k < len(alphabet); k++ {
					if s[j] == alphabet[k] {
						score += k + 1
						break
					}
				}
			}
		}

		if score == 100 {
			fmt.Fprintln(writer, "PERFECT LIFE")
		} else {
			fmt.Fprintln(writer, score)
		}
	}
}
