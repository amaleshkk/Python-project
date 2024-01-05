# enemies = 'skeleton'
enemies = 1

def increase_enemies():
    # enemies = 'zombie'
    global enemies
    enemies += 1
    print(f"enemies inside the function {enemies}")


increase_enemies()
print(f"enemies outside the function {enemies}") 


#Global constants

pi = 3.14159


