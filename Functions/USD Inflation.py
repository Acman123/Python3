def USInflate(money,fromMonth,fromYear,toMonth=0,toYear=0):
    import pip
    import importlib

    pkgs = ['requests','bs4','mechanicalsoup']
    for package in pkgs:
        try:
            importlib.__import__(package)
        except ImportError as e:
            pip.main(['install', package])

    import mechanicalsoup
    import time
    address = "https://data.bls.gov/cgi-bin/cpicalc.pl"
    months = ['January','February','March','April','May','June','July','August','September','October','Novemeber','December']
    getNewDate = mechanicalsoup.StatefulBrowser()
    getNewDate.open(address)
    getNewDate = getNewDate.select_form('form')
    getNewDate = getNewDate.form.find_all('option')
    getNewDate = getNewDate[-1].attrs['value']
    if toMonth == 0:
        toMonth = getNewDate[-2:]
    if toYear == 0:
        toYear = int(getNewDate[:-2])
    elif isinstance(toMonth,str)and len(toMonth) > 2:
        try:
            toMonth = months.index(toMonth)+1
        except ValueError:
            toMonth = time.strftime('%m')
    if isinstance(fromMonth,str) and len(fromMonth) > 2:
        try:
            fromMonth = months.index(fromMonth)+1
        except ValueError:
            fromMonth = time.strftime('%m')
    while toMonth > int(getNewDate[-2:]) and toYear == int(getNewDate[:-2]):
        toMonth = input('Please enter a different month, as data for', months[int(toMonth)-1], 'of', int(getNewDate[:-2]), 'is unavailable.\n')
    while toYear < 1913 or toYear > int(getNewDate[:-2]):
        toYear = input("Final year out of range (1913-2017), please enter a new value.\n")
    while fromYear < 1913 or fromYear > int(getNewDate[:-2]):
        fromYear = input("Initial year out of range (1913-2017), please enter a new value.\n")
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(address)
    browser2 = browser.select_form('form')
    browser2.set('cost1',money)
    browser2.set('year1',str(fromYear) + fromMonth)
    browser2.set('year2', str(toYear) + toMonth)
    resp = browser.submit_selected()

    browser2 = browser.select_form('form')
    result = str(browser2.form.find_all('span')).replace('[<span id="answer">',"").replace('</span>]',"")
    print('$' + str(money),'in',months[int(fromMonth)-1],'of',fromYear,'is worth', result, 'in',months[int(toMonth)-1],'of',toYear,end='.')
