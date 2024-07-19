import pandas as pd

class historyList:
    def __init__(self):
        self.list = []
        self.df_h = pd.DataFrame( columns=['time', 'ao5', 'ao12'])

    def append(self,time):
        self.list.append(time)
    def clr(self):
        self.list=[]
        self.df_h = pd.DataFrame( columns=['time', 'ao5', 'ao12'])

    def len(self): return len(self.list)

    def best(self,num):
        lsBest= self.df_h.min().values
        return lsBest[num]
    def recentList(self,num):
        return self.list[-num:]
    def recentListSorted(self,num):
        return sorted(self.list[-num:])

    def ao(self,num):
        if self.len() < num: 
            return float('nan')
        else: 
            ls=self.recentListSorted(num)
            return sum(ls[1:-1])/(num-2)
        
    def updateDf(self):
        newRow=pd.Series([self.list[-1],self.ao(5),self.ao(12)],index=self.df_h.columns) 
        self.df_h=self.df_h.append(newRow,ignore_index=True)


