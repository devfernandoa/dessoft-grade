sn = str
aprovados = []
l = []
while sn != "não":
    mq = 0
    sn = input("Você deseja inserir mais notas (Sim ou não)")
    if sn == "não":
        break
    q1 = float(input("Qual a primeira nota do quiz"))
    q2 = float(input("Qual a segunda nota do quiz"))
    q3 = float(input("Qual a terceira nota do quiz"))
    q4 = float(input("Qual a quarta nota do quiz"))
    q5 = float(input("Qual a quinta nota do quiz"))
    ai = float(input("Qual a nota da Ai"))
    af = float(input("Qual a nota da Af"))
    ep1 = float(input("Qual a nota do ep1"))
    ep2 = float(input("Qual a nota do ep2"))
    pf = float(input("Qual a nota do pf"))


    l = []
    l.append(q1)
    l.append(q2)
    l.append(q3)
    l.append(q4)
    l.append(q5)
    l.remove(min(l))
    mq = sum(l)/4
    
    ng = 0
    nf = 0
    ng = ep1 * 0.1 + ep2 * 0.2 + pf * 0.7
    ni = ai * 0.4 + af * 0.5 + mq * 0.1
    if ni >= 5 and ng >= 5:
        nf = (ni + ng)/2
    else:
        nf = min(ni, ng)
    print("Nota final do aluno:", nf)
    aprovados.append(nf)
if len(l) > 0:
    médiaF = sum(aprovados)/len(aprovados)
    print("Média da sala:", round(médiaF, 2))

    ap = sum(i >= 5 for i in aprovados)/len(aprovados)
    rp = sum(i < 5 for i in aprovados)/len(aprovados)
    print("Aprovados:", '{:.2f}'.format(ap*100) + "%")
    print("Reprovados:", '{:.2f}'.format(rp*100) + "%")
else:
    print("Média da sala: 0.00")
    print("Aprovados: 0.00%")
    print("Reprovados: 0.00%")