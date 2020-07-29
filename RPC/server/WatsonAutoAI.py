import urllib3, requests, json

iam_token = "eyJraWQiOiIyMDIwMDcyNDE4MzEiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLTZjYjQ2ZTI5LTFjMjEtNGVhYy1hNzYyLTNkZmE4YmY0NTJjZSIsImlkIjoiaWFtLVNlcnZpY2VJZC02Y2I0NmUyOS0xYzIxLTRlYWMtYTc2Mi0zZGZhOGJmNDUyY2UiLCJyZWFsbWlkIjoiaWFtIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC02Y2I0NmUyOS0xYzIxLTRlYWMtYTc2Mi0zZGZhOGJmNDUyY2UiLCJuYW1lIjoid2RwLXdyaXRlciIsInN1YiI6IlNlcnZpY2VJZC02Y2I0NmUyOS0xYzIxLTRlYWMtYTc2Mi0zZGZhOGJmNDUyY2UiLCJzdWJfdHlwZSI6IlNlcnZpY2VJZCIsImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImI3YTFiOWYxOTZjODRlODRhZjIzYjk3MjIzOWY4NTUzIn0sImlhdCI6MTU5NTk2Mjg1OCwiZXhwIjoxNTk1OTY2NDU4LCJpc3MiOiJodHRwczovL2lhbS5ibHVlbWl4Lm5ldC9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.NsLKt_Za_HJ83HAqrhH0O0ir7dhApeeU-2yeZU4qZQk-oUEblsbnbXkv8Batzab2TnxzCEc-GDRRuf9jX7ay5Bo2IhFxemeyC9GEWs3nIu09Zf89X1CiBF449klIDEgZ69wr01sulgsUgfhYSjIBLV5mAlpr6_icUFLxKkPfpgqwOvq3kDt_X_RmthAOiK5NupybhHKZQRksXV3fQx71Btk2kEYy-vug1M-c5ZD4XPqV_NI1mDXRisOMKCI7XtBgBlpin425l8vxSRmraW9Qis_ej0L4NbTikgQ1-bBH0fEn-ACgYDmAnU_HS3Fm1PmcFiqnylJjJPtqWYzBLapZfg"

# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': "9e32887b-dfb2-4b9b-83c3-961b50a6dd9c"}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["IDNUMR", "SAMPLE", "STATE", "MSA_STAT", "TOTKIDS4", "AGEYR_CHILD", "FLG_18_MNTH", 
"FLG_06_MNTH", "AGEPOS4", "SEX", "RELATION", "PLANGUAGE", "K2Q01", "K2Q01_D", "BMICLASS", "K2Q04R", "BWGHT_FLG", "K2Q05", "K2Q10", "K2Q13", 
"K2Q16", "K2Q19", "K2Q22", "CSHCN", "K2Q30A", "K2Q32A", "K2Q33A", "K2Q34A", "K2Q35A", "K2Q36A", "K2Q60A", "K2Q61A", "K2Q37A", "K2Q38A", "K2Q40A",
 "K2Q41A", "K2Q42A", "K2Q43A", "K2Q44A", "K2Q45A", "K2Q46A", "K3Q01", "K3Q02", "K3Q03", "K3Q20", "K3Q22", "K3Q21A", "K3Q21B", "K3Q25", "C4Q04", 
 "K4Q01", "K4Q02", "K4Q04", "S4Q01", "K4Q20R", "K4Q30", "K4Q21R", "K4Q39", "K4Q22", "K4Q23", "K4Q24", "K4Q25", "K4Q31", "K4Q32X01", "K4Q32X02", 
 "K4Q32X03", "K4Q32X04", "K4Q32X05", "K4Q32X06", "K4Q32X07", "K4Q27", "K5Q10", "NUMB_SERVICES", "K5Q20", "K5Q21", "K5Q30", "K5Q31", "K5Q40", "K5Q41",
  "K5Q42", "K5Q43", "K5Q44", "K7Q01", "K7Q02R", "K7Q04R", "K7Q05R", "MULT_REPEATS", "K7Q11", "K7Q30", "K7Q31", "K7Q32", "K7Q33", "K7Q34", "K7Q37", 
  "K7Q38", "K7Q40", "K7Q41", "K7Q50", "K7Q50A", "K7Q60", "K7Q60A", "K7Q91", "K7Q91A", "K7Q61", "K7Q61A", "K7Q62", "K7Q70", "K7Q71", "K7Q79", "K7Q84",
   "K7Q85", "K7Q86", "K7Q82", "K7Q83", "K8Q12R", "K8Q11", "K8Q21", "K8Q30", "K8Q31", "K8Q32", "K8Q34", "K8Q35", "TOTADULT3", "K9Q16R", "C10Q14R", 
   "FAM_MAR_COHAB", "K9Q18", "K9Q20", "K9Q21", "K9Q23", "K9Q24", "K9Q40", "ACE1", "ACE3", "ACE4", "ACE5", "ACE6", "ACE7", "ACE8", "ACE9", "ACE10",
    "K9Q96", "K10Q11", "K10Q12", "K10Q13", "K10Q14", "K10Q20", "K10Q22", "K10Q23", "K10Q30", "K10Q31", "K10Q32", "K10Q34", "K10Q40", "K10Q41",
     "HISPANIC", "RACER", "EDUC_MOMR", "EDUC_DADR", "EDUC_PARR", "HOUSE_GEN", "K11Q43R", "K11Q50", "C10Q41", "POVERTY_LEVELR", "OTH_LANG", "SUMMER",
      "NSCHWT"], 
      
      "values": [["IDNUMR","SAMPLE","STATE", None, None,"AGEYR_CHILD", None, None, None,"SEX", None, None, None, None, None, None, None,
       None,"K2Q10","K2Q13", None,"K2Q19","K2Q22", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,"K4Q22","K4Q23","K4Q24", "K4Q25", None,
         None, None, None, None, None, None, None, None,"K5Q10", None, None, None, None, None, None, None, None, None, None, None, None, None,"K7Q05R", 
         None,"K7Q11","K7Q30","K7Q31","K7Q32", None, None, None, None, None, None, None, None, None, None, None, None,"K7Q61", None,"K7Q62", None, None,
          None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
          None,"ACE3","ACE4","ACE5","ACE6","ACE7","ACE8","ACE9","ACE10","K9Q96", None, None, None, None, None, None, None, None, None, None, None, None,
           None, None, None, None, None, None, None, None, None, None, None, None, None, None]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/10683113-568f-4a56-aa39-5e65001f8836/predictions', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))