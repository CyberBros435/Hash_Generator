from colorama import Fore, Style
import hashlib
import pyfiglet


def display_banner():
    """Display banner with pyfiglet"""
    banner = pyfiglet.figlet_format("HashGen", font="slant")
    print(f"{Fore.BLUE}{banner}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'='*70}{Style.RESET_ALL}\n")


def show_main_menu():
    """Display main menu with all hash options"""
    print(f"{Fore.BLUE}\n\t\t\t\t---:Text to Hash Converter:---{Style.RESET_ALL}")
    hashOptions = [
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
        "sha3_224",
        "sha3_256",
        "sha3_384",
        "sha3_512",
        "blake2b",
        "blake2s",
        "exit",
    ]
    for i, o in enumerate(hashOptions, 1):
        print(f"{Fore.GREEN}[ {i} ]. {Fore.CYAN}{o.upper()}{Style.RESET_ALL}")
    print()


def md5(text):
    text_into_byte = text.encode("utf-8")
    md5_hash = hashlib.md5(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{md5_hash}{Style.RESET_ALL}")


def sha1(text):
    text_into_byte = text.encode("utf-8")
    sha1_hash = hashlib.sha1(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{sha1_hash}{Style.RESET_ALL}")


def sha224(text):
    text_into_byte = text.encode("utf-8")
    sha224_hash = hashlib.sha224(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{sha224_hash}{Style.RESET_ALL}")


def sha256(text):
    text_into_byte = text.encode("utf-8")
    sha256_hash = hashlib.sha256(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{sha256_hash}{Style.RESET_ALL}")


def sha384(text):
    text_into_byte = text.encode("utf-8")
    sha384_hash = hashlib.sha384(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{sha384_hash}{Style.RESET_ALL}")


def sha512(text):
    text_into_byte = text.encode("utf-8")
    sha512_hash = hashlib.sha512(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{sha512_hash}{Style.RESET_ALL}")


def sha3_224(text):
    text_into_byte = text.encode("utf-8")
    sha3_224_hash = hashlib.sha3_224(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{sha3_224_hash}{Style.RESET_ALL}")


def sha3_256(text):
    text_into_byte = text.encode("utf-8")
    sha3_256_hash = hashlib.sha3_256(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{sha3_256_hash}{Style.RESET_ALL}")


def sha3_384(text):
    text_into_byte = text.encode("utf-8")
    sha3_384_hash = hashlib.sha3_384(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{sha3_384_hash}{Style.RESET_ALL}")


def sha3_512(text):
    text_into_byte = text.encode("utf-8")
    sha3_512_hash = hashlib.sha3_512(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{sha3_512_hash}{Style.RESET_ALL}")


def blake2b(text):
    text_into_byte = text.encode("utf-8")
    blake2b_hash = hashlib.blake2b(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{blake2b_hash}{Style.RESET_ALL}")


def blake2s(text):
    text_into_byte = text.encode("utf-8")
    blake2s_hash = hashlib.blake2s(text_into_byte).hexdigest()
    print(f"{Fore.GREEN}{blake2s_hash}{Style.RESET_ALL}")


def handle_hash_option(option_num):
    """Handle selected hash algorithm"""
    hash_handlers = {
        1: ("MD5", md5),
        2: ("SHA1", sha1),
        3: ("SHA224", sha224),
        4: ("SHA256", sha256),
        5: ("SHA384", sha384),
        6: ("SHA512", sha512),
        7: ("SHA3-224", sha3_224),
        8: ("SHA3-256", sha3_256),
        9: ("SHA3-384", sha3_384),
        10: ("SHA3-512", sha3_512),
        11: ("BLAKE2B", blake2b),
        12: ("BLAKE2S", blake2s),
    }

    if option_num not in hash_handlers:
        return False

    algo_name, handler_func = hash_handlers[option_num]
    
    # Show algorithm banner ONCE
    banner = pyfiglet.figlet_format(algo_name, font="small")
    print(f"{Fore.MAGENTA}{banner}{Style.RESET_ALL}")

    while True:
        user_text = input(
            f'{Fore.GREEN}Enter Your Text (q -> "exit"):\t{Style.RESET_ALL}'
        )

        try:
            if user_text.lower() in ["exit", "break", "q"]:
                show_main_menu()
                break
            elif user_text.strip() == "":
                print(f"{Fore.RED}Error: Empty input!{Style.RESET_ALL}\n")
            else:
                handler_func(user_text)
        except Exception as error:
            print(f"{Fore.RED}Error: {error}{Style.RESET_ALL}\n")

    return True


def main():
    display_banner()

    while True:
        show_main_menu()
        try:
            user_option = int(
                input(f"{Fore.BLUE}Enter Your choice:\t{Style.RESET_ALL}")
            )

            if user_option == 13:
                print(f"{Fore.GREEN}Good Bye!!!{Style.RESET_ALL}\n")
                break
            elif 1 <= user_option <= 12:
                handle_hash_option(user_option)
            else:
                print(f"{Fore.RED}Invalid option!!!{Style.RESET_ALL}\n")

        except ValueError:
            print(f"{Fore.RED}Error: Please enter a valid number!{Style.RESET_ALL}\n")
        except Exception as error:
            print(f"{Fore.RED}Error: {error}{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
