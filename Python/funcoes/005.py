usuario = "comum"
usuario_adm = "a"

def validarUsuario(user):
    if (user == "a"):
        return True
    else:
        return False

def validar_senha(usuario, senha):
    validarUsuario(usuario)
    if(senha == "i"):
        return True
    else:
        return False

tentativas = 3
while tentativas < 4:
        usuarioLogin = input("Insira seu usuario: ")
        validarUsuario(usuarioLogin)
        usuarioSenha = input(f"Olá {usuarioLogin}, insira sua senha agora! \n")
        validador = validar_senha(usuarioLogin, usuarioSenha)
        print(validador)
        if validador == True:
            break
        else:
            print("Sistema Bloqueado!")
        tentativas += 1