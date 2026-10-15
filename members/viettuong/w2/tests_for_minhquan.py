import pytest
from members.minhquan.w1.grades import summary  # Thay bằng tên file thực tế của bạn đó (ví dụ: from member3_w1 import summary)

# 1. Test trường hợp danh sách điểm bình thường với số lượng phần tử lẻ
def test_summary_normal_odd():
    scores = [10.0, 5.0, 8.0, 6.0, 9.0]
    result = summary(scores)
    assert result["min"] == 5.0
    assert result["max"] == 10.0
    assert result["mean"] == 7.6
    assert result["median"] == 8.0

# 2. Test trường hợp danh sách điểm bình thường với số lượng phần tử chẵn
def test_summary_normal_even():
    scores = [10.0, 20.0, 30.0, 40.0]
    result = summary(scores)
    assert result["min"] == 10.0
    assert result["max"] == 40.0
    assert result["mean"] == 25.0
    assert result["median"] == 25.0

# 3. Test trường hợp danh sách chỉ có đúng 1 phần tử duy nhất
def test_summary_single_element():
    scores = [7.5]
    result = summary(scores)
    assert result["min"] == 7.5
    assert result["max"] == 7.5
    assert result["mean"] == 7.5
    assert result["median"] == 7.5

# 4. Test trường hợp danh sách rỗng (Kiểm tra xem hàm có raise đúng ValueError không)
def test_summary_empty_list():
    with pytest.raises(ValueError, match="scores must not be empty"):
        summary([])

# 5. [EDGE CASE] Test trường hợp chứa toàn bộ các điểm số bằng nhau hoặc số thực có độ chính xác dài
def test_summary_edge_case_floating_precision():
    # Điểm số có nhiều chữ số thập phân sát nhau và giá trị giống nhau
    scores = [10.123, 10.123, 10.123, 10.123]
    result = summary(scores)
    assert result["min"] == 10.123
    assert result["max"] == 10.123
    assert result["mean"] == 10.123
    assert result["median"] == 10.123