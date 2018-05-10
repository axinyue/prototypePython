

REAL_NAME = "http://111.230.18.174:8080/GMPlatform/" #  "http://ap.threepig.cn:18080/GMPlatform"  #
# setting
INDEX_URL = "%s/index.html"%REAL_NAME
LOGIN_URL ="%s/user/login"%REAL_NAME
PWD = "1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014"

# 维护服务器状态url   {"serverId":serverId,"statusValue":"0"}
SERVER_STATE_URL= "%s/serverstatus/open_server"%REAL_NAME

# 开服url  {"serverId":serverId,"statusValue":"服务器,0"}
START_SERVER_URL = "%s/serverstatus/new_server"%REAL_NAME

# 服务器ls
SERVER_LIST = "%s/giftCode/getServerList"%REAL_NAME
# 响应参数 {"data":[{"subZone":1,"zoneId":1,"zoneName":"封神伊始"},{"subZone":2,"zoneId":2,"zoneName":"武王伐纣"},{"subZone":3,"zoneId":3,"zoneName":"八九玄功"},{"subZone":4,"zoneId":4,"zoneName":"开天辟地"},{"subZone":5,"zoneId":5,"zoneName":"斜月三星"},{"subZone":6,"zoneId":6,"zoneName":"月上海棠"},{"subZone":7,"zoneId":7,"zoneName":"鱼游春水"}],"meta":{"msg":"ok","success":true}}

# 查找角色  {serverId: "7", roleId: "", roleName: "斩魂作人", account: ""}
SELECT_USER = "%s/userInfo/get_user_info"%REAL_NAME
# 响应参数 {"data":[{"openAccount":"AOWAN_259_4990121","talkStatus":0,"exp":0,"level":9,"coin":220,"money":1292210,"account":"AOWAN_0509950169","roleName":"斩魂作人","blockStatus":"0","onlineStatus":1,"channel":"AOWAN","roleId":"700000229"}],"meta":{"msg":"ok","success":true}}

# 创建邮件
# 请求参数 {"serverId":"7","roleId":"700000229","title":"钻石资源发放","content":"钻石资源发放","itemDict":"2_6480","expireTime":"1","coolTime":"0","conditionList":"1__,2__"}
CREATE_EMAIL = "%s/email/create_email"%REAL_NAME
# 相应参数 {"meta":{"msg":"ok","success":true}}

# 查询待审核邮件
# 请求参数
EMAIL_STATE = "%s/email/email_by_state"%REAL_NAME
# 响应参数 {"data":[{"conditionList":"1__,2__","content":"钻石资源发放","coolTime":0,"createAccount":"test1","expireTime":1,"itemDict":"2_6480","lastChangeTime":1525834554354,"roleId":"700000229","serverId":"7","state":0,"taskId":27,"title":"钻石资源发放"}],"meta":{"msg":"ok","success":true}}

# 审核发送邮件
# 请求参数 {taskId: 27}
SEND_EMAIL = "%s/email/send_whitelist_email"%REAL_NAME
# 响应参数 {"data":"发送结果状态码:0","meta":{"msg":"ok","success":true}}

# setting en