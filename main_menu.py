# main_menu.py
# josedaniel_chinea_marrero

from funtions.follow_users.main_follow_users import follow_users
from funtions.like_all_post.main_like_all_post import like_all_posts
from funtions.unfollow_all.main_unfollow_all import unfollow_all


def main_menu(driver):
    def print_menu():
        print("\n" + "="*60)
        print("                  Bienvenido a InstaBot".center(40))
        print("          Desarrollado por José Daniel Chinea Marrero".center(40))
        print("="*60)
        print("Selecciona una opción:")
        print("1. Seguir usuarios")
        print("2. Dejar de seguir a todos")
        print("3. Dar like a todas las publicaciones de una cuenta")
        print("4. Salir")
        print("="*60)

    while True:
        print_menu()
        choice = input("Ingresa el número de la opción que deseas realizar: ")

        if choice == '1':
            accounts = input("Ingresa los nombres de las cuentas de las que quieres seguir a los usuarios, separados por comas: (Ejemplo1, Ejemplo2...)").split(',')
            accounts = [account.strip() for account in accounts]
            follow_users(driver, accounts)
        elif choice == '2':
            unfollow_all(driver)
        elif choice == '3':
            account = input("Ingresa el nombre de la cuenta a la que quieres dar like a todas las publicaciones: ")
            like_all_posts(driver, account)
        elif choice == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
