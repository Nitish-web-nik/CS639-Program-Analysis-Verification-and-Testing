if (:x <= -50) [
    if (:y >= 39) [
        backward 50
        left 45
        forward 110
    ]
]

if (:x >= 139) [
    repeat 2 [
        forward 70
        right 79
        backward 15
    ]
]

if (:x <= 50) [
    if (:y > 150) [
        backward 50
    ]
    if (:y < 0) [
        left 60
    ]
]

pendown

repeat 2 [
    forward 20
    if (:y > 20) [
        right 25
        forward 20
    ]
    else [
        left 25
        forward 20
    ]
    if (:x <= -5) [
        forward 10
    ]
    else [
        :y = :x + :y
    ]
]

if (:x == 0) [
    left 45
    backward 80
]
