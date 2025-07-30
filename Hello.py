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
        "img": "https://i.imgur.com/6r6NdiN.jpg"
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

