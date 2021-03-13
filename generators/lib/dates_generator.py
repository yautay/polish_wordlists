import datetime
import numpy as np
from generators.generator import Generator


class DatesGenerator(Generator):
    def __init__(self, start_date_ddmmyyyy: str, end_date_ddmmyyyy: str, _format: str, delimiter: str, **kwargs):
        super(DatesGenerator, self).__init__(**kwargs)
        self.__delimiter = delimiter
        self.__start_date = self.__set_date(start_date_ddmmyyyy)
        self.__end_date = self.__set_date(end_date_ddmmyyyy)
        self.__generate_data(_format)
        print("Generated {} lines of data".format(self.count_lines(self.file_out)))

    @staticmethod
    def __set_date(ddmmyyyy):
        dd = int(ddmmyyyy[:2])
        mm = int(ddmmyyyy[2:4])
        yyyy = int(ddmmyyyy[4:])
        _date = datetime.date(yyyy, mm, dd)
        return _date

    def __generate_data(self, _format):
        print("Generating list with '{}' format and '{}' delimiter".format(_format, self.__delimiter))
        switcher = {
            "yy": self.__get_yy,
            "yyyy": self.__get_yyyy,
            "mmyyyy": self.__get_mmyyyy,
            "myyyy": self.__get_myyyy,
            "mmyy": self.__get_mmyy,
            "myy": self.__get_myy,
            "ddmmyyyy": self.__get_ddmmyyyy,
            "ddmyyyy": self.__get_ddmyyyy,
            "dmmyyyy": self.__get_dmmyyyy,
            "dmyyyy": self.__get_dmyyyy,
            "ddmmyy": self.__get_ddmmyy,
            "ddmyy": self.__get_ddmyy,
            "dmyy": self.__get_dmyy,
            "dmmyy": self.__get_dmmyy,
        }
        func = switcher.get(_format)
        return func()

    def __get_ddmmyyyy(self):
        delimiter = self.__delimiter
        start = self.__start_date
        end = self.__end_date
        numdays = end - start
        with open(self.file_out, "w") as file:
            for day in range(numdays.days + 1):
                day_data = (start + datetime.timedelta(days=day))
                day_to_str = str(day_data.day)
                mon_to_str = str(day_data.month)
                if len(day_to_str) == 1:
                    day_to_str = "0{}".format(day_to_str)
                if len(mon_to_str) == 1:
                    mon_to_str = "0{}".format(mon_to_str)
                day_entry = "{dd}{deli}{mm}{deli}{yyyy}".format(dd=day_to_str,
                                                                mm=mon_to_str,
                                                                yyyy=day_data.year,
                                                                deli=delimiter)
                file.write(day_entry + "\n")

    def __get_ddmyyyy(self):
        delimiter = self.__delimiter
        start = self.__start_date
        end = self.__end_date
        numdays = end - start
        with open(self.file_out, "w") as file:
            for day in range(numdays.days + 1):
                day_data = (start + datetime.timedelta(days=day))
                day_to_str = str(day_data.day)
                if len(day_to_str) == 1:
                    day_to_str = "0{}".format(day_to_str)
                day_entry = "{dd}{deli}{m}{deli}{yyyy}".format(dd=day_to_str,
                                                               m=day_data.month,
                                                               yyyy=day_data.year,
                                                               deli=delimiter)
                file.write(day_entry + "\n")

    def __get_dmmyyyy(self):
        delimiter = self.__delimiter
        start = self.__start_date
        end = self.__end_date
        numdays = end - start
        with open(self.file_out, "w") as file:
            for day in range(numdays.days + 1):
                day_data = (start + datetime.timedelta(days=day))
                mon_to_str = str(day_data.month)
                if len(mon_to_str) == 1:
                    mon_to_str = "0{}".format(mon_to_str)
                day_entry = "{d}{deli}{mm}{deli}{yyyy}".format(d=day_data.day,
                                                               mm=mon_to_str,
                                                               yyyy=day_data.year,
                                                               deli=delimiter)
                file.write(day_entry + "\n")

    def __get_dmyyyy(self):
        delimiter = self.__delimiter
        start = self.__start_date
        end = self.__end_date
        numdays = end - start
        with open(self.file_out, "w") as file:
            for day in range(numdays.days + 1):
                day_data = (start + datetime.timedelta(days=day))
                day_entry = "{d}{deli}{m}{deli}{yyyy}".format(d=day_data.day,
                                                              m=day_data.month,
                                                              yyyy=day_data.year,
                                                              deli=delimiter)
                file.write(day_entry + "\n")

    def __get_ddmmyy(self):
        delimiter = self.__delimiter
        start = self.__start_date
        end = self.__end_date
        numdays = end - start
        with open(self.file_out, "w") as file:
            for day in range(numdays.days + 1):
                day_data = (start + datetime.timedelta(days=day))
                day_to_str = str(day_data.day)
                mon_to_str = str(day_data.month)
                year_to_str = str(day_data.year)[2:]
                if len(day_to_str) == 1:
                    day_to_str = "0{}".format(day_to_str)
                if len(mon_to_str) == 1:
                    mon_to_str = "0{}".format(mon_to_str)
                day_entry = "{dd}{deli}{mm}{deli}{yy}".format(dd=day_to_str,
                                                              mm=mon_to_str,
                                                              yy=year_to_str,
                                                              deli=delimiter)
                file.write(day_entry + "\n")

    def __get_ddmyy(self):
        delimiter = self.__delimiter
        start = self.__start_date
        end = self.__end_date
        numdays = end - start
        with open(self.file_out, "w") as file:
            for day in range(numdays.days + 1):
                day_data = (start + datetime.timedelta(days=day))
                day_to_str = str(day_data.day)
                year_to_str = str(day_data.year)[2:]
                if len(day_to_str) == 1:
                    day_to_str = "0{}".format(day_to_str)
                day_entry = "{dd}{deli}{m}{deli}{yy}".format(dd=day_to_str,
                                                             m=day_data.month,
                                                             yy=year_to_str,
                                                             deli=delimiter)
                file.write(day_entry + "\n")

    def __get_dmyy(self):
        delimiter = self.__delimiter
        start = self.__start_date
        end = self.__end_date
        numdays = end - start
        with open(self.file_out, "w") as file:
            for day in range(numdays.days + 1):
                day_data = (start + datetime.timedelta(days=day))
                year_to_str = str(day_data.year)[2:]
                day_entry = "{d}{deli}{m}{deli}{yy}".format(d=day_data.day,
                                                            m=day_data.month,
                                                            yy=year_to_str,
                                                            deli=delimiter)
                file.write(day_entry + "\n")

    def __get_dmmyy(self):
        delimiter = self.__delimiter
        start = self.__start_date
        end = self.__end_date
        numdays = end - start
        with open(self.file_out, "w") as file:
            for day in range(numdays.days + 1):
                day_data = (start + datetime.timedelta(days=day))
                mon_to_str = str(day_data.month)
                year_to_str = str(day_data.year)[2:]
                if len(mon_to_str) == 1:
                    mon_to_str = "0{}".format(mon_to_str)
                day_entry = "{d}{deli}{mm}{deli}{yy}".format(d=day_data.day,
                                                             mm=mon_to_str,
                                                             yy=year_to_str,
                                                             deli=delimiter)
                file.writelines(day_entry + "\n")

    def __get_yyyy(self):
        start = int(self.__start_date.year)
        end = int(self.__end_date.year)
        with open(self.file_out, "w") as file:
            while start <= end:
                start += 1
                file.write(str(start) + "\n")

    def __get_yy(self):
        start = int(self.__start_date.year)
        end = int(self.__end_date.year)
        data = [str(start)[2:]]
        with open(self.file_out, "w") as file:
            while start <= end:
                start += 1
                file.write(str(start)[2:] + "\n")

    def __get_mmyyyy(self):
        delimiter = self.__delimiter
        start_y = int(self.__start_date.year)
        start_m = int(self.__start_date.month)
        end_y = int(self.__end_date.year)
        data = np.empty([])
        while start_y <= end_y:
            for month in range(12):
                month += 1
                mm = str(month)
                if len(mm) == 1:
                    data = np.append(data, "0{m}{deli}{yyyy}".format(m=month, yyyy=start_y, deli=delimiter))
                    continue
                data = np.append(data, "{mm}{deli}{yyyy}".format(mm=month, yyyy=start_y, deli=delimiter))
                start_m += 1
            start_y += 1
        delta_start_m = int(self.__start_date.month) - 1
        delta_end_m = 12 - int(self.__end_date.month)
        for x in range(delta_start_m):
            data = np.delete(data, 0)
        for y in range(delta_end_m):
            data = np.delete(data, -1)
        with open(self.file_out, "w") as file:
            file.writelines(data)

    def __get_myyyy(self):
        delimiter = self.__delimiter
        start_y = int(self.__start_date.year)
        start_m = int(self.__start_date.month)
        end_y = int(self.__end_date.year)
        data = np.empty([])
        while start_y <= end_y:
            for month in range(12):
                month += 1
                data = np.append(data, "{m}{deli}{yyyy}".format(m=month, yyyy=start_y, deli=delimiter))
                start_m += 1
            start_y += 1
        delta_start_m = int(self.__start_date.month) - 1
        delta_end_m = 12 - int(self.__end_date.month)
        for x in range(delta_start_m):
            data = np.delete(data, 0)
        for y in range(delta_end_m):
            data = np.delete(data, -1)
        with open(self.file_out, "w") as file:
            file.writelines(data)

    def __get_mmyy(self):
        delimiter = self.__delimiter
        start_y = int(self.__start_date.year)
        start_m = int(self.__start_date.month)
        end_y = int(self.__end_date.year)
        data = np.empty([])
        while start_y <= end_y:
            for month in range(12):
                month += 1
                mm = str(month)
                if len(mm) == 1:
                    data = np.append(data, "0{m}{deli}{yy}".format(m=month, yy=str(start_y)[2:], deli=delimiter))
                    continue
                data = np.append(data, "{mm}{deli}{yy}".format(mm=month, yy=str(start_y)[2:], deli=delimiter))
                start_m += 1
            start_y += 1
        delta_start_m = int(self.__start_date.month) - 1
        delta_end_m = 12 - int(self.__end_date.month)
        for x in range(delta_start_m):
            data = np.delete(data, 0)
        for y in range(delta_end_m):
            data = np.delete(data, -1)
        with open(self.file_out, "w") as file:
            file.writelines(data)

    def __get_myy(self):
        delimiter = self.__delimiter
        start_y = int(self.__start_date.year)
        start_m = int(self.__start_date.month)
        end_y = int(self.__end_date.year)
        data = np.empty([])
        while start_y <= end_y:
            for month in range(12):
                month += 1
                data = np.append(data, "{m}{deli}{yy}".format(m=month, yy=str(start_y)[2:], deli=delimiter))
                start_m += 1
            start_y += 1
        delta_start_m = int(self.__start_date.month) - 1
        delta_end_m = 12 - int(self.__end_date.month)
        for x in range(delta_start_m):
            data = np.delete(data, 0)
        for y in range(delta_end_m):
            data = np.delete(data, -1)
        with open(self.file_out, "w") as file:
            file.writelines(data)
