import os

def generate_qrc(img_folder="img", ui_folder="UI", output_qrc="resources.qrc"):
    qrc_lines = ['<!DOCTYPE RCC><RCC version="1.0">', '<qresource prefix="/">']

    # 處理 img 資料夾中的 .png 圖片
    for root, _, files in os.walk(img_folder):
        for file in files:
            if file.lower().endswith('.png'):
                rel_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
                qrc_lines.append(f'    <file>{rel_path}</file>')

    # 處理 UI 資料夾中的 .ui 檔案
    for root, _, files in os.walk(ui_folder):
        for file in files:
            if file.lower().endswith('.ui'):
                rel_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
                qrc_lines.append(f'    <file>{rel_path}</file>')

    qrc_lines.append('</qresource>')
    qrc_lines.append('</RCC>')

    # 寫入 QRC 檔案
    with open(output_qrc, "w", encoding="utf-8") as f:
        f.write("\n".join(qrc_lines))

# 呼叫函式來產生資源檔案
generate_qrc()