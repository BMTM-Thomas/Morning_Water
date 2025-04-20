
# 阿里云【中国站】
aliyun_ID = ("ven293", "ven319", "ven324", "ven365")
# 腾讯云【中国站】
tencent_CN_ID = ("ven178")
# 腾讯云【国际站】
tencent_Int_ID = ("ven295", "ven414", "ven469")
# 华为 IAM用户登录 【OPSADMIN】
huawei_ID = ("ven388")
# namecheap
namecheap = ("namecheap")

# Tencent_Int_EdgeOne
tencent_edgeOne_ID = (
                  "https://www.tencentcloud.com/account/login?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2Fedgeone%2Fzones",
                  "https://www.tencentcloud.com/account/login/subAccount/200039340025?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2Fedgeone%2Fzones",
                  )

tencent_EdgeOne_1 = (
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-3a7o753j8piq/overview", # ven414 xfh8866.com 123tk
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-3a7nqg1qsyy9/overview", # ven414 yelvlab.com 49tk
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-39xvl2ifs2ky/overview", # ven414 rimword.com a6tk
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-39ox7p1fxbzl/overview", # ven414 txn2jb.com 853tk
                  )

tencent_EdgeOne_2 = (
                  "https://console.tencentcloud.com/edgeone/zones/detail/zone-39c121mjq0xe/overview", # ven469 zone-39c121mjq0xe
                  )

tencent_EdgeOne = (tencent_EdgeOne_1, tencent_EdgeOne_2)  

tencent_EdgeOne_Tag = ("use: 123tk", "use: 49tk", "use: a6tk", "use: 853tk", "use: tk2")

# MongoDB
mongodb_id = (
              "67ef5266cac6b5cc88fb7444", # ven293 CDN
              "67ef5a11cac6b5cc88fb7447", # ven319 CDN
              "67ef5a2ecac6b5cc88fb7448", # ven324 CDN
              "67ef5a44cac6b5cc88fb7449", # ven365 CDN CN
              "67ef5a50cac6b5cc88fb744a", # ven365 CDN AP1
              "67ef5a59cac6b5cc88fb744b", # ven365 CDN AP2
              "67ef5a64cac6b5cc88fb744c", # ven178 CDN流量包
              "67ef5a64cac6b5cc88fb744c", # ven295 直播流量包
              "67fee84058970d6d770955d5", # ven338 中国大陆CDN
            )


if __name__ == "__main__":
    target_id = "67ef5a64cac6b5cc88fb744c"
    index = mongodb_id.index(target_id)
    print("Found at index:", index)