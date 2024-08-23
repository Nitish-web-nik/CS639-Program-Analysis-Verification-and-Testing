pendown
:temp = 100

if (:x > 10)
[
    repeat 4 [
        forward 100
        right 89
        backward 11
    ]
]

if (:x < 0)
[
    left 180
    :temp = -:x
    forward :temp
    
    if (:y > 0)
    [
        right 90
        if (:y > 250)
        [
            backward 100
        ]
        if (:y < 0)
        [
            left 100
        ]
        forward :y
    ]
    else
    [
        left 90
        :temp = -:y
        forward :temp
    ]
]

if (:m < 100)
[
    if (:y > 250)
    [
        backward 100
    ]
    if (:y < 0)
    [
        left 100
    ]
    left 30
    forward 50
    right 45
    forward 70
]
else
[
    right 60
    forward 80
    left 45
    forward 60
]

penup
goto(0, -50)
pendown

forward(50)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(50)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)
right(60)
forward(20)
left(60)
forward(20)

penup
goto(0, 0)
