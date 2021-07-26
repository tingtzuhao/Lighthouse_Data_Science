def pie_chart(dictionary):
    total_freq = sum(dictionary.values())
    return {key : round((value * 360 / total_freq), 1) for key,value in dictionary.items()}