
import numpy as np

from django.db import connections

class threeAvg:
    c = connections['usaunem'].cursor()
    for_three_months = 3

    def close_everything(self):
        self.c.close()


    def counting_till(self,value):
        last_count = c.execute("SELECT COUNT (monthlydates) FROM usaunemploymentavg")
        count_till = last_count.fetchone()[0] - value
        print('checkpoint 2')
        return count_till #returns till which row we have to calculate mean

    def get_three_values(self,counter):
        print('checkpoint 3')
        aa = counter
        ab = counter + 1
        ac = counter + 2
        #mylist = []
        self.c.execute("SELECT gvalue FROM usaunemploymentavg WHERE id IN (?,?,?)", (aa ,ab, ac))
        mylist = self.c.fetchall()
        return mylist



    def do_mean_pass_mean_value_for_id(self,counter_id, mylist=[]):
        print("checkpoint 4")
        avg_num = np.mean(mylist)
        mean = np.around(avg_num, decimals=3)
        #print(mylist)
        print(counter_id)
        self.c.execute("UPDATE usaunemploymentavg SET threemonthavg = (?) WHERE id = (?)", (mean, counter_id))



    def populate_avg_column_for_three(self,value):
        print('checkpoint 1')
        count_till = self.counting_till(value)
        print(count_till)
        counter = 0
        while (count_till > counter): #823 == 823 loop will work
            counter = counter + 1
            xlist = self.get_three_values(counter)
            self.do_mean_pass_mean_value_for_id(counter, xlist)
        return print('Success')





