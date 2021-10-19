from sunfounder_io import PWM,Servo

def test():
    print("Test")

    p0 = PWM("P0")
    p1 = PWM("P1")

    s0 = Servo(p0)
    s1 = Servo(p1)

    s0.angle(0)
    s1.angle(0)

    
if __name__ == "__main__":
    test()