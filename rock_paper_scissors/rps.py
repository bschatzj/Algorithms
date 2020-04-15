#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    answer_Array = []
    options = ["rock", "paper", "scissors"]

    def loop_function(n, playsArray):
        if n == 0:
            answer_Array.append(playsArray)
            return
        else:
            for i in range(len(options)):
                print(options[i])
                option = options[i]
                print(option)
                # WHY IS THIS APPENDING NONE!?!?!?!
                loop_function(n - 1, playsArray + [option])

    loop_function(n, [])

    return answer_Array


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")
