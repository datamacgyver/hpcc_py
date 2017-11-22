# THORpyDownloader
Scirpt to download HPCC files and script results. Just a quick hack my end so go easy on the quality. 

Tested and working on HPCC v6.4.2 and python 3.5.2.

call getHPCCfile.get_a_file(inFileName, hpcc_addr, CSVlogicalFile = False) to access a logical files

call getECLquery.get_a_script_result(scriptLoc, hpcc_addr) to run a query and access the results

Note that while retrieving a file is a multithread process, running a script and getting the results is not. Therefore if your file is quite big you may be better off saving the results of a script call then downloading the file. 


Note that there is a dependency for client tools to run ECL scripts. This must be in your system path. 


Tested and working on Windows 10, will make linux-able in the future (if it isn't already) 