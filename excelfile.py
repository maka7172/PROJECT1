import xlrd

# Open the Workbook
workbook = xlrd.open_workbook("d:\sefars.xlsx")

# Open the worksheet
worksheet = workbook.sheet_by_index(0)

# Iterate the rows and columns
for i in range(0, 5):
    for j in range(0, 4):
        # Print the cell values with tab space
        print(worksheet.cell_value(i, j), end='\t')
        print("") 
print(type(workbook))