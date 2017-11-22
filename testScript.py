import getHPCCfile
import getECLquery

print(getECLquery.get_a_script_result('test.ecl', '10.53.57.31:8010', 'C:/z/odin/HPCC'))
print(getHPCCfile.get_a_file('proagrica::entities::2::productcategory', 'http://10.53.57.31:8010', CSVlogicalFile = False))
