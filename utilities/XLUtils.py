import openpyxl
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def getRowCount(file, sheetName):
    try:
        workbook = openpyxl.load_workbook(file)
        sheet = workbook[sheetName]
        row_count = sheet.max_row
        logger.info(f"Total number of rows in '{sheetName}': {row_count}")
        return row_count
    except Exception as e:
        logger.error(f"Error in getting row count: {e}")
        return None


def getColumnCount(file, sheetName):
    try:
        workbook = openpyxl.load_workbook(file)
        sheet = workbook[sheetName]
        col_count = sheet.max_column
        logger.info(f"Total number of columns in '{sheetName}': {col_count}")
        return col_count
    except Exception as e:
        logger.error(f"Error in getting column count: {e}")
        return None


def readData(file, sheetName, rownum, columnno):
    try:
        workbook = openpyxl.load_workbook(file)
        sheet = workbook[sheetName]
        cell_value = sheet.cell(row=rownum, column=columnno).value
        logger.info(f"Read data from {sheetName} - Row: {rownum}, Column: {columnno} - Value: {cell_value}")
        return cell_value
    except Exception as e:
        logger.error(f"Error in reading data: {e}")
        return None


def writeData(file, sheetName, rownum, columnno, data):
    try:
        workbook = openpyxl.load_workbook(file)
        sheet = workbook[sheetName]
        sheet.cell(row=rownum, column=columnno).value = data
        workbook.save(file)
        logger.info(f"Written data to {sheetName} - Row: {rownum}, Column: {columnno} - Data: {data}")
    except Exception as e:
        logger.error(f"Error in writing data: {e}")
