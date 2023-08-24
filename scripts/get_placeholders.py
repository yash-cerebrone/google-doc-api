def find_placeholder(document, required):
    '''
    Finds the given placeholder in the document
    Args:
    - document (dict): document object to filter
    - required (string): The placeholder required
    Returns:
    - Tuple containing the start and end indices of the placeholder
    '''
    for i in document.get('body')['content']:
        # print(i.keys())
        if 'paragraph' in i.keys():
            try:
                for j in i['paragraph']['elements']:
                    if '#' in j['textRun']['content'] and required in j['textRun']['content']:
                        # print(j['textRun']['content'], i['paragraph']['elements'][-1])
                        startIndex=i['paragraph']['elements'][0]['startIndex']
                        endIndex=i['paragraph']['elements'][-1]['endIndex']

                        return (startIndex, endIndex)
            except Exception as e:
                # print(e)
                continue

        if 'table' in i.keys():
            for j in i['table']['tableRows']:
                
                text_val=j['tableCells'][1]['content'][0]['paragraph']['elements'][0]['textRun']['content']
                if '# LANGUAGES' in  text_val and 'LANGUAGES' in required:
                    startIndex=j['tableCells'][1]['content'][0]['paragraph']['elements'][0]['startIndex']
                    endIndex=j['tableCells'][1]['content'][0]['paragraph']['elements'][0]['endIndex']
                    
                    return (startIndex, endIndex)