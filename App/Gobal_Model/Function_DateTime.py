# -*- coding: utf-8 -*-

'''
    项目名称: 公共函数 - 日期格式化处理
    项目简介: 该函数主要用于输出格式化的日期
    维护记录: 2021-12-18 yjb
'''
from datetime import datetime
import datetime as dateTimeAll


class Date:
    # 日期时间格式化
    def DateTimeFormat(self, dateTime=None, formatStr='%Y-%m-%d %H:%M:%S.%f', cutCount=3):
        '''
            :param dateTime: datetime。日期时间, 默认为当前执行的系统时间
            :param formatStr: string。格式化语句。默认为 yyyy-MM-dd HH:mm:ss.ffffff
            :param cutCount: string。从右起截断长度, 默认为3。即默认输出为 yyyy-MM-dd HH:mm:ss.fff
            :return: 格式化后的日期时间字符串
        '''
        if dateTime is None:
            dateTime = datetime.now()
        if cutCount == 0:
            return dateTime.strftime(formatStr)
        else:
            return dateTime.strftime(formatStr)[:-cutCount]

    # 计算日期时间差
    def DateTimeCalculte(self, startDateTime, endDateTime=None, formatStr='%Y-%m-%d %H:%M:%S.%f', mode='s'):
        '''
            :param startDateTime: datetime。起始日期时间。
            :param endDateTime: datetime。结束日期时间。默认为当前执行的系统时间
            :param formatStr: string。计算时日期格式, 默认为 yyyy-MM-dd HH:mm:ss.ffffff
            :param mode: string。输出结果类型。默认为秒, 预设有: 天(d), 秒(s)
            :return: 指定类型的时间差
        '''
        startDateTime = datetime.strptime(startDateTime, formatStr)
        if endDateTime is None:
            endDateTime = datetime.now()
        else:
            endDateTime = datetime.strptime(endDateTime, formatStr)
        delta = endDateTime - startDateTime
        if mode == 'd':
            return delta.days
        elif mode == 's':
            dayInterval = int(delta.days) * 24 * 60 * 60
            secondInterval = delta.seconds
            return dayInterval + secondInterval

    # 计算指定天数下的时间区间
    def DealDateArea(self, dayNumber, dayType=True):
        today = dateTimeAll.datetime.now()
        # today = today - dateTimeAll.timedelta(days= 31)

        # today = today - dateTimeAll.timedelta(days= 31)
        # print(today)
        # 计算偏移量
        last_offset = dateTimeAll.timedelta(days=1)
        offset = dateTimeAll.timedelta(days=dayNumber)

        if dayType:
            dayNumber = -dayNumber
            offset = dateTimeAll.timedelta(days=dayNumber)
            re_date = (today - last_offset).strftime('%Y-%m-%d')
            today = (today + offset).strftime('%Y-%m-%d')
        else:
            re_date = (today + offset - last_offset).strftime('%Y-%m-%d')
            today = today.strftime('%Y-%m-%d')

        # 获取想要的日期的时间
        return {'startTime': today + ' 00:00:00', 'endTime': re_date + ' 23:59:59'}

    # 计算时间段列表
    def TimeSlot(self, startTime, endTime, timeSlotList=[]):
        startMonth = int(startTime.split('-')[0] + startTime.split('-')[1])
        endMonth = int(endTime.split('-')[0] + endTime.split('-')[1])
        if startMonth == endMonth:

            endMonth = str(endTime.split(' ')[0]) + ' 23:59:59'
            timeSlotList.append([startTime, endMonth])
            # print(timeSlotList)
            return timeSlotList
        else:
            nextMonth = int(startTime.split('-')[1]) + 1
            if nextMonth > 12:
                nextMonth = nextMonth - 12
                if len(str(nextMonth)) == 1:
                    nextMonth = '0' + str(nextMonth)
                else:
                    nextMonth = str(nextMonth)
                nextMonthTime = str(
                    int(startTime.split('-')[0]) + 1) + '-'+nextMonth + '-01 00:00:00'
                startTime = startTime + ' 00:00:00'
                timeSlotList.append([startTime, nextMonthTime])
                return Date().TimeSlot(nextMonthTime, endTime, timeSlotList)
            else:
                if len(str(nextMonth)) == 1:
                    nextMonth = '0' + str(nextMonth)
                else:
                    nextMonth = str(nextMonth)
                nextMonthTime = str(
                    int(startTime.split('-')[0])) + '-' + nextMonth + '-01 00:00:00'
                startTime = startTime + ' 00:00:00'
                timeSlotList.append([startTime, nextMonthTime])
                return Date().TimeSlot(nextMonthTime, endTime, timeSlotList)

    # 计算某个月的第一天于最后一天
    def GetMonthDay(self, monthNumber=''):
        year = int(monthNumber[0:4])
        month = int(monthNumber[4:6])
        dt_start = (datetime(year, int(month), 1)).strftime("%Y-%m-%d")
        if 12 == int(month):
            dt_end = (datetime(year, 12, 31)).strftime("%Y-%m-%d")
        else:
            dt_end = (datetime(year, int(month)+1, 1) -
                      dateTimeAll.timedelta(days=1)).strftime("%Y-%m-%d")

        return {
            'startTime': dt_start,
            'endTime': dt_end
        }

    # 计算时间段内每天的列表
    def getBetweenDay(self, startTime, endTime):
        date_list = []
        begin_date = datetime.strptime(startTime, "%Y-%m-%d")
        end_date = datetime.strptime(endTime, "%Y-%m-%d")
        while begin_date <= end_date:
            # date_start = begin_date.strftime("%Y-%m-%d") + ' 00:00:00'
            date_start = begin_date.strftime("%Y-%m-%d")
            # date_end = begin_date.strftime("%Y-%m-%d") + ' 23:59:59'
            # date_list.append([date_start,date_end])
            date_list.append(date_start)
            begin_date += dateTimeAll.timedelta(days=1)
        return date_list
