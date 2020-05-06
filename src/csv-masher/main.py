#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""同じディレクトリのエクセルファイルを一括でcsv化する
Todo:
    *
"""

import os
import sys
import csv
import openpyxl

# PyInstallerの__file__問題回避
if hasattr(sys, "frozen"):
    SEARCH_FILE_DIRECTORY = os.path.dirname(sys.argv[0])

# ファイル実行時
else:
    SCRIPT_PATH = os.path.dirname(__file__)  # "..\\src\\csv-masher"
    SRC_PATH = os.path.dirname(SCRIPT_PATH)  # "..\\src"
    SEARCH_FILE_DIRECTORY = os.path.join(SRC_PATH, "sample_file")  # "..\\src\\Sample"

EXCEL_EXTENSION = ".xlsx"
CSV_EXTENSION = ".csv"


class CSVMasher(object):
    """メイン生成機能
    """

    def __init__(self):
        self.__excel_files = []
        self.set_excel_files(self.__search_excel_file(SEARCH_FILE_DIRECTORY))

    def create_csv_file(self):
        """csvファイルを生成する
        """
        for excel_file in self.__excel_files:
            excel_name = os.path.basename(excel_file).split(".")[0]
            excel_current_directory = os.path.dirname(excel_file)
            book = openpyxl.load_workbook(excel_file, read_only=True, keep_vba=False)

            for sheet in book.worksheets:
                sheet_name = sheet.title
                export_name = "{excel_name}_{sheet_name}{extension}".format(excel_name=excel_name, sheet_name=sheet_name, extension=CSV_EXTENSION)
                export_csv_path = os.path.join(excel_current_directory, export_name)

                with open(export_csv_path, "w", encoding="utf-8") as f:
                    writer = csv.writer(f)

                    for cols in sheet.rows:
                        writer.writerow([str(_.value or "") for _ in cols])

    def __search_excel_file(self, search_directory):
        """エクセルファイルを取得する
        """
        hit_files = []
        for dir_path, dir_list, file_list in os.walk(search_directory):
            for file_name in file_list:
                if EXCEL_EXTENSION in file_name:
                    hit_files.append(os.path.join(dir_path, file_name))
        return hit_files

    def get_excel_files(self):
        """エクセルファイルを取得する
        Returns:
            list: エクセルのパスリスト
        """
        return self.__excel_files

    def set_excel_files(self, excel_files):
        """エクセルファイルをセットする
        Args:
            excel_files (list): excelのファイルパスリスト
        """
        self.__excel_files = excel_files


if __name__ == "__main__":
    csv_masher = CSVMasher()
    print(csv_masher.get_excel_files())
    csv_masher.create_csv_file()
