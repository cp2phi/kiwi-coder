# 🚀 第 6 关：发射总指挥 / Level 6: launch director
# status 是一个字典：岗位名字 → 它的回答（每次运行都会变，看输出最上面）
# status is a dictionary: station name → its reply (changes every run — see the top of the output)
# 比如 / e.g.  {"booster": " GO", "weather": "no go", "range": "Go"}

# 第 5 关的招式，直接拿来用！/ your trick from level 5 — reuse it!
def is_go(reply):
    return reply.strip().lower() == "go"

def blockers(status):
    # TODO: 交回一个列表：回答不是 go 的岗位名字（按字典里的顺序）
    # TODO: return a list of the station names whose reply is not go (in the dictionary's order)
    return []

def director(status):
    # TODO: 没有 blocker → "GO FOR LAUNCH"
    #       有 → "HOLD: weather, range"（名字之间是逗号 + 空格）
    # TODO: no blockers → "GO FOR LAUNCH"
    #       otherwise → "HOLD: weather, range" (comma + space between names)
    return "GO FOR LAUNCH"

print(blockers(status))
print(director(status))
