def robot_location(record: str) -> str:
    metre = 0
    value = ''
    for x in record:
        if x == 'F':
            metre += int(value)
            value = '0'
        elif x == 'B':
            metre -= int(value)
            value = '0'
        else:
            value += x
    if metre > 0:
        return '+' + str(metre)
    elif metre < 0:
        return str(metre)
    else:
        return '0'


assert (robot_location('') == '0')
assert (robot_location('1F') == '+1')
assert (robot_location('1B') == '-1')
assert (robot_location('100F') == '+100')
assert (robot_location('1B1F') == '0')
assert (robot_location('2B1F') == '-1')
assert (robot_location('1F2B3F') == '+2')
assert (robot_location('1F1F3F') == '+5')
assert (robot_location('1B1B1B') == '-3')
assert (robot_location('1B2F10B') == '-9')
assert (robot_location('100F99B') == '+1')
assert (robot_location('1F2B3F4B') == '-2')
assert (robot_location('5F3B1F10F') == '+13')
assert (robot_location('134F32B33F') == '+135')
assert (robot_location('149B137F79F26F') == '+93')
assert (robot_location('196B52B167B19F21F') == '-375')
assert (robot_location('42B117F106B101B109B28B') == '-269')
assert (robot_location('154B20B16F6B142B100F191B') == '-397')
assert (robot_location('182B49B68B111B76B185B57B136F') == '-592')
assert (robot_location('169B173B36F155F153F108F3B199B98B') == '-190')
assert robot_location('') == '0'

