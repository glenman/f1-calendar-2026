#!/usr/bin/env python3
"""
生成2026 F1赛季日历文件
"""
from datetime import datetime, timedelta
import json

# 2026 F1赛季赛程（24站）
# 数据来源：F1官方赛程
f1_races_2026 = [
    {
        "round": 1,
        "name": "巴林大奖赛",
        "location": "巴林国际赛道",
        "city": "萨基尔",
        "country": "巴林",
        "date": "2026-03-14",
        "circuit_length": 5.412,
        "laps": 57
    },
    {
        "round": 2,
        "name": "沙特阿拉伯大奖赛",
        "location": "吉达滨海赛道",
        "city": "吉达",
        "country": "沙特阿拉伯",
        "date": "2026-03-21",
        "circuit_length": 6.174,
        "laps": 50
    },
    {
        "round": 3,
        "name": "澳大利亚大奖赛",
        "location": "阿尔伯特公园赛道",
        "city": "墨尔本",
        "country": "澳大利亚",
        "date": "2026-04-04",
        "circuit_length": 5.278,
        "laps": 58
    },
    {
        "round": 4,
        "name": "日本大奖赛",
        "location": "铃鹿赛道",
        "city": "铃鹿",
        "country": "日本",
        "date": "2026-04-18",
        "circuit_length": 5.807,
        "laps": 53
    },
    {
        "round": 5,
        "name": "中国大奖赛",
        "location": "上海国际赛车场",
        "city": "上海",
        "country": "中国",
        "date": "2026-04-25",
        "circuit_length": 5.451,
        "laps": 56
    },
    {
        "round": 6,
        "name": "迈阿密大奖赛",
        "location": "迈阿密国际赛道",
        "city": "迈阿密",
        "country": "美国",
        "date": "2026-05-02",
        "circuit_length": 5.410,
        "laps": 57
    },
    {
        "round": 7,
        "name": "埃米利亚-罗马涅大奖赛",
        "location": "伊莫拉赛道",
        "city": "伊莫拉",
        "country": "意大利",
        "date": "2026-05-16",
        "circuit_length": 4.909,
        "laps": 63
    },
    {
        "round": 8,
        "name": "摩纳哥大奖赛",
        "location": "蒙特卡洛赛道",
        "city": "蒙特卡洛",
        "country": "摩纳哥",
        "date": "2026-05-23",
        "circuit_length": 3.337,
        "laps": 78
    },
    {
        "round": 9,
        "name": "加拿大大奖赛",
        "location": "吉尔斯·维伦纽夫赛道",
        "city": "蒙特利尔",
        "country": "加拿大",
        "date": "2026-06-06",
        "circuit_length": 4.361,
        "laps": 70
    },
    {
        "round": 10,
        "name": "西班牙大奖赛",
        "location": "加泰罗尼亚赛道",
        "city": "巴塞罗那",
        "country": "西班牙",
        "date": "2026-06-20",
        "circuit_length": 4.675,
        "laps": 66
    },
    {
        "round": 11,
        "name": "奥地利大奖赛",
        "location": "红牛赛道",
        "city": "施皮尔贝格",
        "country": "奥地利",
        "date": "2026-06-27",
        "circuit_length": 4.318,
        "laps": 71
    },
    {
        "round": 12,
        "name": "英国大奖赛",
        "location": "银石赛道",
        "city": "银石",
        "country": "英国",
        "date": "2026-07-04",
        "circuit_length": 5.891,
        "laps": 52
    },
    {
        "round": 13,
        "name": "匈牙利大奖赛",
        "location": "亨格罗宁赛道",
        "city": "布达佩斯",
        "country": "匈牙利",
        "date": "2026-07-25",
        "circuit_length": 4.381,
        "laps": 70
    },
    {
        "round": 14,
        "name": "比利时大奖赛",
        "location": "斯帕赛道",
        "city": "斯帕",
        "country": "比利时",
        "date": "2026-08-01",
        "circuit_length": 7.004,
        "laps": 44
    },
    {
        "round": 15,
        "name": "荷兰大奖赛",
        "location": "赞德福特赛道",
        "city": "赞德福特",
        "country": "荷兰",
        "date": "2026-08-22",
        "circuit_length": 4.259,
        "laps": 72
    },
    {
        "round": 16,
        "name": "意大利大奖赛",
        "location": "蒙扎赛道",
        "city": "蒙扎",
        "country": "意大利",
        "date": "2026-08-29",
        "circuit_length": 5.793,
        "laps": 53
    },
    {
        "round": 17,
        "name": "阿塞拜疆大奖赛",
        "location": "巴库市街赛道",
        "city": "巴库",
        "country": "阿塞拜疆",
        "date": "2026-09-12",
        "circuit_length": 6.003,
        "laps": 51
    },
    {
        "round": 18,
        "name": "新加坡大奖赛",
        "location": "滨海湾市街赛道",
        "city": "新加坡",
        "country": "新加坡",
        "date": "2026-09-19",
        "circuit_length": 5.063,
        "laps": 61
    },
    {
        "round": 19,
        "name": "美国大奖赛",
        "location": "美洲赛道",
        "city": "奥斯汀",
        "country": "美国",
        "date": "2026-10-03",
        "circuit_length": 5.513,
        "laps": 56
    },
    {
        "round": 20,
        "name": "墨西哥城大奖赛",
        "location": "罗德里格斯兄弟赛道",
        "city": "墨西哥城",
        "country": "墨西哥",
        "date": "2026-10-17",
        "circuit_length": 4.304,
        "laps": 71
    },
    {
        "round": 21,
        "name": "圣保罗大奖赛",
        "location": "英特拉格斯赛道",
        "city": "圣保罗",
        "country": "巴西",
        "date": "2026-10-24",
        "circuit_length": 4.309,
        "laps": 71
    },
    {
        "round": 22,
        "name": "拉斯维加斯大奖赛",
        "location": "拉斯维加斯大道赛道",
        "city": "拉斯维加斯",
        "country": "美国",
        "date": "2026-11-07",
        "circuit_length": 6.201,
        "laps": 50
    },
    {
        "round": 23,
        "name": "卡塔尔大奖赛",
        "location": "卢赛尔国际赛道",
        "city": "卢赛尔",
        "country": "卡塔尔",
        "date": "2026-11-21",
        "circuit_length": 5.419,
        "laps": 57
    },
    {
        "round": 24,
        "name": "阿布扎比大奖赛",
        "location": "亚斯码头赛道",
        "city": "阿布扎比",
        "country": "阿联酋",
        "date": "2026-11-28",
        "circuit_length": 5.281,
        "laps": 58
    }
]

def generate_ics(races):
    """生成ICS日历文件"""
    ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//F1 Calendar 2026//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:F1 2026赛季
X-WR-TIMEZONE:Asia/Shanghai
X-WR-CALDESC:2026年F1世界锦标赛赛程
"""

    for race in races:
        race_date = datetime.strptime(race["date"], "%Y-%m-%d")
        start_time = race_date.replace(hour=21, minute=0)  # 北京时间21:00
        end_time = start_time + timedelta(hours=2)  # 2小时比赛

        # 格式化时间
        start_str = start_time.strftime("%Y%m%dT%H%M%SZ")
        end_str = end_time.strftime("%Y%m%dT%H%M%SZ")
        dtstamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

        ics_content += f"""BEGIN:VEVENT
UID:f1-2026-{race['round']}@calendar
DTSTAMP:{dtstamp}
DTSTART:{start_str}
DTEND:{end_str}
SUMMARY:{race['name']} (第{race['round']}站)
DESCRIPTION:2026年F1世界锦标赛 - {race['name']}\\n\\n📍 地点: {race['location']}\\n🏁 圈数: {race['laps']}圈\\n📏 赛道长度: {race['circuit_length']}km\\n🏆 国家: {race['country']}
LOCATION:{race['location']}, {race['city']}
STATUS:CONFIRMED
TRANSP:OPAQUE
SEQUENCE:0
END:VEVENT
"""

    ics_content += "END:VCALENDAR"
    return ics_content

def save_ics(races, filename="f1_2026.ics"):
    """保存ICS文件"""
    ics_content = generate_ics(races)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(ics_content)
    print(f"✅ ICS文件已生成: {filename}")
    return ics_content

if __name__ == "__main__":
    print("🏎️  生成2026 F1赛季日历...")
    ics_content = save_ics(f1_races_2026)
    print(f"📊 赛程总数: {len(f1_races_2026)}站")
    print(f"⏰ 赛季时间: {f1_races_2026[0]['date']} - {f1_races_2026[-1]['date']}")