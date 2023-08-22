def getProv(cons_id):
    return cons_id.split("_")[0]

def getConst_No(cons_id):
    return int(cons_id.split("_")[1])

def isMajorParty(party_id):
    assert party_id >= 700 and party_id <= 800
    cons_lst = [701,706,707,709,743,763]
    prog_lst = [705,726,762,719,740,773]
    if (party_id not in cons_lst) and (party_id not in prog_lst):
        return False
    else:
        return True

def getComparison(cons_id_toExamine, all_cons_id, method = "province"):
    # A function to create a comparison group
    """
    @cons_id_toExamine: The list of constituency id that we want to examine because of some interesting or suspicious pattern
    @all_cons_id: The list of all constituency id that are potential comparison group(i.e. sample space)
    @method: The method to find the comparison group. The options are by province, by size, and by region. 
    """
    assert method in ["province", "size", "region"]
    if(method == "province"):
        prov_lst = [getProv(cons_id) for cons_id in cons_id_toExamine]
        return [cons_id for cons_id in all_cons_id if cons_id.split("_")[0] in prov_lst]

def getRGB(length):
    # Get random colors
    rgbLst = []
    round = math.floor(length/3)
    for i in range(round):
        initial = np.random.randint(low=0, high=255, size=3)/255
        rgbLst.append(initial)
        rgbLst.append(np.roll(initial,1))
        rgbLst.append(np.roll(initial,2))

    # Add the remaining color
    remain = length-(round*3)
    initial = np.random.randint(low=0, high=255, size=3)/255
    for j in range(remain):
        rgbLst.append(np.roll(initial,j))

    return rgbLst
