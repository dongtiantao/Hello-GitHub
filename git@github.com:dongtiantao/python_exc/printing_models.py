unprinted_designs = ['iphone case','robot pendant','dodecaheron']
completed_models =[]

while unprinted_designs:
    current_design = unprinted_designs.pop()

    #模拟根据设计制作３Ｄ打印模型的过程
    print("Printing model:"+current_design)
    completed_models.append(current_design)

#print(completed_models)

print('\n The following models have been printed:')
for completed_model in completed_models:
    print(completed_model)