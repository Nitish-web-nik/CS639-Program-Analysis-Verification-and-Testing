:a = 80
forward :a
left 90
:b = 100
backward :b
right 90
if(:a > 5)[
    if(:b <= 200)[
        forward 30
        right 90
    ]
    else[
        backward 60
        left 90
    ]
    backward 50
]
else[
    forward 10
]