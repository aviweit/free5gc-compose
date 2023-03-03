import os
import re
import subprocess as sp
import sys
import time
import threading


UERANSIM_DIR = '/home/weit/UERANSIM/'
NR_UE = 'build/nr-ue'
NR_CLI = 'build/nr-cli'

# relative path to proper configuration file
config_map = {
    'gnb0': {
        'slice0': 'config/ue-gnb1-slice0.yaml',
        'slice1': 'config/ue-gnb1-slice1.yaml'
    },
    'gnb1': {
        'slice0': 'config/ue-gnb2-slice0.yaml',
        'slice1': 'config/ue-gnb2-slice1.yaml'
    }
}


# Connection setup for PDU session[1] is successful, TUN interface[uesimtun0, 10.51.0.3] is up.
SUCCESS_RE = re.compile('.*is successful, TUN interface\[(\w+), (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\] is up\.')


def execute(cmd):
    print ("ENTER execute: %s" % cmd)
    popen = sp.Popen(cmd, stdout=sp.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        sys.stdout.write ('EXIT execute [%s]: %s\n' % (return_code, cmd))
        raise sp.CalledProcessError(return_code, cmd)
    sys.stdout.write ('EXIT execute [%s]: %s\n' % (return_code, cmd))


def single_ue_flow(mcc, mnc, msin):
    sys.stdout.write('ENTER single_ue_flow %s %s %s \n' % (mcc, mnc, msin))
    e = execute([UERANSIM_DIR + NR_UE, '-c', UERANSIM_DIR + config_map['gnb0']['slice0'],
                      '-i', 'imsi-%s%s%s' % (mcc, mnc, msin)])
    for l in e:
        matched = SUCCESS_RE.match(l)
        if (matched):
            sys.stdout.write('SUCCESSFUL UE: %s, UE ip %s\n' % (msin, matched.group(2)))
            break
    time.sleep(2)
    # TODO: stream data
    os.system(UERANSIM_DIR + NR_CLI + ' ' + 'imsi-%s%s%s -e \"deregister switch-off\"' % (mcc, mnc, msin))
    sys.stdout.write('EXIT single_ue_flow %s %s %s \n' % (mcc, mnc, msin))
    for l in e:
        # consume rest of stdout from e followed by process termination
        pass


def main(args=None):
    threads = []

    for i in [('208', '93', '0000000001')]:
        x = threading.Thread(target=single_ue_flow, args=i)
        threads.append(x)
        x.start()

    for index, x in enumerate(threads):
        x.join()
        print ("Main    : thread %d done" % index)

    #single_ue_flow('208', '93', '000000000%d' % 1)
    # single_ue_flow('208', '93', '000000000%d' % 2)
    # single_ue_flow('208', '93', '000000000%d' % 3)
    #
    # single_ue_flow('208', '93', '000000000%d' % 4)
    # single_ue_flow('208', '93', '000000000%d' % 5)
    # single_ue_flow('208', '93', '000000000%d' % 6)
    #
    # single_ue_flow('208', '93', '000000000%d' % 7)
    # single_ue_flow('208', '93', '000000000%d' % 8)
    # single_ue_flow('208', '93', '000000000%d' % 9)
   
if __name__ == "__main__":
    main()
