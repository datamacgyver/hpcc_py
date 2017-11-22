import subprocess
import xml.etree.ElementTree as ET
import pandas as pd

POOL_SIZE = 15
GET_FILE_URL = """WsWorkunits/WUResult.json?LogicalName=%s&Cluster=thor&Start=%s&Count=%s"""
USELESS_COLS = ['updateddatetime', '__fileposition__', 'createddatetime']


def run_command(cmd):
    """
    given shell command, returns stdout and stderr
    
    Parameters
    ----------
    cmd: str
        the ECL command to run

    Returns
    -------
    result: str
        xml string of the response
    """
    return subprocess.Popen(cmd
                            , stdout=subprocess.PIPE
                            , stderr=subprocess.PIPE
                            , stdin=subprocess.PIPE
                            , shell=True).communicate()


def parse_response_XML(answer):
    """
    This is the only command needed to run and return a script. Do note that this is not threaded so slower
    than getting a file.

    Parameters
    ----------
    answer: str
        the returned XML of the query

    Returns
    -------
    result: pd.DataFrame
        a DF of the given query
    """

    answer = str(answer).strip()
    if "\\r\\n" in answer:
        answer = answer.split("\\r\\n")
    else:
        answer = answer.split("\\n")

    print("Parsing Results from XML")
    vls = []
    lvls = []

    for line in answer:
        if line.find('<Row>') != -1:
            lvls = []
            newvls = []
            etree = ET.fromstring(line)

            for child in etree:
                if child.tag not in lvls:
                    lvls.append(child.tag)
                newvls.append(child.text)
            vls.append(newvls)

    return pd.DataFrame(vls, columns=lvls)


def get_a_script_result(scriptLoc, hpcc_addr, hpcc_repo = ''):
    """
    main function to run an ECL script
    
    Parameters
    ----------
    scriptLoc: str
        Location of the script to run
    hpcc_addr:
        address of the HPCC cluster
    hpcc_repo:
        location of any needed ECL repository

    Returns
    -------
    result: pd.DataFrame
        dataframe of the given query response
    """
    
    if hpcc_repo != '':
        hpcc_repo = ' -I ' + hpcc_repo
    
    print('running ECL script')
    res = run_command('ecl run --server ' + hpcc_addr +
                      ' --port 8010 --username DS_extractinator --password " " thor ' + scriptLoc +
                      hpcc_repo
                      )
    print('Parsing Response')
    return parse_response_XML(res)



