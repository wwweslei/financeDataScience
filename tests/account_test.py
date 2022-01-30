import numpy
import pytest
import pandas as pd
import sys
import os

from finance import account


def test_python_version():
    assert sys.version_info >= (3, 6), "The python version is not correct"


def test_exists_folder():
    assert os.path.exists(account.EXCEL_FOLDER), "The folder does not exist"


def test_exists_excel_file():
    assert os.path.exists(os.path.join(
        account.EXCEL_FOLDER, account.EXCEL_FILE_NAME)), "The file does not exist"


def test_read_excel_return_is_dataFrame():
    file = account._read_excel(account.EXCEL_FILE_NAME)
    assert type(file) == pd.DataFrame, "The file is not a dataframe"


def test_read_excel_raise_error_if_file_not_found():
    with pytest.raises(FileNotFoundError):
        account._read_excel("FileNotFound.xlsx"), "The file does not exist"


def test_read_excel_return_is_dataFrame_with_correct_columns():
    file = account._read_excel(account.EXCEL_FILE_NAME)
    assert set(file.columns) == set(["Ativo", "Conta", "Preço", "Quantidade Compra",
                                     "Quantidade Venda", "Financeiro Compra", "Financeiro Venda"]
                                    ), "The columns are not correct"


def test_read_excel_return_is_dataFrame_with_correct_index():
    file = account._read_excel(account.EXCEL_FILE_NAME)
    assert set(file.index.names) == set(
        ["Dt. Negociação"]), "The index is not correct"


def test_read_excel_not_empty_file():
    file = account._read_excel(account.EXCEL_FILE_NAME)
    assert not file.empty, "The file is empty"


def test_clear_dataFrame_not_empty_file():
    file = account._read_excel(account.EXCEL_FILE_NAME)
    file = account._clear_dataFrame(file)
    assert not file.empty, "The file is empty"


def test_clear_dataFrame_return_is_dataFrame():
    file = account._read_excel(account.EXCEL_FILE_NAME)
    file = account._clear_dataFrame(file)
    assert type(file) == pd.DataFrame, "The file is not a dataframe"


def test_clear_dataFrame_return_is_dataFrame_with_correct_columns():
    file = account._read_excel(account.EXCEL_FILE_NAME)
    file = account._clear_dataFrame(file)
    assert set(file.columns) == set(["Ticket", "Price", "Buy", "Sell",
                                     "Financial Buy", "Financial Sell", "Qtd"]), "The columns are not correct"


def test_clear_dataFrame_return_is_dataFrame_with_correct_index():
    file = account._read_excel(account.EXCEL_FILE_NAME)
    file = account._clear_dataFrame(file)
    assert set(file.index.names) == set(["Data"]), "The index is not correct"


def test_full_business_not_empty_file():
    file = account.get_full_business()
    assert not file.empty, "The file is empty"


def test_full_business_return_is_dataFrame():
    file = account.get_full_business()
    assert type(file) == pd.DataFrame, "The file is not a dataframe"


def test_full_business_return_is_dataFrame_with_correct_columns():
    file = account.get_full_business()
    assert set(file.columns) == set(["Ticket", "Price", "Buy", "Sell",
                                     "Financial Buy", "Financial Sell", "Qtd"]), "The columns are not correct"


def test_full_business_return_is_dataFrame_with_correct_index():
    file = account.get_full_business()
    assert set(file.index.names) == set(["Data"]), "The index is not correct"


def test_get_simple_portfolio_not_empty_file():
    file = account.get_simple_portfolio()
    assert not file.empty, "The file is empty"


def test_get_simple_portfolio_return_is_Series():
    file = account.get_simple_portfolio()
    assert type(file) == pd.Series, "The file is not a Series"


def test_get_simple_portfolio_return_type_is_int():
    file = account.get_simple_portfolio()
    assert type(file.iloc[0]) == numpy.int64, "The file is not a numpy.int64"


def test_individual_information_not_empty_file():
    file = account.get_individual_information("PETR4")
    assert not file.empty, "The file is empty"


def test_individual_information_return_is_DataFrame():
    file = account.get_individual_information("PETR4")
    assert type(file) == pd.DataFrame, "The file is not a DataFrame"


def test_individual_information_return_is_DataFrame_with_correct_columns():
    file = account.get_individual_information("PETR4")
    assert set(file.columns) == set(["Ticket", "Price", "Buy", "Sell",
                                     "Financial Buy", "Financial Sell",
                                     "Qtd", "Cumulative_return"]), "The columns are not correct"


def test_individual_information_return_is_DataFrame_with_correct_index():
    file = account.get_individual_information("PETR4")
    assert set(file.index.names) == set(["Data"]), "The index is not correct"


def test_clear_individual_information_not_empty_file():
    file = account.get_individual_information("PETR4")
    file = account._clear_individual_information(file)
    assert not file.empty, "The file is empty"


def test_clear_individual_information_return_is_DataFrame():
    file = account.get_individual_information("PETR4")
    file = account._clear_individual_information(file)
    assert type(file) == pd.DataFrame, "The file is not a DataFrame"


def test_clear_individual_information_return_is_DataFrame_with_correct_columns():
    file = account.get_individual_information("PETR4")
    file = account._clear_individual_information(file)
    assert set(file.columns) == set(["Ticket", "Average Value", "Financial Buy",
                                     "Qtd"]), "The columns are not correct"


def test_get_full_portfolio_not_empty_file():
    file = account.get_portfolio()
    assert not file.empty, "The file is empty"


def test_get_full_portfolio_return_is_DataFrame():
    file = account.get_portfolio()
    assert type(file) == pd.DataFrame, "The file is not a DataFrame"


def test_get_full_portfolio_return_is_DataFrame_with_correct_columns():
    file = account.get_portfolio()
    assert set(file.columns) == set(["Ticket", "Average Value", "Financial Buy",
                                     "Qtd"]), "The columns are not correct"


def test_get_full_portfolio_return_is_DataFrame_with_correct_index():
    file = account.get_portfolio()
    assert set(file.index.names) == set(["Data"]), "The index is not correct"


if __name__ == "__main__":
    pytest.main([__file__, "-k", "test_", "-v", "-s"])
