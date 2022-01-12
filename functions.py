# functions
#print("now, some functions")
# def who_am_i():
#   name = "john"
#	age = 29
#	print("my name is: "+name+" and i am "+str(age)+" years old")
# who_am_i()

def mercado(gold):
    if gold > 4:
        return "Você pode comprar, aqui o troco" + str(gold - 4)
    elif gold == 4:
        return "Você pode comprar porque deu o valor exato"
    else:
        return "Você não tem dinheiro suficiente camarada"


print(mercado(5))
