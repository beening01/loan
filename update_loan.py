
import pandas as pd
from loan_data import DATA


def update_readme():
    with pd.ExcelFile(DATA) as xlsx:
        for sheet_name in xlsx.sheet_names:
            if sheet_name == "주택담보대출":   
                df1 = pd.read_excel(xlsx, sheet_name=sheet_name)
            else:
                df2 = pd.read_excel(xlsx, sheet_name=sheet_name)

    md_table = "|날짜|ITEM_NAME1|DATA_VALUE|\n|---|---|---|\n"
    for _, row in df1.iterrows():
        md_table += f"|{row['TIME']}|{row['ITEM_NAME1']}|{row['DATA_VALUE']}|\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# 📈 최근 1년간 주택담보대출 금리 흐름\n\n")
        f.write("![주택담보대출](OUT_DIR/주택담보대출.png)\n\n")
        f.write("## 📋 월별 금리 데이터\n\n")
        f.write(md_table)

        md_table = "|날짜|ITEM_NAME1|DATA_VALUE|\n|---|---|---|\n"
    for _, row in df2.iterrows():
        md_table += f"|{row['TIME']}|{row['ITEM_NAME1']}|{row['DATA_VALUE']}|\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# 📈 최근 1년간 일반신용대출 금리 흐름\n\n")
        f.write("![일반신용대출](OUT_DIR/일반신용대출.png)\n\n")
        f.write("## 📋 월별 금리 데이터\n\n")
        f.write(md_table)

if __name__ == "__main__":
    update_readme()