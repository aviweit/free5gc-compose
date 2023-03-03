import argparse

import os
import subprocess as sp
import time
import threading


def single_ue_flow(mcc, mnc, msin):
    x = threading.Thread(target=os.system, args=('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-%s%s%s' % (mcc, mnc, msin), ))
    x.start()
    time.sleep(2)
    # TODO: stream data
    sp.getoutput('/ueransim/nr-cli imsi-%s%s%s -e \"deregister switch-off\"' % (mcc, mnc, msin))
    x.join()


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
   
    #
    # threads = list()
    # for i in [1 , 2]: #, 3, 4, 5, 6, 7, 8, 9]:
    #     x = threading.Thread(target=single_ue_flow, args=('208', '93', '000000000%d' % i, ))
    #     threads.append(x)
    #     x.start()
    #
    # for index, x in enumerate(threads):
    #     x.join()
    #     print ("Main    : thread %d done", index)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Description of your program')
    # parser.add_argument('-m','--mode', help='select mode (create/terminate)', required=True)
    # args = vars(parser.parse_args())
    main()
