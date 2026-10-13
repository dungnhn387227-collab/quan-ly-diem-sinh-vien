
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cau hinh trang web
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    layout="wide"
)

# 2. Tieu de
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 3. Du lieu 10 sinh vien
data = [
    ["Nguyễn Minh Anh", 8, 7, 9],
    ["Trần Quốc Bảo", 9, 8, 7],
    ["Lê Thị Cẩm", 7, 6, 8],
    ["Phạm Hoàng Duy", 10, 9, 9],
    ["Võ Ngọc Hà", 8, 8, 10],
    ["Đặng Thành Long", 6, 7, 7],
    ["Bùi Khánh Linh", 9, 9, 8],
    ["Ngô Tuấn Kiệt", 7, 8, 9],
    ["Đỗ Phương Mai", 10, 8, 9],
    ["Hoàng Gia Nam", 8, 7, 8]
]

df = pd.DataFrame(data, columns=[
    "Họ tên",
    "Chuyên cần",
    "Giữa kỳ",
    "Cuối kỳ"
])

# 4. Tinh diem tong ket
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)

# 5. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 6. Hien thi bang diem
st.subheader("1. Bảng điểm của 10 sinh viên")

st.dataframe(
    df,
    hide_index=True,
    use_container_width=True
)

# 7. Thong ke diem lop
st.subheader("2. Thống kê kết quả học tập")

diem_trung_binh = df["Tổng kết"].mean()
diem_cao_nhat = df["Tổng kết"].max()
diem_thap_nhat = df["Tổng kết"].min()
so_sinh_vien_dat = (df["Tổng kết"] >= 5).sum()

st.metric(
    "Điểm trung bình của lớp",
    f"{diem_trung_binh:.2f}"
)

# Hien thi sinh vien co diem cao nhat va thap nhat
col1, col2 = st.columns(2)

with col1:
    st.write("**Sinh viên có điểm cao nhất**")
    st.dataframe(
        df[df["Tổng kết"] == diem_cao_nhat][
            ["Họ tên", "Tổng kết"]
        ],
        hide_index=True,
        use_container_width=True
    )

with col2:
    st.write("**Sinh viên có điểm thấp nhất**")
    st.dataframe(
        df[df["Tổng kết"] == diem_thap_nhat][
            ["Họ tên", "Tổng kết"]
        ],
        hide_index=True,
        use_container_width=True
    )

st.metric(
    "Số sinh viên đạt",
    f"{so_sinh_vien_dat}/{len(df)}"
)

# 8. Selectbox chon sinh vien
st.subheader("3. Tra cứu điểm sinh viên")

ten_sinh_vien = st.selectbox(
    "Chọn sinh viên:",
    df["Họ tên"]
)

# Lay thong tin sinh vien duoc chon
sv = df[df["Họ tên"] == ten_sinh_vien].iloc[0]

# Hien thi diem cua sinh vien
c1, c2, c3 = st.columns(3)

c1.metric("Chuyên cần", f"{sv['Chuyên cần']:.1f}")
c2.metric("Giữa kỳ", f"{sv['Giữa kỳ']:.1f}")
c3.metric("Cuối kỳ", f"{sv['Cuối kỳ']:.1f}")

c4, c5 = st.columns(2)

c4.metric("Điểm tổng kết", f"{sv['Tổng kết']:.2f}")
c5.metric("Xếp loại", sv["Xếp loại"])

# 9. Bieu do cot diem tong ket
st.subheader("4. Biểu đồ cột điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(df["Họ tên"], df["Tổng kết"])

ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

plt.xticks(rotation=45, ha="right")

# Hien gia tri diem tren moi cot
for i, diem in enumerate(df["Tổng kết"]):
    ax.text(i, diem + 0.1, f"{diem:.1f}", ha="center")

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 10. Ho ten va MSSV o cuoi trang
st.divider()

st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:12px;">
        Người thực hiện: Nguyễn Hoàng Ngọc Dung<br>
        MSSV: 038308017227
    </div>
    """,
    unsafe_allow_html=True
)
