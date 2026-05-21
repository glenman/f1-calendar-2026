#!/usr/bin/env python3
"""
生成2026 F1赛季完整日历文件（包含所有比赛环节）
"""
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 2026 F1赛季完整赛程（22站，包含所有环节）
# 时间已转换为北京时间
f1_races_2026 = [
    {
        "round": 1,
        "name": "澳大利亚大奖赛",
        "location": "阿尔伯特公园赛道",
        "city": "墨尔本",
        "country": "澳大利亚",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-03-06", "time": "09:30", "duration": 60, "timezone": "Australia/Melbourne"},
            {"name": "二练", "date": "2026-03-06", "time": "13:00", "duration": 60, "timezone": "Australia/Melbourne"},
            {"name": "三练", "date": "2026-03-07", "time": "09:30", "duration": 60, "timezone": "Australia/Melbourne"},
            {"name": "排位赛", "date": "2026-03-07", "time": "13:00", "duration": 60, "timezone": "Australia/Melbourne"},
            {"name": "正赛", "date": "2026-03-08", "time": "12:00", "duration": 120, "timezone": "Australia/Melbourne"}
        ]
    },
    {
        "round": 2,
        "name": "中国大奖赛",
        "location": "上海国际赛车场",
        "city": "上海",
        "country": "中国",
        "type": "冲刺赛周末",
        "sessions": [
            {"name": "一练", "date": "2026-03-13", "time": "11:30", "duration": 60, "timezone": "Asia/Shanghai"},
            {"name": "冲刺赛排位", "date": "2026-03-13", "time": "15:30", "duration": 44, "timezone": "Asia/Shanghai"},
            {"name": "冲刺赛", "date": "2026-03-14", "time": "11:00", "duration": 60, "timezone": "Asia/Shanghai"},
            {"name": "排位赛", "date": "2026-03-14", "time": "15:00", "duration": 60, "timezone": "Asia/Shanghai"},
            {"name": "正赛", "date": "2026-03-15", "time": "15:00", "duration": 120, "timezone": "Asia/Shanghai"}
        ]
    },
    {
        "round": 3,
        "name": "日本大奖赛",
        "location": "铃鹿赛道",
        "city": "铃鹿",
        "country": "日本",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-03-27", "time": "10:30", "duration": 60, "timezone": "Asia/Tokyo"},
            {"name": "二练", "date": "2026-03-27", "time": "14:00", "duration": 60, "timezone": "Asia/Tokyo"},
            {"name": "三练", "date": "2026-03-28", "time": "10:30", "duration": 60, "timezone": "Asia/Tokyo"},
            {"name": "排位赛", "date": "2026-03-28", "time": "14:00", "duration": 60, "timezone": "Asia/Tokyo"},
            {"name": "正赛", "date": "2026-03-29", "time": "13:00", "duration": 120, "timezone": "Asia/Tokyo"}
        ]
    },
    {
        "round": 4,
        "name": "迈阿密大奖赛",
        "location": "迈阿密国际赛道",
        "city": "迈阿密",
        "country": "美国",
        "type": "冲刺赛周末",
        "sessions": [
            {"name": "一练", "date": "2026-05-01", "time": "21:30", "duration": 90, "timezone": "America/New_York"},
            {"name": "冲刺赛排位", "date": "2026-05-02", "time": "01:30", "duration": 44, "timezone": "America/New_York"},
            {"name": "冲刺赛", "date": "2026-05-02", "time": "21:00", "duration": 60, "timezone": "America/New_York"},
            {"name": "排位赛", "date": "2026-05-03", "time": "01:00", "duration": 60, "timezone": "America/New_York"},
            {"name": "正赛", "date": "2026-05-03", "time": "22:00", "duration": 120, "timezone": "America/New_York"}
        ]
    },
    {
        "round": 5,
        "name": "加拿大大奖赛",
        "location": "吉尔斯-维伦纽夫赛道",
        "city": "蒙特利尔",
        "country": "加拿大",
        "type": "冲刺赛周末",
        "sessions": [
            {"name": "一练", "date": "2026-05-23", "time": "01:30", "duration": 60, "timezone": "America/Toronto"},
            {"name": "冲刺赛排位", "date": "2026-05-23", "time": "05:30", "duration": 44, "timezone": "America/Toronto"},
            {"name": "冲刺赛", "date": "2026-05-24", "time": "00:00", "duration": 60, "timezone": "America/Toronto"},
            {"name": "排位赛", "date": "2026-05-24", "time": "04:00", "duration": 60, "timezone": "America/Toronto"},
            {"name": "正赛", "date": "2026-05-25", "time": "04:00", "duration": 120, "timezone": "America/Toronto"}
        ]
    },
    {
        "round": 6,
        "name": "摩纳哥大奖赛",
        "location": "蒙特卡洛赛道",
        "city": "蒙特卡洛",
        "country": "摩纳哥",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-06-05", "time": "13:30", "duration": 60, "timezone": "Europe/Monaco"},
            {"name": "二练", "date": "2026-06-05", "time": "17:00", "duration": 60, "timezone": "Europe/Monaco"},
            {"name": "三练", "date": "2026-06-06", "time": "12:30", "duration": 60, "timezone": "Europe/Monaco"},
            {"name": "排位赛", "date": "2026-06-06", "time": "16:00", "duration": 60, "timezone": "Europe/Monaco"},
            {"name": "正赛", "date": "2026-06-07", "time": "21:00", "duration": 120, "timezone": "Europe/Monaco"}
        ]
    },
    {
        "round": 7,
        "name": "西班牙大奖赛 (巴塞罗那)",
        "location": "巴塞罗那-加泰罗尼亚赛道",
        "city": "巴塞罗那",
        "country": "西班牙",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-06-12", "time": "13:30", "duration": 60, "timezone": "Europe/Madrid"},
            {"name": "二练", "date": "2026-06-12", "time": "17:00", "duration": 60, "timezone": "Europe/Madrid"},
            {"name": "三练", "date": "2026-06-13", "time": "12:30", "duration": 60, "timezone": "Europe/Madrid"},
            {"name": "排位赛", "date": "2026-06-13", "time": "16:00", "duration": 60, "timezone": "Europe/Madrid"},
            {"name": "正赛", "date": "2026-06-14", "time": "21:00", "duration": 120, "timezone": "Europe/Madrid"}
        ]
    },
    {
        "round": 8,
        "name": "奥地利大奖赛",
        "location": "红牛环赛道",
        "city": "施皮尔贝格",
        "country": "奥地利",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-06-26", "time": "18:30", "duration": 60, "timezone": "Europe/Vienna"},
            {"name": "二练", "date": "2026-06-26", "time": "22:00", "duration": 60, "timezone": "Europe/Vienna"},
            {"name": "三练", "date": "2026-06-27", "time": "17:30", "duration": 60, "timezone": "Europe/Vienna"},
            {"name": "排位赛", "date": "2026-06-27", "time": "21:00", "duration": 60, "timezone": "Europe/Vienna"},
            {"name": "正赛", "date": "2026-06-28", "time": "21:00", "duration": 120, "timezone": "Europe/Vienna"}
        ]
    },
    {
        "round": 9,
        "name": "英国大奖赛",
        "location": "银石赛道",
        "city": "银石",
        "country": "英国",
        "type": "冲刺赛周末",
        "sessions": [
            {"name": "一练", "date": "2026-07-03", "time": "19:30", "duration": 60, "timezone": "Europe/London"},
            {"name": "冲刺赛排位", "date": "2026-07-03", "time": "23:30", "duration": 44, "timezone": "Europe/London"},
            {"name": "冲刺赛", "date": "2026-07-04", "time": "19:00", "duration": 60, "timezone": "Europe/London"},
            {"name": "排位赛", "date": "2026-07-04", "time": "23:00", "duration": 60, "timezone": "Europe/London"},
            {"name": "正赛", "date": "2026-07-05", "time": "22:00", "duration": 120, "timezone": "Europe/London"}
        ]
    },
    {
        "round": 10,
        "name": "比利时大奖赛",
        "location": "斯帕-弗朗科尔尚赛道",
        "city": "斯帕",
        "country": "比利时",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-07-17", "time": "19:30", "duration": 60, "timezone": "Europe/Brussels"},
            {"name": "二练", "date": "2026-07-17", "time": "23:00", "duration": 60, "timezone": "Europe/Brussels"},
            {"name": "三练", "date": "2026-07-18", "time": "18:30", "duration": 60, "timezone": "Europe/Brussels"},
            {"name": "排位赛", "date": "2026-07-18", "time": "22:00", "duration": 60, "timezone": "Europe/Brussels"},
            {"name": "正赛", "date": "2026-07-19", "time": "21:00", "duration": 120, "timezone": "Europe/Brussels"}
        ]
    },
    {
        "round": 11,
        "name": "匈牙利大奖赛",
        "location": "亨格罗宁赛道",
        "city": "布达佩斯",
        "country": "匈牙利",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-07-24", "time": "19:30", "duration": 60, "timezone": "Europe/Budapest"},
            {"name": "二练", "date": "2026-07-24", "time": "23:00", "duration": 60, "timezone": "Europe/Budapest"},
            {"name": "三练", "date": "2026-07-25", "time": "18:30", "duration": 60, "timezone": "Europe/Budapest"},
            {"name": "排位赛", "date": "2026-07-25", "time": "22:00", "duration": 60, "timezone": "Europe/Budapest"},
            {"name": "正赛", "date": "2026-07-26", "time": "21:00", "duration": 120, "timezone": "Europe/Budapest"}
        ]
    },
    {
        "round": 12,
        "name": "荷兰大奖赛",
        "location": "赞德福特赛道",
        "city": "赞德福特",
        "country": "荷兰",
        "type": "冲刺赛周末",
        "sessions": [
            {"name": "一练", "date": "2026-08-21", "time": "18:30", "duration": 60, "timezone": "Europe/Amsterdam"},
            {"name": "冲刺赛排位", "date": "2026-08-21", "time": "22:30", "duration": 44, "timezone": "Europe/Amsterdam"},
            {"name": "冲刺赛", "date": "2026-08-22", "time": "18:00", "duration": 60, "timezone": "Europe/Amsterdam"},
            {"name": "排位赛", "date": "2026-08-22", "time": "22:00", "duration": 60, "timezone": "Europe/Amsterdam"},
            {"name": "正赛", "date": "2026-08-23", "time": "21:00", "duration": 120, "timezone": "Europe/Amsterdam"}
        ]
    },
    {
        "round": 13,
        "name": "意大利大奖赛",
        "location": "蒙扎国家赛道",
        "city": "蒙扎",
        "country": "意大利",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-09-04", "time": "19:30", "duration": 60, "timezone": "Europe/Rome"},
            {"name": "二练", "date": "2026-09-04", "time": "23:00", "duration": 60, "timezone": "Europe/Rome"},
            {"name": "三练", "date": "2026-09-05", "time": "18:30", "duration": 60, "timezone": "Europe/Rome"},
            {"name": "排位赛", "date": "2026-09-05", "time": "22:00", "duration": 60, "timezone": "Europe/Rome"},
            {"name": "正赛", "date": "2026-09-06", "time": "21:00", "duration": 120, "timezone": "Europe/Rome"}
        ]
    },
    {
        "round": 14,
        "name": "西班牙大奖赛 (马德里)",
        "location": "马德里赛道",
        "city": "马德里",
        "country": "西班牙",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-09-11", "time": "19:30", "duration": 60, "timezone": "Europe/Madrid"},
            {"name": "二练", "date": "2026-09-11", "time": "23:00", "duration": 60, "timezone": "Europe/Madrid"},
            {"name": "三练", "date": "2026-09-12", "time": "18:30", "duration": 60, "timezone": "Europe/Madrid"},
            {"name": "排位赛", "date": "2026-09-12", "time": "22:00", "duration": 60, "timezone": "Europe/Madrid"},
            {"name": "正赛", "date": "2026-09-13", "time": "21:00", "duration": 120, "timezone": "Europe/Madrid"}
        ]
    },
    {
        "round": 15,
        "name": "阿塞拜疆大奖赛",
        "location": "巴库市街赛道",
        "city": "巴库",
        "country": "阿塞拜疆",
        "type": "常规周末（周六正赛）",
        "sessions": [
            {"name": "一练", "date": "2026-09-24", "time": "16:30", "duration": 60, "timezone": "Asia/Baku"},
            {"name": "二练", "date": "2026-09-24", "time": "20:00", "duration": 60, "timezone": "Asia/Baku"},
            {"name": "三练", "date": "2026-09-25", "time": "16:30", "duration": 60, "timezone": "Asia/Baku"},
            {"name": "排位赛", "date": "2026-09-25", "time": "20:00", "duration": 60, "timezone": "Asia/Baku"},
            {"name": "正赛", "date": "2026-09-26", "time": "19:00", "duration": 120, "timezone": "Asia/Baku"}
        ]
    },
    {
        "round": 16,
        "name": "新加坡大奖赛",
        "location": "滨海湾市街赛道",
        "city": "新加坡",
        "country": "新加坡",
        "type": "冲刺赛周末",
        "sessions": [
            {"name": "一练", "date": "2026-10-09", "time": "17:30", "duration": 60, "timezone": "Asia/Singapore"},
            {"name": "冲刺赛排位", "date": "2026-10-09", "time": "21:30", "duration": 44, "timezone": "Asia/Singapore"},
            {"name": "冲刺赛", "date": "2026-10-10", "time": "17:00", "duration": 60, "timezone": "Asia/Singapore"},
            {"name": "排位赛", "date": "2026-10-10", "time": "21:00", "duration": 60, "timezone": "Asia/Singapore"},
            {"name": "正赛", "date": "2026-10-11", "time": "20:00", "duration": 120, "timezone": "Asia/Singapore"}
        ]
    },
    {
        "round": 17,
        "name": "美国大奖赛",
        "location": "美洲赛道",
        "city": "奥斯汀",
        "country": "美国",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-10-24", "time": "01:30", "duration": 60, "timezone": "America/Chicago"},
            {"name": "二练", "date": "2026-10-24", "time": "05:00", "duration": 60, "timezone": "America/Chicago"},
            {"name": "三练", "date": "2026-10-25", "time": "00:30", "duration": 60, "timezone": "America/Chicago"},
            {"name": "排位赛", "date": "2026-10-25", "time": "04:00", "duration": 60, "timezone": "America/Chicago"},
            {"name": "正赛", "date": "2026-10-26", "time": "03:00", "duration": 120, "timezone": "America/Chicago"}
        ]
    },
    {
        "round": 18,
        "name": "墨西哥城大奖赛",
        "location": "罗德里格斯兄弟赛道",
        "city": "墨西哥城",
        "country": "墨西哥",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-10-31", "time": "02:30", "duration": 60, "timezone": "America/Mexico_City"},
            {"name": "二练", "date": "2026-10-31", "time": "06:00", "duration": 60, "timezone": "America/Mexico_City"},
            {"name": "三练", "date": "2026-11-01", "time": "01:30", "duration": 60, "timezone": "America/Mexico_City"},
            {"name": "排位赛", "date": "2026-11-01", "time": "05:00", "duration": 60, "timezone": "America/Mexico_City"},
            {"name": "正赛", "date": "2026-11-02", "time": "04:00", "duration": 120, "timezone": "America/Mexico_City"}
        ]
    },
    {
        "round": 19,
        "name": "圣保罗大奖赛",
        "location": "英特拉格斯赛道",
        "city": "圣保罗",
        "country": "巴西",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-11-06", "time": "21:30", "duration": 60, "timezone": "America/Sao_Paulo"},
            {"name": "二练", "date": "2026-11-07", "time": "01:00", "duration": 60, "timezone": "America/Sao_Paulo"},
            {"name": "三练", "date": "2026-11-07", "time": "20:30", "duration": 60, "timezone": "America/Sao_Paulo"},
            {"name": "排位赛", "date": "2026-11-08", "time": "00:00", "duration": 60, "timezone": "America/Sao_Paulo"},
            {"name": "正赛", "date": "2026-11-09", "time": "01:00", "duration": 120, "timezone": "America/Sao_Paulo"}
        ]
    },
    {
        "round": 20,
        "name": "拉斯维加斯大奖赛",
        "location": "拉斯维加斯大道赛道",
        "city": "拉斯维加斯",
        "country": "美国",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-11-20", "time": "10:30", "duration": 60, "timezone": "America/Los_Angeles"},
            {"name": "二练", "date": "2026-11-20", "time": "14:00", "duration": 60, "timezone": "America/Los_Angeles"},
            {"name": "三练", "date": "2026-11-21", "time": "09:30", "duration": 60, "timezone": "America/Los_Angeles"},
            {"name": "排位赛", "date": "2026-11-21", "time": "13:00", "duration": 60, "timezone": "America/Los_Angeles"},
            {"name": "正赛", "date": "2026-11-22", "time": "14:00", "duration": 120, "timezone": "America/Los_Angeles"}
        ]
    },
    {
        "round": 21,
        "name": "卡塔尔大奖赛",
        "location": "卢塞尔国际赛道",
        "city": "卢塞尔",
        "country": "卡塔尔",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-11-27", "time": "19:30", "duration": 60, "timezone": "Asia/Qatar"},
            {"name": "二练", "date": "2026-11-27", "time": "23:00", "duration": 60, "timezone": "Asia/Qatar"},
            {"name": "三练", "date": "2026-11-28", "time": "19:30", "duration": 60, "timezone": "Asia/Qatar"},
            {"name": "排位赛", "date": "2026-11-28", "time": "23:00", "duration": 60, "timezone": "Asia/Qatar"},
            {"name": "正赛", "date": "2026-11-29", "time": "23:00", "duration": 120, "timezone": "Asia/Qatar"}
        ]
    },
    {
        "round": 22,
        "name": "阿布扎比大奖赛",
        "location": "亚斯码头赛道",
        "city": "阿布扎比",
        "country": "阿联酋",
        "type": "常规周末",
        "sessions": [
            {"name": "一练", "date": "2026-12-04", "time": "17:30", "duration": 60, "timezone": "Asia/Dubai"},
            {"name": "二练", "date": "2026-12-04", "time": "21:00", "duration": 60, "timezone": "Asia/Dubai"},
            {"name": "三练", "date": "2026-12-05", "time": "17:30", "duration": 60, "timezone": "Asia/Dubai"},
            {"name": "排位赛", "date": "2026-12-05", "time": "21:00", "duration": 60, "timezone": "Asia/Dubai"},
            {"name": "正赛", "date": "2026-12-06", "time": "21:00", "duration": 120, "timezone": "Asia/Dubai"}
        ]
    }
]

def convert_to_beijing(date_str, time_str, timezone_str):
    """将当地时间转换为北京时间"""
    tz = ZoneInfo(timezone_str)
    local_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    local_datetime = local_datetime.replace(tzinfo=tz)
    
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
X-WR-CALNAME:F1 2026赛季（完整赛程）
X-WR-TIMEZONE:Asia/Shanghai
X-WR-CALDESC:2026年F1世界锦标赛完整赛程（包含所有比赛环节）
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
BEGIN:STANDARD
DTSTART:19700101T000000
TZOFFSETFROM:+0800
TZOFFSETTO:+0800
END:STANDARD
END:VTIMEZONE
"""

    session_count = 0
    for race in races:
        for session in race["sessions"]:
            session_count += 1
            
            # 转换为北京时间
            beijing_time = convert_to_beijing(
                session["date"], 
                session["time"], 
                session["timezone"]
            )
            end_time = beijing_time + timedelta(minutes=session["duration"])

            # 格式化时间
            start_str = beijing_time.strftime("%Y%m%dT%H%M%S")
            end_str = end_time.strftime("%Y%m%dT%H%M%S")
            dtstamp = datetime.now(ZoneInfo("UTC")).strftime("%Y%m%dT%H%M%SZ")

            # 格式化当地时间显示
            local_time_display = f"{session['time']} ({session['timezone']})"
            beijing_time_display = beijing_time.strftime("%H:%M (北京时间)")

            ics_content += f"""BEGIN:VEVENT
UID:f1-2026-r{race['round']}-s{session_count}@calendar
DTSTAMP:{dtstamp}
DTSTART;TZID=Asia/Shanghai:{start_str}
DTEND;TZID=Asia/Shanghai:{end_str}
SUMMARY:{race['name']} - {session['name']} (第{race['round']}站)
DESCRIPTION:2026年F1世界锦标赛 - {race['name']}\\n\\n📍 地点: {race['location']}\\n🏆 国家: {race['country']}\\n🎯 周末类型: {race['type']}\\n⏰ 当地时间: {local_time_display}\\n⏰ 北京时间: {beijing_time_display}
LOCATION:{race['location']}, {race['city']}
STATUS:CONFIRMED
TRANSP:OPAQUE
SEQUENCE:0
END:VEVENT
"""

    ics_content += "END:VCALENDAR"
    return ics_content

def save_ics(races, filename="f1_2026_full.ics"):
    """保存ICS文件"""
    ics_content = generate_ics(races)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(ics_content)
    print(f"✅ ICS文件已生成: {filename}")
    
    # 统计比赛环节
    total_sessions = sum(len(race["sessions"]) for race in races)
    sprint_races = sum(1 for race in races if "冲刺赛" in race["type"])
    
    print(f"📊 赛程统计:")
    print(f"   - 总比赛站数: {len(races)}站")
    print(f"   - 总比赛环节: {total_sessions}场")
    print(f"   - 冲刺赛周末: {sprint_races}站")
    print(f"   - 常规周末: {len(races) - sprint_races}站")
    
    return ics_content

if __name__ == "__main__":
    print("🏎️  生成2026 F1赛季完整日历...")
    ics_content = save_ics(f1_races_2026)