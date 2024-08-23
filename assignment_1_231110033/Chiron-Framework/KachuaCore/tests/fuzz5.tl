if (:x <= -50)
[
    if (:y >= 39)
    [
        backward 50
        left 45
        forward 110
    ]
]

if (:x >= 139)
[
    repeat 2 [
        forward 70
        right 79
        backward 15
    ]
]

if (:x <= 50)
[
    if (:y > 150)
    [
        backward 50
    ]
    if (:y < 0)
    [
        left 60
    ]
]

pendown

repeat 2 [
    forward 20
    if (:y > 20)
    [
        right 25
        forward 20
    ]
    else
    [
        left 25
        forward 20
    ]
    if (:x <= -5)
    [
        forward 10
    ]
    else
    [
        :y = :x + :y
    ]
]

if (:x == 0)
[
    left 45
    backward 80
]

pendown

:e = 15

if (:y == 39)
[
    backward 9
]

if (:x > -50 && :y <= 0)
[
    forward 20
    left 80
    backward 9
    right 75
    forward 10
    if (:y < -5)
    [
        right 20
        forward 5
        left 20
    ]
]

if (:x >= 0 && :y > 29)
[
    backward 8
    right 10
    forward 10
    forward 20
    left 90
    if (:y > 5)
    [
        right 40
        backward 8
        left 40
    ]
]

else
[
    backward 19
    :e = :e * 25
    right 60
    if (:y > 5)
    [
        right 30
        backward 80
        left 30
    ]
]

pendown

:e = 45

if (:x >= -119)
[
    backward 9
]

if (:x > 10 && :y <= -30)
[
    forward 20
    :e = 0
    right 30
    right 60
    forward 40
    if (:x < 10)
    [
        right 30
        forward 8
        left 30
    ]
]

if (:x >= 0 && :y > 60)
[
    backward 9
    forward 40
    left 90
    if (:x > 5)
    [
        right 20
        backward 8
        left 20
    ]
]

else
[
    :e = :e * 25
    right 60
    left 90
    goto(-10, 8)
    if (:x > 5)
    [
        right 20
        backward 8
        left 20
    ]
]
