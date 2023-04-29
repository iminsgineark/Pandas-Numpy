# import os
# import requests
# import  json
# import  pickle
# from collections import defaultdict
# import pandas as  pd
# import numpy as np
# def get_user_Data(status = "NR"):
#     url = "http://localhost:8000/user_submission"
#     try:
#         result = requests.get(url)
#         if result.status_code == 200:
#             result = json.loads(result.text)
#             d1 = pd.DataFrame(result,columns=["label","face_encoding"])
#             d2 = pd.DataFrame(d1.pop("face_encoding").values.tolist(),index=d1.index).rename(columns=lambda  x: "fe_{}".format(x + 1))
#             df = d1.join(d2)
#             return df
#       except Exception as e:
#       return None
