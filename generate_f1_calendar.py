#!/usr/bin/env python3
"""
生成2026 F1赛季日历文件
"""
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 2026 F1赛季赛程（24站）- 官方确认赛程
# 时间为当地时间，需要转换为北京时间（UTC+8）
f1_races_2026 = [
    {
        "round": 1,
        "name": "澳大利亚大奖赛",
        "location": "阿尔伯特公园赛道",
        "city": "墨尔本",
        "country": "澳大利亚",
        "date": "2026-03-08",
        "local_time": "15:00",
        "timezone": "Australia/Melbourne",  # UTC+11 (DST)
    },
    {
        "round": 2,
        "name": "中国大奖赛",
        "location": "上海国际赛车场",
        "city": "上海",
        "country": "中国",
        "date": "2026-03-15",
        "local_time": "15:00",
        "timezone": "Asia/Shanghai",  # UTC+8
    },
    {
        "round": 3,
        "name": "日本大奖赛",
        "location": "铃鹿赛道",
        "city": "铃鹿",
        "country": "日本",
        "date": "2026-03-29",
        "local_time": "14:00",
        "timezone": "Asia/Tokyo",  # UTC+9
    },
    {
        "round": 4,
        "name": "巴林大奖赛",
        "location": "萨基尔赛道",
        "city": "萨基尔",
        "country": "巴林",
        "date": "2026-04-12",
        "local_time": "18:00",
        "timezone": "Asia/Bahrain",  # UTC+3
    },
    {
        "round": 5,
        "name": "沙特阿拉伯大奖赛",
        "location": "吉达滨海赛道",
        "city": "吉达",
        "country": "沙特阿拉伯",
        "date": "2026-04-19",
        "local_time": "20:00",
        "timezone": "Asia/Riyadh",  # UTC+3
    },
    {
        "round": 6,
        "name": "迈阿密大奖赛",
        "location": "迈阿密国际赛道",
        "city": "迈阿密",
        "country": "美国",
        "date": "2026-05-03",
        "local_time": "16:00",
        "timezone": "America/New_York",  # UTC-4 (EDT)
    },
    {
        "round": 7,
        "name": "加拿大大奖赛",
        "location": "吉尔斯·维伦纽夫赛道",
        "city": "蒙特利尔",
        "country": "加拿大",
        "date": "2026-05-24",
        "local_time": "16:00",
        "timezone": "America/Toronto",  # UTC-4 (EDT)
    },
    {
        "round": 8,
        "name": "摩纳哥大奖赛",
        "location": "蒙特卡洛赛道",
        "city": "蒙特卡洛",
        "country": "摩纳哥",
        "date": "2026-06-07",
        "local_time": "15:00",
        "timezone": "Europe/Monaco",  # UTC+2 (CEST)
    },
    {
        "round": 9,
        "name": "西班牙大奖赛 (巴塞罗那)",
        "location": "加泰罗尼亚赛道",
        "city": "巴塞罗那",
        "country": "西班牙",
        "date": "2026-06-14",
        "local_time": "15:00",
        "timezone": "Europe/Madrid",  # UTC+2 (CEST)
    },
    {
        "round": 10,
        "name": "奥地利大奖赛",
        "location": "红牛环赛道",
        "city": "施皮尔贝格",
        "country": "奥地利",
        "date": "2026-06-28",
        "local_time": "15:00",
        "timezone": "Europe/Vienna",  # UTC+2 (CEST)
    },
    {
        "round": 11,
        "name": "英国大奖赛",
        "location": "银石赛道",
        "city": "银石",
        "country": "英国",
        "date": "2026-07-05",
        "local_time": "15:00",
        "timezone": "Europe/London",  # UTC+1 (BST)
    },
    {
        "round": 12,
        "name": "比利时大奖赛",
        "location": "斯帕-弗朗科尔尚赛道",
        "city": "斯帕",
        "country": "比利时",
        "date": "2026-07-19",
        "local_time": "15:00",
        "timezone": "Europe/Brussels",  # UTC+2 (CEST)
    },
    {
        "round": 13,
        "name": "匈牙利大奖赛",
        "location": "匈格罗宁赛道",
        "city": "布达佩斯",
        "country": "匈牙利",
        "date": "2026-07-26",
        "local_time": "15:00",
        "timezone": "Europe/Budapest",  # UTC+2 (CEST)
    },
    {
        "round": 14,
        "name": "荷兰大奖赛",
        "location": "赞德福特赛道",
        "city": "赞德福特",
        "country": "荷兰",
        "date": "2026-08-23",
        "local_time": "15:00",
        "timezone": "Europe/Amsterdam",  # UTC+2 (CEST)
    },
    {
        "round": 15,
        "name": "意大利大奖赛",
        "location": "蒙扎国家赛道",
        "city": "蒙扎",
        "country": "意大利",
        "date": "2026-09-06",
        "local_time": "15:00",
        "timezone": "Europe/Rome",  # UTC+2 (CEST)
    },
    {
        "round": 16,
        "name": "西班牙大奖赛 (马德里)",
        "location": "马德里街道赛道",
        "city": "马德里",
        "country": "西班牙",
        "date": "2026-09-13",
        "local_time": "15:00",
        "timezone": "Europe/Madrid",  # UTC+2 (CEST)
    },
    {
        "round": 17,
        "name": "阿塞拜疆大奖赛",
        "location": "巴库城市赛道",
        "city": "巴库",
        "country": "阿塞拜疆",
        "date": "2026-09-26",
        "local_time": "15:00",
        "timezone": "Asia/Baku",  # UTC+4
    },
    {
        "round": 18,
        "name": "新加坡大奖赛",
        "location": "滨海湾街道赛道",
        "city": "新加坡",
        "country": "新加坡",
        "date": "2026-10-11",
        "local_time": "20:00",
        "timezone": "Asia/Singapore",  # UTC+8
    },
    {
        "round": 19,
        "name": "美国大奖赛",
        "location": "美洲赛道 (COTA)",
        "city": "奥斯汀",
        "country": "美国",
        "date": "2026-10-25",
        "local_time": "15:00",
        "timezone": "America/Chicago",  # UTC-5 (CDT)
    },
    {
        "round": 20,
        "name": "墨西哥城大奖赛",
        "location": "罗德里格斯兄弟赛道",
        "city": "墨西哥城",
        "country": "墨西哥",
        "date": "2026-11-01",
        "local_time": "14:00",
        "timezone": "America/Mexico_City",  # UTC-6
    },
    {
        "round": 21,
        "name": "圣保罗大奖赛",
        "location": "若泽·卡洛斯·帕塞赛道",
        "city": "圣保罗",
        "country": "巴西",
        "date": "2026-11-08",
        "local_time": "14:00",
        "timezone": "America/Sao_Paulo",  # UTC-3
    },
    {
        "round": 22,
        "name": "拉斯维加斯大奖赛",
        "location": "拉斯维加斯街道赛道",
        "city": "拉斯维加斯",
        "country": "美国",
        "date": "2026-11-21",
        "local_time": "20:00",
        "timezone": "America/Los_Angeles",  # UTC-8 (PST)
    },
    {
        "round": 23,
        "name": "卡塔尔大奖赛",
        "location": "卢赛尔国际赛道",
        "city": "卢赛尔",
        "country": "卡塔尔",
        "date": "2026-11-29",
        "local_time": "19:00",
        "timezone": "Asia/Qatar",  # UTC+3
    },
    {
        "round": 24,
        "name": "阿布扎比大奖赛",
        "location": "亚斯码头赛道",
        "city": "阿布扎比",
        "country": "阿联酋",
        "date": "2026-12-06",
        "local_time": "17:00",
        "timezone": "Asia/Dubai",  # UTC+4
    }
]

def convert_to_beijing(race):
    """将当地时间转换为北京时间"""
    date_str = race["date"]
    time_str = race["local_time"]
    tz = ZoneInfo(race["timezone"])

    # 解析当地时间
    local_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    local_datetime = local_datetime.replace(tzinfo=tz)

    # 转换为北京时间
    beijing_tz = ZoneInfo("Asia/Shanghai")
    beijing_datetime = local_datetime.astimezone(beijing_tz)

    return beijing_datetime

def generate_ics(races):
    """生成ICS日历文件"""
    ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//F1 Calendar 2026//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:F1 2026赛季
X-WR-TIMEZONE:Asia/Shanghai
X-WR-CALDESC:2026年F1世界锦标赛赛程（北京时间）
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
BEGIN:STANDARD
DTSTART:19700101T000000
TZOFFSETFROM:+0800
TZOFFSETTO:+0800
END:STANDARD
END:VTIMEZONE
"""

    for race in races:
        # 转换为北京时间
        beijing_time = convert_to_beijing(race)
        start_time = beijing_time
        end_time = start_time + timedelta(hours=2)  # 2小时比赛

        # 格式化时间 - 使用北京时间，不添加Z后缀
        start_str = start_time.strftime("%Y%m%dT%H%M%S")
        end_str = end_time.strftime("%Y%m%dT%H%M%S")
        dtstamp = datetime.now(ZoneInfo("UTC")).strftime("%Y%m%dT%H%M%SZ")

        # 格式化当地时间显示
        local_time_display = f"{race['local_time']} ({race['timezone']})"
        beijing_time_display = beijing_time.strftime("%H:%M (北京时间)")

        ics_content += f"""BEGIN:VEVENT
UID:f1-2026-{race['round']}@calendar
DTSTAMP:{dtstamp}
DTSTART;TZID=Asia/Shanghai:{start_str}
DTEND;TZID=Asia/Shanghai:{end_str}
SUMMARY:{race['name']} (第{race['round']}站)
DESCRIPTION:2026年F1世界锦标赛 - {race['name']}\\n\\n📍 地点: {race['location']}\\n🏆 国家: {race['country']}\\n⏰ 当地时间: {local_time_display}\\n⏰ 北京时间: {beijing_time_display}
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

def print_schedule_summary(races):
    """打印赛程摘要"""
    print("\n🏎️  2026 F1赛季赛程（北京时间）:")
    print("=" * 80)
    for race in races:
        beijing_time = convert_to_beijing(race)
        date_str = beijing_time.strftime("%Y-%m-%d")
        time_str = beijing_time.strftime("%H:%M")
        weekday = beijing_time.strftime("%A")
        print(f"第{race['round']:2d}站 | {date_str} {time_str:5s} | {weekday:9s} | {race['name']:<20s} | {race['country']:<10s}")
    print("=" * 80)

if __name__ == "__main__":
    print("🏎️  生成2026 F1赛季日历...")
    ics_content = save_ics(f1_races_2026)
    print(f"📊 赛程总数: {len(f1_races_2026)}站")
    print(f"⏰ 赛季时间: {f1_races_2026[0]['date']} - {f1_races_2026[-1]['date']}")

    # 打印详细赛程
    print_schedule_summary(f1_races_2026)