from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    text = text.strip()

    # Trường hợp 1: Ngày cụ thể, ví dụ "2026-10-30"
    try:
        return date.fromisoformat(text)
    except ValueError:
        pass

    # Trường hợp 2: Ngày tương đối
    if text == "tomorrow":
        return today + timedelta(days=1)

    if text.startswith("in ") and text.endswith(" days"):
        try:
            days = int(text[3:-5].strip())
            if days < 0:
                raise ValueError
            return today + timedelta(days=days)
        except ValueError:
            raise ValueError(f"Invalid date text: {text}")

    # Trường hợp 3: Thứ trong tuần, ví dụ "Fri"
    weekdays = {
        "mon": 0,
        "tue": 1,
        "wed": 2,
        "thu": 3,
        "fri": 4,
        "sat": 5,
        "sun": 6,
    }

    day_name = text[:3].lower()

    if day_name in weekdays and len(text) == 3:
        target = weekdays[day_name]

        # Số ngày cần cộng để đến thứ đó tiếp theo
        days_ahead = (target - today.weekday()) % 7

        # Nếu hôm nay đúng thứ được nhập thì lấy tuần sau
        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    raise ValueError(f"Invalid date text: {text}")


if __name__ == "__main__":
    today = date(2026, 10, 23)

    print(parse_due("2026-10-30", today))
    print(parse_due("tomorrow", today))
    print(parse_due("in 3 days", today))
    print(parse_due("Fri", today))