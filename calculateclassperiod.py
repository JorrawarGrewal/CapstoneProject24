from datetime import datetime


def getclasspd():
    now = datetime.now()

    time_in_mins = (int(now.strftime('%H')) * 60) + int(now.strftime('%M'))
    class_period = 'NOT IN SCHOOL'

    # for wednesdays
    if now.weekday == 3:
        # 7:00 - 8:07
        if 487 > time_in_mins > 420:
            class_period = 1
        # 8:07 - 8:58
        elif 538 > time_in_mins > 487:
            class_period = 2
        # 8:58 - 9:49
        elif 589 > time_in_mins > 538:
            class_period = 3
        # 9:49 - 10:49
        elif 649 > time_in_mins > 589:
            class_period = "HR"
        # 10:59 - 12:39
        elif 759 > time_in_mins > 649:
            class_period = 4
        # 12:49 - 1:30
        elif 810 > time_in_mins > 759:
            class_period = 5
        # 1:40 - 2:22
        elif 862 > time_in_mins > 810:
            class_period = 6

    # for not wednesday
    else:
        # 7:25 - 8:19
        if 499 > time_in_mins > 420:
            class_period = 1
        # 8:19 - 9:22
        if 562 > time_in_mins > 499:
            class_period = 2
        # 9:22 - 10:25
        if 625 > time_in_mins > 562:
            class_period = 3
        # 10:25 - 12:15
        if 735 > time_in_mins > 625:
            class_period = 4
        # 12:15 - 1:18
        if 798 > time_in_mins > 735:
            class_period = 5
        # 1:18 - 2:22
        if 862 > time_in_mins > 798:
            class_period = 6

    return str(class_period)

def late_or_not():
    now = datetime.now()

    time_in_mins = (int(now.strftime('%H')) * 60) + int(now.strftime('%M'))
    late = "PRESENT"

    # for wednesdays
    if now.weekday == 3:
        # 7:25 - 8:07
        if 487 > time_in_mins > 445:
            late = "LATE"
        # 8:07 - 8:58
        elif 538 > time_in_mins > 497:
            late = "LATE"
        # 8:58 - 9:49
        elif 589 > time_in_mins > 548:
            late = "LATE"
        # 9:49 - 10:49
        elif 649 > time_in_mins > 599:
            late = "LATE"
        # 10:59 - 12:39
        elif 759 > time_in_mins > 659:
            late = "LATE"
        # 12:49 - 1:30
        elif 810 > time_in_mins > 769:
            late = "LATE"
        # 1:40 - 2:22
        elif 862 > time_in_mins > 820:
            late = "LATE"

    # for not wednesday
    else:
        # 7:25 - 8:19
        if 499 > time_in_mins > 445:
            late = "LATE"
        # 8:19 - 9:22
        if 562 > time_in_mins > 509:
            late = "LATE"
        # 9:22 - 10:25
        if 625 > time_in_mins > 572:
            late = "LATE"
        # 10:25 - 12:15
        if 735 > time_in_mins > 635:
            late = "LATE"
        # 12:15 - 1:18
        if 798 > time_in_mins > 745:
            late = "LATE"
        # 1:18 - 2:22
        if 862 > time_in_mins > 808:
            late = "LATE"

    return late
