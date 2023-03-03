import os
import subprocess as sp
import sys
import time
import threading


def single_ue_flow(mcc, mnc, msin):
    sys.stdout.write('ENTER single_ue_flow %s %s %s \n' % (mcc, mnc, msin))
    os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-%s%s%s &' % (mcc, mnc, msin))
    time.sleep(10)
    # TODO: stream data
    os.system('/ueransim/nr-cli imsi-%s%s%s -e \"deregister switch-off\"' % (mcc, mnc, msin))
    sys.stdout.write('EXIT single_ue_flow %s %s %s \n' % (mcc, mnc, msin))


def main(args=None):
    single_ue_flow('208', '93', '000000000%d' % 1)
    single_ue_flow('208', '93', '000000000%d' % 2)
    single_ue_flow('208', '93', '000000000%d' % 3)

    single_ue_flow('208', '93', '000000000%d' % 4)
    single_ue_flow('208', '93', '000000000%d' % 5)
    single_ue_flow('208', '93', '000000000%d' % 6)

    single_ue_flow('208', '93', '000000000%d' % 7)
    single_ue_flow('208', '93', '000000000%d' % 8)
    single_ue_flow('208', '93', '000000000%d' % 9)
   
if __name__ == "__main__":
    main()
