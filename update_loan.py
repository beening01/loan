
import pandas as pd
from loan_data import DATA, OUT_DIR


def update_readme():
    with pd.ExcelFile(DATA) as xlsx:
        for sheet_name in xlsx.sheet_names:
            if sheet_name == "주택담보대출":   
                df1 = pd.read_excel(xlsx, sheet_name=sheet_name)
                df1 = df1.tail(12)
            else:
                df2 = pd.read_excel(xlsx, sheet_name=sheet_name)
                df2 = df2.tail(12)

    md_table1 = "|날짜|ITEM_NAME1|DATA_VALUE|\n|---|---|---|\n"
    for _, row in df1.iterrows():
        md_table1 += f"|{row['TIME']}|{row['ITEM_NAME1']}|{row['DATA_VALUE']}|\n"

    md_table2 = "|날짜|ITEM_NAME1|DATA_VALUE|\n|---|---|---|\n"
    for _, row in df2.iterrows():
        md_table2 += f"|{row['TIME']}|{row['ITEM_NAME1']}|{row['DATA_VALUE']}|\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# 📈 최근 1년간 대출 금리 흐름\n\n")

        f.write("## 🏠 주택담보대출\n\n")
        f.write("![주택담보대출](output/주택담보대출.png)\n\n")
        f.write("### 📋 월별 금리 데이터\n\n")
        f.write(md_table1 + "\n\n")

        f.write("## 💳 일반신용대출\n\n")
        f.write("![일반신용대출](output/일반신용대출.png)\n\n")
        f.write("### 📋 월별 금리 데이터\n\n")
        f.write(md_table2 + "\n")


if __name__ == "__main__":
    update_readme()