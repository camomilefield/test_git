import turtle as t
t.speed(100)

def go_snowy(length):
    if length < 5:
        t.forward(length)
    else:
        go_snowy(length / 3)
        t.left(60)
        go_snowy(length / 3)
        t.right(120)
        go_snowy(length / 3)
        t.left(60)
        go_snowy(length / 3)


go_snowy(100)
t.right(120)
go_snowy(100)
t.right(120)
go_snowy(100)