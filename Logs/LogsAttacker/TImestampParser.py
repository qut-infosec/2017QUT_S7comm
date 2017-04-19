__author__ = 'Nicholas Rodofile'
import csv
import datetime
import re

log_filename = 'Attack_script_log_start.log'
#tags = ['Tank_Level', 'Tank_Off_SP_Int', 'Tank_On_SP_Int', 'Tank_Usage_Level']
directory = 'Attacks'
output_log = []

# Reactor_Log0_cut_HMI_Pipe_Solenoid_Off_SP_out.csv
# Reactor_Log0_cut_HMI_Pipe_Solenoid_On_SP_out.csv
# Reactor_Log0_cut_Pipe_Read_Pipeline_Pressure_out.csv
# Tank_Log0_cut_Tank_Level_out.csv
# Tank_Log0_cut_Tank_Off_SP_Int_out.csv
# Tank_Log0_cut_Tank_On_SP_Int_out.csv
# Tank_Log0_cut_Tank_Usage_Level_out.csv

timestamp = re.compile('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[.]\d{6}')
utc_format = "%Y-%m-%d %H:%M:%S.%f"
items = {
    "ChangeLowerThreshold": "3.4",
    "ChangeUpperThreshold": "3.3",
    "ChangeUpperThreshold_Flooding": "3.3 F",
    "ConveyorBeltGateChangeDirection": "1.3",
    "ConveyorBeltGateChangeDirection_Flooding": "1.3 F",
    "ConveyorBeltOff": "1.1",
    "ConveyorBeltOff_Flooding": "1.1 F",
    "ConveyorBeltOn": "1.2",
    "ConveyorBeltOn_Flooding": "1.2 F",
    "ConveyorBeltReset": "1.4",
    "EmergencyStop": "4.2",
    "GlobalReset": "4.1",
    "ReactorOff": "3.1",
    "ReactorOff_Flooding": "3.1 F",
    "ReactorOn": "3.1",
    "ReactorOn_Flooding": "3.1 F",
    "WaterTankOff": "2.1",
    "WaterTankOff_Flooding": "2.1 F",
    "WaterTankOnAuto": "2.2",
    "WaterTankOnAuto_Flooding": "2.2 F",
    "WaterTankOnManu": "2.3",
    "WaterTankOnManu_Flooding": "2.3 F",
}


first = datetime.datetime.strptime("15/12/2016 4:36:29 PM", "%d/%m/%Y %I:%M:%S %p")
print first
with open(log_filename, 'rb') as file:
    for row in file:
        row = row.strip('\n')
        attack_time = datetime.datetime.strptime(re.search(timestamp, row).group(0), utc_format)
        #print start_attack
        row_ = row.split()
        #print attack_time, row_[2]
        from_first = int((attack_time - first).total_seconds())
        output_log.append([from_first, items[row_[2]]]) #, row_[2]
        #items[row_[2]] = 0
        # row[1] = int((log_time - first).total_seconds())
        # row[2] = int(round(float(row[2]), -1))
        #
        # output_log[row[1]] = row[2]
        # print (log_time - first).total_seconds(), log_time, row[2]
#for row in output_log:
#    print row

with open(log_filename+"_out.csv", "wb") as f:
    writer = csv.writer(f)
    for l in output_log:
        print l
        writer.writerow(l)

# for i in sorted(items):
#     print "\"" + i + "\": \"\","