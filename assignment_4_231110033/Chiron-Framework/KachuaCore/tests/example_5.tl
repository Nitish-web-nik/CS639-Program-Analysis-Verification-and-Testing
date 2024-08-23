forward :a
right 90
if(:a <= 5)[
    forward 30
    left 90
    backward 50
    forward :a
]
else[
    forward :a
    left 90
    backward 40
]