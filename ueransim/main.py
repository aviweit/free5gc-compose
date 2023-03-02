import argparse

import os
import subprocess as sp


def main(args):
    if args["mode"] == 'create':
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000001 &')
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000002 &')
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000003 &')
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000004 &')
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000005 &')
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000006 &')
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000007 &')
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000008 &')
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000009 &')
        os.system('/ueransim/nr-ue -c /ueransim/config/uecfg.yaml -i imsi-208930000000010 &')

    if args["mode"] == "terminate":
        os.system('/ueransim/nr-cli imsi-208930000000001 -e \"deregister switch-off\"')
        os.system('/ueransim/nr-cli imsi-208930000000002 -e \"deregister switch-off\"')
        os.system('/ueransim/nr-cli imsi-208930000000003 -e \"deregister switch-off\"')
        os.system('/ueransim/nr-cli imsi-208930000000004 -e \"deregister switch-off\"')
        os.system('/ueransim/nr-cli imsi-208930000000005 -e \"deregister switch-off\"')
        os.system('/ueransim/nr-cli imsi-208930000000006 -e \"deregister switch-off\"')
        os.system('/ueransim/nr-cli imsi-208930000000007 -e \"deregister switch-off\"')
        os.system('/ueransim/nr-cli imsi-208930000000008 -e \"deregister switch-off\"')
        os.system('/ueransim/nr-cli imsi-208930000000009 -e \"deregister switch-off\"')
        os.system('/ueransim/nr-cli imsi-208930000000010 -e \"deregister switch-off\"')
    else:
        raise Exception("Illegal 'mode' %s" % args["mode"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-m','--mode', help='select mode (create/terminate)', required=True)
    args = vars(parser.parse_args())
    main(args)
