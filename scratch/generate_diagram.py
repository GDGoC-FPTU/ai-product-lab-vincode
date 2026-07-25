import os
from PIL import Image, ImageDraw, ImageFont

# Create a high-resolution, professional diagram for 04-workflow-diagram.png
width, height = 1200, 650
image = Image.new("RGB", (width, height), color="#1E1E2E")
draw = ImageDraw.Draw(image)

try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
except Exception:
    font_title = font_header = font_text = font_bold = ImageFont.load_default()

# Title Header
draw.rectangle([0, 0, width, 80], fill="#181825")
draw.text((40, 25), "SƠ ĐỒ QUY TRÌNH VẬN HÀNH HIỆN TẠI (CURRENT-STATE WORKFLOW)", fill="#89B4FA", font=font_title)
draw.text((40, 55), "Xanh SM (GSM) — Xử lý sự cố hết pin thực địa của tài xế xe điện (Tổng thời gian: 15 phút/lượt)", fill="#A6ADC8", font=font_text)

# Define Steps
steps = [
    {
        "title": "Bước 1",
        "subtitle": "Nhận cuộc gọi sự cố",
        "actor": "Tài xế ──> Dispatcher",
        "time": "⏱ 2 phút",
        "desc": "Tài xế gọi tổng đài\nbáo pin cạn kiệt.",
        "is_bottleneck": False,
        "is_handoff": True
    },
    {
        "title": "Bước 2",
        "subtitle": "Tra cứu vị trí GPS",
        "actor": "Dispatcher ──> App GPS",
        "time": "⏱ 2 phút",
        "desc": "Nhập biển số xe,\ntra tọa độ trên bản đồ.",
        "is_bottleneck": False,
        "is_handoff": True
    },
    {
        "title": "Bước 3",
        "subtitle": "Tra cứu trạm sạc trống",
        "actor": "Dispatcher (Thủ công)",
        "time": "⏱ 5 phút 🔴",
        "desc": "Mở Dashboard VinFast,\ntìm trạm trống & tương thích.",
        "is_bottleneck": True,
        "is_handoff": False
    },
    {
        "title": "Bước 4",
        "subtitle": "Soạn & gửi tin nhắn",
        "actor": "Dispatcher (Thủ công)",
        "time": "⏱ 5 phút 🔴",
        "desc": "Gõ tay tin nhắn chỉ đường\ngửi tới App tài xế.",
        "is_bottleneck": True,
        "is_handoff": False
    },
    {
        "title": "Bước 5",
        "subtitle": "Điều xe cứu hộ pin",
        "actor": "Dispatcher ──> Cứu hộ",
        "time": "⏱ 1 phút",
        "desc": "Gọi đội sạc lưu động\nnếu pin < 5%.",
        "is_bottleneck": False,
        "is_handoff": True
    }
]

box_width = 200
box_height = 240
start_x = 40
start_y = 120
gap_x = 32

for i, step in enumerate(steps):
    x = start_x + i * (box_width + gap_x)
    y = start_y

    # Box color based on bottleneck
    bg_color = "#313244"
    border_color = "#F38BA8" if step["is_bottleneck"] else "#89B4FA"
    
    # Draw step card box
    draw.rectangle([x, y, x + box_width, y + box_height], fill=bg_color, outline=border_color, width=3)
    
    # Step title box
    header_bg = "#45475A" if not step["is_bottleneck"] else "#F38BA8"
    header_fg = "#1E1E2E" if step["is_bottleneck"] else "#CDD6F4"
    draw.rectangle([x, y, x + box_width, y + 40], fill=header_bg)
    draw.text((x + 15, y + 10), step["title"] + ": " + step["subtitle"], fill=header_fg, font=font_header)

    # Content
    draw.text((x + 15, y + 55), f"Người làm: {step['actor']}", fill="#F9E2AF", font=font_text)
    draw.text((x + 15, y + 80), f"Thời gian: {step['time']}", fill="#A6E3A1" if not step["is_bottleneck"] else "#F38BA8", font=font_bold)
    
    # Badges
    badge_y = y + 110
    if step["is_bottleneck"]:
        draw.rectangle([x + 15, badge_y, x + 155, badge_y + 24], fill="#F38BA8")
        draw.text((x + 20, badge_y + 4), "🔴 BOTTLENECK", fill="#1E1E2E", font=font_bold)
    if step["is_handoff"]:
        hx = x + 15 if not step["is_bottleneck"] else x + 15
        hy = badge_y if not step["is_bottleneck"] else badge_y + 30
        draw.rectangle([hx, hy, hx + 130, hy + 24], fill="#89B4FA")
        draw.text((hx + 5, hy + 4), "🔄 HANDOFF", fill="#1E1E2E", font=font_bold)

    # Description
    desc_y = y + 175
    draw.text((x + 15, desc_y), step["desc"], fill="#BAC2DE", font=font_text)

    # Arrow to next step
    if i < len(steps) - 1:
        arrow_start = (x + box_width, y + box_height // 2)
        arrow_end = (x + box_width + gap_x, y + box_height // 2)
        draw.line([arrow_start, arrow_end], fill="#89B4FA", width=4)
        # Arrow head
        draw.polygon([
            arrow_end,
            (arrow_end[0] - 10, arrow_end[1] - 6),
            (arrow_end[0] - 10, arrow_end[1] + 6)
        ], fill="#89B4FA")

# Bottom Summary Panel
summary_y = start_y + box_height + 50
draw.rectangle([40, summary_y, width - 40, summary_y + 180], fill="#181825", outline="#45475A", width=2)
draw.text((60, summary_y + 20), "📌 THỐNG KÊ & PHÂN TÍCH QUY TRÌNH THỦ CÔNG:", fill="#FAB387", font=font_header)

draw.text((60, summary_y + 55), "• Tổng thời gian vận hành hiện tại: 15 phút / sự cố (Tài xế phải dừng đỗ chờ trên đường).", fill="#CDD6F4", font=font_text)
draw.text((60, summary_y + 85), "• 🔴 Nút thắt cổ chai (Bottleneck): Bước 3 & 4 tốn tới 10 phút (chiếm 66% tổng thời gian).", fill="#F38BA8", font=font_text)
draw.text((60, summary_y + 115), "• 🔄 Đáo chuyển thông tin (Handoff): 3 điểm handoff giữa Tài xế ↔ Tổng đài ↔ Hệ thống GPS ↔ Cứu hộ.", fill="#89B4FA", font=font_text)
draw.text((60, summary_y + 145), "• 🎯 Cơ hội AI: AI đọc dữ liệu GPS & Trạm sạc tự động ──> Soạn sẵn SMS Nháp (Draft) ──> Giảm thời gian xuống < 3 phút.", fill="#A6E3A1", font=font_bold)

# Save image
output_path = "/home/mung/AI_in_action/DAY02Lab/ai-product-lab-vincode/04-workflow-diagram.png"
image.save(output_path)
print(f"Successfully generated {output_path}")
