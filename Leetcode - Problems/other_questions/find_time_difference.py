# A string represents an interval of time.
# Start and end time of the interval is separated by "-". For ex:- 9:00am-10:00am
# Both the start and end time will be in 12 hour format. You should return the number of minutes between these.
# 8:00am-9:00am should return 60 minutes.
# 1:00pm-11:00am should return 1320 minutes.


# solution:-

from datetime import datetime

class Solution:
    def minutes_in_between(self, time: str) -> int:
        input_list = split_string(time)
        time1 = convert_str_to_24hrs_format(input_list[0])
        time2 = convert_str_to_24hrs_format(input_list[-1])
        return time_difference_returner(time1, time2)


def split_string(stringg: str) -> list:
    string1 = stringg
    replaced_string = string1.replace("-", " ")
    list1 = replaced_string.split(" ")
    return list1


def convert_str_to_24hrs_format(stringg: str) -> datetime.time:
    string1 = stringg.upper()
    format1 = "%I:%M%p"
    string_to_time = datetime.strptime(string1, format1)
    return string_to_time


def time_difference_returner(time1: datetime.time, time2: datetime.time) -> int:
    a = time1
    b = time2
    c = b - a
    minutes = c.seconds/60
    return int(minutes)


if __name__ == '__main__':
    time_difference_object = Solution()
    print(time_difference_object.minutes_in_between("4:25pm-11:00am"))
    print(time_difference_object.minutes_in_between("1:01pm-11:00am"))
