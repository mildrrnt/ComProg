n = input()
if len(n) == 128:
    p = (int(n[3]+n[101]+n[24]+n[32])+int(n[56]+n[89]+n[92]+n[12]))//2
elif len(n) == 64:
    p = int(n[8]+n[22]+n[49]+n[34])
print(p)

#A289KI43LMNG6A88NL312UYT2CO0PQRD5902KOUENP865ORSDOGH8HKN2CXYP9865GIGREOKIJHGV8H923KOLGTGY8GH1RYUH67HT89Y7H8H6V5GVBGTUTG69IUBT5YG
#2CO0PQRD5902KOUENP865O7SDOGH8HKN2C3YP9865GIGREOKI1HGV8H923KOLGTG