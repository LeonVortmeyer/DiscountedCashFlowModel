import json
import requests
import openpyxl
import openpyxl
import format_helpers

mywb = openpyxl.Workbook()
mywb.get_sheet_names
sheet = mywb.active
sheet.title="Intro"

api_key = "YourAPIKey"
base_URL = "https://www.alphavantage.co/query?"
statement = "INCOME_STATEMENT"
tik = "IBM"
symbol = "symbol=" + tik + "&"
statement_type = "function=" + statement + "&"
api_param = "apikey=" + api_key

def main():

    quarter_ends = format_helpers.quarter_format_helper()['quarters']
    quarters_shortened = format_helpers.quarter_format_helper()['shortened quarters']

    class Financials:
        def __init__(self, ticker):
            self.ticker = ticker
            self.response = json.loads(requests.get(base_URL+statement_type+"symbol="+ticker+"&"+api_param).text)


        def setIS(self):
            for i in range(len(quarter_ends)):
                for datapoint in self.response['quarterlyReports']:
                    if datapoint['fiscalDateEnding'] == quarter_ends[i]:
                        setattr(Financials, quarters_shortened[i], datapoint)

    IBM = Financials("IBM")
    IBM.setIS()
    print(IBM.q12017)

    income_statement_topleft_cell_reference = 'B4'
    sheet['B2'] = 'Ticker:'
    sheet['C2'] = IBM.ticker
    sheet[income_statement_topleft_cell_reference] = "Income Statements, quarter ended:"


    def offset_label_reference(core_label_reference, offset):
        return core_label_reference[0] + str(int(core_label_reference[1])+offset)

    totalRevenue_label_reference = offset_label_reference(income_statement_topleft_cell_reference,2)
    costofGoodsAndServicesSold_label_reference = offset_label_reference(income_statement_topleft_cell_reference,3)
    grossProfit_label_reference = offset_label_reference(income_statement_topleft_cell_reference,4)
    grossMargin_label_refernece = offset_label_reference(income_statement_topleft_cell_reference,5)
    operatingExpensesLabel_label_reference = offset_label_reference(income_statement_topleft_cell_reference,7)
    sellingGeneralAndAdministrative_label_reference = offset_label_reference(income_statement_topleft_cell_reference,8)
    researchAndDevelopment_label_reference = offset_label_reference(income_statement_topleft_cell_reference,9)
    otherOperatingExpenses_label_reference = offset_label_reference(income_statement_topleft_cell_reference,10)
    operatingExpenses_reference = offset_label_reference(income_statement_topleft_cell_reference,11)
    operatingIncome_label_reference = offset_label_reference(income_statement_topleft_cell_reference,12)
    operatingMargin_label_reference = offset_label_reference(income_statement_topleft_cell_reference,13)
    interestIncome_label_reference = offset_label_reference(income_statement_topleft_cell_reference,15)
    interestExpense_label_reference = offset_label_reference(income_statement_topleft_cell_reference,16)
    otherNonOperatingIncome_label_reference = offset_label_reference(income_statement_topleft_cell_reference,17)
    incomeBeforeTax_label_reference = offset_label_reference(income_statement_topleft_cell_reference,18)
    incomeTaxExpense_label_reference = offset_label_reference(income_statement_topleft_cell_reference,20)
    netIncome_label_reference = offset_label_reference(income_statement_topleft_cell_reference,21)


    class Metric:
        def __init__(self, name, label, label_reference):
            self.name = name
            self.label = label
            self.label_reference = label_reference
            self.moving_cell_reference_start = chr(ord(label_reference[0])+1)+label_reference[1:]

    fiscalDateEnding = Metric('fiscalDateEnding', 'Quarter Ended', income_statement_topleft_cell_reference)
    totalRevenue = Metric('totalRevenue', 'Revenues', totalRevenue_label_reference)
    costofGoodsAndServicesSold = Metric('costofGoodsAndServicesSold', 'COGS', costofGoodsAndServicesSold_label_reference)
    grossProfit = Metric('grossProfit', 'Gross Profit', grossProfit_label_reference)
    sellingGeneralAndAdministrative = Metric('sellingGeneralAndAdministrative', 'SG&A', sellingGeneralAndAdministrative_label_reference)
    researchAndDevelopment = Metric('researchAndDevelopment', 'R&D', researchAndDevelopment_label_reference)
    operatingExpenses = Metric('operatingExpenses', 'Operating Expenses', operatingExpenses_reference)
    operatingIncome = Metric('operatingIncome', 'Operating Income', operatingIncome_label_reference)
    interestIncome = Metric('interestIncome', 'Interest Income', interestIncome_label_reference)
    interestExpense = Metric('interestExpense', 'Interest Expense', interestExpense_label_reference)
    otherNonOperatingIncome = Metric('otherNonOperatingIncome', 'Other Non-Operating Income', otherNonOperatingIncome_label_reference)
    incomeBeforeTax = Metric('incomeBeforeTax', 'Income Before Tax', incomeBeforeTax_label_reference)
    incomeTaxExpense = Metric('incomeTaxExpense', 'Income Tax Expense', incomeTaxExpense_label_reference)
    netIncome = Metric('netIncome', 'Net Income', netIncome_label_reference)




    #Metrics whose values are pulled directly from the API call
    explicit_metrics = [fiscalDateEnding, totalRevenue, costofGoodsAndServicesSold, sellingGeneralAndAdministrative,researchAndDevelopment,
                  operatingExpenses, operatingIncome, interestIncome, interestExpense,
                  otherNonOperatingIncome, incomeBeforeTax,
                  incomeTaxExpense, netIncome]

    #Metrics whose values are not pulled directly from the API call but calculated in program
    implicit_metrics = []

    #Metrics that serve purely as labels (eg. "Operating Expense Buckets", "Other Income Buckets"
    label_metrics = []


    #Income statement metrics are the union of the three sets above
    IS_metrics = [fiscalDateEnding, totalRevenue, grossProfit, costofGoodsAndServicesSold,
                  sellingGeneralAndAdministrative, researchAndDevelopment,
                  operatingExpenses, operatingIncome, interestIncome, interestExpense,
                  otherNonOperatingIncome, incomeBeforeTax,
                  incomeTaxExpense, netIncome]


    for metric in IS_metrics:
        sheet[metric.label_reference] = metric.label


    for i in range(len(quarter_ends)):
        _shortened = quarters_shortened[i]
        quater_data = getattr(IBM, _shortened)

        for metric in IS_metrics:
            sheet[metric.moving_cell_reference_start] = quater_data[metric.name]
            metric.moving_cell_reference_start = chr(ord(metric.moving_cell_reference_start[0])+1) + metric.moving_cell_reference_start[1:]

        i += 1

    mywb.save('TestFile.xlsx')




if __name__ == '__main__':
    main()