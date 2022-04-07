import openpyxl


class Excel:
    @staticmethod
    def writeExcel(lst):
        path = "\\Users\\amanikanth\\PycharmProjects\\pythonTrack\\main_assignment\\excelfiles\\movieDetails.xlsx"
        wb = openpyxl.load_workbook(path)
        sh1 = wb['Sheet1']
        r = sh1.max_row
        c = sh1.max_column
        for j in range(1,c+1):
            sh1.cell(r+1,j).value = lst[j-1]

        path1="\\Users\\amanikanth\\PycharmProjects\\pythonTrack\\main_assignment\\excelfiles\\movieUpdateDetails.xlsx"
        wb.save(path1);

