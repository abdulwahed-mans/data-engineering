import pandas as pd
import numpy as np
import os

# 1. قراءة البيانات بشكل صحيح
clients = pd.read_csv("clients.csv", sep=";")

# 2. تحقق من البيانات
print(clients.head())  # طباعة أول 5 سجلات
print(clients.info())  # معلومات عامة عن البيانات، مثل نوع البيانات وعدد القيم غير الناقصة

# 3. تنظيف البيانات (هذا مثال عام، قد تحتاج إلى تعديله بناءً على بياناتك)
# إزالة أي صفوف بها قيم مفقودة
clients_cleaned = clients.dropna()

# 4. تحليل البيانات
# حساب الإحصائيات الوصفية
print(clients_cleaned.describe())

# مثال: توزيع العملاء حسب الوظيفة
print(clients_cleaned['job'].value_counts())

# 5. حفظ البيانات   
clients_cleaned.to_csv("clients_cleaned.csv", index=False)  # حفظ البيانات بدون الفهرس  
# Path: clients_cleaned.csv 
print("تم حفظ البيانات بنجاح")


# إظهار الأعمدة الحالية في البيانات
print("الأعمدة الأصلية:")
print(clients.columns)

# تحديد الأعمدة التي نريد الاحتفاظ بها وإعادة تسميتها
# في هذا المثال، سنحتفظ بأعمدة 'age', 'job', 'marital', و 'education' وسنقوم بإعادة تسميتها
columns_to_keep = ['age', 'job', 'marital', 'education']
new_column_names = ['Age', 'Occupation', 'Marital_Status', 'Education_Level']

# تحديد الأعمدة المطلوبة
selected_data = clients[columns_to_keep]

# إعادة تسمية الأعمدة
renamed_data = selected_data.rename(columns=dict(zip(columns_to_keep, new_column_names)))

# عرض البيانات بعد التحويل
print("البيانات بعد التحويل:")
print(renamed_data.head())

