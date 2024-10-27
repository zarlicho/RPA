# import requests
# import os
# headers = {
#     'Accept': 'application/json',
#     'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
#     'Access-Control-Allow-Origin': '*',
#     'Authorization': 'Bearer eQJbhHV7pcZXO2ed3Mz7SSgAFWAHYxS1',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/json',
#     'Obpp-Token': 'NlmIrgnosPXkYhMU5CwpTwTK6MYy64IuENxxLEkbUXOelcIE0Ve0ni/n9udXg2uHjd7RjwOyWdjS4JeUf6LIv+UAbAil2Df+RKaIhKAw0pdkl4oMgJJ8Oy4nKEt5pBFbI9m4',
#     'Origin': 'https://obs-prd-ext-hcc.optum.com',
#     'Referer': 'https://obs-prd-ext-hcc.optum.com/',
#     'Request-Token': '',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
#     'X-B3-SpanId': 'b8403483ae7a66d4',
#     'X-B3-TraceId': '664af7c6d589c05eb8403483ae7a66d4',
#     'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# json_data = {
#     'customerId': '',
#     'customerName': '',
#     'customerPolicyNumber': '',
# }

# response = requests.post(
#     'https://obs-prd-ext-hcc-elr.optum.com/obppcustomersearch/api/customersearch/search/internal',
#     headers=headers,
#     json=json_data,
# )

# for x in response.json():
#     print(x["customerId"])

# import requests

# headers = {
#     'Accept': 'application/json',
#     'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
#     'Access-Control-Allow-Origin': '*',
#     'Authorization': 'Bearer k2knTtBsCLbt1mZJb3Mz4ynHCqQTCVsI',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/json',
#     'Obpp-Token': 'BIgjI/AOEK4U10UW5nXa8SWpP0MDkFjHdsdrme7kAiLrxvkYqj0zo6cxTM2qMzqaVqaQHmIEMeehRxzYpqeSbWuu4M92zlhT6efMPI7nH0DMd+7MfiBi7ijcHQ//Z2EqLEJg',
#     'Origin': 'https://obs-prd-ext-hcc.optum.com',
#     'Referer': 'https://obs-prd-ext-hcc.optum.com/',
#     'Request-Token': 'C1AGCgYdBgcVJhYUFVBVRj8iKipSXk0UHBMbAh8AAi0UUFVGICAmKTVQQ0YDAAwnBQEbCx0XHS0UUFVGQEM+VEhEW0YN',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
#     'X-B3-SpanId': 'ee4a1cbe33a1db13',
#     'X-B3-TraceId': '664b386e7736c8c5ee4a1cbe33a1db13',
#     'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# json_data = {
#     'invoiceType': 'OPEN',
#     'platformId': 'PRIME',
#     'srcCustomerId': '01Q0864',
# }

# response = requests.post(
#     'https://obs-prd-ext-hcc-ctc.optum.com/obppinvoicelisting/api/invoice/getopeninvoicelist',
#     headers=headers,
#     json=json_data,
# )
# for x in response.json()["openInvoiceListing"]:
#     print(x["invoiceNumber"])

# import requests

# headers = {
#     'Accept': 'application/json',
#     'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
#     'Access-Control-Allow-Origin': '*',
#     'Authorization': 'Bearer eQJbhHV7pcZXO2ed3Mz7SSgAFWAHYxS1',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/json',
#     'Obpp-Token': 'NlmIrgnosPXkYhMU5CwpTwTK6MYy64IuENxxLEkbUXOelcIE0Ve0ni/n9udXg2uHjd7RjwOyWdjS4JeUf6LIv+UAbAil2Df+RKaIhKAw0pdkl4oMgJJ8Oy4nKEt5pBFbI9m4',
#     'Origin': 'https://obs-prd-ext-hcc.optum.com',
#     'Referer': 'https://obs-prd-ext-hcc.optum.com/',
#     'Request-Token': '',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
#     'X-B3-SpanId': 'b8403483ae7a66d4',
#     'X-B3-TraceId': '664af7c6d589c05eb8403483ae7a66d4',
#     'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# json_data = {
#     'lineItemTypeCode': '',
#     'benefitGroupId': '',
#     'cprocInvcId': '',
#     'invoiceStatementNumber': '706711433580',
#     'populationId': '',
#     'benefitStatusId': '',
#     'planNumber': '',
#     'policyName': '',
#     'policyNumber': '',
#     'presentmentType': '',
#     'sequenceNumber': '',
#     'srcSystemCode': '110',
#     'tierCode': '',
#     'customerNumber': '1192189566',
#     'customerName': 'KAIROS WATER',
# }

# response = requests.post(
#     'https://obs-prd-ext-hcc-elr.optum.com/obppeligibilityinvoicedetail/api/eligibility/invoice/brms/getdetails/getcsv',
#     headers=headers,
#     json=json_data,
# )
# if response.status_code == 200:
#     save_dir = "document"
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)
#     file_path = os.path.join(save_dir, "test.csv")
#     with open(file_path, "wb") as file:
#         file.write(response.content)
#     print(f"file success to download '{file_path}'")
# else:
#     print(f"failed to download file: {response.status_code} "+"\n"+response.content)

# print(response.content)

import requests

cookies = {
    'akym-d': '5c5AnvFeAHjddzJnAf0gdC',
    'pixel-ubrid': 'v2.0-d5bfcf0457751f9a7f4f429b81bc7c59-1331-1335-1714851208661-0000320888-1716001183414',
    'at_check': 'true',
    'AMCVS_8E391C8B533058250A490D4D%40AdobeOrg': '1',
    's_cc': 'true',
    'oidp': 'AV48Esw-oJOGl5y401zfOjUjaIfbNhoyB0H3SimvyNoRxJW8ExnpciU97wRcNQ==',
    'AMCV_8E391C8B533058250A490D4D%40AdobeOrg': '179643557%7CMCIDTS%7C19866%7CMCMID%7C66632545426636050712743998251708691240%7CMCAAMLH-1716955500%7C3%7CMCAAMB-1716955500%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1716357900s%7CNONE%7CvVersion%7C5.5.0',
    'mbox': 'PC#c64c19de6f92411582b893f981fee1e5.38_0#1779602739|session#9316ada3b6494e7aadf6ca8bd67c6973#1716359799',
    's_gpv_pagename': 'optum%3AOne%20Healthcare%20ID%3Apublic%3Alogin%3Alogin',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'akym-ecid': '66632545426636050712743998251708691240',
    'akym-page-name': 'login',
    'akym-s': '3251f44649de7d2b5fdfd95d13a90f8a54f758a02d2e84a573fd52510d3f0fbc0762efcc349c30ba8f02e5a177e0aac9ac23dd070c93c95a6fe3f24b1fcf2502299a210c76b25211857b6899eaa13a51d35e360a8fc979ad82afd3409b87aa56313f82909b5f01f305394f73bf3d92ddeeab439ed8d54ec6b225859a278aabf03c28fdcdcb6228f710d4bbf9e2b189fd5314149dc3e6ec953683d365e392ee423e721fa96683a8d62f8f0813d790a039e03a11f6235f9e0a6ee7119e861982f884ee1fecd74afade5ecd1d90cca03a24',
    'akym-t': '58sjgS7Q6VWbboLUx2cd5Oo2fQmmgEQaQ2r2zw6gM1o=',
    'akym-ubrid': 'v2.0-d5bfcf0457751f9a7f4f429b81bc7c59-1331-1335-1714851208661-0000320888-1716001183414',
    'akym-ui-path': '/oneapp/index.html#/login',
    'content-type': 'application/json',
    # 'cookie': 'akym-d=5c5AnvFeAHjddzJnAf0gdC; pixel-ubrid=v2.0-d5bfcf0457751f9a7f4f429b81bc7c59-1331-1335-1714851208661-0000320888-1716001183414; at_check=true; AMCVS_8E391C8B533058250A490D4D%40AdobeOrg=1; s_cc=true; oidp=AV48Esw-oJOGl5y401zfOjUjaIfbNhoyB0H3SimvyNoRxJW8ExnpciU97wRcNQ==; AMCV_8E391C8B533058250A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C19866%7CMCMID%7C66632545426636050712743998251708691240%7CMCAAMLH-1716955500%7C3%7CMCAAMB-1716955500%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1716357900s%7CNONE%7CvVersion%7C5.5.0; mbox=PC#c64c19de6f92411582b893f981fee1e5.38_0#1779602739|session#9316ada3b6494e7aadf6ca8bd67c6973#1716359799; s_gpv_pagename=optum%3AOne%20Healthcare%20ID%3Apublic%3Alogin%3Alogin',
    'origin': 'https://identity.onehealthcareid.com',
    'priority': 'u=1, i',
    'referer': 'https://identity.onehealthcareid.com/oneapp/index.html',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'wu44b0puoj-a': 'GNMjhz3KIbGNlQG3kcf12jR41oqDdeEirnp0XtYdWsAsGTeNbdHTYhYDX2lq_Kj0r7Mb6F-JOR0ZoBjGagdczWNqf7tD1HAjJtjMln8xf58JURo1uymod76Z1JEZ4WTEw=lY5LHdwneGCp9z8JhDNw3dBN1kMeygiZn28xwm9-X-4Dxf1=vu4exk-c8pDlwcQJPIBd16_fFG=5IvumMC75qYe2RKWHcMr0YG2kWN8or_9Pr2TA5QB8Kvbm49Kjg7Ajjc=GqW0lm42LvPdN97YItPyfNR460Psu16m5fpT2AE5GvpJ4jw_GPJKl51h_DxDxxPjyH1Fyl4aMwkIvyf0TL1-u61HG7zbDD0rpEkBvCMPge9jxorJsn3ZZi6VuVyJsus1al_Rk7mk1Ns6Ve0pLlIQbBgb5a57PZwXDEr2riMw3yVWBdJIKeAVdd5YVmNqOeZW9HNk=snhuB_MMvT=0WDLgcKLCfvFoQ7LDIP_WXe02vBpjNgFKIyYe8_VUXC=0r3rU2e6XPh9msR8EExcQqu-UD5DRtwEynO0s5X=Ij1u-gQsbl0JyiP-cjJ44mnjVvx7eN_wtd6n_dQlo7Cli6YGJrX5A=IzDNcNPeCT_F9uxqoHY1OYbZO5cvgVBAGAGO0Yg0HD1NttWAza1tXOdn=JWPw3acCi_XamX4MpuoDh-dHDszQ_DKsfVlP1uLGB-_iER3Al8OYGiXOU-AuT3yvxOB0nw=9mFbaxtL25IzfYMkc0QhCeNUqcd7_vFv3Uq9qERyGAyetzu9ivqB5Eqm-pWyNpCNgn39MJRZ3kHnK=Nz1BVdTYPCqOMRyUxE6TEPoG-pYjmU5-vuumBKoHzTN=upEv-WpQjMMKBmyv10a2XRM8eFVXoud1T9E328osT5PiJMjuhUayQ5e3yrpr_7lIoZal09aXn2Bmq9rCr9G_DpYlGyA25jybr0H=1OKB3331fIZnAiVVVEz7BNkDTuzR6hQvrpLUCahfe6Q8rcYeWXOsOby_8-GRTsUe_fX_oCTvQCwwl8gc49sUP8zRAmKIkVE6sVwCi_xluVwK_=J0LiPXMJMFaI42VRxZvrtt08p7xm2YVfU1k22f3a6jZ_UtTM9sVrg6ndp88HLzNn1NYWjJUHW1T5tAs5fXqAJfhQIj7Nz1M-HhW12aWAMtnpkgiCplOAm7mWJEtDQcK6eliRVcAUQFGTzP9QWRk=ua1PXu_Z9ZDzrba4YEwm34459zv4CparUWXW1eyARqG1MVbEs6dxAxP07s-J_X0k7vVA46l6HqfgZblR3ojaVLkqIL1xNqiGyCJb_hH3RaRQMZi6YV0-HoOLw9DR0TC2YWULcEyc6hws7TanyQgTksuvbCl0j=f4Go5RzCTPR_MY2thye2McTWt0uDWHJApwyrzNoBXEid35Zp7wLQ2J4jxgOx4ZbPCn9zLFF10=PR6us-NCsIyxsdFPRI3BupCEzcd-xk0rgJ4JDhs7cn5K0Tpepvmf9tR=Rm==MUFZhF5sr7NtfzIcQRnkkUhHM8b-Gh1=y2Oo70v_NsC7Vm5tG3F_s9e8J2dY1u4_GlpeCLZ1GVfVWb7m09yfCmrb=tgA_352WRo-B5Vnu0ImWlcYWQHMpL3Tpzp-O-9l_=eX0=m2bJot6=isWCEtLls_21UVcb-dOFEVihrqWnVGYnPTTyJ7oivp3bm=_diJ5oRFB0zLWehe6gjjqyb7logAG2JIOFDliJv_2QdnQTjDMTfzeZaMmX07P9XcZ3H_riKca1eG7ww9K4IvXoW9utvNj5tMJCcMnyP09NpUgKKPKbUpK2Fhul_qbReAbAtXdZuWetgGgyG4aIt3im_YMiNvnJoMPh4yjjHlCQ2JDXw2ihDI2hLCMdEdwJtDyn5aewFUIe4_K-QJBavK4spbi8oV5yYNcl-5j3HAuRjx=rt0n97FQ_Rg3=eHJMpPskyk20MuHeBr9NqTIz6Afhdb4PB4bMKjzg37MVqoaeAvq6L4nf34yC3azLh1aRvX8L0vN5X33zfdVdW16a_1zFur52u3ZcjGBHTWC=ZcDx9Qni=x4V-IK_YEemDTI-bHEoCL5ubv0V_yYmUTyOxRKeRYsfbBNaJbUBZhrq4eEA8TdqB5J72bodkHpCbjZjxnKDFgUsGjvUatmu9rwje7zq4C6snZPJMa3tynUN6QKROMxGX94ZozCd9QxfcTKq7ybJOd2u5Lk8HqqkAbDkfc5ObYmgpoZw0Vj5t49g1FmRLz1a4WfHjEA5gdZCvsBqssC0MTA6KohMd_XzGHrfOfcsphBcjd-FBXP=kKo2lEP_8yELTu3pWXD3XaXhzPE02x=QPs1y9fl2jvWD-YAYHsy_979LPZ0LvActOysp48sVmI=2CBHAa2RNMIZbqT7w3VrEi8wPiJwddP5xD5IOqAVQWg-sQGfNzA-dAP2dx85jTfKVJ=mawtFk_erwL34=E25zEc5joj71G1va5_PTzIcw87K8PKiaT5cy_NMGdW5RpgO7iIgXivtOU3AQqHP5-R-FyqTbYUYx88ZLivO-l5Tg5eWM07hTcE0L8wDyEDe6u7tJyXBCtMMMEL5kUwvFzzOhyOvhT9jghA7WXt6AEMAm019aPHBUft5Xki1PIDTx4ndMloDJDlY2aV42_timtgnIaKPTQQJtvj6Zkqa5e=7452xp4NVonv_hWj9gXzL_DYw7Un1vV2Q9ik5nb_3fMTdt1BLnod=MU3DtsARk2oKVF4ZQ1h8lAnLXewzOEdYPxEUNHQu4Xy15Z09xzVZe-40WVMN-DzCbpwHvW49i7BpjwJtLMPp=Z8Btx4UyfsVfGdZzRUNNpwUl0HpGoZvM9ojL4FrNauUqmwrGTRDkVqaEJ-stla4UcbAuF==aut1NZU6KDuPCVDWnIt0pThUY0bBOeVf_WHg1iEBDYBq=RmmauNcusOeHB7VsUbwq9RlEQpvKED58BXgEpJbHeAJXnZZu9H1Bkrm51v5PNCLkCcDsBZih5dXP5MHBMXQeYI7sHbVuJfw4mT7X-KXxL9E_r_ZU6CMY8tPud9BAxLnoKf3g7QR0xygs9IPCN_Jad9F-fWEufu7=C3U56kWY3vblrPntLcpv3AQrPKH8Lb-dNRPz3ClNPnVbyzN7LEpsh6JuyqND6tHZCsYPNY2d-J_ZhN9ed4dhZUWWMNyTUhyuYiHd3_BNFH-IisyyYrb6Ef5mUnwmnU3tgEiawNjs-HJ8rTcuQe0=-CVbfuEXNmC9uimX-Xoxy2y8WQ8cNAsVm0iz5NQ06oFdz98Blir=zD2VsM60_YYykclyUhqRGUBkKV1YOVeG2RvTtTVzkNhiZGzCr9YMFWyJ5qkD2XCblbw-gdLRmNPK_we7nFPj2qfcMmwndDkgZ8kUMMQRF1b=JN=dErQqzHv2jCCUbEql5as_NwbVmvPe4fp32kf46I=mrffL6YPrdeztyMdiP_ysDGb9yFlWO4WAidbTcsRJsiK_L06PbFNdtb24oNUN1LFhJ9FRtYa7HF63nulBa6mcyCs0ma087d04xpPbPHy5OaH4cmCwEG=bvRU62JGUx_7ydymdz3yubvJ0NB9CQPXhvTKa2Aigc09BrGIEEZRXYA4_RU2XCjZLyjqw3e9emcJaAn4MLARy6fo2qetgnqMBGut7ulGatbBnx41gjx8I2FFE35HCFG-ntMskYe5jCYkv3pkcKU4ebqh-6IGIrdGHWOHyrHnvw=NIyexBGopJJkPxWne9nzz=W2--b5U9oUm1jpUwBwX3zl3YcBd62vBC3rPJ--DvvXDslZWy4qXmuEv-t-hNwDOPahjtcMZFd=E4tZ8_L03liQwALsjRi_M=wq45DHd1sMwfzqNw5ZIipGKvmwiXyBwGfdQrKHJkBxHz7Wg=m=PBcuVnzGqQArwZg_Od7hHYcFyhLsjmJ50CbXKExaf3bw0uvZq6cT4eK5Cnz94vk_ohhB_ztlVwW19KEHIAszlrWC-NFP_zuzu8TVQ326fevGhWB6bhpL0KP_6ILy3LK34Wuf3B0d6ommGPLrIiZsAOBfJNnp7Bt1T0wjUhevVX_xlmwvZItU3acN7zdXE67dTh8Yz7uV3tTA2415bUNWKzk_dHB=YYB5vsAu2MMma9Ncy_8NQ__UyKgryVy46rRc_A3TDAbEWK=H6pnUaPT=YQEYpXwHNiB0PvfCEDerF0dMjw3c4fuEqkEj=WFmRZnediyRVB2gfKAHjZKc7y5qwDY6Tye53YAYkPys102xEop0yPq6D=hkt2iehj=YMyB31KxMDzg1NzpmkWT5sABRy8fv1x2_PsBE_nTMzB20xrybqCgzEjRaqrPD1NEGJCZcHoLpATx8BhmnJjrZ80vpnnNd7eh1d7Xw4zgTipfMzM3XpNd9940tC2w3EzNdi_iwAPis5eGmtNczYRAzfL7gjI8qBYwr_rv77X5uacrWscLO3QFbaYC0ZYC1x4vQZnYG6iXRZhklLA7WDArn3WxLTxh7LBDMYhupgTenpI65t9I2k8eojaUwhcOXgR8FE3l9Ifx6HwgV39aDw_Z=Ymxb9ZYdnvnDE5e4991j61T092HL11X7mgpYQqTfm4_kXuGW7j4sDcHxDAsgVjejKTVDo1poxOjLZfFvd3Wcjx9HaIor6bAzt8y1AEadHsEAIEgnuBucP=HxW3TeHE9W9YO7IoK_zY0Er1exe0eNG_x19KNawij4T7WyTMRVsXRBlds6QgHN-PhkMkJIurj1kIdhe8lj_o2p5BxbPwqMhw=3KM3A7wDOQeO9nKArmT8x413oRtJnjAsWWyvF7zpQfL99_okZttzZleRWIb1rDHbpfoN9egLyLyB5E7EoYoA0ir5RYeaqsY_6vgtZ4_Amzr0Mt7jWBRabYVi9cLmT1ilzZMeq-rJ7z-avKldLrLnTiIVNCyoY_G4EIribnl0=peOurxO1D8_L0b71dIewL5OhBHmmqNKGVrsuoFP7gwmV0xxsi6k4Pe5znTkXwciHxlio5qCrV=f9u0d6qg=R_dV7W8JUB6AUOF44Mf=jM0mDaFyvr86RdvBeKkhuqag7n_lqJKQiJdo9f9MiGdINmqJldxLXH60Y3K=LqhFcsDtIzenmGnH32DqimY5Tl1BeIjpODOUI=v8VPojU61Ym27E61-5Wn_3tGrWxi_hY5E85tJ5JnLW6vyhXG9r6CKpe1guReVLjFWjptzhPJ3_YxoORMyKitI3uHtng7p8g=eNAMY7neWgdvPoF9Tr6Jj7VUh4XGdnTQurG1nm3pYz9ZPstvq5uIu9mo0LrvZwQn8kdzOjlfuId=sJndl08uZci4Ahe0-t_DtosfQu4ssrH6y5kPiiKiYEyjyBWipvilRtZBdbtTDIC_ig=2mDDX-DQIpsuuA9zDZwyxmv=Us0FNNbDx1U1NVOCBDc1f1iHF03Qhg6s_YBrxMP4sGJvhwn5ceIwAs0zPcQb89N8jcE4Vv7Aj7tLo9dCqIreuC=xXFIEt_ih2J2HFB6wadK4_HE7mlcrdy1Nk0Vd-nRoH94V=0D4OaGyThpDLuDz_kdyEc1jI98J0oiUJ_kV2uNb=hRMiM07=Qmu3RdNKW0R6Tbi9XlwNkTuRp499W36yjy-roVFsAhhHh=7zGIkuBxAuDKnoX56k-cFep1qtcjrPtGRipPB=-=64RnB9tonlguM0kFt1bYT3JqiN28qrgp9ZK0Jy0L2j1LfKlxIE1q4b2lYdFWy0GIggb55ds6gGGYTg9frLhjDo5cLsZbul6aCPINF4cKKF6F9gh54WlpwqfPGzYsfMtGyd31wCGEv4YF4RzvZXHeUdOW_n2T38o_0PAeUQkuK_of19-0R2x6qDNxwZ83-XZvz2nndAGcNBw1_0G-Aw4eODdTMVra9674ceVNFN9zGil48In0p94Jdo4dEH=fULyHy3t7=07vqxM_lhQ5eM1x8EQ0LgvP72ZJFdGlApisfGy5cMG-uW1TVQvbegixAAxmgHbW0ZWlemO_7rHYt3Pw=1hcBClN20JmvrIztU_KFrN=Ohl7Bcz_i5LClD97Llr=M1_4MYfYWs2GbgwWJ2Gw3QNCHo-0P1pM0uyVkfDAL72Hwor9jH=O7B06hgA9wPWIBYRF9VJwL6v0Nqdyu3a=e-EmyOaCfwDzibh04lhi6Kh1eWtWXIGUMoGPvaEaGlXv=_jWiPLQDcl9CVtifDTO3hawQgNFd4IadqR4v-JNJecuB9uw0b_=FagfiDw1e-DtRWJq1eHybuHQiQ1DyVHKNaCEssDp69UqU75mREvMpQBTOL81X_s1eGg3XG=cPRkKl7ZcMRrIUHVVKgL1x6DJu_2nmlCOfMqy1xktBqT1NdXVmUGJ=X0cq1c=WJg5HF6AkZrOO-k3COpDqiBHaH2PBxPErrkT1mzQG-LGERwrxlqTD6vwFWp8knJi-OnYH_ynuObNinOdc2odj=RBJnxR_pnzXhl=_cqHlr4iK6Kel_sQmnO5NZVQiqc1h4oFK0-i9nftP6TikURTZkKoQkzEMrq2MyP6sephLKfy2yLp3VBXMYoxwo3N5iUII5B1ZwlyrFw4jAn=MRqt1Q7Tnj3WgZRHo0ayWrm9AZPkvu-A4uDQM3z8fUuQzZF8v=YM6taEzTIftKUVzJgigVLKD5cs=oAaxQOwWgfEAiibqJT8V-MpwQybsYsiUmFcnfWt4K5o-ykmZs2O4TKb4dOrCgf1Pe5YdjujQ6gTO4HD7vcBeYqc9nAqLGWB3Ib4bXGw7Fb1PzJzq9nkWXyh53RqXZRsfKWFw_VgiM-_zW2t6ID0TQlypCUoHhZG_Oj_CJgME1tg4=FtmrzzzN78daAVnpGbhGBVXIvgZN38RX0WONPLQdi6jwev83q4hCrcCrylq1VcFHOEoCQ3CoR496Hfsbsp5pTg3lE3Yn7T=sGexmxrBPIbI-g96dtzB0hJ=YJ1zcgTLn6tFNcBefbdQ_ohu-lpv6eQOon4Ivu_dOi-nCF6i3yC=yLIA-zy0jJzbmybW3peJmpEfA3VKnRAd9H4nHWi-zoNh3qXiliqGzBhgpEWwi-Jkq6GmUfx6nk6czOmk87JxPEmkptfVT0t3ykPwjE0OXL=rj=7cUEkdEZi-nKWCo8xCD-vnL7sTjHT6tUEYJbGuiVRUuA5qRYi7YYzGIQPRW1oUMcyBFDu-_xMtDXYzRyGJY5o5_01lurN2B-gmAdpyTu4BXA_y5yFzDKyf5roa37DLLzX9XhB-keIOmBwDs-Wd-0WAIbMBrszIsZky28=fsVqJ1fn=vRGqN2fgxDW_j=ljfa7OKUNl5=o79wAHq1Ryk_ulyywX0=K9nfJNAnZHFYef8Mp2-fX1g_POPxqGn_DyL=JVa6KeD8NLPl6GF-fjmTu45LBnALTND2AWYd2701Y5falwlxQ1uxL2AybyuCDT4Dc_NbJTnjcaPwiOH-4nXhWxkB3J__0j7f-l9XwWcN8MCEfPbQzt4KZ3v9ApCLXjhwAmu02frWblf8lBwEi3ZKZarP4jGnBtvLubsunPo-P2zUlPP7aM-aO5eJkZTC9gX4pT1GZdg=xzbbqLl=886sYkG0M7OKVJc00G9-l7IpPV5xUzy38vMUKvWh=kKUZVV=Nz_xnqYJXmL7MklDWKmgyXH69cR6LLyOrcannj-xj1iU9EbwxLtK_nnCMPnxcha1rM_Ekb4wVPFoqrb_CQCvMl6vghpW3JmsK8VoxAcV_4q1rx-E4j1=2W8RwpMab-e5mOBDc4EE71oHcBxQTETjyetNK2h9X9NoW=9o1Dm8l4Yh-rPwL_RWdyqEXOscZpgy_Op88d_6xJ9rLm2hAmxiW=FEHwjk-ijnnWPK09-=yTLQ2b_Gm=r8-TGGyzNbMKHUcwiC0MkeQ9kLbmiDUqbpExKTKKEQsxc',
    'wu44b0puoj-a0': 'KeuD0GvR-lbK7BE85Ebm8OILgY4CeC39kQuXBfvyFjH6bM4tydmkQsmplXXI__BdI44dT8pDkXls6XFzjHmQQXn9Y=Dvw8KJtdcjPPLTDZkEXj02euiGbrkkxFMD1Ma_zqKDUneI_fV4ov6radZUyMGQ0oVQouXUfz0VfOYuq5JZNjLY5NJp7CLkVFAVH422YquGXE_zFD_lci7IFHQj56IoDl5JqbUwGs3LrtJUx2CvYokDTjiKCRZui9PV-m',
    'wu44b0puoj-b': '-tf21tt',
    'wu44b0puoj-c': 'AOAm556PAQAAkkgv3mN2sVoWqNN1RiK6UzNM8lEkc-HSPSlYjlHo5S1rC9P0',
    'wu44b0puoj-d': 'ABaAhIDBCKGFgQGAAYIQgISigaIAwBGAzvpCzi_33wdR6OUtawvT9P____-GR64xABJ6FyuBYf9sIZKTj7DxOzY',
    'wu44b0puoj-f': 'A_Ow556PAQAAP_EbbKwx1JBIjnvIrUZczw-iJ-WhpAwi7an1lmPlQsy_T2RSAbT7tjCucnvuwH8AAEB3AAAAAA==',
    'wu44b0puoj-z': 'q',
    'x-csrf': 'OID_TOKEN',
    'x-requested-with': 'AsyncRequest',
    'x-sessntabid': '8iyb8vlwfz',
    'x-tab-id': '2VTpjwIB',
}

json_data = {
    'loginValue': 'Betafits2023',
    'manageOptumId': False,
}

# response = requests.post(
#     'https://identity.onehealthcareid.com/api/v1/auth/login-options',
#     cookies=cookies,
#     headers=headers,
#     json=json_data,
# )
fresponse = requests.get("https://identity.onehealthcareid.com/oneapp/index.html#/login")
response = requests.post('https://identity.onehealthcareid.com/api/v1/auth/login-options',cookies=fresponse.cookies,headers=headers,json=json_data)
response2 = requests.post("https://identity.onehealthcareid.com/api/v1/auth/authenticate",cookies={
    'akym-d': '4B0v1BB8vIhUF8K18Sh3SF',
    'pixel-ubrid': 'v2.0-1811b0c5f240e80290284b471ead6e59-1472-1478-1714361039883-0001030980-1716223919682',
    's_fid': '459C48FD7505BCF2-3186632DE0499C66',
    'oidp': 'AV48Esxk4_P4qy5ALba2ePGeWrTdMn8GyYLv_l_pcK3w4y5a26Nr6HBOLTy4Pw==',
    'at_check': 'true',
    'AMCVS_8E391C8B533058250A490D4D%40AdobeOrg': '1',
    'mbox': 'PC#b71e752213bc4bc095c69bda503e31fa.38_0#1779603378|session#f74eb2fa317a4bd0b4ac1bda7346ba8d#1716360438',
    's_cc': 'true',
    's_gpv_pagename': 'optum%3AOne%20Healthcare%20ID%3Apublic%3Alogin%3Apassword',
    'AMCV_8E391C8B533058250A490D4D%40AdobeOrg': '179643557%7CMCIDTS%7C19866%7CMCMID%7C38761225400979175984394326055082877406%7CMCAAMLH-1716828743%7C3%7CMCAAMB-1716358576%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1716366093s%7CNONE%7CMCSYNCSOP%7C411-19871%7CvVersion%7C5.5.0',
},headers=headers,json={"loginValue":"Betafits2023","password":"yz_r^PjPp46QLTD","totp":"","manageOptumId":"false","authenticationType":"PASSWORD"})

print(response.headers)
print(response2.content)
