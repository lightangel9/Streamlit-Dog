import streamlit as st
from page_1_predictions import show as page_1_predictions_show
from page_2_dataset import show as page_2_dataset_show
from page_3_ref_code import show as page_3_ref_code_show

# เมนูเปลี่ยนหน้า
menu = ['1_Predictions', '2_Dataset', '3_RefCode']
choice = st.sidebar.selectbox("เลือกหน้าเว็บ", menu)

# ตรวจสอบเลือกหน้าเว็บและแสดงเนื้อหาตามที่เลือก
if choice == '1_Predictions':
    page_1_predictions_show()
elif choice == '2_Dataset':
    page_2_dataset_show()
elif choice == '3_RefCode':
    page_3_ref_code_show()

