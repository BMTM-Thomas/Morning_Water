
# 阿里云【中国站】
aliyun_ID = ("ven293", "ven319", "ven324", "ven365")
# 腾讯云【中国站】
tencent_CN_ID = ("ven178")
# 腾讯云【国际站】
tencent_Int_ID = ("ven469", "ven473")
# 华为 IAM用户登录 【OPSADMIN】
huawei_ID = ("ven388")
# namecheap
namecheap = ("namecheap")
# zabbix jh-03 site
zabbix = ("vps zabbix (域名監控)")

# Tencent_Int_EdgeOne
tencent_edgeOne_ID = (
                  "https://www.tencentcloud.com/account/login/subAccount/200039340025?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2Fedgeone%2Fzones",
                  "https://www.tencentcloud.com/account/login?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2Fedgeone%2Fzones",
                  )

tencent_EdgeOne_1 = (
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-39c121mjq0xe/overview", # ven469 use: tk2 
                  )

tencent_EdgeOne_2 = (
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-3as3tur0husy/overview", # ven473 asptctest.com 123tk
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-3as3rxnjlyr6/overview", # ven473 gaaamo.com 853tk_1
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-3as3q8k30zzs/overview", # ven473 szdxlexus.com 853tk_2
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-3as3oj093h8y/overview", # ven473 aiqiutong.com 6htv
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-3as3i3be51rm/overview", # ven473 pyswdsyxx.com a6tk_1
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-3as3mkia971t/overview", # ven473 sulinglaw.com a6tk_2
                  )

tencent_EdgeOne = (tencent_EdgeOne_1, tencent_EdgeOne_2)  

tencent_EdgeOne_Tag = ("use: tk2", "use: 123tk", "use: 853tk_1", "use: 853tk_2", "use: 6htv", "use: a6tk_1", "use: a6tk_2")

# MongoDB
mongodb_id = (
              "67ef5266cac6b5cc88fb7440", # ven293 CDN
              "67ef5a11cac6b5cc88fb7441", # ven319 CDN
              "67ef5a2ecac6b5cc88fb7442", # ven324 CDN
              "67ef5a44cac6b5cc88fb7443", # ven365 CDN CN
              "67ef5a50cac6b5cc88fb7444", # ven365 CDN AP1
              "67ef5a59cac6b5cc88fb7445", # ven365 CDN AP2
              "67ef5a64cac6b5cc88fb7446", # ven178 CDN流量包
              "67ef5a64cac6b5cc88fb7447", # ven469 use: tk2
              "67ef5a64cac6b5cc88fb7448", # ven469 use: tk2
              "67ef5a64cac6b5cc88fb7449", # ven473 asptctest.com 123tk 加速流量
              "67ef5a64cac6b5cc88fb744a", # ven473 asptctest.com 123tk 加速请求
              "67ef5a64cac6b5cc88fb744b", # ven473 gaaamo.com 853tk_1 加速流量
              "67ef5a64cac6b5cc88fb744c", # ven473 gaaamo.com 853tk_1 加速请求
              "67ef5a64cac6b5cc88fb744d", # ven473 szdxlexus.com 853tk_2 加速流量
              "67ef5a64cac6b5cc88fb744e", # ven473 szdxlexus.com 853tk_2 加速请求
              "67ef5a64cac6b5cc88fb744f", # ven473 aiqiutong.com 6htv 加速流量
              "67ef5a64cac6b5cc88fb7450", # ven473 aiqiutong.com 6htv 加速请求
              "67ef5a64cac6b5cc88fb7451", # ven473 pyswdsyxx.com a6tk_1 加速流量
              "67ef5a64cac6b5cc88fb7452", # ven473 pyswdsyxx.com a6tk_1 加速请求
              "67ef5a64cac6b5cc88fb7453", # ven473 sulinglaw.com a6tk_2 加速流量
              "67ef5a64cac6b5cc88fb7454", # ven473 sulinglaw.com a6tk_2 加速请求
              "67ef5a64cac6b5cc88fb7455", # ven388 中国大陆CDN
              "67ef5a64cac6b5cc88fb7456", # namecheap
              "67ef5a11cac6b5cc88fb7457", # ven406銀行卡歸屬地查詢
              "67ef5a11cac6b5cc88fb7458", # ven243[jh03-site-01、03、12、18]騰雲cdn站點流量紀錄
            )


if __name__ == "__main__":
    target_id = "67ef5a11cac6b5cc88fb7458"
    index = mongodb_id.index(target_id)
    print("Found at index:", index)