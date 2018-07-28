import numpy
import pandas as pd
import xlrd

class model:
    def __init__(self):

        self.survey_file = "surveydata.xlsx"
        self.survey_file_read = pd.read_excel(self.survey_file)
        self.survey_df = pd.DataFrame(self.survey_file_read)

        #Variables defined for storing and using survey information

        self.nbw=0      #No. of Bus Users in West Delhi
        self.nmw=0      #No. of Metro Users in West Delhi
        self.npw=0      #No. of Personal Convence Users in West Delhi
        self.ncw=0      #No. of Cabs Users in West Delhi
        self.nbe=0      #No. of Bus Users in East Delhi
        self.nme=0      #No. of Metro Users in East Delhi
        self.npe=0      #No. of Personal Convence Users in East Delhi
        self.nce=0      #No. of Cabs Users in East Delhi
        self.nbn=0      #No. of Bus Users in North Delhi
        self.nmn=0      #No. of Metro Users in North Delhi
        self.npn=0      #No. of Personal Convence Users in North Delhi
        self.ncn=0      #No. of Cabs Users in North Delhi
        self.nbs=0      #No. of Bus Users in South Delhi
        self.nms=0      #No. of Metro Users in South Delhi
        self.nps=0      #No. of Personal Convence Users in South Delhi
        self.ncs=0      #No. of Cabs Users in South Delhi

        self.nw=0       #No. of transpost users in West Delhi
        self.ne=0       #No. of transport Users in East Delhi
        self.ns=0       #No. of transport Users in North Delhi
        self.nn=0       #No. of transport Users in South Delhi

        self.pbw = 0    #Percentage of Bus Users in West Delhi
        self.pmw = 0    #Percentage of Metro Users in West Delhi
        self.ppw = 0    #Percentage of Personal Convence Users in West Delhi
        self.pcw = 0    #Percentage of Cab users in West Delhi

        self.pbe = 0    #Percentage of Bus Users in East Delhi
        self.pme = 0    #Percentage of Metro Users in East Delhi
        self.ppe = 0    #Percentage of Personal Convence Users in East Delhi
        self.pce = 0    #Percentage of Cab Users in East Delhi

        self.pbn = 0    #Percentage of Bus Users in North Delhi
        self.pmn = 0    #Percentage of Metro Users in North Delhi
        self.ppn = 0    #Percentage of Personal Convence Users in North Delhi
        self.pcn = 0    #Percentage of Cab Users in North Delhi

        self.pbs = 0    #Percentage of Bus Users in South Delhi
        self.pms = 0    #Percentage of Metro Users in South Delhi
        self.pps = 0    #Percentage of Personal Convence Users in South Delhi
        self.pcs = 0    #Percentage of Cab Users in South Delhi

    def evaluate(self):
        for i in range(0,17) :
            if self.survey_df.Preffered_Transport[i]=="Bus" and self.survey_df.Area[i]=="West Delhi" :
                self.nbw = self.nbw + 1
            elif self.survey_df.Preffered_Transport[i]=="Metro" and self.survey_df.Area[i]=="West Delhi" :
                self.nmw = self.nmw + 1
            elif self.survey_df.Preffered_Transport[i]=="Personal Convence" and self.survey_df.Area[i]=="West Delhi" :
                self.npw = self.npw + 1
            elif self.survey_df.Preffered_Transport[i]=="Cabs" and self.survey_df.Area[i]=="West Delhi" :
                self.ncw = self.ncw + 1
            elif self.survey_df.Preffered_Transport[i]=="Bus" and self.survey_df.Area[i]=="East Delhi" :
                self.nbe = self.nbe + 1
            elif self.survey_df.Preffered_Transport[i]=="Metro" and self.survey_df.Area[i]=="East Delhi" :
                self.nme = self.nme + 1
            elif self.survey_df.Preffered_Transport[i]=="Personal Convence" and self.survey_df.Area[i]=="East Delhi" :
                self.npe = self.npe + 1
            elif self.survey_df.Preffered_Transport[i]=="Cabs" and self.survey_df.Area[i]=="East Delhi" :
                self.nce = self.nce + 1
            elif self.survey_df.Preffered_Transport[i]=="Bus" and self.survey_df.Area[i]=="North Delhi" :
                self.nbn = self.nbn + 1
            elif self.survey_df.Preffered_Transport[i]=="Metro" and self.survey_df.Area[i]=="North Delhi" :
                self.nmn = self.nmn + 1
            elif self.survey_df.Preffered_Transport[i]=="Personal Convence" and self.survey_df.Area[i]=="North Delhi" :
                self.npn = self.npn + 1
            elif self.survey_df.Preffered_Transport[i]=="Cabs" and self.survey_df.Area[i]=="North Delhi" :
                self.ncn = self.ncn + 1
            elif self.survey_df.Preffered_Transport[i]=="Bus" and self.survey_df.Area[i]=="South Delhi" :
                self.nbs = self.nbs + 1
            elif self.survey_df.Preffered_Transport[i]=="Metro" and self.survey_df.Area[i]=="South Delhi" :
                self.nms = self.nms + 1
            elif self.survey_df.Preffered_Transport[i]=="Personal Convence" and self.survey_df.Area[i]=="South Delhi" :
                self.nps = self.nps + 1
            elif self.survey_df.Preffered_Transport[i]=="Cabs" and self.survey_df.Area[i]=="South Delhi" :
                self.ncs = self.ncs + 1
            if self.survey_df.Area[i]=="West Delhi":
                self.nw = self.nw + 1
            elif self.survey_df.Area[i]=="East Delhi":
                self.ne = self.ne + 1
            elif self.survey_df.Area[i]=="North Delhi":
                self.nn = self.nn + 1
            elif self.survey_df.Area[i]=="South Delhi":
                self.ns = self.ns + 1

    def greater(self,w,x,y,z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

        if self.w >= self.x and self.w >= self.y and self.w >= self.z :
            return self.w
        elif self.x >= self.w and self.x >= self.y and self.x >= self.z :
            return self.x
        elif self.y >= self.w and self.y >= self.x and self.y >= self.z :
            return self.y
        elif self.z >= self.w and self.z >= self.x and self.z >= self.y :
            return self.z

    def calculate(self):
        self.pbw = self.nbw/self.nw *100
        self.pmw = self.nmw/self.nw *100
        self.ppw = self.npw/self.nw *100
        self.pcw = self.ncw/self.nw *100

        self.pbe = self.nbe/self.ne *100
        self.pme = self.nme/self.ne *100
        self.ppe = self.npe/self.ne *100
        self.pce = self.nce/self.ne *100

        self.pbn = self.nbn/self.nn *100
        self.pmn = self.nmn/self.nn *100
        self.ppn = self.npn/self.nn *100
        self.pcn = self.ncn/self.nn *100

        self.pbs = self.nbs/self.ns *100
        self.pms = self.nms/self.ns *100
        self.pps = self.nps/self.ns *100
        self.pcs = self.ncs/self.ns *100

    def conclude(self,greater):
        print("\nCONCLUSION:\n")

        if self.pbw == greater(self.pbw,self.pmw,self.ppw,self.pcw):
            print("People in West Delhi prefer bus. So,bus service is to be improved in West Delhi\n")
        elif self.pmw == greater(self.pbw,self.pmw,self.ppw,self.pcw):
            print("People in West Delhi prefer metro. So,metro service is to be improved in West Delhi\n")    
        elif self.ppw == greater(self.pbw,self.pmw,self.ppw,self.pcw):
            print("People in West Delhi prefer Personal Convence. So, traffic control measures are to be taken in West Delhi.\n")
        elif self.pcw == greater(self.pbw,self.pmw,self.ppw,self.pcw):
            print("People in West Delhi prefer cabs. So,Traffic Control service is to be improved in West Delhi\n")

        if self.pbe == greater(self.pbe,self.pme,self.ppe,self.pce):
            print("People in East Delhi prefer bus. So,bus service is to be improved in East Delhi\n")
        elif self.pme == greater(self.pbe,self.pme,self.ppe,self.pce):
            print("People in East Delhi prefer metro. So,metro service is to be improved in East Delhi\n")    
        elif self.ppe == greater(self.pbe,self.pme,self.ppe,self.pce):
            print("People in East Delhi prefer Personal Convence. So, traffic control measures are to be taken in East Delhi.\n")
        elif self.pce == greater(self.pbe,self.pme,self.ppe,self.pce):
            print("People in East Delhi prefer cabs. So,Traffic Control service is to be improved in East Delhi\n")    

        if self.pbn == greater(self.pbn,self.pmn,self.ppn,self.pcn):
            print("People in North Delhi prefer bus. So,bus service is to be improved in North Delhi\n")
        elif self.pmn == greater(self.pbn,self.pmn,self.ppn,self.pcn):
            print("People in North Delhi prefer metro. So,metro service is to be improved in North Delhi\n")    
        elif self.ppn == greater(self.pbn,self.pmn,self.ppn,self.pcn):
            print("People in North Delhi prefer Personal Convence. So, traffic control measures are to be taken in North Delhi.\n")
        elif self.pcn == greater(self.pbn,self.pmn,self.ppn,self.pcn):
            print("People in North Delhi prefer cabs. So,Traffic Control service is to be improved in North Delhi\n")

        if self.pbs == greater(self.pbs,self.pms,self.pps,self.pcs):
            print("People in South Delhi prefer bus. So,bus service is to be improved in South Delhi\n")
        elif self.pms == greater(self.pbs,self.pms,self.pps,self.pcs):
            print("People in South Delhi prefer metro. So,metro service is to be improved in South Delhi\n")    
        elif self.pps == greater(self.pbs,self.pms,self.pps,self.pcs):
            print("People in South Delhi prefer Personal Convence. So, traffic control measures are to be taken in South Delhi.\n")
        elif self.pcs == greater(self.pbs,self.pms,self.pps,self.pcs):
            print("People in South Delhi prefer cabs. So,Traffic Control service is to be improved in South Delhi\n")    

    def display(self):
        print("\nPERCENTAGE STATISTICS:\n")
        print("Percentage of Bus Users in West Delhi : " , self.pbw)
        print("Percentage of Metro Users in West Delhi : " , self.pmw)
        print("Percentage of Personal Convence Users in West Delhi : " , self.ppw)
        print("Percentage of Cab Users in West Delhi : " , self.pcw)
        print("Percentage of Bus Users in East Delhi :" , self.pbe)
        print("Percentage of Metro Users in East Delhi :" , self.pme)
        print("Percentage of Personal Convence Users in East Delhi :" , self.ppe)
        print("Percentage of Cab Users in East Delhi :" , self.pce)
        print("Percentage of Bus Users in North Delhi :" , self.pbn)
        print("Percentage of Metro Users in North Delhi :" , self.pmn)
        print("Percentage of Persoal Convence Users in North Delhi :" , self.ppn)
        print("Percentage of Cab Users in North Delhi :" , self.pcn)
        print("Percentage of Bus Users in South Delhi :" , self.pbs)
        print("Percentage of Metro Users in South Delhi :" , self.pms)
        print("Percentage of Personal Convence Users in South Delhi :" , self.pps)
        print("Percentage of Cab Users in South Delhi :" , self.pcs)

model = model()
model.evaluate()
model.calculate()
model.display()
model.conclude(model.greater)
            
