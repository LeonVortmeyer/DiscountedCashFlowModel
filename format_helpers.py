
#formatting function for quarters
def quarter_format_helper():
    quarter_ends = []
    years = [2017, 2018, 2019, 2020]

    for year in years:
        quarter_ends.append(f"{year}-03-31")
        quarter_ends.append(f"{year}-06-30")
        quarter_ends.append(f"{year}-09-30")
        quarter_ends.append(f"{year}-12-31")

    quarters_shortened = [];
    for quarter in quarter_ends:
            if int(quarter[5:7]) < 4:
                quart = "q1"
            elif int(quarter[5:7]) < 7:
                quart = "q2"
            elif int(quarter[5:7]) < 10:
                quart = "q3"
            else:
                quart = "q4"

            quarters_shortened.append(quart+quarter[0:4])

    return {'shortened quarters': quarters_shortened, 'quarters': quarter_ends}
