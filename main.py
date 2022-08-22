from random import randint
from TableSolverV2 import *
import time
import datetime

def test_allzero():
    table = Table()
    initial_table = table.table_to_string()
    initial_time = time.time()
    table.solve()
    final_time = time.time()
    return {"title": "Blank Grid", "initial_table":initial_table, "final_table":table.table_to_string(), "solution_time":(final_time - initial_time)} 

def test_randnumbers(quantity):
    counter = 0
    table = Table()
    while(counter != quantity):
        rand_position = (randint(0,8), randint(0,8))
        rand_number = randint(1, 9)
        if table.number_is_valid(rand_position[0], rand_position[1], rand_number):
            table.set_number(rand_position, rand_number)
            counter += 1
    
    print("Tabela Gerada Aleatoriamente:\n")
    initial_table = table.table_to_string()
    print(initial_table)

    print("5 segundos para iniciar a resolução...")
    time.sleep(5)
    initial_time = time.time()
    table.solve()
    final_time = time.time()

    return {"title": f"Random Grid {quantity} filled numbers", "initial_table":initial_table, "final_table":table.table_to_string(), "solution_time":(final_time - initial_time)}

def save_log(resolutions):
    log = open(f"{datetime.datetime.now().strftime('%Y-%m-%d|%H:%M:%S')}.txt", 'a')
    for resolution in resolutions:
        log.write(f"Resolution - {resolution['title']} \nInitial table:\n\n")
        log.write(resolution["initial_table"])
        log.write(f"\n\nFinal table:\n\n{resolution['final_table']}\n\n")
        log.write(f"\nSolution time: {resolution['solution_time']}s\n\n")
        log.write("-----------------------------------------------------------------------\n\n")
    
    log.close()

def main():
    allzero = test_allzero()    
    print(f"\nResolvendo com os grids vazios. Tempo de execução: {allzero['solution_time']}s")

    print("10 segundos para o próximo teste")
    time.sleep(10)

    randnumbers_9 = test_randnumbers(9)
    print(f"\nResolvendo com 9 número preenchidos aleatoriamente. Tempo de execução: {randnumbers_9['solution_time']}s")

    print("10 segundos para o próximo teste")
    time.sleep(10)

    randnumbers_20 = test_randnumbers(20)
    print(f"\nResolvendo com 20 número preenchidos aleatoriamente. Tempo de execução: {randnumbers_20['solution_time']}s")

    save_log([allzero, randnumbers_9, randnumbers_20])


if __name__ == "__main__":
    main()