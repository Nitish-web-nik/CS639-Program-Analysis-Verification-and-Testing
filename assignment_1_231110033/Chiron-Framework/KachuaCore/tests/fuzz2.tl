if (:x >= 0 && :y > 29) [
    backward 8
    right 10
    forward 10
    forward 20
    left 90
    if (:y > 5) [
        right 40
        backward 8
        left 40
    ]
] else [
    backward 19
    right 60
    if (:y > 5) [
        right 30
        backward 80
        left 30
    ]
]

pendown


if (:x >= -119) [
    backward 9
]

if (:x > 10 && :y <= -30) [
    forward 20
    right 30
    right 60
    forward 40
    if (:x < 10) [
        right 30
        forward 8
        left 30
    ]
]

if (:x >= 0 && :y > 60) [
    backward 9
    forward 40
    left 90
    if (:x > 5) [
        right 20
        backward 8
        left 20
    ]
] else [
    right 60
    left 90
    goto(-10, 8)
    if (:x > 5) [
        right 20
        backward 8
        left 20
    ]
]