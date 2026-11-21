# ✈️ 部署前的 GO / NO-GO 轮询 / The pre-deploy GO / NO-GO poll
# 真正的发射前，任务控制中心会一个一个问：「GO 还是 NO-GO？」部署也一样！
# Before a real launch, mission control asks every team: "GO or NO-GO?" Deploying works the same way!
# 检查完一项，就把它的 False 改成 True，再运行 / check an item, change its False to True, run again

checks = {
    "从头运行没有红字 / runs from scratch, no red text": False,
    "test() 全部通过 / test() all pass": False,
    "第一行有标题和作者 / title + author on line 1": False,
    "删掉了侦探 print / detective prints removed": False,
    "存成 week12-showcase / saved as week12-showcase": False,
    "没有真名、学校、照片 / no real name, school or photo": False,
}

def all_systems_go(checks):             # 第 10 课的老朋友 / an old friend from Lesson 10
    for item in checks:
        if checks[item] != True:
            return False
    return True

print("📋 GO / NO-GO poll")
for item in checks:
    if checks[item]:
        print("   GO     ✅ " + item)
    else:
        print("   NO-GO  ⛔ " + item)

if all_systems_go(checks):
    print("\n🚀 全部 GO！可以部署了 / All GO — cleared to deploy!")
else:
    print("\n🛑 还有 NO-GO，先修好再部署 / Still NO-GO — fix it before you deploy")
