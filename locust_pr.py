import logging
import os
import queue

from locust import HttpLocust, TaskSet, task, between
# from locust import TaskSequence, seq_task
# from locust.events import request_failure
import requests

logging.getLogger().setLevel(logging.INFO)
logging.getLogger('locust.main').setLevel(logging.DEBUG)
logging.getLogger('locust.runners').setLevel(logging.DEBUG)


def common_config(self):
    with self.client.get("/api/common/config", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def common_recommend(self):
    with self.client.get("/api/common/recommend", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def user_info(self):
    with self.client.get("/api/user/info", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def article_list(self):
    with self.client.get("/api/article/list?pageNo=1", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())


def product_list1(self):
    with self.client.get("/api/product/list?pageNo=1", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())


def product_list2(self):
    with self.client.get("/api/product/list?badge=4&pageNo=1&productType=1", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())


def article_info(self):
    with self.client.get("/api/article/info?id=1211711414624862208", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def article_comment(self):
    with self.client.get("/api/article/comment/lasted?pageNo=1&articleId=1211711414624862208", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())


def giftlessInfo(self):
    with self.client.get("/api/product/giftlessInfo?id=1217813301451309056", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def product_comment(self):
    with self.client.get("/api/product/comment/home?id=1217813301451309056", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def task_info(self):
    with self.client.get("/api/task/info", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def user_signin(self):
    with self.client.post("/api/user/signIn/post", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200 or response.status_code == 400:
            response.success()
        else:
            response.failure(response.json())

def search(self):
    with self.client.get("/api/search/?keyword=多多罗", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def tagRole_search(self):
    with self.client.get("/api/tagRole/search?search=夏目友人", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def get_user_orderlist(self):
    data = {"pageNo": 1}
    with self.client.post("/api/order/getUserOrderList", headers=self.headers, data=data, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())


def get_bill_list(self):
    data = {
           "inorOut":1,
            "pageNo":1,
            "type":1
    }

    with self.client.post("/api/account/getAccountBillList", headers=self.headers, data=data, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def tag_list(self):
    with self.client.get("/api/tag/list?pageNo=1&region=0&keyword=", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def signin_record(self):
    with self.client.get("/api/user/signIn/calendar?month=2020-03", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

def common_collect(self):
    with self.client.get("/api/common/collect/list?pageNo=1", headers=self.headers, catch_response=True) as response:
        if response.status_code == 200:
            if response.json()['msg'] == "OK":
                response.success()
            else:
                response.failure(response.json())
        else:
            response.failure(response.json())

# 定义用户行为
class UserBehavior(TaskSet):
    tasks = {
        common_config : 1,
        common_recommend: 0,
        user_info: 0,
        article_list: 0,
        article_info: 0,
        article_comment: 0,
        product_list1: 0,
        product_list2: 0,
        giftlessInfo: 0,
        product_comment: 0,
        task_info: 0,
        user_signin: 0,
        search: 0,
        tagRole_search: 0,
        get_user_orderlist: 0,
        get_bill_list: 0,
        tag_list: 0,
        signin_record: 0,
        common_collect: 0
    }

    def __init__(self, *args, **kwargs):#初始化函数，继承父类参数
        super(UserBehavior, self).__init__(*args, **kwargs)
        # self.host = "http://{}:{}".format(url,port)
        self.headers = {
            "Content-Type": "application/json",
            "token": ""
        }

    def on_start(self):
        try:
            self.uid = self.locust.q.get(block=False)  # 从队列中取出id赋值给uid
            print(self.uid)
        except queue.Empty:
            print("没有那么多并发用户...")
            exit()

        response = requests.get("http://ip:port/test/user/token?id={}".format(self.uid), headers=self.headers)
        # response = self.client.get("/test/user/token?id={}".format(self.uid), headers=self.headers)
        if response.status_code == 200:
            self.headers["token"] = response.content.decode()
        else:
            self.interrupt()


    def on_stop(self):
        print("----- Test over -----")



class SigninTasks(TaskSet):
    def __init__(self, *args, **kwargs):#初始化函数，继承父类参数
        super(SigninTasks, self).__init__(*args, **kwargs)
        # self.host = "http://ip:port"
        self.headers = {
            "Content-Type": "application/json",
            "token": ""
        }

    def on_start(self):
        pass

    @task
    def signin(self):
        try:
            self.uid = self.locust.q.get(block=False)  # 从队列中取出id赋值给uid
            print(self.uid)
        except queue.Empty:
            print("数据为空了...")
            self.interrupt()

        response = self.client.get("/test/user/token?id={}".format(self.uid), headers=self.headers)
        if response.status_code == 200:
            self.headers["token"] = response.content.decode()


        with self.client.post("/api/user/signIn/post", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                if response.json()['msg'] == "OK":
                    response.success()
                else:
                    response.failure(response.json())
            else:
                response.failure(response.json())

        # self.locust.q.put_nowait(self.uid)


class WebPageUser(HttpLocust):
    host = "http://ip:port"
    task_set = UserBehavior #指向一个用户行为类

    # task_set = SigninTasks
    wait_time = between(0.1, 0.3)

    ids = [1166518362784669696,1171454369304944640,1171459773560791040,1171865622326288384,1171865622397591552,1172011097528475648,1172011097578807296,1172029377706205184,1172029377773314048,1172956264502665216,1172956264720769024,1173427053073014784,1173616375600521216,1173616375696990208,1174504262810476544,1174913957631107072,1174913957714993152,1174916424716525568,1174932071789895680,1174984897824038912,1174984897874370560,1174994963155394560,1174994963209920512,1176139077469085696,1176410926962712576,1176410927042404352,1179393817367814144,1179393817556557824,1179742956769255424,1179742956899278848,1179776217151184896,1179776217222488064,1179776820011081728,1179776820094967808,1180115282123825152,1180115282471952384,1180571776753606656,1180571776854269952,1181580856657977344,1181580856796389376,1184488308831428608,1184488308902731776,1185439443385851904,1188107918424154112,1188342005327994880,1190202751708045312,1190202751942926336,1192224609303273472,1192224609550737408,1192253690984013824,1192253691076288512,1194937404721471488,1194937404876660736,1195007476429234176,1195007476521508864,1195546676098506752,1195546676186587136,1196687636417224704,1196687636475944960,1197021615393611776,1197021615456526336,1198778424064221184,1199324690208792576,1199613648025165824,1199613648079691776,1199870425287368704,1199870425329311744,1200663670384762880,1200810922864549888,1201184946304065536,1201184946346008576,1201318629069561856,1201318629166030848,1201366906804641792,1202905382800859136,1202905382846996480,1205326836125409280,1206506644670783488,1206869833858162688,1207986784655384576,1207986784697327616,1210180531052879872,1211272203018969088,1211272203207712768,1212268449032577024,1212268449082908672,1212566313042452480,1212986472827723776,1214828132402470912,1214828132456996864,1216693698641797120,1216693698692128768,1217352835532857344,1217496331841445888,1217681679196364800,1217681679393497088,1217683777615044608,1217815619999637504,1217819761992278016,1217825351502143488,1217832112967655424,1217834855677566976,1217837475905413120,1218071718887694336,1218071718979969024,1218516830000259072,1218516830214168576,1219904309001461760,1219904309068570624,1219919540868096000,1219919540935204864,1220337828840349696,1221652237386784768,1221652237449699328,1221671644985040896,1221671645068926976,1221697860152598528,1221697860215513088,1222752737914003456,1222752737981112320,1223637159894851584,1223637160125538304,1224265173213126656,1224265173288624128,1225454995759964160,1225454995831267328,1227784650160611328,1227784650223525888,1228221307758321664,1228221307812847616,1228547501175349248,1228547501301178368,1228654305771266048,1228654305821597696,1228698295887470592,1228698295967162368,1228713006787993600,1228713006842519552,1229054086448422912,1229054086502948864,1229325815431307264,1229325815498416128,1229375756237283328,1229741890635571200,1229741890685902848,1229806594229805056,1229819314723364864,1229819314782085120,1230116157969670144,1230384082530082816,1230425514024378368,1230425514129235968,1230850091221262336,1230850091267399680,1230859009708269568,1231465981017071616,1231465981272924160,1232049735280369664,1232049735376838656,1232636063927771136,1232636064003268608,1232840222388002816,1232840222446723072,1233273787516985344,1233273787592482816,1233573827573719040,1233573827649216512,1233737282813435904,1233737282876350464,1233775844602683392,1233775844653015040,1234119528825233408,1234119528875565056,1234398747031511040,1234398747081842688,1234487095431536640,1235007695233228800,1235007695384223744,1235402029585670144,1236170065271857152,1236170065326383104,1236518644733714432,1236518644800823296,1237033131794505728,1237033131861614592,1237192113628651520,1237192113695760384,1237201590327189504,1237201590373326848,1238257483017887744,1238257483097579520,1238293099956936704,1238381681350549504,1238381681518321664,1239595672676605952,1239595672722743296,1239725881249767424,1240533046193561600,1240533046235504640,1241373990908338176]
    q = queue.Queue()  # 实例化一个队列
    for i in ids:
        q.put_nowait(i) # 把每一个user存到队列中


if __name__ == '__main__':
    # os模块执行系统命令，相当于在cmd切换到当前脚本目录，执行locust -f locust_login.py
    os.system("locust -f locust_pr.py --web-host=127.0.0.1")

    # os.system("locust -f locust_pr.py --no-web -c 200 -r 100  -t 2m --only-summary --reset-stats --csv=result")
