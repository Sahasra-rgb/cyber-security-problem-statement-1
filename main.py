import os
from datetime import datetime
from config import *
from utils import virustotal_api
from StaticMalwareAnalysis import StaticMalwareAnalysis

if StaticMalwareAnalysis.check_malware_sample_exists():
    list_file = os.listdir(config['malware-sample-folder'])
    for i in list_file:
        print(f"Starting analysis of {i} at {str(datetime.now())}")
        s = StaticMalwareAnalysis(os.path.join(config['malware-sample-folder'],i))
        file_name = s.create_directory()
        print(f"Directory Created : {file_name}")
        hash_value = s.get_sha256sum()
        print(f"SHA 256 HASH : {hash_value}")
        s.extract_strings()
        s.extractPEINFO()
        print(f"PE INFO Extracted")
        s.move_malware()
        print("Malware sample moved to saved analysis folder")
        results = virustotal_api(hash_value)
        s.set_virustotal_results(results)
        s.create_pdf()
        print("PDF/HTML Created")
