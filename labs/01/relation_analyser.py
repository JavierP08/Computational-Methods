import graphviz # https://graphviz.readthedocs.io/en/stable/index.html

def analyze(valores, alphabet):
    Reflexive = False
    Symmetric = False
    Transitive = False

    for num in alphabet:
        if(num, num) in valores:
            Reflexive = True
            break
            
    for t in valores:
        if (t[0], t[1]) in valores or t[1] in alphabet or t[0] in alphabet:
            Symmetric = True
            break
            
    for t0 in valores:
        for t1 in valores:
            if (t0[0],t1[1]) in valores:
                Transitive = True
                break

    return Reflexive,Symmetric,Transitive

def plot(valores):
    g = graphviz.Digraph('G', filename='graph.log')
    for tuple in valores:
        g.edge(str(tuple[0]),str(tuple[1]))
    g.view()

def main():
    print("Hello World analyzing input!")
    valores = input("Enter your set: ")
    
    print(valores)

    alphabet = {0,1,2,3}
    valores = valores.replace(' ', '').replace('.', '')
    t = set(eval(valores))
    
    Reflexive,Symmetric,Transitive = analyze(t,alphabet)
    
    print(f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}")
    plot(t)

if __name__ == "__main__":
    main()
