__author__ = 'Nicholas Rodofile'
import csv
import datetime
csv_filename = 'Tank_Log0_cut'
tags = ['Tank_Level', 'Tank_Off_SP_Int', 'Tank_On_SP_Int', 'Tank_Usage_Level']
directory = 'Attacks'
output_log = {}

# Reactor_Log0_cut_HMI_Pipe_Solenoid_Off_SP_out.csv
# Reactor_Log0_cut_HMI_Pipe_Solenoid_On_SP_out.csv
# Reactor_Log0_cut_Pipe_Read_Pipeline_Pressure_out.csv
# Tank_Log0_cut_Tank_Level_out.csv
# Tank_Log0_cut_Tank_Off_SP_Int_out.csv
# Tank_Log0_cut_Tank_On_SP_Int_out.csv
# Tank_Log0_cut_Tank_Usage_Level_out.csv

def make_csv(tag):
    first = None
    with open(directory + "/" + csv_filename+'.csv', 'rb') as csvfile:
        logreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in logreader:
            #print row
            if row[0] == tag:
                log_time = datetime.datetime.strptime(row[1], "%d/%m/%Y %I:%M:%S %p")
                if first is None:
                    first = log_time
                    print first.strftime("%d/%m/%Y %I:%M:%S %p")
                row[1] = int((log_time - first).total_seconds())
                row[2] = int(round(float(row[2]), -1))

                output_log[row[1]] = row[2]
                print (log_time - first).total_seconds(), log_time, row[2]
    #for row in output_log:
    #    print row

    with open(directory + "/" + csv_filename+"_"+tag+'_out.csv', "wb") as f:
       writer = csv.writer(f)
       for l in sorted(output_log):
           writer.writerow([str(l) + " " + str(output_log[l])])

if __name__ == '__main__':
    for t in tags:
        make_csv(t)