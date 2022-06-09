import os

import pandas as pd

class Convert:
    def convert_distortion(self, file_path):
        filepath = os.path.abspath(file_path)
        with open(filepath) as f:
            lines_1 = f.readlines()
        list_1 = []
        for i in range(len(lines_1)):
            list_1 += lines_1[i].split('\t')
        while ('' in list_1) or ('\n' in list_1):
            i = 0
            for i in list_1:
                if i == '' or i == '\n':
                    list_1.remove(i)
        while ('' in list_1) or ('\n' in list_1):
            i = 0
            for i in list_1:
                if i == '' or i == '\n':
                    list_1.remove(i)
        i = 0
        while i < len(list_1):
            if list_1[i] == 'Upper Limit PASSED':
                upper_index = i
                break
            i += 1
        i = 0
        while i < len(list_1):
            if '-' in list_1[i]:
                date_index = i
                break
            i += 1

        frequence_1 = []
        for i in range(list_1.index('Dist#1 THD  [%]') + 1, list_1.index('Result')):
            frequence_1.append(list_1[i])

        upper_list = {}
        inter_list = []
        for j in range(upper_index + 1, date_index):
            inter_list.append(list_1[j])
        upper_list['Upper Limit PASSED'] = inter_list
        amplitude_list = {}
        inter_list = []
        for j in range(date_index + 6, len(list_1) - 1):
            inter_list.append(list_1[j])
        amplitude_list['Amplitude'] = inter_list

        df_1 = pd.DataFrame()
        df_1['Date'] = [list_1[date_index]]
        df_1['Time'] = [list_1[date_index + 1]]
        df_1['Calender Week'] = [list_1[date_index + 2]]
        df_1['Projectname'] = [list_1[date_index + 3]]
        df_1['Operator'] = [list_1[date_index + 4]]
        df_1['Serialnumber'] = [list_1[date_index + 5]]

        df_2 = pd.DataFrame()
        df_2['Frequency'] = frequence_1
        df_2['Amplitude'] = amplitude_list['Amplitude']
        df_1 = pd.concat([df_1, df_2], axis=1)

        df_2 = pd.DataFrame()
        df_2['Upper Limit PASSED'] = upper_list['Upper Limit PASSED']
        df_1 = pd.concat([df_1, df_2], axis=1)
        path = os.path.dirname(file_path)
        base = os.path.basename(file_path)
        base = os.path.splitext(base)
        filepath_save = '.'.join([base[0], "xlsx"])
        filepath_save = '/'.join([path, filepath_save])
        df_1.to_excel(filepath_save)
        print("fiche convert avec success")

    def convert_level(self, file_path):
        filepath = os.path.abspath(file_path)
        with open(filepath) as f:
            lines_1 = f.readlines()
        list_1 = []
        for i in range(len(lines_1)):
            list_1 += lines_1[i].split('\t')
        while ('' in list_1) or ('\n' in list_1):
            i = 0
            for i in list_1:
                if i == '' or i == '\n':
                    list_1.remove(i)
            i = 0
        while i < len(list_1):
            if list_1[i] == 'Upper Limit PASSED':
                upper_index = i
                break
            i += 1
        i = 0
        while i < len(list_1):
            if list_1[i] == 'Lower Limit PASSED':
                Lower_index = i
                break
            i += 1
        i = 0
        while i < len(list_1):
            if '-' in list_1[i]:
                date_index = i
                break
            i += 1
        frequence_1 = []
        for i in range(list_1.index('Frequency response [dBSPL]') + 1, list_1.index('Result')):
            frequence_1.append(list_1[i])

        upper_list = {}
        inter_list = []
        for j in range(upper_index + 1, Lower_index):
            inter_list.append(list_1[j])
            upper_list['Upper Limit PASSED'] = inter_list

        Lower_list = {}
        inter_list = []
        for j in range(Lower_index + 1, date_index):
            inter_list.append(list_1[j])
            Lower_list['Lower Limit PASSED'] = inter_list

        amplitude_list = {}
        inter_list = []
        for j in range(date_index + 6, len(list_1) - 1):
            inter_list.append(list_1[j])
        amplitude_list['Amplitude'] = inter_list

        df_1 = pd.DataFrame()
        df_1['Date'] = [list_1[date_index]]
        df_1['Time'] = [list_1[date_index + 1]]
        df_1['Calender Week'] = [list_1[date_index + 2]]
        df_1['Projectname'] = [list_1[date_index + 3]]
        df_1['Operator'] = [list_1[date_index + 4]]
        df_1['Serialnumber'] = [list_1[date_index + 5]]

        df_2 = pd.DataFrame()
        df_3 = pd.DataFrame()
        df_2['Frequency'] = frequence_1
        df_3['Amplitude'] = amplitude_list['Amplitude']
        df_1 = pd.concat([df_1, df_2, df_3], axis=1)

        df_2 = pd.DataFrame()
        df_2['Upper Limit PASSED'] = upper_list['Upper Limit PASSED']
        df_2['Lower Limit PASSED'] = Lower_list['Lower Limit PASSED']
        df_1 = pd.concat([df_1, df_2], axis=1)
        path = os.path.dirname(file_path)
        base = os.path.basename(file_path)
        base = os.path.splitext(base)
        filepath_save = '.'.join([base[0], "xlsx"])
        filepath_save = '/'.join([path, filepath_save])
        df_1.to_excel(filepath_save)
        print("fiche convert avec success")

    def convert_steepness(self, file_path):
        filepath = os.path.abspath(file_path)
        with open(filepath) as f:
            lines_1 = f.readlines()
        list_1 = []
        for i in range(len(lines_1)):
            list_1 += lines_1[i].split('\t')
        while ('' in list_1) or ('\n' in list_1):
            i = 0
            for i in list_1:
                if i == '' or i == '\n':
                    list_1.remove(i)
        upper_index = []
        i = 0
        while i < len(list_1):
            if list_1[i] == 'Upper Limit Chirp#1 PASSED':
                upper_index.append(i)
            i += 1

        date_index = []
        i = 0
        while i < len(list_1):
            if '-' in list_1[i]:
                date_index.append(i)
            i += 1
        frequence_1 = []
        for i in range(list_1.index('Band') + 1, list_1.index('Result')):
            frequence_1.append(list_1[i])

        upper_list = {}
        k = 1
        for p, i in enumerate(upper_index):
            list_inter = []
            if p != len(upper_index) - 1:
                for j in range(i + 2, upper_index[p + 1]):
                    list_inter.append(list_1[j])
            else:
                for j in range(i + 2, date_index[0]):
                    list_inter.append(list_1[j])
                upper_list[' Upper Limit Chirp#1 PASSED{}'.format(k)] = list_inter
                k += 1

        amplitude_list = {}
        k = 1
        for p, i in enumerate(date_index):
            list_inter = []
            if p != len(upper_index) - 1:
                for j in range(i + 7, date_index[p + 1] - 1):
                    list_inter.append(list_1[j])
            else:
                for j in range(i + 7, len(list_1) - 1):
                    list_inter.append(list_1[j])
            amplitude_list['Amplitude {}'.format(k)] = list_inter
            k += 1
        date_list = {}
        Time_list = {}
        Calender_Week_list = {}
        Projectname_list = {}
        Operator_list = {}
        Serialnumber_list = {}
        Steepness_response_chirp_1_list = {}
        for i in range(len(date_index)):
            j = i + 1
            date_list[j] = list_1[date_index[i]]
            Time_list[j] = list_1[date_index[i] + 1]
            Calender_Week_list[j] = list_1[date_index[i] + 2]
            Projectname_list[j] = list_1[date_index[i] + 3]
            Operator_list[j] = list_1[date_index[i] + 4]
            Serialnumber_list[j] = list_1[date_index[i] + 5]
            Steepness_response_chirp_1_list[j] = list_1[date_index[i] + 6]

        df_1 = pd.DataFrame()
        df_1['Date'] = date_list.values()
        df_1['Time'] = Time_list.values()
        df_1['Calender Week'] = Calender_Week_list.values()
        df_1['Projectname'] = Projectname_list.values()
        df_1['Operator'] = Operator_list.values()
        df_1['Serialnumber'] = Serialnumber_list.values()
        df_1['Steepness response chipr 1'] = Steepness_response_chirp_1_list.values()

        df_2 = pd.DataFrame()
        df_2['Frequence'] = frequence_1
        df_1 = pd.concat([df_1, df_2], axis=1)
        for i in amplitude_list.keys():
            df_inter = pd.DataFrame()
            df_inter[i] = amplitude_list[i]
            df_1 = pd.concat([df_1, df_inter], axis=1)
        path = os.path.dirname(file_path)
        base = os.path.basename(file_path)
        base = os.path.splitext(base)
        filepath_save = '.'.join([base[0], "xlsx"])
        filepath_save = '/'.join([path, filepath_save])
        df_1.to_excel(filepath_save)
        print("fiche convert avec success")