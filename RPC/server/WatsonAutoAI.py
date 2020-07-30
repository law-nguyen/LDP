import urllib3, requests, json

class learningDisabilityPredictor():
    def getValue(self):
        iam_token = "eyJraWQiOiIyMDIwMDcyNDE4MzEiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLThkOTJlYjIwLTY0NTMtNDcyYy04NzM1LTEyZjg2MDcyNzE0ZSIsImlkIjoiaWFtLVNlcnZpY2VJZC04ZDkyZWIyMC02NDUzLTQ3MmMtODczNS0xMmY4NjA3MjcxNGUiLCJyZWFsbWlkIjoiaWFtIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC04ZDkyZWIyMC02NDUzLTQ3MmMtODczNS0xMmY4NjA3MjcxNGUiLCJuYW1lIjoid2RwLXdyaXRlciIsInN1YiI6IlNlcnZpY2VJZC04ZDkyZWIyMC02NDUzLTQ3MmMtODczNS0xMmY4NjA3MjcxNGUiLCJzdWJfdHlwZSI6IlNlcnZpY2VJZCIsImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImU1NDU2MjU2NGZhNjRjYzBiZDBkYzU4YjJkNjMyZjMwIn0sImlhdCI6MTU5NjA2OTUxOCwiZXhwIjoxNTk2MDczMTE4LCJpc3MiOiJodHRwczovL2lhbS5ibHVlbWl4Lm5ldC9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOmFwaWtleSIsInNjb3BlIjoiaWJtIG9wZW5pZCIsImNsaWVudF9pZCI6ImRlZmF1bHQiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.aL3BW_laP_b64y3tEudyaZLb_6n1bj2jOziLmHjP45-ifzcxXGx6L7o0Z_CT2usscxALE1xto8mweYw_EjpCkPcyzA8BhlfMQp8FyQGsA2cGkMdHHqFSriw_ZNGNU3ybakJrBeuD4ov7bzLeMA1OTmvkZEgVimCz2YER0FAFOglg98RKhgskWzt43RZMmmNtID4p58vmXo-hhja5E4XyY93P0rOfubJhvorGLxe7dxvMW1rHM4ORWBgoUYxXU-DjyJtFwNsurLzzEKQha7onAgxhEXDntQhnnw0qmDB6tfjulMyfiHYTLIAtTmvCDQoNb__a0nItt04ueGVXPmYFYg"

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': "6873f0f0-6a9e-492f-a50e-54f85695d1bd"}

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


            # TEST CASE   --- EXPECTED VALUE : 1.0
    #    "values": [[60023,1,32, None, None,16, None, None, None,1, None, None, None, None, None, None, None,
    #    None,1,1, None,0,0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    #    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,0,None,1, None, None,
    #    None, None, None, None, None, None, None, None,1, None, None, None, None, None, None, None, None, None, None, None, None, None,0, 
    #    None,1,0,0,1, None, None, None, None, None, None, None, None, None, None, None, None,1, None,1, None, None,
    #    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
    #    None,1,0,1,0,1,6,1,0,1, None, None, None, None, None, None, None, None, None, None, None, None,
    #    None, None, None, None, None, None, None, None, None, None, None, None, None, None]]}]}

        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/65d80087-2070-4024-bb94-9d463a9d6275/predictions', json=payload_scoring, headers=header)

        # Type of dict:  <class 'dict'>
        dict = json.loads(response_scoring.text)   
        
        # Values of dict
        dict_val = dict.values()       

        # Convert dict_val to list
        dict_list = list(dict_val)
        
        # Convert dict_list[0] to the list
        list_list = list(dict_list[0])
      
        # Convert the values of list_list[0] to the list
        value_list = list(list_list[0].values())

        val_list = value_list[1]
        val = val_list[0]
     
        # FINAL VALUE TO RETURN
        final_value = val[0]    # Type : <class 'float'> 
       
        return final_value

def main():
    ldp = learningDisabilityPredictor()
    print(ldp.getValue())

if __name__ == "__main__":
  main()
