import streamlit as st
from PIL import Image

# Setup trang
st.set_page_config(
    page_title="Chợ Đồng Hồ Cũ",
    page_icon="⌚",
    layout="wide"
)

# ======== HEADER ========
st.markdown("""
<style>
h1 {
    font-size: 50px !important;
}
h3 {
    font-size: 30px !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/4703/4703869.png", width=90)
with col2:
    st.markdown("### ⌚ **Chợ Đồng Hồ Cũ**")
    st.caption("Nơi kết nối người đam mê đồng hồ – Mua bán uy tín, thẩm định minh bạch")

st.markdown("---")

# ======== BANNER ========
st.image("https://i.imgur.com/Mc3fCEj.jpg", use_column_width=True)

# ======== CÁC MỤC CHÍNH ========
st.markdown("## 🛍️ Danh mục đồng hồ nổi bật")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://i.imgur.com/QvXYo8U.jpg", caption="🔹 Rolex – Đẳng cấp thượng lưu", use_column_width=True)
with col2:
    st.image("https://i.imgur.com/JL0OQGp.jpg", caption="🔸 Seiko – Thanh lịch Nhật Bản", use_column_width=True)
with col3:
    st.image("https://i.imgur.com/fqufZB3.jpg", caption="🔸 Citizen – Cổ điển, tinh tế", use_column_width=True)

# ======== LỢI ÍCH ========
st.markdown("## ✅ Vì sao chọn Chợ Đồng Hồ Cũ?")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    - 🔍 **Thẩm định chuẩn xác** từ chuyên gia
    - 🛡️ **Bảo vệ người mua** bằng chính sách ký gửi
    - 🤝 **Giao dịch minh bạch** 2 chiều
    - 💬 **Hỗ trợ 24/7** qua live chat
    """)
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/1828/1828675.png", width=200)

# ======== SẢN PHẨM GỢI Ý ========
st.markdown("## 🔥 Gợi ý đồng hồ đang hot")

product_list = [
    {
        "brand": "Rolex Datejust 41",
        "price": "120,000,000 VNĐ",
        "img": "https://i.imgur.com/53cYgPj.jpg"
    },
    {
        "brand": "Seiko Presage Automatic",
        "price": "15,500,000 VNĐ",
        "img": "data:image/webp;base64,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"
    },
    {
        "brand": "Citizen Eco-Drive Blue",
        "price": "9,900,000 VNĐ",
        "img": "https://frodos.com.vn/wp-content/uploads/2023/12/a0.jpg"
    }
]

cols = st.columns(3)
for i, p in enumerate(product_list):
    with cols[i]:
        st.image(p["img"], use_column_width=True)
        st.subheader(f"🕰️ {p['brand']}")
        st.write(f"💰 Giá: **{p['price']}**")
        st.button("🔎 Xem chi tiết", key=f"btn_{i}")

# ======== ĐĂNG KÝ NHẬN TIN ========
st.markdown("---")
st.markdown("### 📧 Đăng ký nhận thông tin khuyến mãi")
email = st.text_input("Nhập email của bạn:")
if st.button("Gửi"):
    st.success("Cảm ơn bạn đã đăng ký!")

# ======== FOOTER ========
st.markdown("---")
st.markdown("© 2025 - Chợ Đồng Hồ Cũ | Made with ❤️ by [Nhóm Công nghệ phần mềm]")

