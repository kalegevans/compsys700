'''This project uses the wfdb library'''
import wfdb
record = wfdb.rdsamp('../mitdb/100', sampto=3000)
annotation = wfdb.rdann('../mitdb/sampledata/100', 'atr', sampto=3000)

wfdb.plotrec(record, annotation = annotation,
         title='Record 100 from MIT-BIH Arrhythmia Database',
         timeunits = 'seconds', figsize = (10,4), ecggrids = 'all')